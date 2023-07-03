import streamlit as st
from PIL import Image
from pathlib import Path
from pages.custom_components import get_local_pages, show_navbar, chapter_spacer, components_spacer
from st_pages import hide_pages, Page, show_pages
from streamlit_extras.card import card


# Set config
st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[1])
st.session_state.current_page = "About Us"
st.session_state.current_index = 1


# Create Navbar
show_navbar()


# about the firm
chapter_spacer()
st.header("About the Firm")
components_spacer()
col1, col2 = st.columns(2)
with col1:
    st.subheader("TEKO is a novel player in legal tech who leverages technological advances for supporting people in getting justice.")
with col2:
    st.markdown('<div style="text-align: justify;">'
                'At TEKO, we remain true to our mission of democratizing the legal sector. '
                'We work hard to shape an industry to avoid  monopolies and choking points. '
                'Our team sees innovation, transparency, democratization, and self-custody '
                'as core values that need to be preserved and re-emphasized.'
                '</div>', unsafe_allow_html = True)
components_spacer()

card1, card2, card3 = st.columns(3)
with card1:
    card(title="2023", text="Founding Year", image="https://images.unsplash.com/photo-1561473905-67b476b45ed2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1359&q=80")
with card2:
    card(title="1.4M", text="Series A Funding", image="https://images.unsplash.com/photo-1527788263495-3518a5c1c42d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1508&q=80")
with card3:
    card(title="178", text="Cups of Coffee", image="https://images.unsplash.com/photo-1512568400610-62da28bc8a13?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80")


# List of profiles
profiles = [
    {
        "name": "Thomas Wagner",
        "image": f"{current_path}/assets/thomas-circle.jpeg",
        "description": "Thomas is currently pursuing his studies in Informatics at the Technical University of Munich. "
                       "His knowledge in state-of-the-art technologies provide valuable approaches for the legal "
                       "sector. "
                       "With his experience at Scalable Capital and interest in entrepreneurship he also contributes "
                       "towards product management and customer relations."
    },
    {
        "name": "Onur Yilmaz",
        "image": f"{current_path}/assets/onur-circle.jpg",
        "description": "Onur is studying Informatics at the Technical University of Munich. "
                       "In his role as a working student at Intel, he developed distributed systems for data "
                       "management. "
                       "His hands-on developing skills make him the swiss knife of coding and our unbeatable "
                       "contributor for all aspects of technology."
    },
    {
        "name": "Eric Näser",
        "image": f"{current_path}/assets/eric-circle.jpeg",
        "description": "Eric is currently pursuing his studies in Information Systems at the Technical University of "
                       "Munich. "
                       "His work experience in Artificial Intelligence at international groups like Siemens and "
                       "Infineon bought him hands-on skills for bringing technological advances to the legal sector. "
                       "An interest and knowledge in entrepreneurship enable him to create an impact to all aspects of "
                       "our company."
    },
    {
        "name": "Klare Nurdun",
        "image": f"{current_path}/assets/klare-circle.jpeg",
        "description": "Klare is presently engaged in her Management and Technology studies at the Technical University "
                       "of Munich. "
                       " Through her professional background at a TUM research insititute she gained practical "
                       "experience in conducting  industrial projects. Furthermore, she has developed marketing skills "
                       "in her work at Rohde & Schwarz."
                       "Her contribution brings the cherry on top of our user-friendly solution."
    },  
    
]

# Display title
chapter_spacer()
st.header('Who We Are')

# Preprocess images to make them the same size
image_size = (300, 300)  # Set the size you want

# Display each profile in a grid
components_spacer()
cols = st.columns(2)  # Adjust the number based on how many columns you want
for i, profile in enumerate(profiles):
    with cols[i % 2]:  # Adjust the modulus based on how many columns you have
        _, image_col, desc_col, _ = st.columns([0.05, 0.35, 0.55, 0.05])
        with image_col:
            img = Image.open(profile['image'])
            img = img.resize(image_size)
            st.image(img)
        with desc_col:
            st.subheader(f"{profile['name']}")
            st.markdown(f'<div style="text-align: justify;"> {profile["description"]} </div>', unsafe_allow_html = True)
    if i % 2 == 1:
        components_spacer()
        cols = st.columns(2)  # Adjust the number based on how many columns you want
