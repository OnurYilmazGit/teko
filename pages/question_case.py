import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import show_navbar, get_local_pages, chapter_spacer, components_spacer


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[1])
wreath_black_image = Image.open(current_path + "/assets/wreath_black.png")
wreath_blue_image = Image.open(current_path + "/assets/wreath_blue.png")
current_step = 3
st.session_state.current_page = "Find Court"
st.session_state.current_index = 3


# initialize session state attributes
question_steps = {"question_crime": "Crime", "question_subject": "Subject", "question_case": "Case",
                  "question_appeal": "Appeal", "question_amount": "Amount", "question_city": "City"}
for attr in question_steps.keys():
    if attr not in st.session_state.keys():
        st.session_state[attr] = None


show_navbar()


with st.sidebar:

    for key, value in question_steps.items():

        if st.session_state[key] or st.session_state[key] is not None:
            col1, col2 = st.columns([0.15, 0.85])
            with col1:
                st.image(wreath_black_image)
            with col2:
                subject = st.button(value)
                if subject:
                    switch_page(key)

        else:
            col1, col2 = st.columns([0.15, 0.85])
            with col1:
                st.image(wreath_blue_image)
            with col2:
                subject = st.button(value)
                if subject:
                    switch_page(key)


# Content: Question
chapter_spacer()
st.subheader("Which case do you want to file?")
st.progress((1.0 / 7) * current_step)
st.markdown('<div style="text-align: justify;">'
            'TODO: Text'
            '</div>', unsafe_allow_html=True)

question_case = st.selectbox(label="", options=("TODO", "TODO"))

next_question = st.button("Next Question")
if next_question:
    st.session_state.question_case = question_case
    switch_page("question_appeal")
