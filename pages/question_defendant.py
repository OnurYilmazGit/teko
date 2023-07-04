import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
import re
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


chapter_spacer()
if st.session_state.current_lang == "English":
    st.subheader(f"What is the full name and address of the defendant?")
    st.progress((1.0 / 7) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'Please provide the address in the shown format.'
                '</div>', unsafe_allow_html=True)
else:
    st.subheader(f"Was ist der volle Name und die Adresse des Beklagten?")
    st.progress((1.0 / 7) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'Bitte geben Sie die Adresse im angegebenen Format an.'
                '</div>', unsafe_allow_html=True)

question_defendant = st.text_area(label="Defendant information", placeholder="Karl Kraus (Mieter/Vermieter),\nMusterstraße 8,\n20566 Muster", 
                                  height=200, max_chars=100, label_visibility="hidden").strip()


if st.session_state.current_lang == "English":
    next_question = st.button("Next question")
    if next_question:
        pattern = r'^[A-Za-z\s\(\).,]+,\s*\n[A-Za-zäöüß\. ]+ \d+,\s*\n\d{5} [A-Za-zäöüß ]+$'
        if bool(re.match(pattern, question_defendant)):
            st.session_state.question_defendant = question_defendant
            switch_page("question_target")
        else:
            st.warning(f"Please provide a correct address format.")
else:
    next_question = st.button("Nächste Frage")
    if next_question:
        pattern = r'^[A-Za-z\s\(\).,]+,\s*\n[A-Za-zäöüß\. ]+ \d+,\s*\n\d{5} [A-Za-zäöüß ]+$'
        if bool(re.match(pattern, question_defendant)):
            st.session_state.question_defendant = question_defendant
            switch_page("question_target")
        else:
            st.warning(f"Bitte geben Sie die Anschrift in einem korrekten Format an.")
