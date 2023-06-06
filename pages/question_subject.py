import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages


hide_pages(["home", "question_subject", "question_amount"])

st.subheader("What is the subject of dispute in your case?")
st.selectbox(label="", options=("Private Rent", "Commercial Rent"))

next_question = st.button("Next Question")
if next_question:
    switch_page("question_amount")