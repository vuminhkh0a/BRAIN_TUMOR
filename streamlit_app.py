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


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

st.title('Brain Tumor classification')

input_image = st.file_uploader('Upload image', type=["jpg", "jpeg", "png"])

if input_image is not None:
  st.write('Received')
  input_image = Image.open(input_image).convert('RGB')
  st.image(input_image, caption='Received image')
else:
  st.write('No image')


test_transform = v2.Compose([
    v2.PILToTensor(),
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    v2.Resize((256, 256))
])

class Classifier(nn.Module):
    def __init__(self, n_output_class):
        super().__init__()
        self.dropout = nn.Dropout()
        self.linear = nn.Linear(2048, n_output_class)
    
    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.dropout(x)
        x = self.linear(x)
        return x

class Backbone(nn.Module):
    def __init__(self):
        super().__init__()
        base_model = resnet50(pretrained=False)
        encoder_layers = list(base_model.children())
        self.backbone = nn.Sequential(*encoder_layers[:9])
    
    def forward(self, x):
        x = self.backbone(x)
        return x
      
backbone = Backbone()
classifier = Classifier(4) 
model = nn.Sequential(backbone, classifier)
model.load_state_dict(torch.load('best_model_Sequential.pth', weights_only=True, map_location=torch.device('cpu')))
model = model.to(device)

if input_image is not None:
  model.eval()
  with torch.no_grad():
    input_image = test_transform(input_image).to(device)
    prediction = model(input_image.unsqueeze(0))
    sm = nn.Softmax(dim=1)
    prediction = sm(prediction)

    # Plot
    prediction = prediction.squeeze().numpy()
    encode_label = {0:'glioma', 1:'meningioma', 2:'notumor', 3:'pituitary'}
    st.write('Predicted class:', encode_label[np.argmax(prediction)])
    fig = plt.figure(figsize=(10, 10))
    sns.barplot(x=prediction, y=['glioma', 'meningioma', 'notumor', 'pituitary'])
    st.pyplot(fig)


