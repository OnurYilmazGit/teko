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
if st.session_state.current_lang == "English":
    st.subheader("What is the cause of action in your case?")
    st.progress((1.0 / 7) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'This information will become relevant when the lawsuit document is created.'
                '</div>', unsafe_allow_html=True)
else:
    st.subheader("Was ist der Grund der Klage in Ihrem Fall?")
    st.progress((1.0 / 7) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'Diese Information ist für die Erstellung des Klagedokumentes erforderlich.'
                '</div>', unsafe_allow_html=True)

if st.session_state.current_lang == "English":
    question_case = st.selectbox(label="", options=("Repayment of the rental deposit", "Settlement of the incidental rental costs", "Other"), label_visibility="hidden")
else:
    question_case = st.selectbox(label="", options=("Rückzahlung der Mietkaution", "Abrechnung der Nebenkosten", "Sonstiges"), label_visibility="hidden")

if st.session_state.current_lang == "English":
    next_question = st.button("Next Question")
    if next_question:
        st.session_state.question_case = question_case
        switch_page("question_appeal")
else:
    next_question = st.button("Nächste Frage")
    if next_question:
        st.session_state.question_case = question_case
        switch_page("question_appeal")
