import streamlit as st

st.title('How to use')

video = open("tutorial.webm", "rb").read()

st.video(video)
