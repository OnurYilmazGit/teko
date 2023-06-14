import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from streamlit_folium import st_folium
import folium
from pages.custom_components import get_local_pages, show_navbar, chapter_spacer, components_spacer
from streamlit_extras.card import card



# Set config
st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[1])
wreath_black_image = Image.open(current_path + "/assets/wreath_black.png")
wreath_blue_image = Image.open(current_path + "/assets/wreath_blue.png")
current_step = 6
st.session_state.current_page = "Find Court"
st.session_state.current_index = 3

# initialize session state attributes
for attr in ['crime', 'subject', 'amount', 'appeal', 'city']:
    if attr not in st.session_state:
        st.session_state[attr] = ''

show_navbar()


with st.sidebar:
    question_steps = {"question_crime": "Crime", "question_subject": "Subject", "question_amount": "Amount",
                      "question_appeal": "Appeal", "question_city": "City"}
    i = 1
    for key, value in question_steps.items():

        if i < current_step:
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

        i += 1


chapter_spacer()
st.subheader("The responsible court is: Amtsgericht München")
st.progress(1.0 / (len(question_steps.keys()) + 1) * current_step)
st.markdown('<div style="text-align: justify;">'
            'Your responsible court is the Amtsgericht München. Since the subject of your dispute is private rent, the '
            'Amtsgericht is in charge of negotiating your case independently from the monetary amount of dispute. '
            'The responsible Amtsgericht at the provided postal code is the Amtsgericht München.'
            '</div>', unsafe_allow_html=True)

chapter_spacer()
info_col, map_col = st.columns(2)
with info_col:
    st.subheader("Amtsgericht München")
    st.markdown('<div style="text-align: justify;">'
                'Pacellistraße 5, 80315 München'
                '</div>', unsafe_allow_html=True)
    components_spacer()
    st.warning("You don't need an lawyer at this court!")
with map_col:
    folium_map = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(folium_map)
    st_data = st_folium(folium_map, width=500, height=300)

components_spacer()
st.subheader("Your answers")
components_spacer()
col1, col2= st.columns(2)
with col1:
    card(title="Tenancy Law", text="Topic", image="https://images.unsplash.com/photo-1598228723793-52759bba239c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80")
with col2:
    card(title="Private Rent", text="Subject", image="https://images.unsplash.com/photo-1582063289852-62e3ba2747f8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80")
col1, col2= st.columns(2)
with col1:
    card(title="Eviction Action", text="Case", image="https://images.unsplash.com/photo-1524633712235-22da046738b4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=764&q=80")
with col2:
    card(title="1.200 Euros", text="Monetary Amount", image="https://images.unsplash.com/photo-1593672715438-d88a70629abe?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80")
col1, col2= st.columns(2)
with col1:
    card(title="No", text="Appeal", image="https://images.unsplash.com/photo-1593115057322-e94b77572f20?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1471&q=80")
with col2:
    card(title="81735", text="Postal Code", image="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1544&q=80")

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
        switch_page("home")
with col2:
    img = Image.open(f"{current_path}/assets/document.jpg")
    st.image(img)