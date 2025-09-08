import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import cv2
from PIL import Image
import torch
import torch.nn as nn
from torch.nn import CrossEntropyLoss
import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler
from torch.utils.data import random_split, Dataset, DataLoader, Subset
from torchvision.transforms import v2
from torchvision.models import resnet50, ResNet50_Weights, efficientnet_b0, EfficientNet_B0_Weights
from sklearn.metrics import multilabel_confusion_matrix, ConfusionMatrixDisplay
from huggingface_hub import hf_hub_download


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

st.title('Brain Tumor classification')

input_image = st.file_uploader('Upload image', type=["jpg", "jpeg", "png"])

if input_image:
  st.write('Received')
  st.write(type(input_image))


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

model.load_state_dict(torch.load('best_model_Sequential.pth', weights_only=True))
model.eval()



