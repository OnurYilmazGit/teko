import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
import re
from pathlib import Path
from pages.custom_components import *


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 6
st.session_state.current_page = "Find Court"
st.session_state.current_index = 3


# initialize session state attributes
question_steps, document_steps = get_question_dicts()
for attr in list(question_steps.keys()) + list(document_steps.keys()):
    if attr not in st.session_state.keys():
        st.session_state[attr] = None


show_navbar()
show_sidebar()

address = st.session_state.question_plaintiff
amount = str(st.session_state.question_amount2)

# Split the string into lines
lines = address.split('\n')

# Get the street and city
street = lines[1].strip()
street = street.replace(',', '')
zipcode_city = lines[2].strip()

# Create new string in the desired format
new_address = f"{street} in {zipcode_city}"



chapter_spacer()
st.subheader(f"Please select relevant evidence or provide your own")
st.progress((1.0 / 7) * current_step)

translation_dict = {"Rental deposit: rental contract": "Kaution: Mietvertrag",
                    "Rental deposit: transfer receipt": "Kaution: Überweisungsbeleg",
                    "Rental deposit: letter of termination": "Kaution: Kündigungsschreiben",
                    "Incidental rental costs: letter": "Betriebskosten: Schreiben"
                    }

evidence_dict = {"Rental deposit: rental contract": "Der Kläger begehrt Rückzahlung einer Mietkaution nach beendetem Mietvertrag. Mit Mietvertrag vom dd.mm.yyyy mietete der Kläger vom Beklagten die Mietwohnung in der "
                 + new_address + " (im Folgenden 'Wohnung').\n\n",
                 "Rental deposit: transfer receipt": "Am dd.mm.yyyy zahlte der Kläger an den Beklagten vertragsgemäß die Kaution in Höhe von " + amount + " Euro.\n\n",
                 "Rental deposit: letter of termination": "Das Mietverhältnis endete durch Kündigung des Klägers mit Ablauf des dd.mm.yyyy. Nachdem der Kläger den Beklagten mit Schreiben vom dd.mm.yyyy zur Rückzahlung der Mietkaution aufforderte, erhielt er keine Antwort.\n\n",
                 "Incidental rental costs: letter": "In dem Schreiben vom dd.mm.yyy bestimmte der Kläger eine vorprozessuale Frist zur Vermeidung der vorliegenden Klage zum dd.mm.yyyy. Trotzdem rechnete der Beklagte bislang jedoch nicht über die Betriebskosten ab.\n\n"}

selected_evidence = st.multiselect(label="", options=evidence_dict.keys())
st.markdown('<div style="text-align: justify;">'
            'Please refine the evidence provided to fit your case. Please fill in the relevant dates.'
            '</div>', unsafe_allow_html=True)



cnt = 1
desc_string = ""
for selection in selected_evidence:
    selection_ger = translation_dict[selection]
    desc_string += evidence_dict[selection] 
    desc_string += "Beweis: Anlage K " + str(cnt) + " - " + selection_ger + " vom dd.mm.yyyy (Kopie)\n\n"
    cnt += 1

question_evidence = st.text_area(label="label", value=desc_string, height=400, label_visibility="hidden").strip()

next_question = st.button("Create draft")
if next_question:
    st.session_state.question_evidence = question_evidence
    switch_page("question_ending")
