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
if "current_lang" not in st.session_state.keys():
    st.session_state.current_lang = "English"
    st.session_state.lang_index = 0
if st.session_state.current_lang == "English":
    st.session_state.current_page = "Home"
    st.session_state.current_index = 0
else:
    st.session_state.current_page = "Startseite"
    st.session_state.current_index = 0


# Create Navbar
show_navbar()


# Content: Solution
col1, col2 = st.columns(2)
with col1:
    suits_image = Image.open(current_path + "/assets/house.jpg")
    st.image(suits_image)
with col2:
    if st.session_state.current_lang == "English":
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
    else:
        st.subheader("Wir sind Ihr digitaler Assistent zu Mietrecht")
        components_spacer()
        st.markdown('<div style="text-align: justify;">'
                    'TEKO hilft Ihnen bei der Lösung rechtlicher Streitigkeiten rund um das Thema Mietrecht. Wir '
                    'unterstützen Sie bei der Navigation durch das Labyrinth des deutschen Gerichtssystems. Unser '
                    'digitaler Assistent unterstützt Sie dabei, das richtige Gericht zu finden und die entsprechenden '
                    'Unterlagen einzureichen.'
                    '</div>', unsafe_allow_html=True)
        components_spacer()
        st.markdown('<div style="text-align: justify;">'
                    'Sie können mehr Informationen über uns hier finden:'
                    '</div>', unsafe_allow_html=True)
        about_us = st.button("Über uns")
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
    if st.session_state.current_lang == "English":
        _, col2, _ = st.columns([0.28, 0.44, 0.28])
        with col2:
            st.subheader("Access to Law")
    else:
        _, col2, _ = st.columns([0.24, 0.52, 0.24])
        with col2:
            st.subheader("Zugang zu Recht")
    _, col2, _ = st.columns([0.15, 0.7, 0.15])
    with col2:
        st.markdown('<div style="text-align: justify;">'
                    'Wir sind der festen Überzeugung, dass jeder Bürger Zugang zu Gerechtigkeit haben sollte – '
                    'wir bei TEKO stellen dies sicher.'
                    '</div>', unsafe_allow_html=True)
with benefit2:
    _, col2, _ = st.columns([0.3, 0.4, 0.3])
    with col2:
        decision_image = Image.open(current_path + "/assets/decision-tree.png")
        st.image(decision_image)

    if st.session_state.current_lang == "English":
        _, col2, _ = st.columns([0.24, 0.52, 0.24])
        with col2:
            st.subheader("Intuitive Process")
    else:
        _, col2, _ = st.columns([0.22, 0.56, 0.22])
        with col2:
            st.subheader("Intuitiver Prozess")
    _, col2, _ = st.columns([0.15, 0.7, 0.15])
    with col2:
        if st.session_state.current_lang == "English":
            st.markdown('<div style="text-align: justify;">'
                        'Our easy-to-understand question-and-answer format guides you through the process, with our '
                        'decision tree algorithm providing highly accurate results.'
                        '</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="text-align: justify;">'
                        'Unser leicht verständliches Frage-und-Antwort-Format führt Sie durch den Prozess, wobei '
                        'unser Entscheidungs-Algorithmus äußerst genaue Ergebnisse liefert.'
                        '</div>', unsafe_allow_html=True)
with benefit3:
    _, col2, _ = st.columns([0.3, 0.4, 0.3])
    with col2:
        coin_image = Image.open(current_path + "/assets/coin.png")
        st.image(coin_image)

    if st.session_state.current_lang == "English":
        _, col2, _ = st.columns([0.16, 0.68, 0.16])
        with col2:
            st.subheader("Time and Cost Savings")
    else:
        _, col2, _ = st.columns([0.10, 0.8, 0.10])
        with col2:
            st.subheader("Zeit- und Geldersparnisse")
    _, col2, _ = st.columns([0.15, 0.7, 0.15])
    with col2:
        if st.session_state.current_lang == "English":
            st.markdown('<div style="text-align: justify;">'
                        'No more wasting time and money - you have all valid information in one place!'
                        '</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div style="text-align: justify;">'
                        'Verschwenden Sie keine Zeit und Geld mehr – Sie haben alle gültigen Informationen an '
                        'einem Ort!'
                        '</div>', unsafe_allow_html=True)


chapter_spacer()
if st.session_state.current_lang == "English":
    start_survey = st.button("Find Court")
else:
    start_survey = st.button("Gericht Finden")
if start_survey:
    switch_page("question_crime")