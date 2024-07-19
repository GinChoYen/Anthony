import torch  # Import PyTorch library for tensor operations and deep learning, including building and training neural networks, performing automatic differentiation, and leveraging GPU acceleration.
import torch.nn as nn  # Import PyTorch's neural network module for creating and managing neural network layers, loss functions, and optimization routines.
import os  # Import OS module for interacting with the file system, handling file paths, and accessing environment variables.
import random  # Import random module for generating random numbers, making random choices, and performing random shuffling.
import numpy as np  # Import NumPy for numerical operations, handling large multi-dimensional arrays, and performing mathematical computations.
import pandas as pd  # Import Pandas for data manipulation and analysis, including dataframes for structured data and various data processing functions.
import copy  # Import copy module for creating deep and shallow copies of objects to avoid modifying the original object.
from torch.utils.data import DataLoader, Dataset  # Import DataLoader for batching, shuffling, and parallel loading of data, and Dataset for defining custom data sources.
from torch.cuda.amp import autocast, GradScaler  # Import utilities for automatic mixed precision to reduce memory usage and accelerate training by managing floating-point precision.
from tqdm import tqdm  # Import tqdm for displaying progress bars during loops and iterations to monitor progress in a user-friendly manner.
from transformers import (AutoTokenizer, AutoConfig, AutoModelForSequenceClassification, get_linear_schedule_with_warmup)  # Import tools from Hugging Face Transformers for natural language processing tasks, including tokenization, model configuration, sequence classification, and learning rate scheduling.
from sklearn.model_selection import KFold  # Import KFold for performing cross-validation to assess the performance of machine learning models and ensure generalization.
from torch.optim import AdamW  # Import AdamW optimizer for adaptive learning rate optimization, incorporating weight decay to improve model performance.


os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Disable parallelism in tokenizers
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"  # Configure max split size for CUDA allocations

class EarlyStopping:
    """Early stops the training if validation loss doesn't improve after a given patience."""
    def __init__(self, patience=7, verbose=False, delta=0):
        self.patience = patience  # Number of epochs to wait for improvement
        self.verbose = verbose  # Verbosity flag
        self.counter = 0  # Counter for early stopping
        self.best_score = None  # Best score for early stopping
        self.early_stop = False  # Early stopping flag
        self.val_loss_min = np.inf  # Minimum validation loss
        self.delta = delta  # Minimum change to qualify as improvement

    def __call__(self, val_loss, model):
        score = -val_loss  # Convert loss to score

        if self.best_score is None:
            self.best_score = score  # Set initial best score
            self.save_checkpoint(val_loss, model)  # Save initial model
        elif score < self.best_score + self.delta:
            self.counter += 1  # Increment counter if no improvement
            print(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True  # Trigger early stopping
        else:
            self.best_score = score  # Update best score
            self.save_checkpoint(val_loss, model)  # Save improved model
            self.counter = 0  # Reset counter

    def save_checkpoint(self, val_loss, model):
        if self.verbose:
            print(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        if not os.path.exists('models'):
            os.makedirs('models')  # Create models directory if it doesn't exist
        torch.save(model.state_dict(), 'finish_model.pkl')  # Save model state dictionary
        self.val_loss_min = val_loss  # Update minimum validation loss

class CustomDataset(Dataset):
    def __init__(self, data, maxlen, with_labels=True, bert_model='bert-base-uncased'):
        self.data = data  # pandas dataframe
        self.tokenizer = AutoTokenizer.from_pretrained(bert_model)  # Initialize tokenizer
        self.maxlen = maxlen  # Maximum sequence length
        self.with_labels = with_labels  # Flag to indicate if dataset has labels

        if self.with_labels:
            label_mapping = {label: idx for idx, label in enumerate(self.data['category_name'].unique())}  # Map labels to integers
            self.data['label'] = self.data['category_name'].map(label_mapping)  # Map category_name to label
            self.data = self.data[self.data['label'].apply(lambda x: str(x).isdigit())]  # Ensure labels are integers

        self.label_mapping = label_mapping  # Save label mapping

        print("Filtered dataset length:", len(self.data))  # Print filtered dataset length

    def __len__(self):
        return len(self.data)  # Return length of dataset

    def __getitem__(self, index):
        sent1 = str(self.data.iloc[index]['name'])  # Get name field
        sent2 = str(self.data.iloc[index]['item_description'])  # Get item_description field
        encoded_pair = self.tokenizer(sent1, sent2,
                                      padding='max_length',
                                      truncation='longest_first',
                                      max_length=self.maxlen,
                                      return_tensors='pt')  # Tokenize the input pair
        token_ids = encoded_pair['input_ids'].squeeze(0)  # Extract token ids
        attn_masks = encoded_pair['attention_mask'].squeeze(0)  # Extract attention masks
        token_type_ids = encoded_pair['token_type_ids'].squeeze(0)  # Extract token type ids

        if self.with_labels:
            label = int(self.data.iloc[index]['label'])  # Get label
            return token_ids, attn_masks, token_type_ids, torch.tensor(label)  # Return inputs and label
        else:
            return token_ids, attn_masks, token_type_ids  # Return inputs

def set_seed(seed):
    torch.manual_seed(seed)  # Set random seed for torch
    torch.cuda.manual_seed_all(seed)  # Set random seed for all CUDA devices
    torch.backends.cudnn.deterministic = True  # Ensure deterministic behavior for CuDNN
    torch.backends.cudnn.benchmark = False  # Disable CuDNN benchmarking
    np.random.seed(seed)  # Set random seed for numpy
    random.seed(seed)  # Set random seed for random
    os.environ['PYTHONHASHSEED'] = str(seed)  # Set PYTHONHASHSEED environment variable

def evaluate_loss(model, device, criterion, dataloader):
    model.eval()  # Set model to evaluation mode
    mean_loss = 0.0  # Initialize mean loss
    count = 0  # Initialize count

    with torch.no_grad():
        for it, (seq, attn_masks, token_type_ids, labels) in enumerate(tqdm(dataloader)):
            seq, attn_masks, token_type_ids, labels = \
                seq.to(device), attn_masks.to(device), token_type_ids.to(device), labels.to(device)  # Move inputs to device
            outputs = model(input_ids=seq, attention_mask=attn_masks, token_type_ids=token_type_ids)  # Forward pass
            mean_loss += criterion(outputs.logits, labels).item()  # Calculate loss
            count += 1  # Increment count
    return mean_loss / count  # Return mean loss

class bert:
    def __init__(self, model, criterion, optimizer, scheduler, epochs,
                 gradient_accumulation_steps, early_stopping, fp16=True):
        self.early_stopping = early_stopping  # Early stopping object
        self.model = model  # Model
        self.fp16 = fp16  # Flag for mixed precision training
        if self.fp16:
            self.scaler = GradScaler()  # Gradient scaler for mixed precision
        self.optimizer = optimizer  # Optimizer
        self.scheduler = scheduler  # Learning rate scheduler
        self.epochs = epochs  # Number of epochs
        self.gradient_accumulation_steps = gradient_accumulation_steps  # Gradient accumulation steps
        self.criterion = criterion  # Loss criterion

    def print_gpu_utilization(self):
        print(f"Allocated: {torch.cuda.memory_allocated() / 1024 ** 3:.1f} GB")  # Print allocated GPU memory
        print(f"Reserved: {torch.cuda.memory_reserved() / 1024 ** 3:.1f} GB")  # Print reserved GPU memory


    def step(self, dataset, bs, device):
        best_loss = np.inf  # Initialize best loss
        best_ep = 1  # Initialize best epoch
        nb_iterations = int(len(dataset) * 0.8)  # Calculate number of iterations
        print_every = max(nb_iterations // 5, 1)  # Ensure print_every is at least 1
        kf = KFold(n_splits=5, shuffle=True, random_state=0)  # Initialize KFold
        for ep in range(self.epochs):
            for fold, (train_index, val_index) in enumerate(kf.split(dataset)):
                train_fold = torch.utils.data.dataset.Subset(dataset, train_index)  # Create train subset
                val_fold = torch.utils.data.dataset.Subset(dataset, val_index)  # Create validation subset

                train_loader = DataLoader(train_fold, batch_size=bs, num_workers=0, pin_memory=True)  # Initialize train DataLoader
                val_loader = DataLoader(val_fold, batch_size=bs, num_workers=0, pin_memory=True)  # Initialize validation DataLoader
                self.model.train()  # Set model to training mode
                train_loss = 0.0  # Initialize train loss
                for it, (seq, attn_masks, token_type_ids, labels) in enumerate(tqdm(train_loader)):
                    seq, attn_masks, token_type_ids, labels = \
                        seq.to(device, non_blocking=True), attn_masks.to(device, non_blocking=True), token_type_ids.to(device, non_blocking=True), labels.to(device, non_blocking=True)  # Move inputs to device

                    # Debugging: Check if tensors are on CUDA
                    assert seq.is_cuda, "Sequence is not on CUDA"  # Check if sequence is on CUDA
                    assert attn_masks.is_cuda, "Attention masks are not on CUDA"  # Check if attention masks are on CUDA
                    assert token_type_ids.is_cuda, "Token type IDs are not on CUDA"  # Check if token type IDs are on CUDA
                    assert labels.is_cuda, "Labels are not on CUDA"  # Check if labels are on CUDA
                    print(f"Batch {it} is on device: {seq.device}")  # Print batch device
                    self.print_gpu_utilization()  # Print GPU utilization

                    with autocast():
                        outputs = self.model(seq, attn_masks, token_type_ids)  # Forward pass with mixed precision
                        loss = self.criterion(outputs.logits, labels)  # Calculate loss
                        loss = loss / self.gradient_accumulation_steps  # Normalize loss

                    if self.fp16:
                        self.scaler.scale(loss).backward()  # Backward pass with mixed precision
                    else:
                        loss.backward()  # Backward pass

                    train_loss += loss.item()  # Accumulate train loss
                    if (it + 1) % self.gradient_accumulation_steps == 0:
                        if self.fp16:
                            self.scaler.step(self.optimizer)  # Optimizer step with mixed precision
                            self.scaler.update()  # Update scaler
                        else:
                            self.optimizer.step()  # Optimizer step
                        self.scheduler.step()  # Update learning rate
                        self.optimizer.zero_grad()  # Zero gradients
                        torch.cuda.synchronize()  # Ensure all CUDA ops are done

                    if (it + 1) % print_every == 0:
                        print()
                        print("No.{}Fold/{} of epoch {} complete. Loss : {} "
                              .format(fold, nb_iterations, ep + 1, train_loss / print_every))  # Print progress
                        train_loss = 0.0  # Reset train loss

                val_loss = evaluate_loss(self.model, device, self.criterion, val_loader)  # Evaluate validation loss
                print()
                print("Epoch {} Fold {} complete! Validation Loss : {}".format(ep + 1, fold, val_loss))  # Print validation loss

                if val_loss < best_loss:
                    print("Best validation loss improved from {} to {}".format(best_loss, val_loss))  # Print improvement
                    print()
                    net_copy = copy.deepcopy(self.model)  # Save model copy
                    best_loss = val_loss  # Update best loss
                    best_ep = ep + 1  # Update best epoch
            self.early_stopping(val_loss, self.model)  # Check early stopping
            if self.early_stopping.early_stop:
                print("Early Stopping!")  # Print early stopping
                break
        path_to_model = 'models/{}_val_loss_{}_ep_{}.pt'.format('bert', round(best_loss, 5), best_ep)  # Define model path
        torch.save(net_copy.state_dict(), path_to_model)  # Save model state dictionary
        print("The model has been saved in {}".format(path_to_model))  # Print save path

        del loss  # Delete loss variable
        torch.cuda.empty_cache()  # Empty CUDA cache

def main():
    # parameters
    maxlen = 128  # Maximum sequence length
    bert_model = "bert-base-uncased"  # BERT model
    bs = 16  # Batch size
    iters_to_accumulate = 2  # Gradient accumulation steps
    lr = 1e-5  # Learning rate
    epochs = 10  # Number of epochs
    set_seed(1)  # Set seed for reproducibility

    df = pd.read_csv('data/train.tsv', delimiter='\t')  # Load dataset
    df = df.head(2000)  # Use a smaller subset for testing
    dataset = CustomDataset(df, maxlen, bert_model)  # Create dataset

    num_labels = len(dataset.label_mapping)  # Get number of labels
    criterion = nn.CrossEntropyLoss()  # Define loss criterion
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # Set device

    config = AutoConfig.from_pretrained(bert_model, num_labels=num_labels)  # Load model config
    model = AutoModelForSequenceClassification.from_pretrained(bert_model, config=config)  # Load pre-trained model
    model.to(device)  # Move model to device

    optimizer = AdamW(model.parameters(), lr=lr, weight_decay=1e-2)  # Define optimizer
    early_stopping = EarlyStopping(patience=3, verbose=True)  # Define early stopping

    if torch.cuda.device_count() > 1:
        model = nn.DataParallel(model)  # Enable multi-GPU training

    num_warmup_steps = 50  # Define warmup steps
    t_total = int((len(dataset) * 0.8) // iters_to_accumulate) * epochs  # Calculate total training steps
    lr_scheduler = get_linear_schedule_with_warmup(optimizer=optimizer, num_warmup_steps=num_warmup_steps, num_training_steps=t_total)  # Define learning rate scheduler

    trainer = bert(model, criterion, optimizer, lr_scheduler, epochs, iters_to_accumulate, early_stopping)  # Initialize trainer

    try:
        test_loader = DataLoader(dataset, batch_size=bs, num_workers=0, pin_memory=True)  # Initialize test DataLoader
        for it, (seq, attn_masks, token_type_ids, labels) in enumerate(test_loader):
            seq, attn_masks, token_type_ids, labels = \
                seq.to(device), attn_masks.to(device), token_type_ids.to(device), labels.to(device)  # Move inputs to device
            print(f"Batch {it} loaded successfully")  # Print batch load success
            print(f"Sequence on device: {seq.device}, Attention masks on device: {attn_masks.device}, Token type IDs on device: {token_type_ids.device}, Labels on device: {labels.device}")  # Print devices
            if it == 5:
                break

        trainer.step(dataset, bs, device)  # Start training
    except Exception as e:
        print(f"Error occurred: {e}")  # Print exception

if __name__ == "__main__":
    main()  # Run main function
