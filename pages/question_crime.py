import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


def check_all_questions_answered(session_state):
    # Returns False if any question is unanswered
    return all([bool(session_state[attr]) for attr in ['crime', 'subject', 'amount', 'appeal', 'city']])


def update_next_question_state():
    if 'next_question_sidebar' not in st.session_state:
        st.session_state.next_question_sidebar = False


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[1])
wreath_black_image = Image.open(current_path + "/assets/wreath_black.png")
wreath_blue_image = Image.open(current_path + "/assets/wreath_blue.png")
current_step = 1

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


# Content: Question
chapter_spacer()
st.subheader("Is this case the matter of a current criminal proceeding?")
st.progress(1.0 / (len(question_steps.keys()) + 1) * current_step)
st.markdown('<div style="text-align: justify;">'
            'In the context of a criminal proceeding, a court cannot be selected by a citizen. Please refer to your '
            'subpoena for the appropriate court of a criminal proceeding.'
            '</div>', unsafe_allow_html=True)

if st.session_state.crime is None:
    crime = st.selectbox(label="Please select an option", options=("", "Yes", "No"))
    if crime != "":
        st.session_state.crime = crime
else:
    st.session_state.crime = st.selectbox(label="Please select an option", options=("Yes", "No"),
                                          index=["Yes", "No"].index(st.session_state.crime))
    update_next_question_state()

next_question_content = st.button("Next Question", key='next_question_content')
if next_question_content:
    if st.session_state.crime == "":
        st.warning("Please answer the question before proceeding.")
    else:
        switch_page("question_subject")
