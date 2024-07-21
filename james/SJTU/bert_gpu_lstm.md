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
C:\2024-movie\BERT-SJTU-NLU2023-main\venv\Scripts\python.exe C:\2024-movie\BERT-SJTU-NLU2023-main\bert_gpu_lstm.py 
Filtered dataset length: 2000
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
Allocated: 0.0 GB
Reserved: 0.0 GB
  1%|          | 1/100 [00:00<00:32,  3.06it/s]Batch 1 is on device: cuda:0
Allocated: 0.0 GB
Reserved: 0.2 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
  4%|▍         | 4/100 [00:00<00:09, 10.28it/s]Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
  7%|▋         | 7/100 [00:00<00:06, 14.64it/s]Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 10%|█         | 10/100 [00:00<00:05, 17.30it/s]Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 13%|█▎        | 13/100 [00:00<00:04, 18.59it/s]Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 16%|█▌        | 16/100 [00:00<00:04, 19.90it/s]Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 19%|█▉        | 19/100 [00:01<00:04, 19.88it/s]Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 22%|██▏       | 22/100 [00:01<00:03, 20.46it/s]Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 25%|██▌       | 25/100 [00:01<00:03, 21.47it/s]Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 28%|██▊       | 28/100 [00:01<00:03, 21.53it/s]Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 31%|███       | 31/100 [00:01<00:03, 22.35it/s]Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 34%|███▍      | 34/100 [00:01<00:03, 21.67it/s]Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 37%|███▋      | 37/100 [00:01<00:02, 21.97it/s]Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 40%|████      | 40/100 [00:02<00:02, 22.37it/s]Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 43%|████▎     | 43/100 [00:02<00:02, 22.59it/s]Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 46%|████▌     | 46/100 [00:02<00:02, 22.75it/s]Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 49%|████▉     | 49/100 [00:02<00:02, 21.85it/s]Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 52%|█████▏    | 52/100 [00:02<00:02, 21.86it/s]Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 55%|█████▌    | 55/100 [00:02<00:02, 22.04it/s]Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 58%|█████▊    | 58/100 [00:02<00:01, 21.62it/s]Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 61%|██████    | 61/100 [00:03<00:01, 22.13it/s]Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 64%|██████▍   | 64/100 [00:03<00:01, 21.93it/s]Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 67%|██████▋   | 67/100 [00:03<00:01, 21.59it/s]Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 70%|███████   | 70/100 [00:03<00:01, 22.19it/s]Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 73%|███████▎  | 73/100 [00:03<00:01, 22.42it/s]Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 76%|███████▌  | 76/100 [00:03<00:01, 22.31it/s]Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 79%|███████▉  | 79/100 [00:03<00:00, 22.73it/s]Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 82%|████████▏ | 82/100 [00:03<00:00, 22.13it/s]Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 85%|████████▌ | 85/100 [00:04<00:00, 22.74it/s]Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 88%|████████▊ | 88/100 [00:04<00:00, 22.37it/s]Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 91%|█████████ | 91/100 [00:04<00:00, 22.76it/s]Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 94%|█████████▍| 94/100 [00:04<00:00, 22.25it/s]Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
 97%|█████████▋| 97/100 [00:04<00:00, 22.26it/s]Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.2 GB
100%|██████████| 100/100 [00:04<00:00, 20.96it/s]
100%|██████████| 25/25 [00:00<00:00, 52.31it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 1 Fold 0 complete! Validation Loss : 5.917139587402343
Best validation loss improved from inf to 5.917139587402343

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 25.39it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 23.13it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.72it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.88it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.19it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.47it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.48it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.05it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 21.81it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 21.92it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.44it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 21.78it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 22.25it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 21.83it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 22.01it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.38it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.57it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 21.90it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.29it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 21.67it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.38it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 21.78it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 22.11it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.30it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 21.93it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:01, 21.82it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 22.27it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 21.77it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 21.34it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 21.56it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 20.36it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 20.69it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 21.01it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.96it/s]
100%|██████████| 25/25 [00:00<00:00, 48.64it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 1 Fold 1 complete! Validation Loss : 5.901770057678223
Best validation loss improved from 5.917139587402343 to 5.901770057678223

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.33it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 21.89it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 21.56it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 21.56it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:04, 21.21it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 21.58it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 21.14it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 19.81it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 20.74it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 20.13it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 20.80it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:03, 20.70it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.15it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:02<00:02, 20.97it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 20.61it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 20.15it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 20.51it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 20.33it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:02, 20.36it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 20.49it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:03<00:01, 19.58it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 65%|██████▌   | 65/100 [00:03<00:01, 19.65it/s]Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 67%|██████▋   | 67/100 [00:03<00:01, 18.67it/s]Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 70%|███████   | 70/100 [00:03<00:01, 19.25it/s]Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 73%|███████▎  | 73/100 [00:03<00:01, 20.10it/s]Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 76%|███████▌  | 76/100 [00:03<00:01, 21.07it/s]Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 79%|███████▉  | 79/100 [00:03<00:00, 22.05it/s]Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 82%|████████▏ | 82/100 [00:03<00:00, 22.78it/s]Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 85%|████████▌ | 85/100 [00:04<00:00, 23.29it/s]Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 88%|████████▊ | 88/100 [00:04<00:00, 23.20it/s]Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 91%|█████████ | 91/100 [00:04<00:00, 23.73it/s]Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 94%|█████████▍| 94/100 [00:04<00:00, 23.78it/s]Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 97%|█████████▋| 97/100 [00:04<00:00, 24.22it/s]Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.35it/s]
100%|██████████| 25/25 [00:00<00:00, 53.43it/s]

Epoch 1 Fold 2 complete! Validation Loss : 5.880725383758545
Best validation loss improved from 5.901770057678223 to 5.880725383758545

  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 25.03it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.33it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.70it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.55it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.96it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 24.58it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.73it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 24.64it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:02, 24.67it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.53it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.59it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 21.85it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:03, 19.35it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 20.61it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 21.37it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 20.85it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 21.05it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 18.45it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:02, 19.48it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:02, 18.28it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 19.41it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:03<00:01, 19.32it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 20.13it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 20.84it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 19.79it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:01, 16.87it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 80%|████████  | 80/100 [00:03<00:01, 17.29it/s]Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 83%|████████▎ | 83/100 [00:03<00:00, 19.00it/s]Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 85%|████████▌ | 85/100 [00:04<00:00, 19.16it/s]Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 88%|████████▊ | 88/100 [00:04<00:00, 20.40it/s]Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 91%|█████████ | 91/100 [00:04<00:00, 20.42it/s]Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 94%|█████████▍| 94/100 [00:04<00:00, 21.33it/s]Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 97%|█████████▋| 97/100 [00:04<00:00, 22.41it/s]Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 20.65it/s]
100%|██████████| 25/25 [00:00<00:00, 52.20it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 1 Fold 3 complete! Validation Loss : 5.837127723693848
Best validation loss improved from 5.880725383758545 to 5.837127723693848

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.89it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.79it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.37it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 21.43it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:04, 19.09it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:04, 20.15it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 20.91it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 21.94it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.91it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.56it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.82it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 21.99it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.05it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 20.77it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 21.97it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.60it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.39it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.65it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.08it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.20it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.27it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.81it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 24.18it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.95it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.91it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.97it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.52it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.65it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.07it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.60it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 23.08it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.44it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.37it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.74it/s]
100%|██████████| 25/25 [00:00<00:00, 53.04it/s]

Epoch 1 Fold 4 complete! Validation Loss : 5.776653537750244
Best validation loss improved from 5.837127723693848 to 5.776653537750244

Validation loss decreased (inf --> 5.776654).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 22.44it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 23.19it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.81it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.74it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.67it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.86it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.31it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.99it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 24.33it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.31it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.53it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.38it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.60it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.38it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.47it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:01<00:02, 24.33it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.45it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.40it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.59it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.16it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.69it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.76it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.11it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:02<00:01, 24.03it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.33it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.39it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.52it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.26it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.31it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 24.37it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 23.42it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 21.81it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.74it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.89it/s]
100%|██████████| 25/25 [00:00<00:00, 54.58it/s]

Epoch 2 Fold 0 complete! Validation Loss : 5.671767845153808
Best validation loss improved from 5.776653537750244 to 5.671767845153808

  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.49it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.85it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.97it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.01it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.39it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 24.17it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.28it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 23.93it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 24.26it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.11it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.15it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.66it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.52it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.39it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 22.71it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.30it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.57it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.53it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.81it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.91it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.38it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.21it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.48it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 24.33it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.39it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.12it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.46it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.71it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.93it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.96it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 24.08it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 24.27it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.40it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.94it/s]
100%|██████████| 25/25 [00:00<00:00, 55.29it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 2 Fold 1 complete! Validation Loss : 5.578927173614502
Best validation loss improved from 5.671767845153808 to 5.578927173614502

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 24.01it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.69it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 21.94it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.45it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.12it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.16it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.97it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.37it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.86it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.81it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 22.03it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.41it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 22.95it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.40it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.86it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 24.05it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.29it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.39it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.01it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.06it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.38it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.13it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 23.04it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.81it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.29it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.65it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.96it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.10it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.04it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.76it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 24.10it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 24.10it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.11it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.48it/s]
100%|██████████| 25/25 [00:00<00:00, 52.63it/s]

Epoch 2 Fold 2 complete! Validation Loss : 5.499498386383056
Best validation loss improved from 5.578927173614502 to 5.499498386383056

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 19.78it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 21.94it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.40it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.16it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.71it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.79it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.16it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 24.10it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 24.17it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.22it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.40it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.12it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.29it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.16it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.39it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 24.20it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.27it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.18it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.42it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.16it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.44it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.27it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.47it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.69it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.16it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.34it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.82it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.43it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.84it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.10it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 23.62it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.60it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.00it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.78it/s]
100%|██████████| 25/25 [00:00<00:00, 51.48it/s]

Epoch 2 Fold 3 complete! Validation Loss : 5.398478565216064
Best validation loss improved from 5.499498386383056 to 5.398478565216064

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.72it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.34it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.26it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.91it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.73it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.38it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 21.19it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 21.87it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.68it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.02it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.87it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.14it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.79it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.05it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 22.03it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 21.94it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.79it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.26it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.70it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.11it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.87it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.64it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 22.76it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 20.80it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 20.62it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:01, 21.42it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 21.81it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 21.57it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.41it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 22.22it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.92it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.35it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.28it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.46it/s]
100%|██████████| 25/25 [00:00<00:00, 54.79it/s]

Epoch 2 Fold 4 complete! Validation Loss : 5.377079467773438
Best validation loss improved from 5.398478565216064 to 5.377079467773438

Validation loss decreased (5.776654 --> 5.377079).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 24.02it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.04it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.29it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.03it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.95it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.77it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.22it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.23it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.75it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 23.19it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.43it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:03, 21.24it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 22.22it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.74it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.36it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.57it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.98it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.06it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.20it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.35it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.58it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.50it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.48it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 24.14it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.88it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.54it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.71it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.14it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.71it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.15it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 23.61it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.08it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.63it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.53it/s]
100%|██████████| 25/25 [00:00<00:00, 53.05it/s]

Epoch 3 Fold 0 complete! Validation Loss : 5.359058494567871
Best validation loss improved from 5.377079467773438 to 5.359058494567871

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.55it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.98it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.35it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.22it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.60it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 24.09it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.38it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 24.34it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:02, 24.41it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 23.30it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.87it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.26it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.39it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.41it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.74it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.04it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.92it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.22it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.04it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.01it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.32it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.34it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 22.70it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.72it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.23it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.45it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.89it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.88it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.05it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 24.10it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 23.32it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.62it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.84it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.46it/s]
100%|██████████| 25/25 [00:00<00:00, 49.96it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 3 Fold 1 complete! Validation Loss : 5.365248222351074
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.51it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.22it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.97it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.54it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.15it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.20it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 21.95it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 21.63it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 19.41it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 20.28it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 20.48it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:03, 20.99it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.00it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 21.09it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 21.02it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 21.68it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.36it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.67it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.46it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.68it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.80it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.32it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 22.80it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.34it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.83it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.12it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 22.16it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.27it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.28it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 21.77it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.55it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.91it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.71it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.41it/s]
100%|██████████| 25/25 [00:00<00:00, 53.22it/s]

Epoch 3 Fold 2 complete! Validation Loss : 5.361548290252686
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.27it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.35it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 22.27it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 20.92it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:04, 21.16it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 21.95it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.63it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 22.80it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.26it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.85it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.24it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.03it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.81it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 21.57it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 22.44it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.93it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.50it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.83it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.23it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.92it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.26it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.00it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 23.27it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.42it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 22.89it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.67it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.13it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.58it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.59it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 20.50it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 21.47it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 21.96it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.30it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.44it/s]
100%|██████████| 25/25 [00:00<00:00, 52.61it/s]

Epoch 3 Fold 3 complete! Validation Loss : 5.281493930816651
Best validation loss improved from 5.359058494567871 to 5.281493930816651

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.92it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.00it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 21.67it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.26it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 22.90it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.09it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.46it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.64it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.95it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.00it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.36it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.40it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.74it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.61it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.72it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.83it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.33it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.17it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.30it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.53it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.89it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.07it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.46it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 24.49it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.61it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.53it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.66it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.55it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.76it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 24.46it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 23.93it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:03<00:00, 24.05it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.67it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 24.07it/s]
100%|██████████| 25/25 [00:00<00:00, 54.29it/s]

Epoch 3 Fold 4 complete! Validation Loss : 5.290080337524414
Validation loss decreased (5.377079 --> 5.290080).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.54it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.63it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.80it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.74it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.90it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 24.00it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.39it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 24.30it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:02, 24.52it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.43it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.71it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.46it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.23it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.52it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 22.93it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.30it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.83it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.84it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.15it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.52it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.45it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 21.62it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 22.66it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.94it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.14it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.91it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 22.77it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.88it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.35it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.65it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 23.05it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.47it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.12it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.20it/s]
100%|██████████| 25/25 [00:00<00:00, 49.71it/s]

Epoch 4 Fold 0 complete! Validation Loss : 5.292745304107666
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 22.76it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 23.32it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.04it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.97it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.30it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.70it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.06it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 24.01it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.17it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.37it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 22.31it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.38it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.63it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 21.14it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 21.70it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.65it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.21it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.09it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.43it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.03it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.94it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.03it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.68it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 24.63it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.90it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.87it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.93it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.91it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 25.06it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 24.21it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 24.17it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 24.34it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.28it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.59it/s]
100%|██████████| 25/25 [00:00<00:00, 53.63it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 4 Fold 1 complete! Validation Loss : 5.2883631706237795
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.90it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:05, 17.45it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  8%|▊         | 8/100 [00:00<00:05, 17.77it/s]Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 11%|█         | 11/100 [00:00<00:04, 20.09it/s]Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 14%|█▍        | 14/100 [00:00<00:04, 20.30it/s]Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 17%|█▋        | 17/100 [00:00<00:03, 21.30it/s]Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 20%|██        | 20/100 [00:00<00:03, 21.87it/s]Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 23%|██▎       | 23/100 [00:01<00:03, 22.55it/s]Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 26%|██▌       | 26/100 [00:01<00:03, 21.62it/s]Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 29%|██▉       | 29/100 [00:01<00:03, 19.69it/s]Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 32%|███▏      | 32/100 [00:01<00:03, 20.83it/s]Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 35%|███▌      | 35/100 [00:01<00:02, 22.01it/s]Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 38%|███▊      | 38/100 [00:01<00:02, 22.61it/s]Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 41%|████      | 41/100 [00:01<00:02, 22.05it/s]Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 44%|████▍     | 44/100 [00:02<00:02, 22.52it/s]Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 47%|████▋     | 47/100 [00:02<00:02, 22.82it/s]Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 50%|█████     | 50/100 [00:02<00:02, 22.89it/s]Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 53%|█████▎    | 53/100 [00:02<00:02, 18.28it/s]Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 56%|█████▌    | 56/100 [00:02<00:02, 19.14it/s]Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 59%|█████▉    | 59/100 [00:02<00:02, 20.50it/s]Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 62%|██████▏   | 62/100 [00:02<00:01, 21.24it/s]Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 65%|██████▌   | 65/100 [00:03<00:01, 21.63it/s]Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 68%|██████▊   | 68/100 [00:03<00:01, 18.95it/s]Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 71%|███████   | 71/100 [00:03<00:01, 20.34it/s]Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 74%|███████▍  | 74/100 [00:03<00:01, 21.22it/s]Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 77%|███████▋  | 77/100 [00:03<00:01, 19.00it/s]Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 80%|████████  | 80/100 [00:03<00:00, 20.22it/s]Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 83%|████████▎ | 83/100 [00:03<00:00, 21.33it/s]Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 86%|████████▌ | 86/100 [00:04<00:00, 21.79it/s]Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 89%|████████▉ | 89/100 [00:04<00:00, 22.72it/s]Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 92%|█████████▏| 92/100 [00:04<00:00, 21.50it/s]Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 95%|█████████▌| 95/100 [00:04<00:00, 21.14it/s]Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 98%|█████████▊| 98/100 [00:04<00:00, 22.06it/s]Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.02it/s]
100%|██████████| 25/25 [00:00<00:00, 47.29it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 4 Fold 2 complete! Validation Loss : 5.29890214920044
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 22.15it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 19.08it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 20.86it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 21.33it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:04, 20.91it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 21.61it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.46it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 22.26it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.34it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 21.51it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 21.06it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 21.76it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 22.80it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.20it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 23.76it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 24.10it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.34it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.54it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.68it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.81it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 25.02it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.96it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.96it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 25.09it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:00, 25.15it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.98it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 25.18it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 25.01it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 25.22it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 25.08it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 24.16it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.40it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.12it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.48it/s]
100%|██████████| 25/25 [00:00<00:00, 50.96it/s]

Epoch 4 Fold 3 complete! Validation Loss : 5.224977245330811
Best validation loss improved from 5.281493930816651 to 5.224977245330811

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 25.51it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.53it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.81it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.55it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.79it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 24.72it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.87it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 23.72it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 24.15it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.21it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.34it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.38it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.58it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.59it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.63it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:01<00:02, 24.48it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.47it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.00it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.65it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.04it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.20it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 22.58it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 23.24it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.68it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 22.38it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.51it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 22.94it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.86it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.00it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.57it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 22.83it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.79it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.24it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.51it/s]
100%|██████████| 25/25 [00:00<00:00, 55.45it/s]

Epoch 4 Fold 4 complete! Validation Loss : 5.232643890380859
Validation loss decreased (5.290080 --> 5.232644).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 25.08it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.83it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.83it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.67it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.77it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 24.70it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.75it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 24.68it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:02, 24.80it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.62it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.68it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.85it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.20it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.30it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.88it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:01<00:02, 24.00it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.32it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.02it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.76it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.96it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.80it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.89it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.32it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:02<00:01, 24.37it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.76it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.70it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.89it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.67it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.72it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 24.87it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 25.04it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:03<00:00, 25.02it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 25.12it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 24.46it/s]
100%|██████████| 25/25 [00:00<00:00, 55.35it/s]

Epoch 5 Fold 0 complete! Validation Loss : 5.268725662231446
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.98it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.16it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.61it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.43it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.90it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 24.62it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.87it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 24.68it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:02, 24.79it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.71it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.77it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.78it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.83it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.81it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.67it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:01<00:02, 24.33it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.66it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.98it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.11it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.01it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.11it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.12it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 23.41it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:02<00:01, 22.62it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 22.63it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.19it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.78it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.41it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.00it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.73it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 24.16it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:03<00:00, 24.03it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.99it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 24.04it/s]
100%|██████████| 25/25 [00:00<00:00, 52.04it/s]

Epoch 5 Fold 1 complete! Validation Loss : 5.23733232498169
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 24.13it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.77it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.87it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.03it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.46it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.46it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.93it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.28it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:04, 16.14it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 29%|██▉       | 29/100 [00:01<00:04, 15.32it/s]Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 31%|███       | 31/100 [00:01<00:04, 16.21it/s]Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:04, 16.44it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 35%|███▌      | 35/100 [00:01<00:03, 17.25it/s]Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 38%|███▊      | 38/100 [00:01<00:03, 18.54it/s]Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 40%|████      | 40/100 [00:02<00:03, 18.58it/s]Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 43%|████▎     | 43/100 [00:02<00:02, 19.66it/s]Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 46%|████▌     | 46/100 [00:02<00:02, 19.98it/s]Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 49%|████▉     | 49/100 [00:02<00:02, 20.61it/s]Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 52%|█████▏    | 52/100 [00:02<00:02, 20.42it/s]Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 55%|█████▌    | 55/100 [00:02<00:02, 21.29it/s]Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 58%|█████▊    | 58/100 [00:02<00:01, 22.12it/s]Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 61%|██████    | 61/100 [00:03<00:01, 22.18it/s]Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 64%|██████▍   | 64/100 [00:03<00:01, 22.40it/s]Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 67%|██████▋   | 67/100 [00:03<00:01, 21.96it/s]Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 70%|███████   | 70/100 [00:03<00:01, 20.05it/s]Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 73%|███████▎  | 73/100 [00:03<00:01, 21.05it/s]Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 76%|███████▌  | 76/100 [00:03<00:01, 21.07it/s]Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 79%|███████▉  | 79/100 [00:03<00:00, 21.80it/s]Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 82%|████████▏ | 82/100 [00:04<00:00, 21.81it/s]Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 85%|████████▌ | 85/100 [00:04<00:00, 20.36it/s]Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 88%|████████▊ | 88/100 [00:04<00:00, 21.03it/s]Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 91%|█████████ | 91/100 [00:04<00:00, 22.01it/s]Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 94%|█████████▍| 94/100 [00:04<00:00, 22.24it/s]Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 97%|█████████▋| 97/100 [00:04<00:00, 22.17it/s]Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 20.76it/s]
100%|██████████| 25/25 [00:00<00:00, 46.27it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 5 Fold 2 complete! Validation Loss : 5.267979736328125
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 21.98it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.90it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.83it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.58it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.97it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.36it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.19it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 21.72it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 19.79it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 20.68it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 20.61it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:03, 20.96it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.66it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 20.88it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 20.72it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 21.50it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 20.15it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 20.88it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 21.81it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.52it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 20.32it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:03<00:01, 18.88it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 68%|██████▊   | 68/100 [00:03<00:01, 18.72it/s]Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 70%|███████   | 70/100 [00:03<00:01, 18.97it/s]Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 18.95it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 74%|███████▍  | 74/100 [00:03<00:01, 18.74it/s]Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 77%|███████▋  | 77/100 [00:03<00:01, 19.84it/s]Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 80%|████████  | 80/100 [00:03<00:00, 20.73it/s]Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 83%|████████▎ | 83/100 [00:03<00:00, 21.70it/s]Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 86%|████████▌ | 86/100 [00:04<00:00, 21.48it/s]Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 89%|████████▉ | 89/100 [00:04<00:00, 22.28it/s]Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 92%|█████████▏| 92/100 [00:04<00:00, 22.68it/s]Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 95%|█████████▌| 95/100 [00:04<00:00, 22.77it/s]Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 98%|█████████▊| 98/100 [00:04<00:00, 22.16it/s]Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.17it/s]
100%|██████████| 25/25 [00:00<00:00, 51.22it/s]

Epoch 5 Fold 3 complete! Validation Loss : 5.19688793182373
Best validation loss improved from 5.224977245330811 to 5.19688793182373

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.38it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.60it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 22.32it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.05it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:04, 20.96it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:04, 20.48it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:01<00:03, 19.80it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 20.13it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 21.12it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 21.79it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.37it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.76it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.03it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.07it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 22.32it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.53it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.43it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 21.78it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.19it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.61it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.26it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 22.81it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 23.20it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.81it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 22.76it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.60it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 21.17it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 21.80it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.52it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 23.01it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 23.41it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.61it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.75it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.38it/s]
100%|██████████| 25/25 [00:00<00:00, 51.61it/s]

Epoch 5 Fold 4 complete! Validation Loss : 5.197669277191162
Validation loss decreased (5.232644 --> 5.197669).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.26it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.13it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.38it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.67it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.01it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.28it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.56it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.09it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.12it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.47it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.22it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.47it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 22.69it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 21.97it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 21.38it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 21.33it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.08it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.09it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 21.95it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 21.63it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.17it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 21.73it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 22.50it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.53it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 22.83it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.04it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.52it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.73it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.04it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.33it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.69it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.08it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.55it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.67it/s]
100%|██████████| 25/25 [00:00<00:00, 51.32it/s]

Epoch 6 Fold 0 complete! Validation Loss : 5.259382877349854
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.73it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 21.13it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 22.34it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 20.84it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:04, 21.07it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:04, 19.15it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 20%|██        | 20/100 [00:01<00:05, 15.68it/s]Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 23%|██▎       | 23/100 [00:01<00:04, 17.35it/s]Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 26%|██▌       | 26/100 [00:01<00:03, 18.77it/s]Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 29%|██▉       | 29/100 [00:01<00:03, 20.27it/s]Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 32%|███▏      | 32/100 [00:01<00:03, 20.40it/s]Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 35%|███▌      | 35/100 [00:01<00:03, 20.20it/s]Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 38%|███▊      | 38/100 [00:01<00:02, 21.25it/s]Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 41%|████      | 41/100 [00:02<00:02, 21.14it/s]Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 44%|████▍     | 44/100 [00:02<00:02, 21.49it/s]Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 47%|████▋     | 47/100 [00:02<00:02, 19.77it/s]Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 50%|█████     | 50/100 [00:02<00:02, 20.47it/s]Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 53%|█████▎    | 53/100 [00:02<00:02, 21.04it/s]Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 56%|█████▌    | 56/100 [00:02<00:02, 20.59it/s]Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 59%|█████▉    | 59/100 [00:02<00:01, 20.87it/s]Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 62%|██████▏   | 62/100 [00:03<00:01, 21.14it/s]Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 65%|██████▌   | 65/100 [00:03<00:01, 21.00it/s]Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 68%|██████▊   | 68/100 [00:03<00:01, 21.71it/s]Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 71%|███████   | 71/100 [00:03<00:01, 22.40it/s]Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 74%|███████▍  | 74/100 [00:03<00:01, 22.74it/s]Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 77%|███████▋  | 77/100 [00:03<00:00, 23.19it/s]Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 80%|████████  | 80/100 [00:03<00:00, 23.26it/s]Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 83%|████████▎ | 83/100 [00:03<00:00, 23.42it/s]Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 86%|████████▌ | 86/100 [00:04<00:00, 23.30it/s]Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 89%|████████▉ | 89/100 [00:04<00:00, 23.76it/s]Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 92%|█████████▏| 92/100 [00:04<00:00, 23.90it/s]Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 95%|█████████▌| 95/100 [00:04<00:00, 22.85it/s]Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 98%|█████████▊| 98/100 [00:04<00:00, 22.59it/s]Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.23it/s]
100%|██████████| 25/25 [00:00<00:00, 51.18it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 6 Fold 1 complete! Validation Loss : 5.225444469451904
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 21.79it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 21.37it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 22.73it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 21.94it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 22.07it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.01it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 21.11it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 20.52it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 20.81it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 21.67it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.61it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.04it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.65it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.78it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 23.96it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.91it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.90it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.86it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.60it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 21.59it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.14it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 21.55it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 22.16it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 20.79it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 21.49it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.33it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 22.68it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.56it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 21.96it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 22.01it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.38it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 21.40it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.17it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.22it/s]
100%|██████████| 25/25 [00:00<00:00, 49.90it/s]

Epoch 6 Fold 2 complete! Validation Loss : 5.254926700592041
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.38it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.16it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.77it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.52it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.88it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.95it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.15it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 24.04it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 24.20it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.14it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.10it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.85it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.37it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.88it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 22.36it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.46it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.60it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.25it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:02, 20.88it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:02, 19.02it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 20.06it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 19.88it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 20.78it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 20.29it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 21.08it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:01, 20.40it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 21.52it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 21.53it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.00it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 22.67it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 21.97it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 21.48it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 21.49it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.99it/s]
100%|██████████| 25/25 [00:00<00:00, 50.38it/s]

Epoch 6 Fold 3 complete! Validation Loss : 5.192677421569824
Best validation loss improved from 5.19688793182373 to 5.192677421569824

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 24.07it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.42it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.03it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.21it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 22.47it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 21.48it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.33it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 22.18it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.09it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 20.40it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 21.41it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 21.46it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 20.90it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 20.96it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 21.44it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 21.76it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.49it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.08it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 21.84it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 21.55it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 21.51it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:03<00:01, 21.54it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 22.67it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.89it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.30it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.57it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.19it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.09it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.46it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 24.40it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 24.83it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.85it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.71it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.53it/s]
100%|██████████| 25/25 [00:00<00:00, 46.32it/s]

Epoch 6 Fold 4 complete! Validation Loss : 5.191266250610352
Best validation loss improved from 5.192677421569824 to 5.191266250610352

Validation loss decreased (5.197669 --> 5.191266).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  2%|▏         | 2/100 [00:00<00:05, 17.55it/s]Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  5%|▌         | 5/100 [00:00<00:04, 20.00it/s]Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  8%|▊         | 8/100 [00:00<00:04, 20.80it/s]Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 11%|█         | 11/100 [00:00<00:04, 22.08it/s]Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 14%|█▍        | 14/100 [00:00<00:03, 22.66it/s]Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 17%|█▋        | 17/100 [00:00<00:03, 23.44it/s]Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 20%|██        | 20/100 [00:00<00:03, 23.29it/s]Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 23%|██▎       | 23/100 [00:01<00:03, 23.41it/s]Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 26%|██▌       | 26/100 [00:01<00:03, 23.28it/s]Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 29%|██▉       | 29/100 [00:01<00:03, 23.52it/s]Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 32%|███▏      | 32/100 [00:01<00:02, 23.29it/s]Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 35%|███▌      | 35/100 [00:01<00:02, 22.77it/s]Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 38%|███▊      | 38/100 [00:01<00:02, 23.04it/s]Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 41%|████      | 41/100 [00:01<00:02, 23.50it/s]Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 44%|████▍     | 44/100 [00:01<00:02, 21.21it/s]Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 47%|████▋     | 47/100 [00:02<00:02, 19.70it/s]Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 50%|█████     | 50/100 [00:02<00:02, 20.80it/s]Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 53%|█████▎    | 53/100 [00:02<00:02, 21.64it/s]Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 56%|█████▌    | 56/100 [00:02<00:02, 20.82it/s]Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 59%|█████▉    | 59/100 [00:02<00:02, 20.25it/s]Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 62%|██████▏   | 62/100 [00:02<00:01, 20.53it/s]Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 65%|██████▌   | 65/100 [00:02<00:01, 21.42it/s]Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 68%|██████▊   | 68/100 [00:03<00:01, 20.42it/s]Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 71%|███████   | 71/100 [00:03<00:01, 19.07it/s]Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 74%|███████▍  | 74/100 [00:03<00:01, 20.35it/s]Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 77%|███████▋  | 77/100 [00:03<00:01, 21.55it/s]Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 80%|████████  | 80/100 [00:03<00:00, 22.25it/s]Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 83%|████████▎ | 83/100 [00:03<00:00, 22.94it/s]Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 86%|████████▌ | 86/100 [00:03<00:00, 23.17it/s]Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 89%|████████▉ | 89/100 [00:04<00:00, 23.78it/s]Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 92%|█████████▏| 92/100 [00:04<00:00, 23.98it/s]Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 95%|█████████▌| 95/100 [00:04<00:00, 21.78it/s]Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 98%|█████████▊| 98/100 [00:04<00:00, 20.65it/s]Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.65it/s]
100%|██████████| 25/25 [00:00<00:00, 49.67it/s]

Epoch 7 Fold 0 complete! Validation Loss : 5.254244956970215
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.38it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.16it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 20.79it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:05, 17.18it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:04, 18.76it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:04, 19.45it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:01<00:03, 20.74it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 21.14it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 21.63it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.33it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 21.70it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:03, 18.71it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:03, 20.24it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:02<00:02, 21.39it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 22.31it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.28it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.38it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.69it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.73it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 21.48it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 20.60it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:03<00:01, 20.80it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 21.57it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 21.32it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 21.96it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.53it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.06it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.22it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:04<00:00, 21.12it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 20.99it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 21.81it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.50it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.19it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.47it/s]
100%|██████████| 25/25 [00:00<00:00, 50.90it/s]

Epoch 7 Fold 1 complete! Validation Loss : 5.2189584159851075
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 22.55it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 23.32it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.88it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.78it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.13it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.19it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.51it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.25it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 21.90it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 21.85it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.62it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.97it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.40it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.60it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.18it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 24.30it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:01, 24.69it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.38it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.56it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.63it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.80it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.78it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.97it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 24.73it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.27it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.21it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.44it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.67it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.98it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.77it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 23.34it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.64it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.04it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.77it/s]
100%|██████████| 25/25 [00:00<00:00, 52.88it/s]

Epoch 7 Fold 2 complete! Validation Loss : 5.246916809082031
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.47it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.74it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.39it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.00it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.38it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.86it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.97it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 22.95it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.35it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 23.49it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.87it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.87it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.82it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.05it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.21it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 24.17it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.49it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.82it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.16it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.23it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.40it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.16it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 23.54it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.87it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.48it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.75it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.11it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.90it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.29it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.28it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 23.00it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.31it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.59it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.75it/s]
100%|██████████| 25/25 [00:00<00:00, 53.25it/s]

Epoch 7 Fold 3 complete! Validation Loss : 5.190437812805175
Best validation loss improved from 5.191266250610352 to 5.190437812805175

Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 20.54it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 21.36it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 22.67it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.11it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.60it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.65it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.83it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.22it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.60it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 23.73it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.11it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.18it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.99it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.89it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.00it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.62it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.89it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.49it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.92it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.13it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.23it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 21.67it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 22.63it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.52it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 22.75it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.99it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.52it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.75it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.67it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.82it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 24.32it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 24.46it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.96it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.51it/s]
100%|██████████| 25/25 [00:00<00:00, 53.53it/s]

Epoch 7 Fold 4 complete! Validation Loss : 5.18568717956543
Best validation loss improved from 5.190437812805175 to 5.18568717956543

Validation loss decreased (5.191266 --> 5.185687).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.80it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.27it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.18it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.51it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.25it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.43it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.84it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.65it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.88it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 23.78it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.97it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.03it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.10it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.05it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.20it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.99it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.24it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.07it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.16it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.87it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.30it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.68it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.11it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 24.13it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.55it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.57it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.88it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.75it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.64it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.39it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 23.16it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.35it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.89it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.79it/s]
100%|██████████| 25/25 [00:00<00:00, 53.28it/s]

Epoch 8 Fold 0 complete! Validation Loss : 5.249760780334473
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 25.05it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.58it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.93it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.14it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.58it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.45it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.73it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.34it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.63it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 23.68it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.98it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:03, 20.93it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.99it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.49it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.13it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.59it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.09it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.48it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.99it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.20it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.28it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 22.24it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 22.90it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.02it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 22.86it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.19it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.71it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.80it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.12it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.39it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.66it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.44it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.92it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.34it/s]
100%|██████████| 25/25 [00:00<00:00, 51.69it/s]

Epoch 8 Fold 1 complete! Validation Loss : 5.214451503753662
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.78it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:05, 18.35it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 20.12it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 20.96it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 21.51it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.24it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.05it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.07it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.39it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 23.05it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 22.10it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.74it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.37it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.80it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 24.23it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 24.17it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.28it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 24.26it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.68it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 24.16it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.58it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.98it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.39it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.60it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.15it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.57it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.29it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.48it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.84it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.06it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.42it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.89it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.48it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.16it/s]
100%|██████████| 25/25 [00:00<00:00, 52.90it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 8 Fold 2 complete! Validation Loss : 5.241014804840088
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.61it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.84it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.02it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.88it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.30it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.99it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.28it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 24.20it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 24.16it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 24.10it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.70it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.83it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 22.39it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.12it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 22.95it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.05it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.17it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.81it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.16it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.00it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.27it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.71it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 23.50it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.84it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.29it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.26it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.62it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.33it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.42it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 24.40it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 24.83it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 24.74it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 24.79it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.86it/s]
100%|██████████| 25/25 [00:00<00:00, 54.30it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 8 Fold 3 complete! Validation Loss : 5.187216510772705
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 21.62it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.63it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.25it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.43it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.73it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.55it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.43it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 22.86it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.38it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 23.50it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.08it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.62it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.40it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 21.66it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 22.40it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.75it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.26it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.43it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.93it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.91it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 21.91it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 22.62it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 23.39it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.78it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.04it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.22it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.31it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.29it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.96it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.10it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 23.24it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.69it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.89it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.18it/s]
100%|██████████| 25/25 [00:00<00:00, 54.74it/s]

Epoch 8 Fold 4 complete! Validation Loss : 5.181627025604248
Best validation loss improved from 5.18568717956543 to 5.181627025604248

Validation loss decreased (5.185687 --> 5.181627).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 25.54it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 23.00it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.95it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.13it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.40it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 24.20it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.34it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.65it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.14it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 23.29it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.05it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.41it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.07it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.23it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.40it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.45it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.76it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.63it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.13it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.30it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.77it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 22.88it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 23.62it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.82it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.51it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.43it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 24.70it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 24.74it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 24.75it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 24.87it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 24.43it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 24.18it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.73it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.76it/s]
100%|██████████| 25/25 [00:00<00:00, 51.53it/s]

Epoch 9 Fold 0 complete! Validation Loss : 5.247144260406494
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.15it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 19.25it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 21.37it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 20.31it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 21.84it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.61it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.65it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.12it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.52it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 23.63it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 24.09it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 24.24it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.35it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.97it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.31it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 21.91it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 22.14it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.67it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.38it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.73it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.15it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.18it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.48it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 24.22it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.41it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.20it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 21.75it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.10it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.36it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.27it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.51it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.34it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.04it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.95it/s]
100%|██████████| 25/25 [00:00<00:00, 52.34it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 9 Fold 1 complete! Validation Loss : 5.210148029327392
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:03, 24.60it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 24.01it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.22it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.23it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.65it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.39it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 23.71it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.70it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 23.86it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.01it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.57it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:03, 20.67it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 21.67it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 20.49it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 21.31it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 20.73it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 21.02it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 21.50it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:02, 21.43it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.04it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.15it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 21.52it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 21.77it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 20.73it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 20.95it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:01, 20.98it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 21.76it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 20.44it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 21.31it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 21.35it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 21.89it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 21.67it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 21.90it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.93it/s]
100%|██████████| 25/25 [00:00<00:00, 44.84it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 9 Fold 2 complete! Validation Loss : 5.23590841293335
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 21.90it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 21.48it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 22.67it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 21.78it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 21.54it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.12it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 20.65it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 21.18it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.11it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 21.33it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 21.65it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.11it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 22.55it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.94it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 22.82it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.64it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 21.76it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.04it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.65it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.09it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.71it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.35it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 23.71it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.93it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.20it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.08it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.24it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.43it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.11it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.43it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 23.21it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.35it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.76it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.56it/s]
100%|██████████| 25/25 [00:00<00:00, 53.93it/s]

Epoch 9 Fold 3 complete! Validation Loss : 5.184705581665039
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.87it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.50it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 22.65it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 23.16it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 23.80it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.47it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 21.02it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 21.89it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.77it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.83it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.36it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.55it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 24.03it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 24.20it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 22.99it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 20.50it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 21.72it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.53it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.13it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.34it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.81it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 22.63it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 22.61it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 20.22it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 20.46it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:01, 21.04it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 21.94it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 22.13it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.23it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 22.24it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 19.70it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 18.43it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 98%|█████████▊| 98/100 [00:04<00:00, 18.57it/s]Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 21.77it/s]
100%|██████████| 25/25 [00:00<00:00, 52.24it/s]

Epoch 9 Fold 4 complete! Validation Loss : 5.178486442565918
Best validation loss improved from 5.181627025604248 to 5.178486442565918

Validation loss decreased (5.181627 --> 5.178486).  Saving model ...
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:05, 18.99it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  5%|▌         | 5/100 [00:00<00:05, 16.93it/s]Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  7%|▋         | 7/100 [00:00<00:05, 17.45it/s]Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:05, 17.09it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 19.58it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:04, 21.20it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.08it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:01<00:03, 22.81it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 22.62it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.57it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 20.21it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:03, 20.36it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:03, 21.30it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 22.17it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.70it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 23.18it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.07it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.20it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 20.80it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:02, 20.81it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 21.64it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 22.70it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:03<00:01, 23.24it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 23.97it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 24.25it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 24.59it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 24.65it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.64it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 21.42it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.48it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 23.13it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 23.35it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 23.18it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.75it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.21it/s]
100%|██████████| 25/25 [00:00<00:00, 52.45it/s]

Epoch 10 Fold 0 complete! Validation Loss : 5.244281883239746
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.43it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.95it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 22.88it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 21.77it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 21.59it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.35it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.49it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 23.07it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.74it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 22.94it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.88it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.21it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.33it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.17it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.63it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 22.56it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.15it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.99it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.45it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 22.63it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.19it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.12it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 23.27it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.27it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.56it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.22it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.45it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.23it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.47it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.05it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.49it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.36it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.71it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.92it/s]
100%|██████████| 25/25 [00:00<00:00, 50.65it/s]

Epoch 10 Fold 1 complete! Validation Loss : 5.2062551879882815
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  0%|          | 0/100 [00:00<?, ?it/s]Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.26it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 22.94it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 23.20it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:04, 21.48it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 22.09it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 21.97it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 22.48it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 22.58it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.73it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 23.06it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.28it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.07it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.43it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.36it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.63it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.51it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.08it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.28it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 22.99it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.36it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.58it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.28it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 23.23it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.11it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.56it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 22.77it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.17it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.13it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 22.37it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 22.27it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 22.81it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.42it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.80it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.92it/s]
100%|██████████| 25/25 [00:00<00:00, 48.56it/s]
  0%|          | 0/100 [00:00<?, ?it/s]
Epoch 10 Fold 2 complete! Validation Loss : 5.232755393981933
Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 21.53it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:04, 20.74it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:04, 21.85it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 22.14it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 22.67it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 22.49it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 21.38it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:01<00:03, 21.80it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 22.27it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:03, 21.87it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 22.54it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 22.85it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.24it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 22.64it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:02<00:02, 23.09it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.23it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 23.21it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:02, 22.89it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 23.33it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.42it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 23.91it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 23.23it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:03<00:01, 23.65it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 22.75it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 22.04it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:01, 21.88it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 21.49it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 21.47it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 21.64it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:04<00:00, 21.59it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:04<00:00, 21.97it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 22.46it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 23.20it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 22.47it/s]
100%|██████████| 25/25 [00:00<00:00, 54.35it/s]

Epoch 10 Fold 3 complete! Validation Loss : 5.182922706604004
  0%|          | 0/100 [00:00<?, ?it/s]Batch 0 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 1 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 2 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  3%|▎         | 3/100 [00:00<00:04, 23.74it/s]Batch 3 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 4 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 5 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  6%|▌         | 6/100 [00:00<00:03, 23.82it/s]Batch 6 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 7 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 8 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
  9%|▉         | 9/100 [00:00<00:03, 24.17it/s]Batch 9 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 10 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 11 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 12%|█▏        | 12/100 [00:00<00:03, 24.33it/s]Batch 12 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 13 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 14 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 15%|█▌        | 15/100 [00:00<00:03, 24.06it/s]Batch 15 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 16 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 17 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 18%|█▊        | 18/100 [00:00<00:03, 23.90it/s]Batch 18 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 19 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 20 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 21%|██        | 21/100 [00:00<00:03, 24.24it/s]Batch 21 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 22 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 23 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 24%|██▍       | 24/100 [00:00<00:03, 23.91it/s]Batch 24 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 25 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 26 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 27%|██▋       | 27/100 [00:01<00:03, 24.33it/s]Batch 27 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 28 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 29 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 30%|███       | 30/100 [00:01<00:02, 23.48it/s]Batch 30 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 31 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 32 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 33%|███▎      | 33/100 [00:01<00:02, 23.67it/s]Batch 33 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 34 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 35 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 36%|███▌      | 36/100 [00:01<00:02, 23.77it/s]Batch 36 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 37 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 38 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 39%|███▉      | 39/100 [00:01<00:02, 23.76it/s]Batch 39 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 40 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 41 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 42%|████▏     | 42/100 [00:01<00:02, 23.35it/s]Batch 42 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 43 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 44 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 45%|████▌     | 45/100 [00:01<00:02, 23.63it/s]Batch 45 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 46 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 47 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 48%|████▊     | 48/100 [00:02<00:02, 23.91it/s]Batch 48 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 49 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 50 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 51%|█████     | 51/100 [00:02<00:02, 24.18it/s]Batch 51 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 52 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 53 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 54%|█████▍    | 54/100 [00:02<00:01, 23.53it/s]Batch 54 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 55 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 56 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 57%|█████▋    | 57/100 [00:02<00:01, 24.05it/s]Batch 57 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 58 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 59 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 60%|██████    | 60/100 [00:02<00:01, 23.78it/s]Batch 60 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 61 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 62 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 63%|██████▎   | 63/100 [00:02<00:01, 24.03it/s]Batch 63 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 64 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 65 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 66%|██████▌   | 66/100 [00:02<00:01, 24.04it/s]Batch 66 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 67 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 68 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 69%|██████▉   | 69/100 [00:02<00:01, 24.25it/s]Batch 69 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 70 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 71 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 72%|███████▏  | 72/100 [00:03<00:01, 23.71it/s]Batch 72 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 73 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 74 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 75%|███████▌  | 75/100 [00:03<00:01, 23.75it/s]Batch 75 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 76 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 77 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 78%|███████▊  | 78/100 [00:03<00:00, 23.53it/s]Batch 78 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 79 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 80 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 81%|████████  | 81/100 [00:03<00:00, 23.76it/s]Batch 81 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 82 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 83 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 84%|████████▍ | 84/100 [00:03<00:00, 23.19it/s]Batch 84 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 85 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 86 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 87%|████████▋ | 87/100 [00:03<00:00, 23.54it/s]Batch 87 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 88 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 89 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 90%|█████████ | 90/100 [00:03<00:00, 23.42it/s]Batch 90 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 91 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 92 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 93%|█████████▎| 93/100 [00:03<00:00, 22.29it/s]Batch 93 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 94 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 95 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 96%|█████████▌| 96/100 [00:04<00:00, 21.48it/s]Batch 96 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 97 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
Batch 98 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
 99%|█████████▉| 99/100 [00:04<00:00, 22.43it/s]Batch 99 is on device: cuda:0
Allocated: 0.1 GB
Reserved: 0.3 GB
100%|██████████| 100/100 [00:04<00:00, 23.52it/s]
100%|██████████| 25/25 [00:00<00:00, 55.44it/s]

Epoch 10 Fold 4 complete! Validation Loss : 5.174915428161621
Best validation loss improved from 5.178486442565918 to 5.174915428161621

Validation loss decreased (5.178486 --> 5.174915).  Saving model ...
The model has been saved in models/lstm_val_loss_5.17492_ep_10.pt
Could not load symbol cublasGetSmCountTarget from cublas64_11.dll. Error code 127

Process finished with exit code 0
