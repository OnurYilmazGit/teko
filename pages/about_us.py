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
# Current path
current_path = str(Path(__file__).parents[1])

# Define about us information
people_info = {
    "Person 1": {
        "image_path": f"{current_path}/assets/house.jpg",
        "description": "Description for Person 1."
    },
    "Person 2": {
        "image_path": f"{current_path}/assets/house.jpg",
        "description": "Description for Person 2."
    },
    "Person 3": {
        "image_path": f"{current_path}/assets/house.jpg",
        "description": "Description for Person 3."
    },
    "Person 4": {
        "image_path": f"{current_path}/assets/house.jpg",
        "description": "Description for Person 4."
    },
}

# Title
st.title("About Us")

# Loop over people
for person, info in people_info.items():
    # Create two columns
    col1, col2 = st.columns(2)

    # First column: image
    with col1:
        image = Image.open(info["image_path"])
        st.image(image, width=int(image.size[0]*0.125))

    # Second column: info
    with col2:
        st.header(person)
        st.write(info["description"])


# Create Navbar
show_navbar()
