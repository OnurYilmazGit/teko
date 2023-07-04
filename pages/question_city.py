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


chapter_spacer()
if st.session_state.current_lang == "English":
    st.subheader("In which city does the defendant live? Please provide the PLZ.")
    st.markdown('<div style="text-align: justify;">'
                'This information is necessary to provide you with the respective court in the relevant area.'
                '</div>', unsafe_allow_html=True)
else:
    st.subheader("In welcher Stadt wohnt der Beklagte? Bitte geben Sie die PLZ an.")
    st.markdown('<div style="text-align: justify;">'
                'Diese Information is erforderlich um das zuständige Gericht in der relevanten Region zu finden.'
                '</div>', unsafe_allow_html=True)
st.progress((1.0 / 7) * current_step)

if st.session_state.current_lang == "English":
    question_city = st.text_input(label="", placeholder="PLZ", help="The PLZ contains 5 digits and refers to one specific city.", max_chars=5).strip()
else:
    question_city = st.text_input(label="", placeholder="PLZ", help="Die PLZ besteht aus fünf Ziffern und bezieht sich auf Ihren Wohnort", max_chars=5).strip()

if st.session_state.current_lang == "English":
    next_question = st.button("Finalize Test")
    if next_question:
        if (len(question_city) is not 5) or (not question_city.isdigit()):
            st.warning(f"Please insert a correct PLZ.")
        else:
            st.session_state.question_city = question_city
            unanswered_questions = [key.replace("question_", "").capitalize() for key, value in st.session_state.items() if (value in [None, ""] and key in question_steps.keys())]
            if unanswered_questions:
                unanswered_questions_str = ", ".join(unanswered_questions)
                st.warning(f"Please answer the following question(s): {unanswered_questions_str}")
            else:
                switch_page("survey_results")

else:
    next_question = st.button("Fragebogen abschließen")
    if next_question:
        if (len(question_city) is not 5) or (not question_city.isdigit()):
            st.warning(f"Bitte geben Sie eine korrekte PLZ ein.")
        else:
            st.session_state.question_city = question_city
            unanswered_questions = [key.replace("question_", "").capitalize() for key, value in st.session_state.items()
                                    if (value in [None, ""] and key in question_steps.keys())]
            if unanswered_questions:
                unanswered_questions_str = ", ".join(unanswered_questions)
                st.warning(f"Bitte beantworten Sie die folgende(n) Frage(n): {unanswered_questions_str}")
            else:
                switch_page("survey_results")