import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[1])
wreath_black_image = Image.open(current_path + "/assets/wreath_black.png")
wreath_blue_image = Image.open(current_path + "/assets/wreath_blue.png")
current_step = 3

# initialize session state attributes
for attr in ['crime', 'subject', 'amount', 'appeal', 'city']:
    if attr not in st.session_state:
        st.session_state[attr] = None

show_navbar()


with st.sidebar:
    question_steps = {"question_crime": "Crime", "question_subject": "Subject", "question_amount": "Amount",
                      "question_appeal": "Appeal", "question_city": "City"}
    i = 1
    for key, value in question_steps.items():

        if i < current_step:
            col1, col2 = st.columns([0.15, 0.85])
            with col1:
                st.image(wreath_black_image)
            with col2:
                subject = st.button(value)
                if subject:
                    switch_page(key)

        else:
            col1, col2 = st.columns([0.15, 0.85])
            with col1:
                st.image(wreath_blue_image)
            with col2:
                subject = st.button(value)
                if subject:
                    switch_page(key)

        i += 1


chapter_spacer()
st.subheader("What is the monetary amount of dispute in your case?")
st.markdown('<div style="text-align: justify;">'
            'The monetary amount of dispute influences the objective juristiction of your case. While disputes about '
            'commercial rents up to 5000 Euros are always negotiated at the Amtsgericht, higher monetary amounts are '
            'discussed at the Landesgericht.'
            '</div>', unsafe_allow_html=True)
st.progress(1.0 / (len(question_steps.keys()) + 1) * current_step)

if st.session_state.amount is None:
    amount = st.selectbox(label="", options=("", "Less than 5000 Euros", "More than 5000 Euros"))
    if amount != "":
        st.session_state.amount = amount
else:
    st.session_state.amount = st.selectbox(label="", options=("Less than 5000 Euros", "More than 5000 Euros"), index=["Less than 5000 Euros", "More than 5000 Euros"].index(st.session_state.amount))

next_question = st.button("Next Question")
if next_question:
    if st.session_state.amount == "":
        st.warning("Please answer the question before proceeding.")
    else:
        switch_page("question_appeal")
