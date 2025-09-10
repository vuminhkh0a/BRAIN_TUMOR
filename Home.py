import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from PIL import Image
import torch
import torch.nn as nn
from torchvision.transforms import v2
from torchvision.models import resnet50

import model
from model import test_transform, model
import tumor_wiki
from tumor_wiki import explain
import setup
from setup import overall
overall()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

st.title('🧠 Brain Tumor MRI Diagnosis App')
st.divider()
st.markdown('Github repository: https://github.com/vuminhkh0a/BRAIN_TUMOR')
st.divider()
st.markdown('### Model input')
st.markdown('The model accepts brain scan MRI image (.jpg, .jpeg, .png) as input')
st.markdown('### Model output')
st.markdown("""
The model's output corresponds to one of four **distinct medical conditions** based on the MRI scan:
- **Glioma**, **Meningioma**, **Pituitary** – types of brain tumor  
- **No Tumor** – healthy brain with no signs of tumor
""")
st.divider()
st.markdown('### Upload image')
input_image = st.file_uploader('⚠️ This app is hosted on Streamlit Community Cloud, so it may take a little time to load at the beginning.', type=["jpg", "jpeg", "png"])

if input_image is not None:
  st.write('Image received!')
  input_image = Image.open(input_image).convert('RGB')
  st.image(input_image)
  
st.divider()

if input_image is not None:
  model.eval()
  with torch.no_grad():
    input_image = test_transform(input_image).to(device)
    prediction = model(input_image.unsqueeze(0))
    sm = nn.Softmax(dim=1)
    prediction = sm(prediction)

    prediction = prediction.squeeze().numpy()
    encode_label = {0:'Glioma', 1:'Meningioma', 2:'No tumor', 3:'Pituitary'}
    case = encode_label[np.argmax(prediction)]
    st.markdown(f'### Result: {case}')
    fig = plt.figure(figsize=(10, 10))
    sns.barplot(x=prediction, y=['Glioma', 'Meningioma', 'No tumor', 'Pituitary'], palette='Set2')
    plt.xlabel('Confidences')
    plt.ylabel('Classes')
    st.pyplot(fig)

    st.divider()
    explain(case)
  


