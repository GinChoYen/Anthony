I setup by enviroment by the following way. Need to check for GPU 
1. python -m pip install --upgrade pip
2. python-3.10.11-amd64  python C:\Users\bonni\AppData\Local\Programs\Python\Python310
3. using the ide install each needed packages
running bert.py  takes long time:  
![image](https://github.com/user-attachments/assets/03e8f373-b265-463e-a2bd-67e73f906040)  
- Use nvidia-smi:  
- Monitor GPU usage during training:  
watch -n 1 nvidia-smi  

![image](https://github.com/user-attachments/assets/2b7fed2e-c4ed-4416-a153-8db0ecc9c109)


# BERT-SJTU-NLU2023
This is a BERT-base solution on the course NLU2023 of Shanghai Jiao Tong University.

## Requirements and Environment
- python == 3.10.11
- pytorch == 1.12.1
- transformers == 4.28.1

## Dataset
Trivial Natural Language Inference (TNLI).

## Training BERT model
```
python bert.py
```
## Training BERT with cutoff
```
python bert_cutoff.py
```
## Training BERT with CreAT
```
python bert_creat.py
```
## Training DeBERTa
```
python deberta.py
```

## Testing
```
python test.py
```
numpy              1.23.5
python -m pip install --upgrade pip
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1+cu113 -f https://download.pytorch.org/whl/torch_stable.html


