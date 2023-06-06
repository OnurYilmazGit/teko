import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages


hide_pages(["home", "question_subject", "question_amount"])

st.subheader("What is the monetary amount of dispute in your case?")
st.selectbox(label="", options=("<= 5000 Euros", "> 5000 Euros"))

next_question = st.button("Next Question")
if next_question:
    switch_page("")