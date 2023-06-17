import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *
from src.google_maps import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 1
st.session_state.current_page = "Find Court"
st.session_state.current_index = 3


# initialize session state attributes
question_steps, document_steps = get_question_dicts()
for attr in list(question_steps.keys()) + list(document_steps.keys()):
    if attr not in st.session_state.keys():
        st.session_state[attr] = None


show_navbar()
show_sidebar()

court_decision = st.session_state.question_court
court_location = get_address(court_decision)

chapter_spacer()
st.subheader(f"The Court Finder identified {court_decision} as the appropriate court.")
st.progress((1.0 / 7) * current_step)
st.markdown('<div style="text-align: justify;">'
            'Please confirm the court selection or enter the details of another court.'
            '</div>', unsafe_allow_html=True)

question_court_address = st.text_input(label="Appropriate Court", value=court_decision+', '+court_location, max_chars=100, label_visibility="hidden").strip()


next_question = st.button("Next question")

if next_question:
    st.session_state.question_court = question_court_address
    switch_page("question_plaintiff")
