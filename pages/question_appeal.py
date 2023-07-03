import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 4
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
    st.subheader("Has this case already been negotiated in front of court? Do you want to appeal?")
    st.markdown('<div style="text-align: justify;">'
                'Appeals against decisions of an Amtsgericht or Landesgericht are usually negotiated at the '
                'Oberlandesgericht.'
                '</div>', unsafe_allow_html=True)
else:
    st.subheader("HWurde Ihr Fall bereits vor gericht verhandelt? Möchten Sie Beschwerde einlegen oder in Berufung gehen?")
    st.markdown('<div style="text-align: justify;">'
                'Beschwerden und Berufung gegen die Entscheidungen eines Amtsgerichts oder Landesgerichts '
                'werden vor dem Oberlandesgericht. verhandelt. '
                '</div>', unsafe_allow_html=True)
st.progress((1.0 / 7) * current_step)

if st.session_state.current_lang == "English":
    question_appeal = st.selectbox(label="", options=("No", "Yes"))
    next_question = st.button("Next Question")
else:
    question_appeal = st.selectbox(label="", options=("Nein", "Ja"))
    next_question = st.button("Nächste Frage")

if next_question:
    st.session_state.question_appeal = question_appeal
    switch_page("question_amount")
