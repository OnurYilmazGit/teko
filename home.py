import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path


st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
hide_pages(["home", "question_subject", "question_amount"])

st.markdown('<h1 style="text-align: center;">TEKO</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center;">Unlocking Justice. Made Easy.</h2>', unsafe_allow_html=True)

current_path = str(Path(__file__).parents[0])
suits_image = Image.open(current_path + "/assets/suits.jpeg")
st.image(suits_image)


next_question = st.button("Start Survey")
if next_question:
    switch_page("question_crime")