import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from streamlit_folium import st_folium
import folium
from pages.custom_components import *
from streamlit_extras.card import card
from src.decision_tree import *
from src.google_maps import *
from src.web_scraper import *


# Set config
st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[1])
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
court_type, explanation = find_court_type(subject=st.session_state.question_subject,
                                          appeal=st.session_state.question_appeal,
                                          amount=st.session_state.question_amount,
                                          lang=st.session_state.current_lang)

court_decision = receive_court(plz=st.session_state.question_city, court_type=court_type)
court_location = get_address(court_decision)
court_location = court_location.replace(', ', ',<br>')
court_coordinates = get_coordinates(court_decision)

if st.session_state.current_lang == "English":
    st.subheader(f"The responsible court is: {court_decision}")
    st.progress(1.0 / (len(question_steps.keys()) + 1) * current_step)
    st.markdown(f'<div style="text-align: justify;"> {explanation} </div>', unsafe_allow_html=True)
else:
    st.subheader(f"Das zuständige Gericht ist: {court_decision}")
    st.progress(1.0 / (len(question_steps.keys()) + 1) * current_step)
    st.markdown(f'<div style="text-align: justify;"> {explanation} </div>', unsafe_allow_html=True)

chapter_spacer()
info_col, map_col = st.columns(2)
with info_col:
    st.subheader(court_decision)
    st.markdown(f'<div style="text-align: justify;">{court_location}</div>', unsafe_allow_html=True)

    components_spacer()
    if st.session_state.current_lang == "English":
        if court_type == "Amtsgericht":
            st.warning("You don't need a lawyer because your responsible court is an Amtsgericht!")
        else:
            st.warning("You need a lawyer because your responsible court is a Landgericht!")
    else:
        if court_type == "Amtsgericht":
            st.warning("Sie benötigen keinen Anwalt weil das zuständige Gericht ein Amtsgericht ist!")
        else:
            st.warning("Sie benötigen einen Anwalt weil das zuständige Gericht ein Landgericht ist!")
with map_col:
    folium_map = folium.Map(location=court_coordinates, zoom_start=16)
    folium.Marker(court_coordinates, popup="Liberty Bell", tooltip="Liberty Bell").add_to(folium_map)
    st_data = st_folium(folium_map, width=500, height=300)

if st.session_state.current_lang == "English":
    components_spacer()
    st.subheader("Your answers")
    components_spacer()
    col1, col2 = st.columns(2)
    with col1:
        card(title=st.session_state.question_crime, text="Topic", image="https://images.unsplash.com/photo-1598228723793-52759bba239c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80")
    with col2:
        card(title=st.session_state.question_subject, text="Subject", image="https://images.unsplash.com/photo-1582063289852-62e3ba2747f8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80")
    col1, col2 = st.columns(2)
    with col1:
        card(title=st.session_state.question_case, text="Case", image="https://images.unsplash.com/photo-1524633712235-22da046738b4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=764&q=80")
    with col2:
        card(title=st.session_state.question_appeal, text="Appeal", image="https://images.unsplash.com/photo-1593115057322-e94b77572f20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1471&q=80")
    col1, col2 = st.columns(2)
    with col1:
        card(title=str(st.session_state.question_amount)+" Euro", text="Monetary Amount", image="https://images.unsplash.com/photo-1593672715438-d88a70629abe?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80")
    with col2:
        card(title=st.session_state.question_city, text="Postal Code", image="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1544&q=80")
else:
    components_spacer()
    st.subheader("Ihre Antworten")
    components_spacer()
    col1, col2 = st.columns(2)
    with col1:
        card(title=st.session_state.question_crime, text="Rechtsgebiet", image="https://images.unsplash.com/photo-1598228723793-52759bba239c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80")
    with col2:
        card(title=st.session_state.question_subject, text="Bereich", image="https://images.unsplash.com/photo-1582063289852-62e3ba2747f8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80")
    col1, col2 = st.columns(2)
    with col1:
        card(title=st.session_state.question_case, text="Fall", image="https://images.unsplash.com/photo-1524633712235-22da046738b4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=764&q=80")
    with col2:
        card(title=st.session_state.question_appeal, text="Berufung", image="https://images.unsplash.com/photo-1593115057322-e94b77572f20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1471&q=80")
    col1, col2 = st.columns(2)
    with col1:
        card(title=str(st.session_state.question_amount)+" Euro", text="Streitwert", image="https://images.unsplash.com/photo-1593672715438-d88a70629abe?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80")
    with col2:
        card(title=st.session_state.question_city, text="PLZ", image="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1544&q=80")

if st.session_state.current_lang == "English":
    components_spacer()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Do you need help with filing the necessary documents?")
        st.text("")
        st.markdown('<div style="text-align: justify;">'
                    'With TEKO you can file cases without stress and effort. Our digital solution guides you though the '
                    'process and asks you the necessary questions. At the end, we will provide you with your individual '
                    'document to file your case.'
                    '</div>', unsafe_allow_html=True)
        st.text("")
        next_question = st.button("Create Documents")
        if next_question:
            st.session_state.question_court = court_decision
            switch_page("question_court")
    with col2:
        img = Image.open(f"{current_path}/assets/document.jpg")
        st.image(img)
else:
    components_spacer()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Benötigen Sie Hilfe bei der Erstellung der notwendigen Dokumente?")
        st.text("")
        st.markdown('<div style="text-align: justify;">'
                    'Mit TEKO können Sie Klagen ohne Stress einreichen. Unsere digitale Lösung führt Sie durch den ' 
                    'Prozess und stellt Ihnen die notwendigen Fragen. Am Ende stellen wir Ihnen Ihr individuelles Dokument ' 
                    'zur Verfügung, um Ihren Fall einzureichen.'
                    '</div>', unsafe_allow_html=True)
        st.text("")
        next_question = st.button("Dokumente erstellen")
        if next_question:
            st.session_state.question_court = court_decision
            switch_page("question_court")
    with col2:
        img = Image.open(f"{current_path}/assets/document.jpg")
        st.image(img)
