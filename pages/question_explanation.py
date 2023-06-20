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
target = st.session_state.question_target

explanation_dict = {"Rückzahlung Mietkaution": "Der Beklagte wird verurteilt, an den Kläger " + amount + 
                 " Euro zuzüglich Zinsen in Höhe fünf Prozentpunkten über dem Basiszinssatz aus diesem Betrag seit Rechtshängigkeit zu zahlen."
                 + "\n\nFür den Fall, dass das Gericht das schriftliche Vorverfahren anordnet, wird beantragt, ein Versäumnisurteil (§ 331 Absatz 3 ZPO) zu erlassen, sofern der Beklagte trotz Aufforderung seine Verteidigungsabsicht nicht zeitgerecht anzeigt (§ 276 Absatz 1 ZPO).\n\n",
                 "ABC": "XYZ\n\n", "Evidence 3": "Desc 3\n"}


explanation = explanation_dict[target]

print(explanation)

chapter_spacer()
st.subheader(f"Please give a concise explanation for your case. This should include what you want to achieve with your case and the description of the facts.")
st.progress((1.0 / 7) * current_step)


question_explanation = st.text_area(label="Concise Explanation for the case.", value=explanation, placeholder="Concise Explanation for the case.",
                                    height=1000, label_visibility="hidden").strip()

next_question = st.button("Next question")

if next_question:
    st.session_state.question_explanation = question_explanation
    switch_page("question_evidence")
