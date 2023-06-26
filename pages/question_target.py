import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 4
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
st.subheader(f"Please provide the reason for filing the case")
st.progress((1.0 / 7) * current_step)

question_target = st.selectbox(label="Your information", options=("Rückzahlung Mietkaution", "Abrechnung der Nebenkosten"), label_visibility="hidden").strip()

if question_target == "Rückzahlung Mietkaution":
    st.markdown('<div style="text-align: justify;">'
            'Please note that you can usually get your deposit back at the earliest 6 months after handing over the rental property.'
            '<br>''<br>'
            '</div>', unsafe_allow_html=True)
    
elif question_target == "Abrechnung der Nebenkosten":
    st.markdown('<div style="text-align: justify;">'
            'Please note that you must give the landlord a period of 12 months after the end of the billing period until he needs to provide you with the utility bill.'
            '<br>''<br>'
            '</div>', unsafe_allow_html=True)



next_question = st.button("Next question")

if next_question:
    st.session_state.question_target = question_target
    switch_page("question_amount2")
