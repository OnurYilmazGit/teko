import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras import card
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from streamlit_option_menu import option_menu
from pages.custom_components import get_local_pages, show_navbar, chapter_spacer, components_spacer


# Set config
st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[0])
st.session_state.current_page = "Home"
st.session_state.current_index = 0


# Create Navbar
show_navbar()


# Content: Solution
col1, col2 = st.columns(2)
with col1:
    suits_image = Image.open(current_path + "/assets/house.jpg")
    st.image(suits_image)
with col2:
    st.subheader("We are your digital assistant in tenancy law")
    components_spacer()
    st.markdown('<div style="text-align: justify;">'
                'TEKO helps you in solving legal disputes about tenancy law. We got you covered for navigating through '
                'the labyrinth of the German court sytem. Our digital assistant supports you in finding the correct '
                'court and filing the corresponding documents.'
                '</div>', unsafe_allow_html=True)
    components_spacer()
    st.markdown('<div style="text-align: justify;">'
                'You can find more information about us here:'
                '</div>', unsafe_allow_html=True)
    about_us = st.button("About Us")
    if about_us:
        switch_page("about_us")


# Content: Value Proposition
chapter_spacer()
benefit1, benefit2, benefit3 = st.columns(3)
with benefit1:
    _, col2, _ = st.columns([0.3, 0.4, 0.3])
    with col2:
        key_image = Image.open(current_path + "/assets/key.png")
        st.image(key_image)
    _, col2, _ = st.columns([0.28, 0.44, 0.28])
    with col2:
        st.subheader("Access to Law")
    _, col2, _ = st.columns([0.15, 0.7, 0.15])
    with col2:
        st.markdown('<div style="text-align: justify;">'
                    'We strongly believe that every citizen should have access to justice - with TEKO this will be '
                    'ensured.'
                    '</div>', unsafe_allow_html=True)
with benefit2:
    _, col2, _ = st.columns([0.3, 0.4, 0.3])
    with col2:
        decision_image = Image.open(current_path + "/assets/decision-tree.png")
        st.image(decision_image)
    _, col2, _ = st.columns([0.24, 0.52, 0.24])
    with col2:
        st.subheader("Intuitive Process")
    _, col2, _ = st.columns([0.15, 0.7, 0.15])
    with col2:
        st.markdown('<div style="text-align: justify;">'
                    'Our easy-to-understand question-and-answer format guides you through the process, with our '
                    'decision tree algorithm providing highly accurate results.'
                    '</div>', unsafe_allow_html=True)
with benefit3:
    _, col2, _ = st.columns([0.3, 0.4, 0.3])
    with col2:
        coin_image = Image.open(current_path + "/assets/coin.png")
        st.image(coin_image)
    _, col2, _ = st.columns([0.16, 0.68, 0.16])
    with col2:
        st.subheader("Time and Cost Savings")
    _, col2, _ = st.columns([0.15, 0.7, 0.15])
    with col2:
        st.markdown('<div style="text-align: justify;">'
                    'No more wasting time and money - you have all valid information in one place!'
                    '</div>', unsafe_allow_html=True)


chapter_spacer()
start_survey = st.button("Find Court")
if start_survey:
    switch_page("question_crime")