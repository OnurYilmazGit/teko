import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages

hide_pages(["home", "question_subject", "question_amount"])
st.set_page_config(initial_sidebar_state="collapsed")

st.text("Moin")

next_question = st.button("Start Survey")
if next_question:
    switch_page("question_subject")