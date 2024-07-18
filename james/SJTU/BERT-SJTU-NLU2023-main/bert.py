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
from transformers import (AutoTokenizer, AutoConfig, AutoModelForSequenceClassification, get_linear_schedule_with_warmup)
from sklearn.model_selection import KFold
from torch.optim import AdamW

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"

class EarlyStopping:
    """Early stops the training if validation loss doesn't improve after a given patience."""
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
            if (self.counter >= self.patience):
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
        torch.save(model.state_dict(), 'finish_model.pkl')
        self.val_loss_min = val_loss

class CustomDataset(Dataset):
    def __init__(self, data, maxlen, with_labels=True, bert_model='bert-base-uncased'):
        self.data = data  # pandas dataframe
        self.tokenizer = AutoTokenizer.from_pretrained(bert_model)
        self.maxlen = maxlen
        self.with_labels = with_labels

        if self.with_labels:
            # Map non-integer labels to integers
            label_mapping = {label: idx for idx, label in enumerate(self.data['category_name'].unique())}
            self.data['label'] = self.data['category_name'].map(label_mapping)
            # Ensure the labels column is correct
            self.data = self.data[self.data['label'].apply(lambda x: str(x).isdigit())]

        self.label_mapping = label_mapping  # Save mapping for later use

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
        token_type_ids = encoded_pair['token_type_ids'].squeeze(0)

        if self.with_labels:
            label = int(self.data.iloc[index]['label'])  # Ensure label is an integer
            return token_ids, attn_masks, token_type_ids, torch.tensor(label)
        else:
            return token_ids, attn_masks, token_type_ids

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
        for it, (seq, attn_masks, token_type_ids, labels) in enumerate(tqdm(dataloader)):
            seq, attn_masks, token_type_ids, labels = \
                seq.to(device), attn_masks.to(device), token_type_ids.to(device), labels.to(device)
            outputs = model(input_ids=seq, attention_mask=attn_masks, token_type_ids=token_type_ids)
            mean_loss += criterion(outputs.logits, labels).item()
            count += 1
    return mean_loss / count

class bert:
    def __init__(self, model, criterion, optimizer, scheduler, epochs,
                 gradient_accumulation_steps, early_stopping, fp16=True):
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

    def print_gpu_utilization(self):
        print(f"Allocated: {torch.cuda.memory_allocated() / 1024 ** 3:.1f} GB")
        print(f"Reserved: {torch.cuda.memory_reserved() / 1024 ** 3:.1f} GB")

    def step(self, dataset, bs, device):
        best_loss = np.inf
        best_ep = 1
        nb_iterations = int(len(dataset) * 0.8)
        print_every = max(nb_iterations // 5, 1)  # Ensure print_every is at least 1
        kf = KFold(n_splits=5, shuffle=True, random_state=0)
        for ep in range(self.epochs):
            for fold, (train_index, val_index) in enumerate(kf.split(dataset)):
                train_fold = torch.utils.data.dataset.Subset(dataset, train_index)
                val_fold = torch.utils.data.dataset.Subset(dataset, val_index)

                train_loader = DataLoader(train_fold, batch_size=bs, num_workers=0, pin_memory=True)  # Set num_workers to 0
                val_loader = DataLoader(val_fold, batch_size=bs, num_workers=0, pin_memory=True)  # Set num_workers to 0
                self.model.train()
                train_loss = 0.0
                for it, (seq, attn_masks, token_type_ids, labels) in enumerate(tqdm(train_loader)):
                    seq, attn_masks, token_type_ids, labels = \
                        seq.to(device, non_blocking=True), attn_masks.to(device, non_blocking=True), token_type_ids.to(device, non_blocking=True), labels.to(device, non_blocking=True)

                    # Debugging: Check if tensors are on CUDA
                    assert seq.is_cuda, "Sequence is not on CUDA"
                    assert attn_masks.is_cuda, "Attention masks are not on CUDA"
                    assert token_type_ids.is_cuda, "Token type IDs are not on CUDA"
                    assert labels.is_cuda, "Labels are not on CUDA"
                    print(f"Batch {it} is on device: {seq.device}")
                    self.print_gpu_utilization()

                    with autocast():
                        outputs = self.model(seq, attn_masks, token_type_ids)
                        loss = self.criterion(outputs.logits, labels)
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
                        self.scheduler.step()
                        self.optimizer.zero_grad()
                        torch.cuda.synchronize()  # Ensure all CUDA ops are done

                    if (it + 1) % print_every == 0:
                        print()
                        print("No.{}Fold/{} of epoch {} complete. Loss : {} "
                              .format(fold, nb_iterations, ep + 1, train_loss / print_every))
                        train_loss = 0.0

                val_loss = evaluate_loss(self.model, device, self.criterion, val_loader)
                print()
                print("Epoch {} Fold {} complete! Validation Loss : {}".format(ep + 1, fold, val_loss))

                if val_loss < best_loss:
                    print("Best validation loss improved from {} to {}".format(best_loss, val_loss))
                    print()
                    net_copy = copy.deepcopy(self.model)
                    best_loss = val_loss
                    best_ep = ep + 1
            self.early_stopping(val_loss, self.model)
            if self.early_stopping.early_stop:
                print("Early Stopping!")
                break
        path_to_model = 'models/{}_val_loss_{}_ep_{}.pt'.format('bert', round(best_loss, 5), best_ep)
        torch.save(net_copy.state_dict(), path_to_model)
        print("The model has been saved in {}".format(path_to_model))

        del loss
        torch.cuda.empty_cache()

def main():
    # parameters
    maxlen = 128
    bert_model = "bert-base-uncased"
    bs = 32  # Reduced batch size to fit in memory
    iters_to_accumulate = 2
    lr = 2e-5
    epochs = 8
    set_seed(1)

    df = pd.read_csv('data/train.tsv', delimiter='\t')
    df = df.head(100)  # Take only the first 1000 rows for testing
    dataset = CustomDataset(df, maxlen, bert_model)

    num_labels = len(dataset.label_mapping)
    criterion = nn.CrossEntropyLoss()
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    config = AutoConfig.from_pretrained(bert_model, num_labels=num_labels)
    model = AutoModelForSequenceClassification.from_pretrained(bert_model, config=config)
    model.to(device)

    optimizer = AdamW(model.parameters(), lr=lr, weight_decay=1e-2)
    early_stopping = EarlyStopping(patience=1, verbose=True)

    if torch.cuda.device_count() > 1:
        model = nn.DataParallel(model)

    num_warmup_steps = 20
    t_total = int((len(dataset) * 0.8) // iters_to_accumulate) * epochs
    lr_scheduler = get_linear_schedule_with_warmup(optimizer=optimizer, num_warmup_steps=num_warmup_steps, num_training_steps=t_total)

    trainer = bert(model, criterion, optimizer, lr_scheduler, epochs, iters_to_accumulate, early_stopping)

    try:
        test_loader = DataLoader(dataset, batch_size=bs, num_workers=0, pin_memory=True)  # Set num_workers to 0
        for it, (seq, attn_masks, token_type_ids, labels) in enumerate(test_loader):
            seq, attn_masks, token_type_ids, labels = \
                seq.to(device), attn_masks.to(device), token_type_ids.to(device), labels.to(device)
            print(f"Batch {it} loaded successfully")
            print(f"Sequence on device: {seq.device}, Attention masks on device: {attn_masks.device}, Token type IDs on device: {token_type_ids.device}, Labels on device: {labels.device}")
            if it == 5:
                break

        trainer.step(dataset, bs, device)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
