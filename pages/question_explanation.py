import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 5
st.session_state.current_page = "Find Court"
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
                        " Euro zuzüglich Zinsen in Höhe fünf Prozentpunkten über dem Basiszinssatz aus diesem Betrag seit Rechtshängigkeit zu zahlen."+
                        "\n\nFür den Fall, dass das Gericht das schriftliche Vorverfahren anordnet, wird beantragt, ein Versäumnisurteil (§ 331 Absatz 3 ZPO) zu erlassen, sofern der Beklagte trotz Aufforderung seine Verteidigungsabsicht nicht zeitgerecht anzeigt (§ 276 Absatz 1 ZPO).\n\n",
                    "Abrechnung der Nebenkosten": "Der Beklagte wird verurteilt, über die in der " + city +
                        " gelegene Wohnung in der Zeit vom 01.01 - 31.12.yyyy angefallenen Betriebskosten abzurechnen.\n\n"+
                        "Der Kläger mietete die im Antrag genauer bezeichnete Wohnung im Jahr yyyy an. Der Kläger hat für die Betriebskosten insgesamt eine monatliche Vorauszahlung in Höhe von XX Euro zu leisten." +
                        " Die gesetzlichen Bestimmungen sehen eine Frist zur Abrechnung innerhalb von spätestens zwölf Monaten seit Ende des Abrechnungszeitraumes vor. Der Beklage hätte damit über die Betriebskosten spätestens bis zum 31.12.yyyy abrechnen müssen. Obgleich der Kläger vor der Abrechnung auf ebendiese Pflicht hingewiesen hat, blieb der Beklagte untätig."}


explanation = explanation_dict[target]

print(explanation)

chapter_spacer()
st.subheader(f"Please give a concise explanation for your case.")
st.progress((1.0 / 7) * current_step)
st.markdown('<div style="text-align: justify;">'
            'The explanation should include what you want to achieve with your case and the description of the facts.'
            '</div>', unsafe_allow_html=True)


question_explanation = st.text_area(label="Concise Explanation for the case.", value=explanation, placeholder="Concise Explanation for the case.",
                                    height=1000, label_visibility="hidden").strip()

next_question = st.button("Next question")

if next_question:
    st.session_state.question_explanation = question_explanation
    switch_page("question_evidence")
