# 🧠 Brain Tumor MRI Diagnosis App

This is my first personal project in computer vision for healthcare, and it is **still under development**.
The model accepts brain scan MRI image (.jpg, .jpeg, .png) as input and it classified to one of four distinct medical conditions based on the MRI scan: 
- Glioma  
- Meningioma
- No Tumor  
- Pituitary 

## Demo App

Link of the demo app is here: https://vuminhkhoa-brain-health.streamlit.app/
> ⚠️ This app is hosted on Streamlit Community Cloud, so it may take a little time to load at the beginning.
[![Tutorial video](https://www.youtube.com/watch?v=NZRNdIJdrVk)](https://www.youtube.com/watch?v=NZRNdIJdrVk)

## Features

- Upload MRI brain scan images and classify them into one of four classes: "Glioma", "Meningioma", "No Tumor", or "Pituitary"
- Trained on the dataset from https://github.com/sartajbhuvaji/brain-tumor-classification-dataset
- Fine-tuned using a pretrained PyTorch ResNet50 model with RadImageNet weights from https://huggingface.co/Lab-Rasool/RadImageNet
- Built with **Streamlit** and **PyTorch**

## Project Status

The app has completed its **main functionality**:  
- ✅ MRI brain scan **classification into 4 classes**
- ✅ User-friendly interface built with Streamlit  
- ✅ Achieved ~90% test accuracy  
- 🚧 Planned improvements: Adding tumor segmentation feature  

## Local Setup

```bash
git clone https://github.com/vuminhkh0a/BRAIN_TUMOR.git
cd BRAIN_TUMOR
pip install -r requirements.txt
streamlit run Home.py
```
