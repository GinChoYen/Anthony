import torch  # Import PyTorch library for tensor operations and deep learning
import torch.nn as nn  # Import neural network module from PyTorch
import os  # Import OS module for interacting with the operating system
import random  # Import random module for generating random numbers
import numpy as np  # Import NumPy for numerical operations
import pandas as pd  # Import Pandas for data manipulation
import copy  # Import copy module for copying objects
from torch.utils.data import DataLoader, Dataset  # Import DataLoader and Dataset for handling data
from torch.cuda.amp import autocast, GradScaler  # Import utilities for automatic mixed precision
from tqdm import tqdm  # Import tqdm for progress bar
from transformers import (AutoTokenizer, AutoConfig, AutoModelForCausalLM, get_linear_schedule_with_warmup)  # Import Transformer models and utilities
from sklearn.model_selection import KFold  # Import KFold for cross-validation
from torch.optim import AdamW  # Import AdamW optimizer

os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Disable parallelism in tokenizers
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"  # Set CUDA allocation configuration

class EarlyStopping:
    """
    EarlyStopping class to stop the training if validation loss doesn't improve after a given patience.
    """
    def __init__(self, patience=7, verbose=False, delta=0):
        self.patience = patience  # Number of epochs to wait for improvement
        self.verbose = verbose  # Verbose flag to print messages
        self.counter = 0  # Counter for patience
        self.best_score = None  # Best score seen so far
        self.early_stop = False  # Flag to indicate if early stopping should be done
        self.val_loss_min = np.inf  # Minimum validation loss seen so far
        self.delta = delta  # Minimum change to qualify as an improvement

    def __call__(self, val_loss, model):
        score = -val_loss  # Invert the validation loss to maximize the score

        if self.best_score is None:  # If no best score has been set
            self.best_score = score  # Set the initial best score
            self.save_checkpoint(val_loss, model)  # Save the initial model checkpoint
        elif score < self.best_score + self.delta:  # If the score has not improved enough
            self.counter += 1  # Increment the patience counter
            print(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:  # If patience counter exceeds patience
                self.early_stop = True  # Set early stopping flag
        else:  # If the score has improved
            self.best_score = score  # Update the best score
            self.save_checkpoint(val_loss, model)  # Save the new model checkpoint
            self.counter = 0  # Reset the patience counter

    def save_checkpoint(self, val_loss, model):
        if self.verbose:  # If verbose flag is set
            print(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        if not os.path.exists('models'):  # If models directory does not exist
            os.makedirs('models')  # Create the models directory
        torch.save(model.state_dict(), 'finish_model.pkl')  # Save the model's state dictionary
        self.val_loss_min = val_loss  # Update the minimum validation loss

class CustomDataset(Dataset):
    """
    CustomDataset class to handle the data loading and processing for GPT-2 model.
    """
    def __init__(self, data, maxlen, with_labels=True, gpt_model='gpt2'):
        self.data = data  # Dataframe containing the dataset
        self.tokenizer = AutoTokenizer.from_pretrained(gpt_model)  # Load tokenizer for the specified GPT-2 model
        self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})  # Add a padding token to the tokenizer
        self.maxlen = maxlen  # Maximum length of the sequences
        self.with_labels = with_labels  # Flag to indicate if the dataset has labels

        if self.with_labels:  # If the dataset has labels
            label_mapping = {label: idx for idx, label in enumerate(self.data['category_name'].unique())}  # Create a mapping from labels to indices
            self.data['label'] = self.data['category_name'].map(label_mapping)  # Map labels to indices
            self.data = self.data[self.data['label'].apply(lambda x: str(x).isdigit())]  # Filter out non-numeric labels

        self.label_mapping = label_mapping  # Save the label mapping
        print("Filtered dataset length:", len(self.data))  # Print the length of the filtered dataset

    def __len__(self):
        return len(self.data)  # Return the length of the dataset

    def __getitem__(self, index):
        sent1 = str(self.data.iloc[index]['name'])  # Get the name field of the data at the specified index
        sent2 = str(self.data.iloc[index]['item_description'])  # Get the item_description field of the data at the specified index
        encoded_pair = self.tokenizer(sent1, sent2,
                                      padding='max_length',  # Pad the sequences to the maximum length
                                      truncation='longest_first',  # Truncate the sequences to the maximum length
                                      max_length=self.maxlen,  # Set the maximum length of the sequences
                                      return_tensors='pt')  # Return the sequences as PyTorch tensors
        token_ids = encoded_pair['input_ids'].squeeze(0)  # Get the token IDs and remove the batch dimension
        attn_masks = encoded_pair['attention_mask'].squeeze(0)  # Get the attention masks and remove the batch dimension

        if self.with_labels:  # If the dataset has labels
            label = int(self.data.iloc[index]['label'])  # Get the label at the specified index
            labels = token_ids.clone()  # Clone the token IDs
            labels[labels == self.tokenizer.pad_token_id] = -100  # Replace padding token with -100 for loss computation
            return token_ids, attn_masks, labels  # Return the token IDs, attention masks, and labels
        else:
            return token_ids, attn_masks  # Return the token IDs and attention masks

def set_seed(seed):
    torch.manual_seed(seed)  # Set the seed for generating random numbers for PyTorch
    torch.cuda.manual_seed_all(seed)  # Set the seed for generating random numbers for all GPUs
    torch.backends.cudnn.deterministic = True  # Make CuDNN deterministic
    torch.backends.cudnn.benchmark = False  # Disable the CuDNN benchmark mode
    np.random.seed(seed)  # Set the seed for generating random numbers for NumPy
    random.seed(seed)  # Set the seed for generating random numbers for random module
    os.environ['PYTHONHASHSEED'] = str(seed)  # Set the seed for Python hash-based operations

def evaluate_loss(model, device, criterion, dataloader):
    model.eval()  # Set the model to evaluation mode
    mean_loss = 0.0  # Initialize the mean loss
    count = 0  # Initialize the count

    with torch.no_grad():  # Disable gradient computation
        for it, (seq, attn_masks, labels) in enumerate(tqdm(dataloader)):  # Iterate over the data loader
            seq, attn_masks, labels = seq.to(device), attn_masks.to(device), labels.to(device)  # Move the sequences, attention masks, and labels to the device
            outputs = model(input_ids=seq, attention_mask=attn_masks, labels=labels)  # Get the model outputs
            mean_loss += outputs.loss.item()  # Accumulate the loss
            count += 1  # Increment the count
    return mean_loss / count  # Return the mean loss

class gpt:
    """
    GPT class to handle training and evaluation of the GPT-2 model.
    """
    def __init__(self, model, criterion, optimizer, scheduler, epochs,
                 gradient_accumulation_steps, early_stopping, fp16=True):
        self.early_stopping = early_stopping  # Early stopping object
        self.model = model  # Model to be trained
        self.fp16 = fp16  # Flag to enable mixed precision training
        if self.fp16:
            self.scaler = GradScaler()  # Gradient scaler for mixed precision
        self.optimizer = optimizer  # Optimizer for training
        self.scheduler = scheduler  # Scheduler for learning rate
        self.epochs = epochs  # Number of epochs to train
        self.gradient_accumulation_steps = gradient_accumulation_steps  # Number of steps to accumulate gradients
        self.criterion = criterion  # Loss function

    def print_gpu_utilization(self):
        print(f"Allocated: {torch.cuda.memory_allocated() / 1024 ** 3:.1f} GB")  # Print the allocated GPU memory
        print(f"Reserved: {torch.cuda.memory_reserved() / 1024 ** 3:.1f} GB")  # Print the reserved GPU memory

    def step(self, dataset, bs, device):
        best_loss = np.inf  # Initialize the best loss
        best_ep = 1  # Initialize the best epoch
        nb_iterations = int(len(dataset) * 0.8)  # Calculate the number of iterations per epoch
        print_every = max(nb_iterations // 5, 1)  # Calculate the frequency of printing the loss
        kf = KFold(n_splits=5, shuffle=True, random_state=0)  # Create a KFold object for cross-validation
        for ep in range(self.epochs):  # Iterate over the epochs
            for fold, (train_index, val_index) in enumerate(kf.split(dataset)):  # Iterate over the folds
                train_fold = torch.utils.data.dataset.Subset(dataset, train_index)  # Create a subset for training
                val_fold = torch.utils.data.dataset.Subset(dataset, val_index)  # Create a subset for validation

                train_loader = DataLoader(train_fold, batch_size=bs, num_workers=0, pin_memory=True)  # Create a data loader for training
                val_loader = DataLoader(val_fold, batch_size=bs, num_workers=0, pin_memory=True)  # Create a data loader for validation
                self.model.train()  # Set the model to training mode
                train_loss = 0.0  # Initialize the training loss
                for it, (seq, attn_masks, labels) in enumerate(tqdm(train_loader)):  # Iterate over the training data
                    seq, attn_masks, labels = seq.to(device, non_blocking=True), attn_masks.to(device, non_blocking=True), labels.to(device, non_blocking=True)  # Move the data to the device

                    with autocast():  # Enable mixed precision
                        outputs = self.model(input_ids=seq, attention_mask=attn_masks, labels=labels)  # Get the model outputs
                        loss = outputs.loss  # Get the loss from the model outputs
                        loss = loss / self.gradient_accumulation_steps  # Scale the loss by the gradient accumulation steps

                    if self.fp16:  # If mixed precision is enabled
                        self.scaler.scale(loss).backward()  # Scale the loss and backpropagate
                    else:
                        loss.backward()  # Backpropagate

                    train_loss += loss.item()  # Accumulate the training loss
                    if (it + 1) % self.gradient_accumulation_steps == 0:  # If it's time to update the weights
                        if self.fp16:  # If mixed precision is enabled
                            self.scaler.step(self.optimizer)  # Update the weights
                            self.scaler.update()  # Update the scaler
                        else:
                            self.optimizer.step()  # Update the weights
                        self.scheduler.step()  # Update the learning rate
                        self.optimizer.zero_grad()  # Zero the gradients
                        torch.cuda.synchronize()  # Synchronize the CUDA operations

                    if (it + 1) % print_every == 0:  # If it's time to print the loss
                        print()
                        print("No.{}Fold/{} of epoch {} complete. Loss : {} "
                              .format(fold, nb_iterations, ep + 1, train_loss / print_every))  # Print the loss
                        train_loss = 0.0  # Reset the training loss

                val_loss = evaluate_loss(self.model, device, self.criterion, val_loader)  # Evaluate the validation loss
                print()
                print("Epoch {} Fold {} complete! Validation Loss : {}".format(ep + 1, fold, val_loss))  # Print the validation loss

                if val_loss < best_loss:  # If the validation loss has improved
                    print("Best validation loss improved from {} to {}".format(best_loss, val_loss))  # Print the improvement
                    print()
                    net_copy = copy.deepcopy(self.model)  # Copy the model
                    best_loss = val_loss  # Update the best loss
                    best_ep = ep + 1  # Update the best epoch
            self.early_stopping(val_loss, self.model)  # Check if early stopping should be done
            if self.early_stopping.early_stop:  # If early stopping should be done
                print("Early Stopping!")  # Print early stopping message
                break
        path_to_model = 'models/{}_val_loss_{}_ep_{}.pt'.format('gpt2', round(best_loss, 5), best_ep)  # Create the path to save the model
        torch.save(net_copy.state_dict(), path_to_model)  # Save the model's state dictionary
        print("The model has been saved in {}".format(path_to_model))  # Print the path where the model is saved

        del loss  # Delete the loss variable
        torch.cuda.empty_cache()  # Empty the CUDA cache

def main():
    maxlen = 128  # Maximum length of the sequences
    gpt_model = "gpt2"  # Use GPT-2 model
    bs = 16  # Batch size
    iters_to_accumulate = 2  # Number of steps to accumulate gradients
    lr = 1e-5  # Learning rate
    epochs = 10  # Number of epochs to train
    set_seed(1)  # Set the random seed

    df = pd.read_csv('data/train.tsv', delimiter='\t')  # Load the dataset
    df = df.head(2000)  # Use a subset of the dataset for training
    dataset = CustomDataset(df, maxlen, gpt_model=gpt_model)  # Create the custom dataset

    num_labels = len(dataset.label_mapping) if 'label' in df.columns else None  # Get the number of labels
    criterion = nn.CrossEntropyLoss() if num_labels else None  # Define the loss function
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")  # Set the device

    # Load the GPT-2 model and tokenizer
    config = AutoConfig.from_pretrained(gpt_model)  # Load the model configuration
    model = AutoModelForCausalLM.from_pretrained(gpt_model, config=config)  # Load the model
    model.resize_token_embeddings(len(dataset.tokenizer))  # Resize the token embeddings
    model.to(device)  # Move the model to the device

    # Initialize the optimizer and scheduler
    optimizer = AdamW(model.parameters(), lr=lr)  # Define the optimizer
    total_steps = len(dataset) // bs * epochs  # Calculate the total number of steps
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=0,  # Set the number of warmup steps
        num_training_steps=total_steps  # Set the total number of training steps
    )

    # Early stopping
    early_stopping = EarlyStopping(patience=3, verbose=True)  # Define the early stopping criteria

    # Training
    trainer = gpt(
        model=model,  # Set the model
        criterion=criterion,  # Set the loss function
        optimizer=optimizer,  # Set the optimizer
        scheduler=scheduler,  # Set the scheduler
        epochs=epochs,  # Set the number of epochs
        gradient_accumulation_steps=iters_to_accumulate,  # Set the gradient accumulation steps
        early_stopping=early_stopping,  # Set the early stopping criteria
        fp16=True  # Enable mixed precision training
    )

    trainer.step(dataset, bs, device)  # Start the training

if __name__ == "__main__":
    main()  # Run the main function
