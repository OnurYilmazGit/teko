import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 2
st.session_state.current_page = "Find Court"
st.session_state.current_index = 3


# initialize session state attributes
question_steps, document_steps = get_question_dicts()
for attr in list(question_steps.keys()) + list(document_steps.keys()):
    if attr not in st.session_state.keys():
        st.session_state[attr] = None


show_navbar()
show_sidebar()


chapter_spacer()
st.subheader("What is the subject of dispute in your case?")
st.progress((1.0 / 7) * current_step)
st.markdown('<div style="text-align: justify;">'
            'The subject of dispute influences the objective juristiction of your case. While disputes about private '
            'rents are always negotiated at the Amtsgericht, commercial rent is either discussed at the Amtsgericht or '
            'Landesgericht.'
            '</div>', unsafe_allow_html=True)


question_subject = st.selectbox(label="", options=("Private Rent", "Commercial Rent"))
next_question = st.button("Next Question")
if next_question:
    st.session_state.question_subject = question_subject
    switch_page("question_case")
