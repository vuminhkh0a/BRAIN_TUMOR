import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
import os
from PIL import Image
import torch
import torch.nn as nn
from torchvision.transforms import v2
from torchvision.models import resnet50
from sklearn.metrics import multilabel_confusion_matrix, ConfusionMatrixDisplay
import model
from model import test_transform, model


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# st.set_page_config(page_title='Brain MRI Diagnosis App')
# st.sidebar.success('Please select a page')
# st.title('Brain MRI Diagnosis App')

main_page = st.Page(page='streamlit_app.py', title='Brain MRI Diagnosis App', default=True)
page1 = st.Page(page='streamlit_app_page1.py', title='How to use')
page2 = st.Page(page='streamlit_app_page2.py', title='About me')
pg = st.navigation([main_page, page1, page2])


input_image = st.file_uploader('Please upload your brain MRI image', type=["jpg", "jpeg", "png"])

if input_image is not None:
  st.write('Image received!')
  input_image = Image.open(input_image).convert('RGB')
  st.image(input_image)
else:
  st.write('No image is chosen!')

if input_image is not None:
  model.eval()
  with torch.no_grad():
    input_image = test_transform(input_image).to(device)
    prediction = model(input_image.unsqueeze(0))
    sm = nn.Softmax(dim=1)
    prediction = sm(prediction)

    # Plot
    prediction = prediction.squeeze().numpy()
    encode_label = {0:'Glioma', 1:'Meningioma', 2:'No tumor', 3:'Pituitary'}
    st.write('Predicted class:', encode_label[np.argmax(prediction)])
    fig = plt.figure(figsize=(10, 10))
    sns.barplot(x=prediction, y=['Glioma', 'Meningioma', 'No tumor', 'Pituitary'], palette='Set2')
    plt.xlabel('Confidences')
    plt.ylabel('Classes')
    st.pyplot(fig)


