the output looks good. The test batches are successfully being loaded and processed on the CUDA device. Here are the key points that indicate everything is working correctly:

Batch Processing:

The batches are being processed and loaded on the CUDA device (cuda:0), as indicated by lines like Batch 82 is on device: cuda:0.
The memory allocation and reservation details are being printed, which helps in monitoring the GPU utilization.
Validation Loss Improvement:

The validation loss is improving over epochs and folds, as indicated by lines like Best validation loss improved from 5.359058494567871 to 5.281493930816651.
This indicates that the model is learning and getting better with each epoch.
Training Progress:

The progress bar shows the training progress for each fold and epoch.
The model is saving the state when validation loss improves, ensuring the best model is retained.
Overall, the log shows that the training process is functioning as expected, with batches being processed correctly, validation loss decreasing, and model checkpoints being saved. If there are specific areas or details you would like to verify or if you need further assistance, please let me know!

---
C:\2024-movie\BERT-SJTU-NLU2023-main\venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm 2023.1.6/plugins/python/helpers/pydev/pydevconsole.py" --mode=client --host=127.0.0.1 --port=50207 
  import sys; print('Python %s on %s' % (sys.version, sys.platform))  
  sys.path.extend(['C:\\2024-movie\\BERT-SJTU-NLU2023-main'])  
C:\2024-movie\BERT-SJTU-NLU2023-main\venv\Scripts\python.exe "C:/Program Files/JetBrains/PyCharm 2023.1.6/plugins/python/helpers/pydev/pydevconsole.py" --mode=client --host=127.0.0.1 --port=50207 
  import sys; print('Python %s on %s' % (sys.version, sys.platform))
  sys.path.extend(['C:\\2024-movie\\BERT-SJTU-NLU2023-main'])
  PyDev console: starting.
  Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
  runfile('C:\\2024-movie\\BERT-SJTU-NLU2023-main\\bert_gpu_lstm.py', wdir='C:\\2024-movie\\BERT-SJTU-NLU2023-main')
  Filtered dataset length: 2000
  Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
  You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
  Batch 0 loaded successfully
  Sequence on device: cuda:0, Attention masks on device: cuda:0, Token type IDs on device: cuda:0, Labels on device: cuda:0
  Batch 1 loaded successfully
  Sequence on device: cuda:0, Attention masks on device: cuda:0, Token type IDs on device: cuda:0, Labels on device: cuda:0
  Batch 2 loaded successfully
  Sequence on device: cuda:0, Attention masks on device: cuda:0, Token type IDs on device: cuda:0, Labels on device: cuda:0
  Batch 3 loaded successfully
  Sequence on device: cuda:0, Attention masks on device: cuda:0, Token type IDs on device: cuda:0, Labels on device: cuda:0
  Batch 4 loaded successfully
  Sequence on device: cuda:0, Attention masks on device: cuda:0, Token type IDs on device: cuda:0, Labels on device: cuda:0
  Batch 5 loaded successfully
  Sequence on device: cuda:0, Attention masks on device: cuda:0, Token type IDs on device: cuda:0, Labels on device: cuda:0
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 0.4 GB
  Reserved: 0.5 GB
    1%|          | 1/100 [00:00<01:21,  1.21it/s]Batch 1 is on device: cuda:0
  Allocated: 0.9 GB
  Reserved: 1.8 GB
    2%|▏         | 2/100 [00:00<00:43,  2.27it/s]Batch 2 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 2.5 GB
    3%|▎         | 3/100 [00:01<00:29,  3.34it/s]Batch 3 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
    4%|▍         | 4/100 [00:01<00:22,  4.22it/s]Batch 4 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 5 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
    6%|▌         | 6/100 [00:01<00:16,  5.75it/s]Batch 6 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 7 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
    8%|▊         | 8/100 [00:01<00:13,  6.80it/s]Batch 8 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
    9%|▉         | 9/100 [00:01<00:12,  7.33it/s]Batch 9 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   10%|█         | 10/100 [00:01<00:12,  7.28it/s]Batch 10 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   11%|█         | 11/100 [00:02<00:11,  7.68it/s]Batch 11 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   12%|█▏        | 12/100 [00:02<00:11,  7.52it/s]Batch 12 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 13 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   14%|█▍        | 14/100 [00:02<00:10,  8.14it/s]Batch 14 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   15%|█▌        | 15/100 [00:02<00:10,  8.36it/s]Batch 15 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   16%|█▌        | 16/100 [00:02<00:10,  8.00it/s]Batch 16 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   17%|█▋        | 17/100 [00:02<00:10,  8.00it/s]Batch 17 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   18%|█▊        | 18/100 [00:02<00:10,  7.73it/s]Batch 18 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   19%|█▉        | 19/100 [00:03<00:10,  8.06it/s]Batch 19 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   20%|██        | 20/100 [00:03<00:10,  7.40it/s]Batch 20 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   21%|██        | 21/100 [00:03<00:10,  7.77it/s]Batch 21 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   22%|██▏       | 22/100 [00:03<00:10,  7.31it/s]Batch 22 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   23%|██▎       | 23/100 [00:03<00:09,  7.92it/s]Batch 23 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   24%|██▍       | 24/100 [00:03<00:09,  7.66it/s]Batch 24 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 25 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   26%|██▌       | 26/100 [00:03<00:09,  8.04it/s]Batch 26 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 27 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   28%|██▊       | 28/100 [00:04<00:08,  8.34it/s]Batch 28 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 29 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   30%|███       | 30/100 [00:04<00:08,  8.40it/s]Batch 30 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 31 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   32%|███▏      | 32/100 [00:04<00:07,  8.55it/s]Batch 32 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 33 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   34%|███▍      | 34/100 [00:04<00:08,  7.70it/s]Batch 34 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   35%|███▌      | 35/100 [00:05<00:08,  7.93it/s]Batch 35 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   36%|███▌      | 36/100 [00:05<00:08,  7.66it/s]Batch 36 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   37%|███▋      | 37/100 [00:05<00:07,  7.95it/s]Batch 37 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   38%|███▊      | 38/100 [00:05<00:07,  7.96it/s]Batch 38 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 39 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   40%|████      | 40/100 [00:05<00:07,  8.12it/s]Batch 40 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 41 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   42%|████▏     | 42/100 [00:05<00:06,  8.47it/s]Batch 42 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 43 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   44%|████▍     | 44/100 [00:06<00:06,  8.30it/s]Batch 44 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   45%|████▌     | 45/100 [00:06<00:06,  8.44it/s]Batch 45 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   46%|████▌     | 46/100 [00:06<00:06,  8.09it/s]Batch 46 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   47%|████▋     | 47/100 [00:06<00:06,  8.32it/s]Batch 47 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   48%|████▊     | 48/100 [00:06<00:06,  7.87it/s]Batch 48 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 49 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   50%|█████     | 50/100 [00:06<00:05,  8.36it/s]Batch 50 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   51%|█████     | 51/100 [00:07<00:05,  8.53it/s]Batch 51 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   52%|█████▏    | 52/100 [00:07<00:05,  8.25it/s]Batch 52 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 53 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   54%|█████▍    | 54/100 [00:07<00:05,  8.36it/s]Batch 54 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 55 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   56%|█████▌    | 56/100 [00:07<00:05,  8.42it/s]Batch 56 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 57 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   58%|█████▊    | 58/100 [00:07<00:04,  8.64it/s]Batch 58 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   59%|█████▉    | 59/100 [00:07<00:04,  8.73it/s]Batch 59 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   60%|██████    | 60/100 [00:08<00:04,  8.55it/s]Batch 60 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   61%|██████    | 61/100 [00:08<00:04,  8.85it/s]Batch 61 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   62%|██████▏   | 62/100 [00:08<00:04,  7.80it/s]Batch 62 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 63 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   64%|██████▍   | 64/100 [00:08<00:04,  8.09it/s]Batch 64 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 65 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   66%|██████▌   | 66/100 [00:08<00:04,  8.38it/s]Batch 66 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 67 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   68%|██████▊   | 68/100 [00:09<00:03,  8.24it/s]Batch 68 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   69%|██████▉   | 69/100 [00:09<00:03,  8.40it/s]Batch 69 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   70%|███████   | 70/100 [00:09<00:03,  8.22it/s]Batch 70 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 71 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   72%|███████▏  | 72/100 [00:09<00:03,  8.33it/s]Batch 72 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 73 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   74%|███████▍  | 74/100 [00:09<00:03,  8.32it/s]Batch 74 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   75%|███████▌  | 75/100 [00:09<00:02,  8.48it/s]Batch 75 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   76%|███████▌  | 76/100 [00:10<00:02,  8.12it/s]Batch 76 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   77%|███████▋  | 77/100 [00:10<00:02,  8.44it/s]Batch 77 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   78%|███████▊  | 78/100 [00:10<00:03,  7.19it/s]Batch 78 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   79%|███████▉  | 79/100 [00:10<00:02,  7.62it/s]Batch 79 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   80%|████████  | 80/100 [00:10<00:02,  7.24it/s]Batch 80 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   81%|████████  | 81/100 [00:10<00:02,  7.62it/s]Batch 81 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   82%|████████▏ | 82/100 [00:10<00:02,  7.62it/s]Batch 82 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   83%|████████▎ | 83/100 [00:10<00:02,  7.99it/s]Batch 83 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   84%|████████▍ | 84/100 [00:11<00:02,  7.19it/s]Batch 84 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 85 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   86%|████████▌ | 86/100 [00:11<00:01,  7.87it/s]Batch 86 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 87 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   88%|████████▊ | 88/100 [00:11<00:01,  7.92it/s]Batch 88 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 89 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   90%|█████████ | 90/100 [00:11<00:01,  7.86it/s]Batch 90 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 91 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   92%|█████████▏| 92/100 [00:12<00:00,  8.07it/s]Batch 92 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 93 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   94%|█████████▍| 94/100 [00:12<00:00,  8.15it/s]Batch 94 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   95%|█████████▌| 95/100 [00:12<00:00,  8.26it/s]Batch 95 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   96%|█████████▌| 96/100 [00:12<00:00,  7.99it/s]Batch 96 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 97 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
   98%|█████████▊| 98/100 [00:12<00:00,  8.26it/s]Batch 98 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  Batch 99 is on device: cuda:0
  Allocated: 1.7 GB
  Reserved: 3.0 GB
  100%|██████████| 100/100 [00:13<00:00,  7.67it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.57it/s]
  Epoch 1 Fold 0 complete! Validation Loss : 5.877351512908936
  Best validation loss improved from inf to 5.877351512908936
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.0 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.5 GB
    2%|▏         | 2/100 [00:00<00:11,  8.44it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:11,  8.65it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.46it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.69it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.08it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:11,  8.26it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.54it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.39it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.58it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.09it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:10,  8.47it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.31it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.41it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:02<00:09,  8.40it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.29it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.39it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.14it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:02<00:09,  8.11it/s]Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  7.63it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:03<00:09,  7.69it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:10,  7.30it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:09,  7.39it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:09,  7.45it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:09,  7.16it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:09,  7.59it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:04<00:09,  7.31it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:04<00:08,  7.74it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:08,  7.55it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:08,  7.71it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.08it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  7.80it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:05<00:08,  7.49it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:05<00:07,  7.91it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:05<00:07,  7.68it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:07,  8.00it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.23it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  7.92it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.21it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:06<00:06,  7.73it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:06<00:06,  8.08it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:06<00:06,  7.51it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:06,  7.93it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.15it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:07<00:05,  8.28it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:07<00:04,  8.48it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:07<00:04,  8.60it/s]Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.22it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.33it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.60it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:08<00:04,  8.71it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:08<00:04,  8.45it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:03,  8.47it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.63it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.60it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:09<00:03,  8.50it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:09<00:02,  8.50it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.60it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.58it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:10<00:02,  8.56it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:10<00:01,  8.73it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:10<00:01,  8.80it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.62it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.50it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.51it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:11<00:00,  8.27it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  8.43it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:11<00:00,  8.68it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.43it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.73it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.18it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:12<00:00,  8.23it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.67it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 1 Fold 1 complete! Validation Loss : 5.732309856414795
  Best validation loss improved from 5.877351512908936 to 5.732309856414795
  Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:10,  9.14it/s]Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.43it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.36it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.42it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.69it/s]Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:11,  8.21it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.59it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.49it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.70it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.59it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.64it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.66it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.61it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.76it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.95it/s]Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.50it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.51it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.45it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.47it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.44it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.84it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.69it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.82it/s]Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.66it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.45it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.40it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.53it/s]Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  7.60it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:06,  7.89it/s]Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:06,  7.69it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:06<00:06,  8.02it/s]Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:06,  7.51it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  7.90it/s]Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:06,  7.30it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  7.82it/s]Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  7.60it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:05,  7.99it/s]Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:05,  7.60it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:07<00:05,  8.00it/s]Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:05,  7.71it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.22it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.33it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  8.11it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:08<00:03,  8.31it/s]Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:03,  8.00it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.11it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.32it/s]Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  7.76it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.06it/s]Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  7.94it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:09<00:03,  8.24it/s]Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:09<00:02,  8.17it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.32it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.32it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.39it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:10<00:01,  8.38it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.25it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  7.94it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.14it/s]Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  7.90it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.30it/s]Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:11<00:01,  7.97it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:11<00:00,  8.24it/s]Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  7.89it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.07it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.03it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.36it/s]Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:12<00:00,  8.27it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.01it/s]
  Epoch 1 Fold 2 complete! Validation Loss : 5.619560871124268
  Best validation loss improved from 5.732309856414795 to 5.619560871124268
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.34it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:11,  8.66it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.39it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:11,  8.63it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.19it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.47it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:01<00:12,  7.41it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:12,  7.47it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:12,  7.31it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:11,  7.83it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:11,  7.82it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:10,  8.25it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:02<00:09,  8.42it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.20it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.32it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.49it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.23it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.34it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:09,  7.98it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.16it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.16it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.27it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:07,  8.35it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.60it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.24it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  7.95it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:07,  8.25it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  7.73it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:05<00:07,  8.04it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:05<00:07,  7.53it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:05<00:07,  7.81it/s]Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:07,  7.12it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:07,  7.35it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:08,  6.42it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:07,  7.04it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:06<00:07,  6.63it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:06<00:07,  7.12it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:06<00:06,  7.53it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:06,  7.41it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:06,  7.81it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:06,  6.97it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:06,  7.48it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:07<00:06,  6.70it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:07<00:06,  6.93it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:07<00:06,  6.18it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:07<00:06,  6.62it/s]Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:07,  5.68it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:08<00:06,  6.05it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:08<00:06,  5.66it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:08<00:06,  6.06it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:08<00:06,  5.82it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:08<00:05,  6.33it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:08<00:06,  5.25it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:09<00:06,  5.28it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:09<00:06,  4.71it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:09<00:05,  5.30it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:09<00:05,  5.51it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:09<00:04,  6.30it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:09<00:04,  5.90it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:10<00:04,  6.53it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:10<00:04,  5.58it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:10<00:03,  6.03it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:10<00:03,  6.64it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:11<00:02,  7.06it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:11<00:03,  6.14it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:11<00:02,  6.50it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:11<00:02,  6.73it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:11<00:02,  7.11it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:12<00:01,  7.11it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:12<00:01,  7.38it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:12<00:01,  7.29it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:12<00:01,  7.37it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:12<00:01,  7.71it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:12<00:00,  7.97it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:13<00:00,  7.53it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:13<00:00,  7.87it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:13<00:00,  7.43it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:13<00:00,  7.65it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:13<00:00,  7.10it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:13<00:00,  7.40it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:13<00:00,  7.17it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.40it/s]
  Epoch 1 Fold 3 complete! Validation Loss : 5.382505474090576
  Best validation loss improved from 5.619560871124268 to 5.382505474090576
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.42it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:11,  8.69it/s]Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.01it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.42it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.59it/s]Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.40it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.59it/s]Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:11,  8.02it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.00it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.16it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:10,  8.27it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.34it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.60it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.55it/s]Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.33it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.53it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.50it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.54it/s]Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.17it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.48it/s]Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.34it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.56it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.68it/s]Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:07,  8.49it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.41it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.66it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.54it/s]Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.33it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.46it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.60it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.58it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.76it/s]Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.59it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.55it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.69it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.77it/s]Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.34it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.55it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:06<00:04,  8.67it/s]Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.50it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:07<00:04,  8.65it/s]Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.37it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.67it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.78it/s]Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.56it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.70it/s]Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:03,  8.49it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.50it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.77it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.84it/s]Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.63it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.86it/s]Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.31it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.40it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.57it/s]Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.33it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.53it/s]Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.38it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.37it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.54it/s]Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.11it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  8.37it/s]Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  7.98it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  7.81it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  7.61it/s]Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:01,  7.21it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:11<00:00,  7.28it/s]Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  7.08it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:11<00:00,  7.32it/s]Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  6.78it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  7.34it/s]Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  7.03it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  7.54it/s]Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:12<00:00,  8.30it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.48it/s]
  Epoch 1 Fold 4 complete! Validation Loss : 5.157646102905273
  Best validation loss improved from 5.382505474090576 to 5.157646102905273
  Validation loss decreased (inf --> 5.157646).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:11,  8.76it/s]Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:13,  7.37it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.25it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.38it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.44it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.47it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.55it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.66it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.58it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.75it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.82it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.63it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.59it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.77it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.84it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.39it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.43it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.66it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:08,  8.52it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.16it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.52it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.64it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.48it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.63it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.16it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.31it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.40it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.38it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.13it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.37it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.42it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:06<00:05,  8.54it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.20it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.39it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.28it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.38it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:05,  8.54it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:05,  8.14it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.29it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.58it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.69it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.52it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.52it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.64it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:03,  8.48it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.49it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.63it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.19it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.42it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.02it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:09<00:02,  8.01it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.40it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.54it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.15it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.30it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.38it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.36it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  8.50it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.37it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.23it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.33it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  8.39it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.43it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.46it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.44it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.36it/s]
  Epoch 2 Fold 0 complete! Validation Loss : 5.010769271850586
  Best validation loss improved from 5.157646102905273 to 5.010769271850586
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.50it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.51it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.69it/s]Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.46it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.49it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.29it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.37it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.53it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.52it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.67it/s]Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.34it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.36it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.48it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:02<00:08,  8.67it/s]Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.40it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.47it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.66it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.67it/s]Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.34it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.59it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.77it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.83it/s]Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.56it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.75it/s]Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.24it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.35it/s]Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.62it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:05<00:06,  8.72it/s]Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.27it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.59it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.69it/s]Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.50it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.64it/s]Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:06,  8.16it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.55it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.99it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.53it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.52it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.58it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:07<00:04,  8.81it/s]Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.62it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.57it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  8.48it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.74it/s]Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.47it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.48it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.61it/s]Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.19it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.08it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.24it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.32it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.57it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.44it/s]Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.32it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.38it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.53it/s]Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.39it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.43it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.56it/s]Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.16it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.27it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.60it/s]Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  8.28it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:11<00:00,  8.48it/s]Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.34it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  7.94it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.46it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.44it/s]
  Epoch 2 Fold 1 complete! Validation Loss : 4.771525974273682
  Best validation loss improved from 5.010769271850586 to 4.771525974273682
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.45it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:11,  8.70it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.40it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.44it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.46it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.26it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.53it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:10,  8.64it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.25it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:10,  8.33it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:02<00:09,  8.49it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:10,  8.10it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.24it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.42it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.31it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:02<00:09,  8.50it/s]Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.08it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.53it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.46it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.64it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.42it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.61it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.22it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.67it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.13it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:07,  8.29it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.36it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.22it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.27it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.55it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:05<00:07,  8.10it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.01it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.39it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.53it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.15it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:06,  8.36it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:06<00:06,  7.98it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.18it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.16it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.49it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.13it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:05,  8.27it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.48it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:07<00:04,  8.75it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.48it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.62it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.44it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  8.45it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:03,  8.61it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:08<00:03,  8.71it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.26it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.46it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.32it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.64it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.73it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:09<00:02,  8.24it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:09<00:02,  8.46it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.30it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.39it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.22it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:10<00:01,  8.52it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.51it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.51it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.66it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.44it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.46it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  8.67it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:11<00:00,  8.75it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.56it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.68it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.49it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.41it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.57it/s]
  Epoch 2 Fold 2 complete! Validation Loss : 4.585336675643921
  Best validation loss improved from 4.771525974273682 to 4.585336675643921
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.46it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.61it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.95it/s]Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.63it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.57it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.70it/s]Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.42it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.68it/s]Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.47it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.47it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.47it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.68it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.62it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.39it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.60it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.57it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.51it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.71it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.77it/s]Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.60it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.78it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.84it/s]Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.36it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.14it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:07,  8.33it/s]Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.58it/s]Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:07,  8.12it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.52it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.64it/s]Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.47it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.70it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.79it/s]Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.57it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.55it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.83it/s]Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.72it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.82it/s]Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.56it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.78it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.52it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.85it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.90it/s]Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.66it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.59it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.86it/s]Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.74it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.64it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.79it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.86it/s]Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.63it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.80it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.87it/s]Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.63it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.57it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.68it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.82it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.71it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.82it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  9.01it/s]Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.63it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.79it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.85it/s]Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.63it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.81it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.87it/s]Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.63it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.66it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.56it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 2 Fold 3 complete! Validation Loss : 4.2668476390838626
  Best validation loss improved from 4.585336675643921 to 4.2668476390838626
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:09,  9.98it/s]Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:12,  7.90it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.60it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.81it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.88it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.61it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.72it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.63it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.79it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  9.01it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.59it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.78it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.67it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.81it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.70it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.63it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.76it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:07,  8.96it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.60it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.78it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.84it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.44it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.61it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.77it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.67it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.80it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:04<00:06,  9.00it/s]Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.60it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.78it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.67it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.81it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.70it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.79it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.68it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.81it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.71it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.83it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.71it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.82it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.87it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.67it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.60it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.76it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.67it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.80it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.86it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.66it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.75it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.53it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.51it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.72it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.96it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.55it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.76it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.65it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.60it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.76it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.67it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.66it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.73it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.54it/s]
  Epoch 2 Fold 4 complete! Validation Loss : 4.050106391906739
  Best validation loss improved from 4.2668476390838626 to 4.050106391906739
  Validation loss decreased (5.157646 --> 4.050106).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.84it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.99it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.75it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.90it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.74it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:09,  8.86it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:09,  8.91it/s]Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.68it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.84it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.90it/s]Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.64it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.75it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.66it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.61it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.76it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.48it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.67it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.61it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.76it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:03<00:07,  8.81it/s]Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.63it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.72it/s]Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.54it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:07,  8.67it/s]Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.46it/s]Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.73it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:04<00:06,  8.81it/s]Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.56it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.69it/s]Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.48it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.49it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.57it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.67it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.62it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.76it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.68it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.62it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.59it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.78it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.84it/s]Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.64it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.74it/s]Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.54it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.53it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.64it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.89it/s]Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.59it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.55it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.74it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.81it/s]Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.59it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.78it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.85it/s]Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.62it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.56it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.76it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.65it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.59it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.82it/s]Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.48it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.71it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.80it/s]Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.58it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.69it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.54it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 3 Fold 0 complete! Validation Loss : 3.982960653305054
  Best validation loss improved from 4.050106391906739 to 3.982960653305054
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:10,  9.11it/s]Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:12,  7.77it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.55it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.52it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.75it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.63it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.80it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:09,  8.94it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.61it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.80it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.85it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.62it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.56it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.67it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.14it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.58it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.67it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.48it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.71it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.63it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.79it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.84it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.59it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.77it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.85it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.62it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.81it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.87it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.35it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.64it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.59it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.77it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.84it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.63it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.59it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.77it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.85it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.64it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.82it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:06<00:04,  8.88it/s]Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.66it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.82it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.89it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.66it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.60it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.79it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.69it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.83it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.73it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.66it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.57it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.74it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.81it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.63it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.59it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.77it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.68it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.82it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.88it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.68it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.62it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.79it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.69it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.70it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.53it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 3 Fold 1 complete! Validation Loss : 3.8134638118743895
  Best validation loss improved from 3.982960653305054 to 3.8134638118743895
  Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.50it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.87it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.69it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.85it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.91it/s]Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.68it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:09,  8.86it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:09,  8.92it/s]Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.67it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.61it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.79it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.70it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.84it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.73it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.86it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.91it/s]Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.70it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.64it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.80it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.70it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.64it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.79it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.71it/s]Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.83it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.73it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.67it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.81it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.87it/s]Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.71it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.64it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.81it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.87it/s]Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.66it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.60it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.78it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.69it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.83it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.89it/s]Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.68it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.79it/s]Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.57it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.55it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.76it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.68it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.83it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.88it/s]Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.66it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.83it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.90it/s]Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.67it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.61it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.79it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.85it/s]Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.64it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.60it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.78it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.85it/s]Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.55it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:10<00:00,  8.77it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.85it/s]Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.63it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.74it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.49it/s]
  Epoch 3 Fold 2 complete! Validation Loss : 3.7048409271240232
  Best validation loss improved from 3.8134638118743895 to 3.7048409271240232
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.49it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.85it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.93it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.63it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.59it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.80it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.85it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.64it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.59it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.78it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.69it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.83it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:08,  8.89it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.56it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.70it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.85it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.91it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.19it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.52it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.64it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.47it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.73it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.82it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.61it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.57it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.77it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.68it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.63it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.78it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:05,  8.84it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.40it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.66it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:05<00:05,  8.76it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.57it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.55it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.76it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.83it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.61it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.82it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:07<00:04,  8.89it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.66it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.78it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.54it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.71it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.62it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.80it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.86it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.40it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.66it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.76it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.56it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.70it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.50it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.67it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.47it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.49it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.72it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.65it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.80it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.87it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.66it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.60it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.78it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.70it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.84it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.88it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.69it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.57it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 3 Fold 3 complete! Validation Loss : 3.470324602127075
  Best validation loss improved from 3.7048409271240232 to 3.470324602127075
  Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.51it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.51it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.79it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.87it/s]Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.63it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.58it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.78it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.68it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.70it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.57it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.55it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.73it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:02<00:08,  8.80it/s]Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.62it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.59it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.77it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.84it/s]Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.61it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.81it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.88it/s]Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.65it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.60it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.72it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.80it/s]Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.60it/s]Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.57it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.77it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.84it/s]Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.38it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.43it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.47it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.49it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.50it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.50it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.51it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.51it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.69it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.76it/s]Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.59it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.56it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.55it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:07<00:03,  8.66it/s]Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.26it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.57it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.68it/s]Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.51it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:03,  7.88it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.30it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.46it/s]Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.22it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.59it/s]Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.42it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.47it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.62it/s]Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.45it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.48it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.70it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.64it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.80it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.71it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.83it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.89it/s]Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.61it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.49it/s]
  Epoch 3 Fold 4 complete! Validation Loss : 3.340862913131714
  Best validation loss improved from 3.470324602127075 to 3.340862913131714
  Validation loss decreased (4.050106 --> 3.340863).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.51it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.59it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.83it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.91it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.65it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.59it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.78it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.69it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.83it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.89it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.68it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.61it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.58it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.44it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.40it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.52it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.17it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.30it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.38it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.52it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:08,  8.16it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.29it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.46it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.34it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:07,  8.53it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  7.59it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:07,  7.97it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.16it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.43it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.56it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.43it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.47it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.70it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.64it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.79it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.85it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.66it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.60it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.57it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.75it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.82it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.63it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.81it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:08<00:03,  8.87it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.65it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.59it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.57it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.76it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.68it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.82it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.87it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.67it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.62it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.58it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  8.69it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.52it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.77it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.55it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.54it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.76it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.66it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.62it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.59it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.48it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 4 Fold 0 complete! Validation Loss : 3.353330364227295
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:10,  9.10it/s]Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.39it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.47it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.77it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.66it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.61it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.78it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.70it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.78it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:10,  7.91it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.28it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.56it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.67it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.51it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.52it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.71it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.81it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.61it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.58it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.77it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.85it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.63it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.81it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.88it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.65it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.84it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.90it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.39it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.44it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.69it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.63it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.79it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:05<00:05,  8.85it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.65it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.76it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.56it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.55it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.68it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.49it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.42it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.66it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.76it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.51it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  8.29it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.47it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.09it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.48it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.50it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.71it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.64it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.79it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.85it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.66it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.81it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.88it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.65it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.60it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.57it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.68it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.51it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.51it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.72it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.81it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.60it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.57it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.64it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.47it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 4 Fold 1 complete! Validation Loss : 3.236436710357666
  Best validation loss improved from 3.340862913131714 to 3.236436710357666
  Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:10,  9.14it/s]Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.40it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.48it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.78it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.67it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.83it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.89it/s]Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:11,  7.93it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.36it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.41it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.65it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.42it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.45it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.65it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.61it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.77it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.83it/s]Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.65it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.75it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.82it/s]Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.62it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.59it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.77it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.85it/s]Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.63it/s]Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.59it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:04<00:06,  8.70it/s]Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.26it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.59it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.71it/s]Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.52it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.52it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.74it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.81it/s]Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.61it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:04,  8.81it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.88it/s]Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.64it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.59it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.78it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.85it/s]Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.64it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.59it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.77it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:07<00:03,  8.84it/s]Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.64it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.83it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.89it/s]Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.66it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.77it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.85it/s]Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.63it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.59it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.78it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.69it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.83it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  8.89it/s]Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.68it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.63it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.59it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.76it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.68it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.82it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.88it/s]Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.68it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.50it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 4 Fold 2 complete! Validation Loss : 3.1667442512512207
  Best validation loss improved from 3.236436710357666 to 3.1667442512512207
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.50it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.74it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.86it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.58it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.56it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.78it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.85it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.36it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.65it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.83it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.89it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.67it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.60it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.79it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:02<00:08,  8.86it/s]Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.65it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.83it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.89it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.66it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.59it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.79it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.70it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.83it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.73it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.66it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.80it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:04<00:06,  8.86it/s]Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.67it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.40it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.57it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.54it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.73it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.80it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.62it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.58it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.77it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.69it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.83it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.73it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.65it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.61it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.76it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.68it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.81it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.87it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.68it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.63it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.80it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.70it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.64it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.79it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.85it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.65it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.82it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.67it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.82it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.88it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.68it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.85it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.89it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.72it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.37it/s]
  Epoch 4 Fold 3 complete! Validation Loss : 2.9404092741012575
  Best validation loss improved from 3.1667442512512207 to 2.9404092741012575
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:10,  9.06it/s]Batch 2 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.74it/s]Batch 4 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.92it/s]Batch 6 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.97it/s]Batch 7 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.69it/s]Batch 8 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.62it/s]Batch 10 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:09,  8.81it/s]Batch 12 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:09,  8.88it/s]Batch 13 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.66it/s]Batch 14 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.84it/s]Batch 16 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.91it/s]Batch 17 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.66it/s]Batch 18 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.77it/s]Batch 20 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:08,  8.85it/s]Batch 21 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.35it/s]Batch 22 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.43it/s]Batch 24 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.26it/s]Batch 26 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.34it/s]Batch 28 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.59it/s]Batch 30 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.69it/s]Batch 31 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.53it/s]Batch 32 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.52it/s]Batch 34 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.72it/s]Batch 36 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.80it/s]Batch 37 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.61it/s]Batch 38 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.72it/s]Batch 39 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.52it/s]Batch 40 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.77it/s]Batch 42 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:04<00:06,  8.84it/s]Batch 43 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.61it/s]Batch 44 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.56it/s]Batch 46 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.47it/s]Batch 48 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.37it/s]Batch 50 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.48it/s]Batch 52 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.58it/s]Batch 54 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.55it/s]Batch 56 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.54it/s]Batch 58 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.53it/s]Batch 60 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.53it/s]Batch 62 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.46it/s]Batch 64 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:04,  8.58it/s]Batch 65 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  8.45it/s]Batch 66 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.60it/s]Batch 67 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.44it/s]Batch 68 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.47it/s]Batch 70 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.48it/s]Batch 72 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.50it/s]Batch 74 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.51it/s]Batch 76 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.70it/s]Batch 78 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.78it/s]Batch 79 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.59it/s]Batch 80 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.71it/s]Batch 81 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.53it/s]Batch 82 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.81it/s]Batch 83 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.40it/s]Batch 84 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.42it/s]Batch 86 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.67it/s]Batch 88 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.77it/s]Batch 89 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.57it/s]Batch 90 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.56it/s]Batch 92 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.54it/s]Batch 94 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.53it/s]Batch 96 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.53it/s]Batch 98 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.1 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.60it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.35it/s]
  Epoch 4 Fold 4 complete! Validation Loss : 2.924403314590454
  Best validation loss improved from 2.9404092741012575 to 2.924403314590454
  Validation loss decreased (3.340863 --> 2.924403).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.52it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.52it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.79it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.68it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.84it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.90it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.68it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.62it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.80it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.86it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.64it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.60it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.57it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.55it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.54it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.50it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.51it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.69it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.77it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:08,  7.93it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.14it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.46it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:07,  8.59it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.45it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.47it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.48it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.50it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.69it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.77it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.59it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.55it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.54it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.73it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.81it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.61it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.57it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.56it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.75it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.82it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.63it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.58it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.70it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.78it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.60it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.57it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.55it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.53it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.65it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.50it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.64it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.47it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.64it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.44it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.47it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.49it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.70it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.79it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.59it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.73it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.52it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.51it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.52it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.57it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.57it/s]
  Epoch 5 Fold 0 complete! Validation Loss : 2.922291669845581
  Best validation loss improved from 2.924403314590454 to 2.922291669845581
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:10,  9.11it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:10,  9.12it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.23it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.39it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.45it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.70it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.64it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.80it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.71it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.65it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.80it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.71it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.83it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.73it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.85it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:07,  8.90it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.70it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.63it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.80it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.71it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.84it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.73it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.81it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.72it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.66it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.79it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.71it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.84it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.89it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.69it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:04,  8.85it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.90it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.67it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.62it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.80it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.70it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.84it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.89it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.69it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:07<00:03,  8.85it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.91it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.68it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.52it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.53it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.73it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.66it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.80it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.86it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.67it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.78it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.85it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.64it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.37it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.41it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.65it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.61it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.70it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.54it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.71it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.52it/s]
  Epoch 5 Fold 1 complete! Validation Loss : 2.8075363540649416
  Best validation loss improved from 2.922291669845581 to 2.8075363540649416
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:10,  9.09it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.73it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.91it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.76it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.67it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.62it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.72it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.85it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.90it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.67it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.85it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:08,  8.91it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.67it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.61it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.80it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.70it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:07,  8.83it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.73it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.85it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.74it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:06,  8.86it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.91it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.47it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.49it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.71it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.84it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:05,  8.89it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.68it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.62it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.80it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.71it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.78it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.59it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.73it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:06<00:04,  8.82it/s]Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.61it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.81it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.88it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.64it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.60it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.79it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:07<00:03,  8.86it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.65it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.59it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.78it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.69it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.83it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.73it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.85it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.89it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.69it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.63it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.79it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.86it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.60it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.57it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.77it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.84it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:10<00:00,  8.64it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.83it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.88it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.75it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.47it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 5 Fold 2 complete! Validation Loss : 2.776853151321411
  Best validation loss improved from 2.8075363540649416 to 2.776853151321411
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.49it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.53it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.79it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.68it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.62it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.78it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:09,  8.85it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.65it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.60it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.78it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.85it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.63it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.59it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.78it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.85it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.64it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.82it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:07,  8.88it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.58it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.80it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.87it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.63it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.82it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.88it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.65it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.85it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.91it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.67it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.60it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.78it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:05,  8.85it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.64it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.59it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.78it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.69it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:04,  8.83it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.88it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.68it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.61it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.80it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.71it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.65it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.80it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.71it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.82it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.68it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.82it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.73it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.85it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.90it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.70it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.64it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.81it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.87it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.66it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.60it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.78it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.85it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.64it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:10<00:00,  8.59it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.78it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.84it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.74it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.50it/s]
  Epoch 5 Fold 3 complete! Validation Loss : 2.59855770111084
  Best validation loss improved from 2.776853151321411 to 2.59855770111084
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.81it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  9.00it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  9.04it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.69it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.89it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.95it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.68it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.62it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.58it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.77it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.68it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.82it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:08,  8.88it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.68it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.61it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.79it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.69it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:07,  8.83it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.73it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.84it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:03<00:07,  8.90it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.69it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.85it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.91it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.68it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.62it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.80it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.87it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.58it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.79it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.87it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.64it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.83it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.89it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.65it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.60it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.79it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.69it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.83it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.89it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.68it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.62it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.79it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:07<00:03,  8.70it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.64it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.79it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.86it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.65it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.76it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.55it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.79it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.86it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.64it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.59it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.76it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.67it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.77it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.69it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.82it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.88it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:10<00:00,  8.67it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.62it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.75it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.38it/s]
  Epoch 5 Fold 4 complete! Validation Loss : 2.6215556621551515
  Validation loss decreased (2.924403 --> 2.621556).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.51it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.87it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.95it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.65it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.86it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.93it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.67it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.78it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.45it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.74it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.65it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.81it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.71it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.85it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.74it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.86it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.90it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.69it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.63it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.79it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.86it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.65it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.82it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.89it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.66it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.61it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.80it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.70it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.83it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:05,  8.89it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.68it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.63it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.79it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.86it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.64it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.77it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.85it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.63it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.59it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.78it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.69it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.84it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.74it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:07<00:03,  8.84it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.90it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.67it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.84it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.89it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.67it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.61it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.79it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.85it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.64it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.76it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.55it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.53it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.75it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.67it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.82it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.73it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:10<00:00,  8.66it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.74it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.34it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.72it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.50it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 6 Fold 0 complete! Validation Loss : 2.621947422027588
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.51it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.52it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.52it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.75it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.82it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.61it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.58it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.64it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.72it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.85it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.90it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.69it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.63it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.39it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.62it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.72it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.02it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.42it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:08,  8.56it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.41it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.44it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.68it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.78it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.59it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.56it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:07,  7.97it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.15it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.33it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.25it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.44it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.32it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.52it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:06,  7.80it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.10it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.26it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.34it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.41it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.45it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.47it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.49it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  8.50it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:03,  8.50it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.64it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.73it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.57it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.55it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.66it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.50it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.51it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.52it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.52it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.34it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.57it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  8.46it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.35it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.42it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.64it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.74it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  8.31it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.40it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.55it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  7.69it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.47it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.21it/s]
  Epoch 6 Fold 1 complete! Validation Loss : 2.524854736328125
  Best validation loss improved from 2.59855770111084 to 2.524854736328125
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.47it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.85it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.93it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.30it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.41it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.42it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.45it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:10,  8.58it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  7.97it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:10,  8.32it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:10,  8.13it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:02<00:09,  8.38it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.26it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.49it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.03it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.25it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.58it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.70it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.51it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.51it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.52it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.72it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:07,  8.64it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.78it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.34it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.52it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.52it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.35it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.57it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.56it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.72it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:05<00:05,  8.80it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.61it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.58it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.76it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.68it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.62it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.77it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.84it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.64it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.75it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.55it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.70it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.50it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.51it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.72it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.81it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.61it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.58it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.55it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.75it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.81it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.62it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.52it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.72it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  8.81it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.48it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.58it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.61it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.74it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:11<00:00,  8.89it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.68it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.61it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.58it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.35it/s]
  Epoch 6 Fold 2 complete! Validation Loss : 2.5069783878326417
  Best validation loss improved from 2.524854736328125 to 2.5069783878326417
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.50it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.87it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.95it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.63it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.58it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.79it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.64it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.80it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.85it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.64it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.59it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.57it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.75it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.67it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.80it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.86it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.67it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.60it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.77it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.69it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.83it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.88it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.44it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.69it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.62it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.78it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.85it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.65it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.61it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.79it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.69it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.27it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.43it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.46it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.65it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:07<00:04,  8.73it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.34it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.41it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.64it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.74it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.56it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.55it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.75it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.83it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.37it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.65it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.74it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.55it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.54it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.75it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.67it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.62it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.78it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.68it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.82it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.87it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.67it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.61it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.74it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.67it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.36it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 6 Fold 3 complete! Validation Loss : 2.318904986381531
  Best validation loss improved from 2.5069783878326417 to 2.318904986381531
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.50it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.87it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.94it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.62it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.77it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.52it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.70it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.48it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.49it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.73it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.81it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.60it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.57it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.77it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.68it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.82it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.78it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.85it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.65it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.61it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.78it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.69it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.83it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:04<00:07,  8.89it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.43it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.46it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.60it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.45it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.48it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.50it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.69it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.63it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.79it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.85it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.66it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.60it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.77it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.69it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.83it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.73it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.85it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.89it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.69it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:07<00:03,  8.79it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.50it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.75it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.66it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.61it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.78it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.70it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.65it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.79it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.85it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.66it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.76it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.55it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.54it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.75it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.82it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.62it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.58it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.78it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.84it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.69it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.33it/s]
  Epoch 6 Fold 4 complete! Validation Loss : 2.355167155265808
  Validation loss decreased (2.621556 --> 2.355167).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:10,  9.14it/s]Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:13,  7.30it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.01it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.00it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:11,  8.26it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:11,  8.19it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.43it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:11,  7.74it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.30it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.59it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.71it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.53it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:02<00:09,  8.68it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:10,  7.93it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.17it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.51it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.51it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.63it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.24it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.44it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.31it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.40it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.44it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.58it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:07,  8.34it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.38it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.64it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.74it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.56it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.55it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.54it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.53it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.71it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.79it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.61it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:06<00:05,  8.73it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.52it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.68it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.47it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.49it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:05,  8.29it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.19it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:07<00:04,  8.36it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  7.82it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  7.88it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:04,  8.12it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  7.86it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:08<00:04,  8.15it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:04,  7.84it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:08<00:03,  8.16it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  7.83it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.15it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.11it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.38it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  7.96it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:03,  8.28it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:09<00:02,  8.10it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:09<00:02,  8.38it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  7.95it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.27it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  7.59it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  7.99it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  7.44it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:10<00:02,  7.88it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:10<00:02,  7.63it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:10<00:01,  8.03it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  7.45it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  7.88it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  7.36it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  7.86it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:11<00:00,  8.11it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:11<00:00,  8.32it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  7.99it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.19it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.38it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.03it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:12<00:00,  8.25it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.23it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 7 Fold 0 complete! Validation Loss : 2.374077458381653
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:12,  7.84it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.22it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.11it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:11,  8.27it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.44it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.33it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.53it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.37it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:10,  8.57it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.36it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.43it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:02<00:09,  8.59it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.43it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.60it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.13it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.29it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.37it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.40it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.44it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.35it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.05it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.22it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:07,  8.33it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.48it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.37it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.43it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.44it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:05<00:06,  8.46it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.42it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.46it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.58it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.21it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:06,  8.33it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.60it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.70it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.53it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.75it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.83it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.61it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.58it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.56it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.35it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.58it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.68it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:03,  8.52it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:08<00:03,  8.66it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.49it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.50it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.72it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.80it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.60it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:09<00:02,  8.73it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.24it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.59it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.56it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.55it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.56it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.55it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.53it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.53it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  8.71it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:11<00:00,  8.79it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.56it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.55it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.48it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.35it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 7 Fold 1 complete! Validation Loss : 2.281479949951172
  Best validation loss improved from 2.318904986381531 to 2.281479949951172
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.51it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.52it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.53it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.52it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.73it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.65it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.65it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.61it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.57it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.55it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.65it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.25it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.56it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.67it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.51it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.65it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.46it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.49it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.63it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.46it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.63it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.43it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.61it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.43it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.47it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.49it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.51it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.51it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.51it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.52it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.52it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.70it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.77it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.36it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.43it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:05,  8.39it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.43it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.45it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.48it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  8.50it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.48it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:08<00:03,  8.39it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.09it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.30it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  7.51it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  7.88it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  7.41it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:09<00:03,  7.86it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:09<00:02,  8.12it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  7.38it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  7.78it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  7.84it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.17it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  7.57it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:10<00:02,  7.75it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.03it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.20it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.31it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.46it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:11<00:00,  8.12it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  8.07it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.23it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.26it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.41it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.36it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.12it/s]
  Epoch 7 Fold 2 complete! Validation Loss : 2.25589955329895
  Best validation loss improved from 2.281479949951172 to 2.25589955329895
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.52it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:11,  8.75it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.03it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:11,  8.39it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  7.92it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:11,  8.27it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:11,  7.87it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.42it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.59it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.42it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:10,  8.60it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.12it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:10,  8.30it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:10,  8.17it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.10it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.06it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.16it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:09,  7.94it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.14it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.10it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.31it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:09,  7.74it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  7.85it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:08,  8.08it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.28it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:08,  7.97it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  7.98it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:07,  7.98it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:08,  7.32it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:05<00:07,  7.48it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:05<00:08,  7.15it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:05<00:07,  7.33it/s]Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:08,  6.99it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:07,  7.50it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:07,  6.92it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:07,  7.45it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:06<00:07,  6.88it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:06<00:06,  7.42it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:06<00:07,  6.85it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:06<00:06,  7.40it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:07,  6.84it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:06,  7.15it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:06,  6.69it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:07<00:06,  7.28it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:07<00:06,  6.74it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:07<00:05,  7.31it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:07<00:06,  6.96it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:07<00:05,  7.50it/s]Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:05,  6.90it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:07<00:05,  7.20it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:08<00:05,  6.72it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:08<00:05,  7.29it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:08<00:05,  6.77it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:08<00:04,  7.33it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:08<00:04,  6.80it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:08<00:04,  7.36it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:08<00:04,  6.82it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:09<00:04,  7.38it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:09<00:04,  7.05it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:09<00:03,  7.30it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:09<00:04,  7.00it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:09<00:03,  7.53it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:09<00:03,  6.89it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:09<00:03,  7.43it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:10<00:03,  6.86it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:10<00:03,  7.41it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:10<00:03,  6.84it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:10<00:02,  7.15it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:10<00:02,  6.91it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:10<00:02,  6.97it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:10<00:02,  6.58it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:11<00:02,  7.18it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:11<00:02,  6.92it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:11<00:02,  6.97it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:11<00:02,  6.38it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:11<00:01,  6.79it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:11<00:01,  6.47it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:11<00:01,  7.09it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:12<00:01,  6.87it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:12<00:01,  7.17it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:12<00:01,  6.70it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:12<00:00,  7.27it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:12<00:00,  6.77it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:12<00:00,  7.09it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:12<00:00,  7.09it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:13<00:00,  7.60it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:13<00:00,  6.95it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:13<00:00,  7.44it/s]
  100%|██████████| 25/25 [00:01<00:00, 13.51it/s]
  Epoch 7 Fold 3 complete! Validation Loss : 2.1010475826263426
  Best validation loss improved from 2.25589955329895 to 2.1010475826263426
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:10,  9.14it/s]Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:14,  6.82it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:12,  7.71it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:13,  7.14it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:12,  7.42it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:13,  7.03it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:12,  7.56it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:01<00:13,  6.90it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:12,  7.44it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:13,  6.85it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:11,  7.42it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:12,  7.08it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:11,  7.33it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:12,  7.02it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:02<00:11,  7.51it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:02<00:12,  6.90it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:02<00:11,  7.45it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:11,  6.87it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:11,  7.36it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:11,  7.04it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:10,  7.52it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:03<00:11,  6.91it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:03<00:10,  7.41it/s]Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:03<00:10,  7.07it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:03<00:10,  7.33it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:10,  7.02it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:10,  7.29it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:10,  6.99it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:04<00:09,  7.23it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:04<00:10,  6.95it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:04<00:09,  7.40it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:04<00:09,  7.04it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:04<00:09,  7.29it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:09,  7.00it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:08,  7.52it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:05<00:09,  6.91it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:05<00:08,  7.45it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:05<00:08,  7.09it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:05<00:08,  7.34it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:05<00:08,  7.03it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:05<00:07,  7.55it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:05<00:08,  6.93it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:05<00:07,  7.47it/s]Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:06<00:07,  7.11it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:06<00:07,  7.35it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:06<00:07,  6.99it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:06<00:07,  7.52it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:06<00:07,  6.91it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:06<00:06,  7.46it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:06<00:07,  7.10it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:07<00:06,  7.60it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:07<00:06,  6.96it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:07<00:06,  7.49it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:07<00:06,  7.13it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:07<00:06,  7.49it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:07<00:06,  6.89it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:07<00:05,  7.43it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:08<00:05,  7.08it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:08<00:05,  7.59it/s]Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:08<00:05,  6.95it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:08<00:05,  7.49it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:08<00:05,  6.90it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:08<00:04,  7.45it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:08<00:05,  7.09it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:08<00:04,  7.59it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:09<00:04,  7.71it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:09<00:04,  8.08it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:09<00:04,  7.24it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:09<00:04,  7.72it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:09<00:04,  7.23it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:09<00:03,  7.72it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:09<00:03,  7.02it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:10<00:03,  7.54it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:10<00:03,  6.92it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:10<00:03,  7.46it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:10<00:03,  6.88it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:10<00:03,  7.43it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:10<00:03,  6.86it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:10<00:02,  7.41it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:11<00:02,  7.04it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:11<00:02,  7.55it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:11<00:02,  6.93it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:11<00:02,  7.47it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:11<00:02,  7.12it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:11<00:02,  7.36it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:11<00:01,  7.04it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:12<00:01,  7.29it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:12<00:01,  6.99it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:12<00:01,  7.52it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:12<00:01,  6.92it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:12<00:01,  7.46it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:12<00:01,  7.02it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:12<00:00,  7.28it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:13<00:00,  6.99it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:13<00:00,  7.52it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:13<00:00,  6.91it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:13<00:00,  7.46it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:13<00:00,  6.88it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:13<00:00,  7.43it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:13<00:00,  7.23it/s]
  100%|██████████| 25/25 [00:01<00:00, 13.27it/s]
  Epoch 7 Fold 4 complete! Validation Loss : 2.162189245223999
  Validation loss decreased (2.355167 --> 2.162189).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:10,  9.14it/s]Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:14,  6.83it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:12,  7.71it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:14,  6.82it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:12,  7.51it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:13,  7.09it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:12,  7.37it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:01<00:13,  6.90it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:12,  7.46it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:13,  6.83it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:12,  7.40it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:12,  7.06it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:11,  7.58it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:12,  6.95it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:02<00:11,  7.49it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:02<00:12,  6.89it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:02<00:11,  7.44it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:12,  6.82it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:10,  7.38it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:11,  7.02it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:10,  7.55it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:03<00:11,  6.93it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:03<00:10,  7.47it/s]Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:03<00:11,  6.88it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:03<00:10,  7.42it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:10,  6.84it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:09,  7.40it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:10,  6.84it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:04<00:09,  7.40it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:04<00:10,  6.83it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:04<00:09,  7.40it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:04<00:09,  7.06it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:04<00:09,  7.31it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:09,  7.01it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:08,  7.54it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:05<00:09,  6.71it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   37%|███▋      | 37/100 [00:05<00:08,  7.29it/s]Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:05<00:09,  6.77it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:05<00:08,  7.33it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:05<00:08,  7.03it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:05<00:08,  7.25it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:05<00:07,  7.64it/s]Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:06<00:07,  7.19it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:06<00:07,  7.50it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:06<00:06,  7.83it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:06<00:06,  7.63it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:06<00:06,  7.98it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:06<00:06,  7.48it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:07<00:06,  7.50it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:07<00:06,  7.83it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:07<00:06,  7.62it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:07<00:05,  7.98it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:07<00:05,  7.71it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:07<00:05,  8.07it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:07<00:05,  7.35it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:08<00:05,  7.35it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:08<00:05,  7.72it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:08<00:05,  7.54it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:08<00:04,  7.90it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:08<00:04,  7.66it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:08<00:04,  8.03it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:08<00:04,  7.24it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:09<00:04,  7.44it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:09<00:04,  6.87it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:09<00:04,  7.34it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:09<00:03,  7.71it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:09<00:03,  7.54it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:09<00:03,  7.92it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:10<00:03,  7.94it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:10<00:03,  7.75it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:10<00:02,  8.03it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:10<00:02,  8.39it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:10<00:02,  8.53it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:10<00:02,  8.16it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:11<00:01,  8.48it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:11<00:01,  8.62it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:11<00:01,  8.45it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:11<00:01,  8.26it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:11<00:01,  8.36it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:12<00:00,  8.42it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:12<00:00,  8.54it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:12<00:00,  8.42it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:12<00:00,  8.58it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:12<00:00,  8.14it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:12<00:00,  8.30it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:13<00:00,  7.63it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.23it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 8 Fold 0 complete! Validation Loss : 2.1573082780838013
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.50it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:11,  8.74it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.41it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.45it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.73it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.83it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.23it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.34it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.62it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.58it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.76it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.83it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.63it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.75it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.55it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.78it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.86it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.63it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.56it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:07,  8.76it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.67it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.62it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.59it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.75it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.82it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.63it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.80it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:04<00:06,  8.87it/s]Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.63it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.59it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.78it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.85it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.63it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.59it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.73it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.66it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.80it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:06<00:04,  8.86it/s]Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.66it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.61it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.58it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.75it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.82it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.62it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.66it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.53it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.72it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.79it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.59it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.57it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.76it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.68it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.82it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.87it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.67it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  8.78it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.57it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.79it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.87it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.63it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.58it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.78it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.64it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.69it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.24it/s]
  Epoch 8 Fold 1 complete! Validation Loss : 2.08629105091095
  Best validation loss improved from 2.1010475826263426 to 2.08629105091095
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:10,  9.09it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    3%|▎         | 3/100 [00:00<00:10,  9.09it/s]Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.22it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.67it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.79it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.56it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.72it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.45it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.48it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.72it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.81it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.60it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.34it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.61it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.58it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.76it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.63it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.77it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.84it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.64it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.60it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.58it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.75it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.67it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.81it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.87it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.66it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.61it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.78it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.69it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.83it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:05<00:05,  8.89it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.68it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.62it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.78it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.85it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.65it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.60it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.78it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.85it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.64it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.59it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.78it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.64it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.79it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.70it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.83it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.89it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.69it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.62it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.79it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.86it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.65it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.64it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.89it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.55it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.83it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.89it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.66it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.93it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.50it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.77it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.85it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.61it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.72it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.21it/s]
  Epoch 8 Fold 2 complete! Validation Loss : 2.0776167345046996
  Best validation loss improved from 2.08629105091095 to 2.0776167345046996
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.48it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.86it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.71it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.64it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.81it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.71it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.84it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.89it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.67it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.83it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.88it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.66it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.61it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.79it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.70it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.63it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:07,  8.79it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.71it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.83it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:03<00:07,  8.86it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.69it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.63it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.80it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.64it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.80it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.86it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.66it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.77it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.57it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.55it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.76it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.66it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:04,  8.82it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.72it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.84it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:06<00:04,  8.89it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.69it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.62it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.80it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.71it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.84it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.89it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.68it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.62it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.80it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.86it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.65it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.60it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.22it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.17it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.30it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.56it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.42it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.46it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.48it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.50it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.69it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.78it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.59it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.76it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.84it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.69it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.35it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 8 Fold 3 complete! Validation Loss : 1.8750938415527343
  Best validation loss improved from 2.0776167345046996 to 1.8750938415527343
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.53it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.88it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.94it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.64it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.85it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.92it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.66it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.60it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.63it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.79it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.78it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.55it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.55it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.75it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.66it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.81it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.72it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:07,  8.84it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.88it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.69it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.61it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.59it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.76it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.68it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.81it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.54it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.37it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.25it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:06,  8.33it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:05<00:05,  8.45it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.36it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.52it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.13it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.37it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  7.92it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:05,  8.21it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:05,  7.86it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.38it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:07<00:04,  8.56it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.41it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.59it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.42it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:04,  8.47it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.70it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:08<00:03,  8.79it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.59it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.56it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.68it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.23it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.44it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.03it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:09<00:02,  8.31it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  7.93it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.25it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  7.35it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  7.84it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.09it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:10<00:01,  8.44it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:10<00:01,  8.57it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.44it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.60it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.43it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.46it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:11<00:00,  8.49it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.71it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.79it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.53it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.66it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.51it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.36it/s]
  Epoch 8 Fold 4 complete! Validation Loss : 2.0041404581069946
  Validation loss decreased (2.162189 --> 2.004140).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:10,  9.14it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.73it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.90it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.96it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.69it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.81it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:11,  7.97it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.44it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.47it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.70it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   17%|█▋        | 17/100 [00:01<00:09,  8.78it/s]Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.59it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.74it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:08,  8.82it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.60it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.56it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.77it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.69it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.63it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.78it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.70it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.83it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.73it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.85it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.89it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.69it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.63it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.80it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:05,  8.86it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.65it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.60it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.78it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.70it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.64it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.79it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.70it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.65it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.74it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.66it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.80it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:07<00:03,  8.86it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.67it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.62it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.79it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.85it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.65it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.60it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.78it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.85it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.64it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.59it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.78it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.85it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.64it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.59it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.77it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.84it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.63it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.75it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.55it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.79it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.86it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.71it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.20it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 9 Fold 0 complete! Validation Loss : 1.9995397758483886
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.53it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.86it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.69it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.86it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.92it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.68it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.62it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.80it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.71it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.85it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.73it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.66it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.79it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.71it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.83it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.55it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.72it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.66it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.74it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.68it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.81it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.87it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.68it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.62it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.58it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.56it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.74it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.67it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.63it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.65it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.73it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.67it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.80it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.71it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.86it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.58it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.78it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:07<00:03,  8.85it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.64it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.82it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.88it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.65it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.60it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.79it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.64it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.80it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.86it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.66it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.77it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.56it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.54it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.76it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.83it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.62it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.58it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.78it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.69it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.72it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.39it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 9 Fold 1 complete! Validation Loss : 1.9378536367416381
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.47it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.85it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.94it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.64it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.77it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.66it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:09,  8.82it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:09,  8.89it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.67it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.62it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.78it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.85it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.64it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.83it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:02<00:08,  8.89it/s]Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.66it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.60it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.79it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.70it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.84it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.89it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.68it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.62it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.79it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.86it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.65it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.60it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.76it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.67it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.82it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.88it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.67it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.56it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.75it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.82it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.62it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.82it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   59%|█████▉    | 59/100 [00:06<00:04,  8.89it/s]Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.64it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.60it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.79it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.86it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.65it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.53it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.32it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.64it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.59it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.77it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.84it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.64it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.59it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.77it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.84it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.63it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.37it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.63it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.73it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.55it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.53it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.53it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.73it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.92it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.70it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.79it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.57it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.70it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.37it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 9 Fold 2 complete! Validation Loss : 1.9559195518493653
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    1%|          | 1/100 [00:00<00:10,  9.14it/s]Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.40it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.48it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:11,  8.50it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.50it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.72it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.66it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.81it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.86it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.66it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.60it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.78it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.70it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.79it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.85it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.64it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.60it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:07,  8.78it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.85it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.64it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.59it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.56it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.62it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.71it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.64it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.61it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.77it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.83it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.65it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.60it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.76it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.84it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.64it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.60it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.78it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.69it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.82it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.88it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.68it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.62it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.62it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.77it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.69it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.83it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.89it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.68it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.62it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.79it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.86it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.64it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.59it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.77it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.84it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.63it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.59it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.78it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.69it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.82it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   97%|█████████▋| 97/100 [00:11<00:00,  8.88it/s]Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.68it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.70it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.35it/s]
  Epoch 9 Fold 3 complete! Validation Loss : 1.7395631313323974
  Best validation loss improved from 1.8750938415527343 to 1.7395631313323974
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.50it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.86it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.70it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.86it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.92it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.66it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:09,  8.84it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:09,  8.90it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.66it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.60it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.79it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.70it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:08,  8.84it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   23%|██▎       | 23/100 [00:02<00:08,  8.88it/s]Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.67it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.60it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.78it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.85it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.64it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.59it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.78it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:03<00:07,  8.85it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.65it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.60it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.66it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.81it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   43%|████▎     | 43/100 [00:04<00:06,  8.88it/s]Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.67it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.62it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.79it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.69it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.83it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.89it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.67it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.61it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.78it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.69it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.83it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.89it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.69it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.62it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.79it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   69%|██████▉   | 69/100 [00:07<00:03,  8.86it/s]Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.65it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.60it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.78it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.84it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.64it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.59it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.78it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.85it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.63it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.85it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.61it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.57it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.78it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.69it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.64it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.77it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.83it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:10<00:00,  8.64it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.82it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.88it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.74it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.24it/s]
  Epoch 9 Fold 4 complete! Validation Loss : 1.8550338554382324
  Validation loss decreased (2.004140 --> 1.855034).  Saving model ...
    0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.53it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.53it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.83it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.90it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:11,  8.34it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.67it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.62it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.79it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.85it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:10,  8.38it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.44it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.27it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.35it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:09,  8.40it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.44it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.56it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.44it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   29%|██▉       | 29/100 [00:03<00:08,  8.66it/s]Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.21it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:08,  8.59it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:08,  8.17it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   33%|███▎      | 33/100 [00:03<00:07,  8.44it/s]Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:04<00:08,  8.10it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.37it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.43it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.66it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.61it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.59it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.76it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:06,  8.82it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.56it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.75it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:06<00:05,  8.67it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.82it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   55%|█████▌    | 55/100 [00:06<00:05,  8.88it/s]Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.43it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.68it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:07<00:04,  8.61it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.56it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.62it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.57it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.74it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.67it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.62it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.82it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.61it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.78it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.85it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:09<00:02,  8.64it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   79%|███████▉  | 79/100 [00:09<00:02,  8.76it/s]Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.55it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.53it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.75it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.83it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.62it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.59it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.78it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.83it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.89it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.67it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.62it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.80it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.85it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.62it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.24it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 10 Fold 0 complete! Validation Loss : 1.843567476272583
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:12,  7.96it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:11,  8.27it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.65it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.77it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.56it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.79it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   11%|█         | 11/100 [00:01<00:10,  8.87it/s]Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.34it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   13%|█▎        | 13/100 [00:01<00:10,  8.54it/s]Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:10,  8.38it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:10,  8.21it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.55it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.69it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.77it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.58it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.56it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:03<00:08,  8.74it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.81it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.62it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:07,  8.80it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.87it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.65it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.59it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.78it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.69it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.82it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   41%|████      | 41/100 [00:04<00:06,  8.88it/s]Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.68it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.62it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.78it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   47%|████▋     | 47/100 [00:05<00:05,  8.85it/s]Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.64it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.83it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:05<00:05,  8.90it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.67it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.60it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.79it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   57%|█████▋    | 57/100 [00:06<00:04,  8.85it/s]Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.64it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.60it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.78it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  9.00it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.72it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   65%|██████▌   | 65/100 [00:07<00:03,  8.82it/s]Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.60it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.55it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.76it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.83it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.62it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.58it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   75%|███████▌  | 75/100 [00:08<00:02,  8.70it/s]Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.52it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   77%|███████▋  | 77/100 [00:08<00:02,  8.78it/s]Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.44it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.72it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.64it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.80it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.86it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.66it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.60it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.78it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.69it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.64it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.79it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.70it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.66it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.36it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 10 Fold 1 complete! Validation Loss : 1.790725998878479
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.47it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.86it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.70it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.63it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.80it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.70it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.84it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   15%|█▌        | 15/100 [00:01<00:09,  8.89it/s]Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.68it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.62it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.80it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:08,  8.86it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.66it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.61it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.78it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.68it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:07,  8.83it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   31%|███       | 31/100 [00:03<00:07,  8.89it/s]Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.68it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.62it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.75it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.67it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.82it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.73it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.84it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.90it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.70it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.64it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.80it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   51%|█████     | 51/100 [00:05<00:05,  8.86it/s]Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.64it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.58it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.78it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.70it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.83it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   61%|██████    | 61/100 [00:06<00:04,  8.89it/s]Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.67it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.61it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.79it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.86it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.65it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.60it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.77it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   73%|███████▎  | 73/100 [00:08<00:03,  8.84it/s]Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.64it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.60it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.63it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.77it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.69it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.64it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.78it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   87%|████████▋ | 87/100 [00:09<00:01,  8.85it/s]Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.65it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.80it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.87it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.65it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.60it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:10<00:00,  8.78it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.68it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.77it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.73it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.38it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 10 Fold 2 complete! Validation Loss : 1.7660767769813537
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.53it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.88it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.96it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.64it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.94it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.63it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    9%|▉         | 9/100 [00:01<00:10,  8.76it/s]Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.52it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.53it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.76it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.67it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.62it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.78it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:08,  8.85it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.65it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.60it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.77it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   27%|██▋       | 27/100 [00:03<00:08,  8.84it/s]Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.64it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.60it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.75it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.67it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.62it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.78it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.85it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:07,  8.42it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.45it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.68it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.76it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.58it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:06,  8.56it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.59it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.76it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   53%|█████▎    | 53/100 [00:06<00:05,  8.82it/s]Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.63it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.57it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.76it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.67it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.81it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.87it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.67it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.61it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.57it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.75it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   71%|███████   | 71/100 [00:08<00:03,  8.82it/s]Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.39it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:03,  8.44it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.67it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.61it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.59it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.75it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   83%|████████▎ | 83/100 [00:09<00:01,  8.82it/s]Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.63it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.59it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.77it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   89%|████████▉ | 89/100 [00:10<00:01,  8.84it/s]Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.64it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.83it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   93%|█████████▎| 93/100 [00:10<00:00,  8.89it/s]Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.58it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   95%|█████████▌| 95/100 [00:10<00:00,  8.72it/s]Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  7.70it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.04it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.65it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.25it/s]
    0%|          | 0/100 [00:00<?, ?it/s]
  Epoch 10 Fold 3 complete! Validation Loss : 1.602610275745392
  Best validation loss improved from 1.7395631313323974 to 1.602610275745392
  Batch 0 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 1 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    2%|▏         | 2/100 [00:00<00:11,  8.53it/s]Batch 2 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 3 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    4%|▍         | 4/100 [00:00<00:10,  8.88it/s]Batch 4 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    5%|▌         | 5/100 [00:00<00:10,  8.94it/s]Batch 5 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    6%|▌         | 6/100 [00:00<00:10,  8.63it/s]Batch 6 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    7%|▋         | 7/100 [00:00<00:10,  8.78it/s]Batch 7 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
    8%|▊         | 8/100 [00:00<00:10,  8.53it/s]Batch 8 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 9 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   10%|█         | 10/100 [00:01<00:10,  8.53it/s]Batch 10 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 11 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   12%|█▏        | 12/100 [00:01<00:10,  8.76it/s]Batch 12 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 13 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   14%|█▍        | 14/100 [00:01<00:09,  8.67it/s]Batch 14 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 15 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   16%|█▌        | 16/100 [00:01<00:09,  8.62it/s]Batch 16 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 17 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   18%|█▊        | 18/100 [00:02<00:09,  8.78it/s]Batch 18 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   19%|█▉        | 19/100 [00:02<00:09,  8.85it/s]Batch 19 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   20%|██        | 20/100 [00:02<00:09,  8.65it/s]Batch 20 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   21%|██        | 21/100 [00:02<00:09,  8.76it/s]Batch 21 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   22%|██▏       | 22/100 [00:02<00:09,  8.46it/s]Batch 22 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 23 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   24%|██▍       | 24/100 [00:02<00:08,  8.73it/s]Batch 24 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   25%|██▌       | 25/100 [00:02<00:08,  8.82it/s]Batch 25 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   26%|██▌       | 26/100 [00:02<00:08,  8.61it/s]Batch 26 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 27 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   28%|██▊       | 28/100 [00:03<00:08,  8.58it/s]Batch 28 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 29 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   30%|███       | 30/100 [00:03<00:08,  8.55it/s]Batch 30 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 31 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   32%|███▏      | 32/100 [00:03<00:07,  8.53it/s]Batch 32 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 33 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   34%|███▍      | 34/100 [00:03<00:07,  8.73it/s]Batch 34 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   35%|███▌      | 35/100 [00:04<00:07,  8.80it/s]Batch 35 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   36%|███▌      | 36/100 [00:04<00:07,  8.62it/s]Batch 36 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 37 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   38%|███▊      | 38/100 [00:04<00:07,  8.80it/s]Batch 38 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   39%|███▉      | 39/100 [00:04<00:06,  8.87it/s]Batch 39 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   40%|████      | 40/100 [00:04<00:06,  8.65it/s]Batch 40 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 41 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   42%|████▏     | 42/100 [00:04<00:06,  8.59it/s]Batch 42 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 43 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   44%|████▍     | 44/100 [00:05<00:06,  8.79it/s]Batch 44 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   45%|████▌     | 45/100 [00:05<00:06,  8.86it/s]Batch 45 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   46%|████▌     | 46/100 [00:05<00:06,  8.65it/s]Batch 46 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 47 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   48%|████▊     | 48/100 [00:05<00:05,  8.83it/s]Batch 48 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   49%|████▉     | 49/100 [00:05<00:05,  8.89it/s]Batch 49 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   50%|█████     | 50/100 [00:05<00:05,  8.65it/s]Batch 50 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 51 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   52%|█████▏    | 52/100 [00:05<00:05,  8.60it/s]Batch 52 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 53 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   54%|█████▍    | 54/100 [00:06<00:05,  8.58it/s]Batch 54 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 55 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   56%|█████▌    | 56/100 [00:06<00:05,  8.76it/s]Batch 56 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 57 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   58%|█████▊    | 58/100 [00:06<00:04,  8.67it/s]Batch 58 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 59 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   60%|██████    | 60/100 [00:06<00:04,  8.63it/s]Batch 60 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 61 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   62%|██████▏   | 62/100 [00:07<00:04,  8.79it/s]Batch 62 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   63%|██████▎   | 63/100 [00:07<00:04,  8.85it/s]Batch 63 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   64%|██████▍   | 64/100 [00:07<00:04,  8.65it/s]Batch 64 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 65 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   66%|██████▌   | 66/100 [00:07<00:03,  8.75it/s]Batch 66 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   67%|██████▋   | 67/100 [00:07<00:03,  8.82it/s]Batch 67 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   68%|██████▊   | 68/100 [00:07<00:03,  8.62it/s]Batch 68 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 69 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   70%|███████   | 70/100 [00:08<00:03,  8.58it/s]Batch 70 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 71 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   72%|███████▏  | 72/100 [00:08<00:03,  8.57it/s]Batch 72 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 73 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   74%|███████▍  | 74/100 [00:08<00:02,  8.75it/s]Batch 74 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 75 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   76%|███████▌  | 76/100 [00:08<00:02,  8.67it/s]Batch 76 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 77 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   78%|███████▊  | 78/100 [00:08<00:02,  8.62it/s]Batch 78 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 79 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   80%|████████  | 80/100 [00:09<00:02,  8.77it/s]Batch 80 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   81%|████████  | 81/100 [00:09<00:02,  8.84it/s]Batch 81 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   82%|████████▏ | 82/100 [00:09<00:02,  8.64it/s]Batch 82 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 83 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   84%|████████▍ | 84/100 [00:09<00:01,  8.81it/s]Batch 84 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   85%|████████▌ | 85/100 [00:09<00:01,  8.87it/s]Batch 85 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   86%|████████▌ | 86/100 [00:09<00:01,  8.66it/s]Batch 86 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 87 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   88%|████████▊ | 88/100 [00:10<00:01,  8.61it/s]Batch 88 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 89 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   90%|█████████ | 90/100 [00:10<00:01,  8.78it/s]Batch 90 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   91%|█████████ | 91/100 [00:10<00:01,  8.85it/s]Batch 91 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   92%|█████████▏| 92/100 [00:10<00:00,  8.63it/s]Batch 92 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 93 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   94%|█████████▍| 94/100 [00:10<00:00,  8.37it/s]Batch 94 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 95 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   96%|█████████▌| 96/100 [00:11<00:00,  8.43it/s]Batch 96 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  Batch 97 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   98%|█████████▊| 98/100 [00:11<00:00,  8.66it/s]Batch 98 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
   99%|█████████▉| 99/100 [00:11<00:00,  8.75it/s]Batch 99 is on device: cuda:0
  Allocated: 2.2 GB
  Reserved: 3.6 GB
  100%|██████████| 100/100 [00:11<00:00,  8.69it/s]
  100%|██████████| 25/25 [00:01<00:00, 14.35it/s]
  Epoch 10 Fold 4 complete! Validation Loss : 1.7277302026748658
  Validation loss decreased (1.855034 --> 1.727730).  Saving model ...
  The model has been saved in models/bert_val_loss_1.60261_ep_10.pt
  

