 # Importing required packages
import streamlit as st
import user_persona
import company_info
import openai_model
import data

# To use this app, you need an .env file with the OPENAI API
# and you need to fill in the ID in the assistant.py file

PAGES = {
    "Persona": user_persona,
    "Channel": company_info,
    "Deine Daten": data,
    "Chatbot": openai_model,
}
# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.sidebar.title('Menü')
selection = st.sidebar.radio("Gehe zu", list(PAGES.keys()))

page = PAGES[selection]
page.app()