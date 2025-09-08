# 🧠 Brain MRI Diagnosis App

An experimental Streamlit application for detecting brain tumors from medical images. This project is **still under development**.

## Demo App

https://vuminhkhoa-brain-health.streamlit.app/

## Features

- Upload MRI brain scan images  
- Early-stage implementation of tumor classification 
- Trained with dataset from https://github.com/sartajbhuvaji/brain-tumor-classification-dataset
- Trained with pretrained Resnet50 model using RadImageNet weights
- Built with **Streamlit** for quick prototyping and deployment  
- Code written in **Python** with focus on PyTorch

## Project Status

The app has completed its **main functionality**:  
- ✅ MRI brain scan **classification into 4 classes**:  
  - Glioma  
  - Meningioma  
  - No Tumor  
  - Pituitary  
- ✅ User-friendly interface with Streamlit
- ✅ Achieved ~90% testing accuracy
- 🚧 Further improvements planned: 

## Local Setup

To run the app locally:

```bash
git clone https://github.com/vuminhkh0a/BRAIN_TUMOR.git
cd BRAIN_TUMOR
pip install -r requirements.txt
streamlit run app.py
