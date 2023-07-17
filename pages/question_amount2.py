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

target = st.session_state.question_target
amount = st.session_state.question_amount

chapter_spacer()
if st.session_state.current_lang == "English":
    st.subheader(f"Please confirm the monetary amount of dispute in your case")
    st.progress((1.0 / 8) * current_step)
    if target == "Repayment of the rental deposit":
        st.markdown('<div style="text-align: justify;">'
                'Please confirm the amount of dispute or enter the correct amount. Please note that in cases involving utility bills, the amount is usually set at one-third of the utility bill paid for that year.'
                '</div>', unsafe_allow_html=True)
        amount = int(st.session_state.question_amount)
    elif target == "Settlement of the incidental rental costs":
        st.markdown('<div style="text-align: justify;">'
                'Please confirm the amount of dispute or enter the correct amount.'
                '</div>', unsafe_allow_html=True)
        amount = int(int(st.session_state.question_amount) / 3)
else:
    st.subheader(f"Bitte bestätigen sie den Streitwert in Ihrem Fall.")
    st.progress((1.0 / 8) * current_step)
    if target == "Abrechnung der Nebenkosten":
        st.markdown('<div style="text-align: justify;">'
                'Bitte bestätigen Sie den Streitwert oder geben Sie den richtigen Betrag ein. Bitte beachten Sie, dass in Fällen, in denen es um die Abrechnung der Nebenkosten geht, der Betrag in der Regel auf ein Drittel der für das betreffende Jahr gezahlten Nebenkosten festgesetzt wird.'
                '</div>', unsafe_allow_html=True)
        amount = int(int(st.session_state.question_amount)/3)
    elif target == "Rückzahlung Mietkaution":
        st.markdown('<div style="text-align: justify;">'
                'Bitte bestätigen Sie den angegebenen Streitwert oder geben Sie den korrekten Streitwert an'
                '</div>', unsafe_allow_html=True)
        amount = int(st.session_state.question_amount)

question_amount2 = st.number_input(label="The amount of dispute", value=amount,  min_value=1, label_visibility="hidden")


if st.session_state.current_lang == "English":
    next_question = st.button("Next question")
    if next_question:
        st.session_state.question_amount2 = question_amount2
        switch_page("question_explanation")
else:
    next_question = st.button("Nächste Frage")
    if next_question:
        st.session_state.question_amount2 = question_amount2
        switch_page("question_explanation")
