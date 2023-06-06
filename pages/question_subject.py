import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path


hide_pages(["home", "question_crime", "question_subject", "question_amount", "question_appeal", "question_city",
            "survey_results"])
current_path = str(Path(__file__).parents[1])
wreath_black_image = Image.open(current_path + "/assets/wreath_black.png")
wreath_blue_image = Image.open(current_path + "/assets/wreath_blue.png")
current_step = 2

with st.sidebar:

    question_steps = {"question_crime": "Crime", "question_subject": "Subject", "question_amount": "Amount",
                      "question_appeal": "Appeal", "question_city": "City"}
    print("LEEEN", len(question_steps.keys()))
    i=1
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

st.subheader("What is the subject of dispute in your case?")
st.progress(1.0 / (len(question_steps.keys()) + 1) * current_step)
st.markdown('<div style="text-align: justify;">'
            'The subject of dispute influences the objective juristiction of your case. While disputes about private '
            'rents are always negotiated at the Amtsgericht, commercial rent is either discussed at the Amtsgericht or '
            'Landesgericht.'
            '</div>', unsafe_allow_html=True)
st.selectbox(label="", options=("Private Rent", "Commercial Rent"))

next_question = st.button("Next Question")
if next_question:
    switch_page("question_amount")