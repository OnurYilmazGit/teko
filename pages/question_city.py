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
current_step = 5

# initialize session state attributes
for attr in ['crime', 'subject', 'amount', 'appeal', 'city']:
    if attr not in st.session_state:
        st.session_state[attr] = ''

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
st.subheader("In which city do you live? Please provide the PLZ.")
st.markdown('<div style="text-align: justify;">'
            'TODO: Text'
            '</div>', unsafe_allow_html=True)
st.progress(1.0 / (len(question_steps.keys()) + 1) * current_step)

city = st.text_input(label="", placeholder="PLZ", max_chars=5)
if city.strip() != "":
    st.session_state.city = city

next_question = st.button("Finalize Test")
if next_question:
    unanswered_questions = [key.replace("question_", "").capitalize() for key, value in st.session_state.items() if value in [None, ""]]
    if unanswered_questions:
        unanswered_questions_str = ", ".join(unanswered_questions)
        st.warning(f"Please answer the following question(s): {unanswered_questions_str}")
    else:
        switch_page("survey_results")
