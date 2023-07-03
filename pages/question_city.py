import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 6
st.session_state.current_page = "Find Court"
st.session_state.current_index = 3


# initialize session state attributes
question_steps, document_steps = get_question_dicts()
for attr in list(question_steps.keys()) + list(document_steps.keys()):
    if attr not in st.session_state.keys():
        st.session_state[attr] = None


show_navbar()
show_sidebar()


chapter_spacer()
st.subheader("In which city do you live? Please provide the PLZ.")
st.markdown('<div style="text-align: justify;">'
            'TODO: Text'
            '</div>', unsafe_allow_html=True)
st.progress((1.0 / 7) * current_step)

question_city = st.text_input(label="", placeholder="PLZ", help="The PLZ contains 5 digits and refers to one specific city.", max_chars=5).strip()

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
