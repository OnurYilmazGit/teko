import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 5
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
    st.subheader("What is the monetary amount of dispute in your case?")
    st.markdown('<div style="text-align: justify;">'
                'The monetary amount of dispute influences the objective juristiction of your case. While disputes about '
                'commercial rents up to 5000 Euros are always negotiated at the Amtsgericht, higher monetary amounts are '
                'discussed at the Landgericht.'
                '</div>', unsafe_allow_html=True)
else:
    st.subheader("Wie hoch ist der Streitwert Ihres Falles?")
    st.markdown('<div style="text-align: justify;">'
                'Der Streitwert des Falles bestimmmt die sachliche Zuständigkeit eines Gerichtes. Während Streitigkeiten '
                'über gewerbliche Mieten bis zu 5000 Euro immer am Amtsgericht verhandelt werden, sind die Landgerichte '
                'für Streitwerte über 5000 Euro zuständig. '
                '</div>', unsafe_allow_html=True)
st.progress((1.0 / 7) * current_step)

question_amount = st.number_input(label="The amount of dispute", min_value=1, label_visibility="hidden")

if st.session_state.current_lang == "English":
    next_question = st.button("Next Question")
else:
    next_question = st.button("Nächste Frage")
if next_question:
    st.session_state.question_amount = question_amount
    switch_page("question_city")
