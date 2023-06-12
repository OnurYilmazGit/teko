import streamlit as st
from PIL import Image
from pathlib import Path
from pages.custom_components import get_local_pages, show_navbar, chapter_spacer, components_spacer
from st_pages import hide_pages, Page, show_pages


# Set config
st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
hide_pages(get_local_pages())
current_path = str(Path(__file__).parents[1])
st.session_state.current_page = "About Us"
st.session_state.current_index = 1

# Create Navbar
show_navbar()

# List of profiles
profiles = [
    {
        "name": "Thomas",
        "image": f"{current_path}/assets/Thomas.jpeg",
        "description": "Thomas is a software engineer with a passion for AI."
    },
    {
        "name": "Onur",
        "image": f"{current_path}/assets/Onur.jpg",
        "description": "Onur is a data scientist who loves uncovering insights from data."
    },
    {
        "name": "Eric",
        "image": f"{current_path}/assets/Eric.png",
        "description": "Eric is a software engineer with a passion for AI."
    },
    {
        "name": "Klare",
        "image": f"{current_path}/assets/Klare.png",
        "description": "Klare is a data scientist who loves uncovering insights from data."
    },  
    
]

# Display title
st.title('Who We Are')

# Preprocess images to make them the same size
image_size = (300, 300)  # Set the size you want

# Display each profile in a grid
cols = st.columns(2)  # Adjust the number based on how many columns you want
for i, profile in enumerate(profiles):
    with cols[i % 2]:  # Adjust the modulus based on how many columns you have
        img = Image.open(profile['image'])
        img = img.resize(image_size)
        st.image(img)
        st.markdown(f"**{profile['name']}**")
        st.markdown(profile['description'])
    if i % 2 == 1:
        cols = st.columns(2)  # Adjust the number based on how many columns you want
