import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages, Page, show_pages
from PIL import Image
from pathlib import Path
from pages.custom_components import *
from fpdf import FPDF


st.set_page_config(initial_sidebar_state="expanded", layout="wide")
hide_pages(get_local_pages())
current_step = 8
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
if st.session_state.current_lang == "English":
    st.subheader(f"Please make sure that the created document is correct.")
    st.progress((1.0 / 8) * current_step)
else:
    st.subheader(f"Bitte stellen Sie sicher, dass das generierte Dokument korrekt ist.")
    st.progress((1.0 / 8) * current_step)

court = st.session_state.question_court.replace(', ', ',\n')
plaintiff = st.session_state.question_plaintiff.replace(', ', ',\n')
defendant = st.session_state.question_defendant.replace(', ', ',\n')
target = st.session_state.question_target.replace(', ', ',\n')
amount = str(st.session_state.question_amount2)
explanation = st.session_state.question_explanation
evidence = st.session_state.question_evidence

if st.session_state.current_lang == "English":
    ending_dict = {
        "Repayment of the rental deposit": "Dem Kläger steht gegen den Beklagten ein Anspruch auf Rückzahlung der Kaution gemäß § 566a Satz 2 BGB zu. Nach § 566 Satz 1 BGB tritt der Erwerber der Mietsache in die Verpflichtung zur Rückzahlung der Kaution ein.\n\n" +
                                   "Weiterer Sach- und Rechtsvortrag einschließlich entsprechender Beweisangebote bleiben ausdrücklich vorbehalten. Sollte das Gericht den bisherigen Sachvortrag oder die bisherigen Beweisangebote des Klägers nicht für ausreichend erachten, oder die hier vertretene Rechtsauffassung nicht teilen, so wird ausdrücklich um einen entsprechenden - ggf. telefonischen - Hinweis gebeten.",
        "Settlement of the incidental rental costs": "Der Kläger hat ein Interesse an der Abrechnung, weil er die Kostenentwicklung während seiner Mietzeit nachvollziehen muss. Die Verpflichtung des Beklagten zur Abrechnung der Betriebskosten ergibt sich zudem aus §§ 556 Abs. 3, 259 BGB.\n\n" +
                                      "Weiterer Sach- und Rechtsvortrag einschließlich entsprechender Beweisangebote bleiben ausdrücklich vorbehalten. Sollte das Gericht den bisherigen Sachvortrag oder die bisherigen Beweisangebote des Klägers nicht für ausreichend erachten, oder die hier vertretene Rechtsauffassung nicht teilen, so wird ausdrücklich um einen entsprechenden - ggf. telefonischen - Hinweis gebeten."}
else:
    ending_dict = {"Rückzahlung Mietkaution": "Dem Kläger steht gegen den Beklagten ein Anspruch auf Rückzahlung der Kaution gemäß § 566a Satz 2 BGB zu. Nach § 566 Satz 1 BGB tritt der Erwerber der Mietsache in die Verpflichtung zur Rückzahlung der Kaution ein.\n\n"+
                    "Weiterer Sach- und Rechtsvortrag einschließlich entsprechender Beweisangebote bleiben ausdrücklich vorbehalten. Sollte das Gericht den bisherigen Sachvortrag oder die bisherigen Beweisangebote des Klägers nicht für ausreichend erachten, oder die hier vertretene Rechtsauffassung nicht teilen, so wird ausdrücklich um einen entsprechenden - ggf. telefonischen - Hinweis gebeten.",
                   "Abrechnung der Nebenkosten": "Der Kläger hat ein Interesse an der Abrechnung, weil er die Kostenentwicklung während seiner Mietzeit nachvollziehen muss. Die Verpflichtung des Beklagten zur Abrechnung der Betriebskosten ergibt sich zudem aus §§ 556 Abs. 3, 259 BGB.\n\n" +
                    "Weiterer Sach- und Rechtsvortrag einschließlich entsprechender Beweisangebote bleiben ausdrücklich vorbehalten. Sollte das Gericht den bisherigen Sachvortrag oder die bisherigen Beweisangebote des Klägers nicht für ausreichend erachten, oder die hier vertretene Rechtsauffassung nicht teilen, so wird ausdrücklich um einen entsprechenden - ggf. telefonischen - Hinweis gebeten."}

lines = plaintiff.split('\n')
name = lines[0].strip().replace(',', '')
name = name.replace('(Vermieter)', '')
name = name.replace('(Mieter)', '')

ending = ending_dict[target] + "\n\n" + "Mit freundlichen Grüßen\n" + name 

question_ending = st.text_area(label="Your information", value="An das \n\n" + court + "\n\n"
                                                                + "Klage" + "\n\n" + plaintiff + "\n\n"
                                                                + "-- Kläger --" + "\n\n" + "gegen" + "\n\n"
                                                                + defendant + "\n\n" + "-- Beklagter --" + "\n\n" 
                                                                + "wegen: " + target + "\n\n"
                                                                + "Streitwert: " + amount + " Euro\n\n"
                                                                + "Erhebe ich Klage und beantrage zu erkennen:" + "\n\n" 
                                                                + explanation + "\n\nBegründung\n\n"
                                                                + evidence + "\n\n"
                                                                + ending
                                                                , height=1500, max_chars=10000, label_visibility="hidden").strip()

if st.session_state.current_lang == "English":
    create_pdf = st.button("Create PDF")
else: 
    create_pdf = st.button("PDF erstellen")

if create_pdf:
    st.session_state.question_ending = question_ending

    question_ending = question_ending.encode('latin-1', 'replace').decode('latin-1')


    blocks = question_ending.split('\n\n')

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for block in blocks:
        lines = block.split('\n')
        for line in lines:
            #pdf.cell(w=0, h=5, txt=line, border=1, ln=1, align = 'L') 
            pdf.multi_cell(0, 5, line, align='L')
        pdf.cell(w=0, h=5, txt="", ln=1, align = 'L')
    pdf.output("Klage " + target + ".pdf")
    st.success('pdf successfully created!', icon="✅")
