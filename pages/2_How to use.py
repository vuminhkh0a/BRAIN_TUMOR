import streamlit as st
import setup
from setup import overall

st.title('How to use')
overall()

video = open("tutorial.webm", "rb").read()

st.video(video)
