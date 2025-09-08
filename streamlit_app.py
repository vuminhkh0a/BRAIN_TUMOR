import streamlit as st
import torch

st.title('Brain Tumor classification')

input_image = st.file_uploader('Upload image', type=["jpg", "jpeg", "png"])

if input_image:
  st.write('Received')
