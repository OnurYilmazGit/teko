import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 6
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

amount = str(st.session_state.question_amount2)
plaintiff = st.session_state.question_plaintiff
lines = plaintiff.split("\n")
city = ', '.join([line.rstrip(',') for line in lines[1:]])

target = st.session_state.question_target

explanation_dict = {"Rückzahlung Mietkaution": "Der Beklagte wird verurteilt, an den Kläger " + amount + 
                        " Euro zuzüglich Zinsen in Höhe fünf Prozentpunkten über dem Basiszinssatz aus diesem Betrag seit Rechtshängigkeit zu zahlen.",
                    "Abrechnung der Nebenkosten": "Der Beklagte wird verurteilt, über die in der " + city +
                        " gelegene Wohnung in der Zeit vom 01.01 - 31.12.yyyy angefallenen Betriebskosten abzurechnen.\n\n"+
                        "Der Kläger mietete die im Antrag genauer bezeichnete Wohnung im Jahr yyyy an. Der Kläger hat für die Betriebskosten insgesamt eine monatliche Vorauszahlung in Höhe von XX Euro zu leisten." +
                        " Die gesetzlichen Bestimmungen sehen eine Frist zur Abrechnung innerhalb von spätestens zwölf Monaten seit Ende des Abrechnungszeitraumes vor. Der Beklage hätte damit über die Betriebskosten spätestens bis zum 31.12.yyyy abrechnen müssen. Obgleich der Kläger vor der Abrechnung auf ebendiese Pflicht hingewiesen hat, blieb der Beklagte untätig."}


explanation = explanation_dict[target]

print(explanation)

chapter_spacer()
if st.session_state.current_lang == "English":
    st.subheader(f"Please give a concise explanation for your case.")
    st.progress((1.0 / 8) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'The explanation should include what you want to achieve with your case and the description of the facts.'
                '</div>', unsafe_allow_html=True)
else:
    st.subheader(f"Bitte geben Sie eine präzise Erläuterung für Ihren Fall.")
    st.progress((1.0 / 8) * current_step)
    st.markdown('<div style="text-align: justify;">'
                'Die Erklärung sollte beinhalten, was Sie mit Ihrem Fall erreichen wollen und die Beschreibung des Sachverhalts. Bitte füllen Sie etwaige Platzhalter für Datumsangaben und Geldbeträge aus.'
                '</div>', unsafe_allow_html=True)


question_explanation = st.text_area(label="Concise Explanation for the case.", value=explanation, placeholder="Concise Explanation for the case.",
                                    height=300, label_visibility="hidden").strip()


if st.session_state.current_lang == "English":
    next_question = st.button("Next question")
    if next_question:
        st.session_state.question_explanation = question_explanation
        switch_page("question_evidence")
else:
    next_question = st.button("Nächste Frage")
    if next_question:
        st.session_state.question_explanation = question_explanation
        switch_page("question_evidence")
