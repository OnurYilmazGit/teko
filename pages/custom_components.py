import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras import card
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from streamlit_option_menu import option_menu


def show_navbar():

    lang_bar_style = {
        "container": {"background-color": "white"},
        "nav-link-selected": {"background-color": "silver"}
    }

    col1, col2, col3, col4 = st.columns([0.10, 0.05, 0.55, 0.3])
    with col1:
        st.header("TEKO")
    with col2:
        st.header("|")
    with col3:
        st.header("Unlocking Justice. Made Easy.")
    with col4:
        st.text("")
        lang_bar = option_menu(None, ["English", "Deutsch"], icons=['translate', 'translate'], menu_icon="cast",
                               default_index=st.session_state.lang_index, orientation="horizontal", styles=lang_bar_style)

    navbar_style = {
        "nav-link-selected": {"background-color": "black"}
    }
    if st.session_state.current_lang == "English":
        navbar = option_menu(None, ["Home", "About Us", "FAQ", "Find Court"],
                         icons=['house', 'people', "question-circle", "book"], menu_icon="cast", default_index=st.session_state.current_index,
                         orientation="horizontal", styles=navbar_style)
    else:
        navbar = option_menu(None, ["Startseite", "Über Uns", "FAQ", "Gericht Finden"],
                         icons=['house', 'people', "question-circle", "book"], menu_icon="cast",
                         default_index=st.session_state.current_index,
                         orientation="horizontal", styles=navbar_style)

    if lang_bar != st.session_state.current_lang:
        if lang_bar == "English":
            st.session_state.current_lang = "English"
            st.session_state.lang_index = 0
            if st.session_state.current_page == "Startseite":
                navbar = "Home"
            elif st.session_state.current_page == "Über Uns":
                navbar = "About Us"
            elif st.session_state.current_page == "FAQ":
                navbar = "FAQ_de"
            elif st.session_state.current_page == "Gericht Finden":
                navbar = "Find Court"
            else:
                print("Error")
        if lang_bar == "Deutsch":
            st.session_state.current_lang = "Deutsch"
            st.session_state.lang_index = 1
            if st.session_state.current_page == "Home":
                navbar = "Startseite"
            elif st.session_state.current_page == "About Us":
                navbar = "Über Uns"
            elif st.session_state.current_page == "FAQ":
                navbar = "FAQ2"
            elif st.session_state.current_page == "Find Court":
                navbar = "Gericht Finden"
            else:
                print("Error")

    if navbar != st.session_state.current_page:
        if navbar in ["Home", "Startseite"]:
            switch_page("home")
        if navbar in ["About Us", "Über Uns"]:
            switch_page("about_us")
        if navbar in ["FAQ", "FAQ2"]:
            switch_page("faq")
        if navbar in ["Find Court", "Gericht Finden"]:
            switch_page("question_crime")


def get_question_dicts():
    if st.session_state.current_lang == "English":
        question_steps = {"question_crime": "Crime", "question_subject": "Subject", "question_case": "Case",
                          "question_appeal": "Appeal", "question_amount": "Amount", "question_city": "City"}
        document_steps = {"question_court": "Court", "question_plaintiff": "Plaintiff", "question_defendant": "Defendant",
                          "question_target": "Target", "question_amount2": "Amount Check", "question_explanation": "Explanation",
                          "question_evidence": "Evidence", "question_ending": "Ending"}
    else:
        question_steps = {"question_crime": "Rechtsgebiet", "question_subject": "Thema", "question_case": "Fall",
                          "question_appeal": "Beschwerde", "question_amount": "Betrag", "question_city": "Ort"}
        document_steps = {"question_court": "Gericht", "question_plaintiff": "Ankläger",
                          "question_defendant": "Angeklagter",
                          "question_target": "Ziel", "question_amount2": "Betrag Prüfen",
                          "question_explanation": "Begründung",
                          "question_evidence": "Beweise", "question_ending": "Abschluss"}
    return question_steps, document_steps


def show_sidebar():
    current_path = str(Path(__file__).parents[1])
    wreath_black_image = Image.open(current_path + "/assets/wreath_black.png")
    wreath_blue_image = Image.open(current_path + "/assets/wreath_blue.png")
    question_steps, document_steps = get_question_dicts()

    if st.session_state.current_lang =="English":
        expander_string1 = "Find the correct court"
        expander_string2 = "Create your lawsuit document"
    else:
        expander_string1 = "Gericht finden"
        expander_string2 = "Klageschrift erstellen"

    with st.sidebar:

        with st.expander(expander_string1):

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

        with st.expander(expander_string2):

            for key, value in document_steps.items():

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


def get_local_pages():
    pages = ["home", "question_crime", "question_subject", "question_amount", "question_appeal", "question_city",
            "survey_results", "question_court", "question_plaintiff", "question_defendant", "question_target", "question_amount2"
             "question_evidence", "question_ending", "custom_components", "about_us", "faq", "question_case", "question_amount2",
             "question_explanation", "question_evidence"]
    return pages


def components_spacer():
    st.text("")
    st.text("")


def chapter_spacer():
    st.text("")
    st.text("")
    st.text("")
    st.text("")