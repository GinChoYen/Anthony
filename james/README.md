Install CUDA Toolkit:  
Download and install the CUDA Toolkit from the NVIDIA CUDA Toolkit download page.  https://developer.nvidia.com/cuda-downloads  

Install cuDNN:  
Download cuDNN from the NVIDIA cuDNN download page. Follow the installation instructions to place the cuDNN files in the CUDA Toolkit directory.  https://developer.nvidia.com/cudnn-downloads  

Update Environment Variables:  
Ensure that the environment variables for CUDA are set correctly. Add the following paths to your system environment variables:  

    C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.x\bin  
    C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.x\libnvvp  
Example Python Script to Check Installation  
import torch  
import random  
import numpy as np  
SEED = 1234  
random.seed(SEED)  
np.random.seed(SEED)  
torch.manual_seed(SEED)  
torch.backends.cudnn.deterministic = True  
print(f"CUDA available: {torch.cuda.is_available()}")  
print(f"CUDA version: {torch.version.cuda}")  
print(f"cuDNN version: {torch.backends.cudnn.version()}")      
OUTPUT:  
CUDA available: True   
CUDA version: 11.1    
cuDNN version: 8005   
![image](https://github.com/user-attachments/assets/b24c6d62-9eaf-4a4e-b385-afc8e8695309)


---
https://github.com/Abhishekjl/Sentiment-analyis-BERT-Trained-/tree/master  
![image](https://github.com/GinChoYen/Anthony/assets/22329486/0d531acb-1fc6-439b-9619-3fa24a1d4c5b)


