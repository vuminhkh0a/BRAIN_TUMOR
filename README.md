# 🧠 Brain Tumor MRI Diagnosis App

This is my first personal project in computer vision for healthcare, and it is **still under development**.

## Demo App

Link of the demo app is here: https://vuminhkhoa-brain-health.streamlit.app/

## Features

- Upload MRI brain scan images and classify them into one of four classes: "Glioma", "Meningioma", "No Tumor", or "Pituitary"
- Trained on the dataset from https://github.com/sartajbhuvaji/brain-tumor-classification-dataset
- Fine-tuned using a pretrained PyTorch ResNet50 model with RadImageNet weights from https://huggingface.co/Lab-Rasool/RadImageNet
- Built with **Streamlit** and **PyTorch**

## Project Status

The app has completed its **main functionality**:  
- ✅ MRI brain scan **classification into 4 classes**:  
  - Glioma  
  - Meningioma  
  - No Tumor  
  - Pituitary  
- ✅ User-friendly interface built with Streamlit  
- ✅ Achieved ~90% test accuracy  
- 🚧 Planned improvements: Adding tumor segmentation feature  

## Local Setup

```bash
git clone https://github.com/vuminhkh0a/BRAIN_TUMOR.git
cd BRAIN_TUMOR
pip install -r requirements.txt
streamlit run Home.py

## Tutorial
