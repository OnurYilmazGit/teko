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
st.session_state.current_page = "FAQ"
st.session_state.current_index = 2

# Create Navbar
show_navbar()

# Define FAQ information
faq_info = {
    "Question 1": "Answer 1.",
    "Question 2": "Answer 2.",
    "Question 3": "Answer 3.",
    "Question 4": "Answer 4.",
}

# Title
st.title("Frequently Asked Questions")

# Loop over questions
for question, answer in faq_info.items():
    # Check if question is not empty
    if question.strip() != "":
        # Create expander for each question
        expander = st.expander(label=question) 
        expander.write(answer)



