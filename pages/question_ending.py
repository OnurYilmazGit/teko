import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 7
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
st.subheader(f"Please provide the relevant evidence for your case")
st.progress((1.0 / 7) * current_step)

court = st.session_state.question_court.replace(', ', ',\n')
plaintiff = st.session_state.question_plaintiff.replace(', ', ',\n')
defendant = st.session_state.question_defendant.replace(', ', ',\n')
target = st.session_state.question_target.replace(', ', ',\n')
amount = str(st.session_state.question_amount2)
explanation = st.session_state.question_explanation
evidence = st.session_state.question_evidence

question_ending = st.text_area(label="Your information", value="An das \n\n" + court + "\n\n"
                                                                + "Klage" + "\n\n" + plaintiff + "\n\n"
                                                                + "-- Kläger --" + "\n\n" + "gegen" + "\n\n"
                                                                + defendant + "\n\n" + "-- Beklagter --" + "\n\n" 
                                                                + "wegen: " + target + "\n\n"
                                                                + "Streitwert: " + amount + "€\n\n"
                                                                + "Ich erhebe Klage und beantrage zu erkennen:" + "\n\n" 
                                                                + explanation + "\n\nBegründung" + "\n\n"
                                                                + evidence
                                                                , height=1500, max_chars=10000, label_visibility="hidden").strip()

next_question = st.button("Next question")

if next_question:
    st.session_state.question_ending = question_ending
    switch_page("question_ending")