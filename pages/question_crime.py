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
current_step = 1

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

st.subheader("Is this case the matter of a current criminal proceeeding?")
st.progress(1.0 / (len(question_steps.keys()) + 1) * current_step)
st.markdown('<div style="text-align: justify;">'
            'In the context of criminal proceeding, a court can not be selected by a citizen. Please refer to your '
            'subpoena for the appropriate court of a criminal proceeding.'
            '</div>', unsafe_allow_html=True)
st.selectbox(label="", options=("Yes", "No"))

next_question = st.button("Next Question")
if next_question:
    switch_page("question_subject")