import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 5
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
st.subheader("What is the monetary amount of dispute in your case?")
st.markdown('<div style="text-align: justify;">'
            'The monetary amount of dispute influences the objective juristiction of your case. While disputes about '
            'commercial rents up to 5000 Euros are always negotiated at the Amtsgericht, higher monetary amounts are '
            'discussed at the Landesgericht.'
            '</div>', unsafe_allow_html=True)
st.progress((1.0 / 7) * current_step)

question_amount = st.number_input(label="The amount of dispute", min_value=1, label_visibility="hidden")

next_question = st.button("Next Question")
if next_question:
    st.session_state.question_amount = question_amount
    switch_page("question_city")
