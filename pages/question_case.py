import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 3
if st.session_state.current_lang == "English":
    st.session_state.current_page = "Find Court"
    st.session_state.current_index = 3
else:
    st.session_state.current_page = "Gericht Finden"
    st.session_state.current_index = 3


# initialize session state attributes
question_steps, document_steps = get_question_dicts()
for attr in list(question_steps.keys()) + list(document_steps.keys()):
    if attr not in st.session_state.keys():
        st.session_state[attr] = None


show_navbar()
show_sidebar()


# Content: Question
chapter_spacer()
st.subheader("What is the subproblem of tenancy law is the subject of dispute in your case?")
st.progress((1.0 / 7) * current_step)
st.markdown('<div style="text-align: justify;">'
            'TEKO is currently only able to provide support in cases about repayment of rental deposit and '
            'settlement of incidental rental costs.'
            '</div>', unsafe_allow_html=True)
if st.session_state.current_lang == "English":
    question_case = st.selectbox(label="", options=("Repayment of the rental deposit", "Settlement of the incidental rental costs", "Other"), label_visibility="hidden")
else:
    question_case = st.selectbox(label="", options=("Rückzahlung der Mietkaution", "Abrechnung der Nebenkosten", "Sonstiges"), label_visibility="hidden")

next_question = st.button("Next Question")
if next_question:
    st.session_state.question_case = question_case
    switch_page("question_appeal")
