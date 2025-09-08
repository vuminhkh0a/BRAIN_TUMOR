import streamlit as st

st.title('Brain Tumor classification')

input_image = st.file_uploader(type=["jpg", "jpeg", "png"])

if input_image:
  st.write('Received')
