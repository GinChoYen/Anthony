import torch
import torch.nn as nn
import os
import random
import numpy as np
import pandas as pd
import copy
from torch.utils.data import DataLoader, Dataset
from torch.cuda.amp import autocast, GradScaler
from tqdm import tqdm
from transformers import AutoTokenizer, AutoConfig, AutoModelForCausalLM, get_linear_schedule_with_warmup
from sklearn.model_selection import KFold
from torch.optim import AdamW

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"

class EarlyStopping:
    def __init__(self, patience=7, verbose=False, delta=0):
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.inf
        self.delta = delta

    def __call__(self, val_loss, model):
        score = -val_loss
        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
        elif score < self.best_score + self.delta:
            self.counter += 1
            print(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        if self.verbose:
            print(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        if not os.path.exists('models'):
            os.makedirs('models')
        torch.save(model.state_dict(), f'models/model_epoch_{self.best_score:.4f}.pt')
        self.val_loss_min = val_loss

class CustomDataset(Dataset):
    def __init__(self, data, maxlen, with_labels=True, gpt_model='gpt2'):
        self.data = data
        self.tokenizer = AutoTokenizer.from_pretrained(gpt_model)
        self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        self.maxlen = maxlen
        self.with_labels = with_labels

        if self.with_labels:
            label_mapping = {label: idx for idx, label in enumerate(self.data['category_name'].unique())}
            self.data['label'] = self.data['category_name'].map(label_mapping)
            self.data = self.data[self.data['label'].apply(lambda x: str(x).isdigit())]

        self.label_mapping = label_mapping
        print("Filtered dataset length:", len(self.data))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        sent1 = str(self.data.iloc[index]['name'])
        sent2 = str(self.data.iloc[index]['item_description'])
        encoded_pair = self.tokenizer(sent1, sent2,
                                      padding='max_length',
                                      truncation='longest_first',
                                      max_length=self.maxlen,
                                      return_tensors='pt')
        token_ids = encoded_pair['input_ids'].squeeze(0)
        attn_masks = encoded_pair['attention_mask'].squeeze(0)

        if self.with_labels:
            label = int(self.data.iloc[index]['label'])
            labels = token_ids.clone()
            labels[labels == self.tokenizer.pad_token_id] = -100
            return token_ids, attn_masks, labels
        else:
            return token_ids, attn_masks

def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(seed)
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)

def evaluate_loss(model, device, criterion, dataloader):
    model.eval()
    mean_loss = 0.0
    count = 0

    with torch.no_grad():
        for it, (seq, attn_masks, labels) in enumerate(tqdm(dataloader)):
            seq, attn_masks, labels = seq.to(device), attn_masks.to(device), labels.to(device)
            outputs = model(input_ids=seq, attention_mask=attn_masks, labels=labels)
            mean_loss += outputs.loss.item()
            count += 1
    return mean_loss / count

class GPTTrainer:
    def __init__(self, model, criterion, optimizer, scheduler, epochs,
                 gradient_accumulation_steps, early_stopping, gpt_model, fp16=True):
        self.early_stopping = early_stopping
        self.model = model
        self.fp16 = fp16
        if self.fp16:
            self.scaler = GradScaler()
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.epochs = epochs
        self.gradient_accumulation_steps = gradient_accumulation_steps
        self.criterion = criterion
        self.gpt_model = gpt_model

    def print_gpu_utilization(self):
        print(f"Allocated: {torch.cuda.memory_allocated() / 1024 ** 3:.1f} GB")
        print(f"Reserved: {torch.cuda.memory_reserved() / 1024 ** 3:.1f} GB")

    def step(self, dataset, bs, device):
        best_loss = np.inf
        best_ep = 1
        nb_iterations = int(len(dataset) * 0.8)
        print_every = max(nb_iterations // 5, 1)
        kf = KFold(n_splits=5, shuffle=True, random_state=0)

        for ep in range(self.epochs):
            for fold, (train_index, val_index) in enumerate(kf.split(dataset)):
                train_fold = torch.utils.data.dataset.Subset(dataset, train_index)
                val_fold = torch.utils.data.dataset.Subset(dataset, val_index)

                train_loader = DataLoader(train_fold, batch_size=bs, num_workers=0, pin_memory=True)
                val_loader = DataLoader(val_fold, batch_size=bs, num_workers=0, pin_memory=True)
                self.model.train()
                train_loss = 0.0

                for it, (seq, attn_masks, labels) in enumerate(tqdm(train_loader)):
                    seq, attn_masks, labels = seq.to(device, non_blocking=True), attn_masks.to(device, non_blocking=True), labels.to(device, non_blocking=True)

                    with autocast():
                        outputs = self.model(input_ids=seq, attention_mask=attn_masks, labels=labels)
                        loss = outputs.loss
                        loss = loss / self.gradient_accumulation_steps

                    if self.fp16:
                        self.scaler.scale(loss).backward()
                    else:
                        loss.backward()

                    train_loss += loss.item()
                    if (it + 1) % self.gradient_accumulation_steps == 0:
                        if self.fp16:
                            self.scaler.step(self.optimizer)
                            self.scaler.update()
                        else:
                            self.optimizer.step()

                        self.optimizer.zero_grad()  # Reset gradients after stepping optimizer

                        if it == len(train_loader) - 1:
                            self.scheduler.step()  # Adjust the learning rate at the end of the loop

                    if (it + 1) % print_every == 0:
                        print()
                        print(f"Epoch {ep + 1} Fold {fold} Iteration {it + 1}/{nb_iterations} Loss: {train_loss / print_every:.4f}")
                        train_loss = 0.0

                val_loss = evaluate_loss(self.model, device, self.criterion, val_loader)
                print()
                print(f"Epoch {ep + 1} Fold {fold} complete! Validation Loss: {val_loss:.4f}")

                if val_loss < best_loss:
                    print(f"Best validation loss improved from {best_loss:.4f} to {val_loss:.4f}")
                    print()
                    net_copy = copy.deepcopy(self.model)
                    best_loss = val_loss
                    best_ep = ep + 1

            self.early_stopping(val_loss, self.model)
            if self.early_stopping.early_stop:
                print("Early Stopping!")
                break

            self.print_gpu_utilization()  # Print GPU utilization at the end of each epoch

        path_to_model = f'models/{self.gpt_model}_val_loss_{best_loss:.5f}_ep_{best_ep}.pt'
        torch.save(net_copy.state_dict(), path_to_model)
        print(f"The model has been saved in {path_to_model}")

        del loss
        torch.cuda.empty_cache()

def main():
    maxlen = 128
    gpt_model = "gpt2"
    bs = 16
    iters_to_accumulate = 2
    lr = 1e-5
    epochs = 10
    set_seed(1)

    df = pd.read_csv('data/train.tsv', delimiter='\t')
    df = df.head(2000)
    dataset = CustomDataset(df, maxlen, gpt_model=gpt_model)

    num_labels = len(dataset.label_mapping) if 'label' in df.columns else None
    criterion = nn.CrossEntropyLoss() if num_labels else None
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    config = AutoConfig.from_pretrained(gpt_model)
    model = AutoModelForCausalLM.from_pretrained(gpt_model, config=config)
    model.resize_token_embeddings(len(dataset.tokenizer))
    model.to(device)

    optimizer = AdamW(model.parameters(), lr=lr)
    total_steps = (len(dataset) // bs // iters_to_accumulate) * epochs
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=0,
        num_training_steps=total_steps
    )

    early_stopping = EarlyStopping(patience=3, verbose=True)

    trainer = GPTTrainer(
        model=model,
        criterion=criterion,
        optimizer=optimizer,
        scheduler=scheduler,
        epochs=epochs,
        gradient_accumulation_steps=iters_to_accumulate,
        early_stopping=early_stopping,
        gpt_model=gpt_model,
        fp16=True
    )

    trainer.step(dataset, bs, device)

if __name__ == "__main__":
    main()
