 # Importing required packages
import streamlit as st
import user_persona
import company_info
import openai_model
import data

# To use this app, you need an .env file with the OPENAI API
# and you need to fill in the ID in the assistant.py file

PAGES = {
    "Wer bist du?": user_persona,
    "Wer bin ich?": company_info,
    "Deine Daten": data,
    "Chatbot": openai_model,
}

st.sidebar.title('Menü')
selection = st.sidebar.radio("Gehe zu", list(PAGES.keys()))

page = PAGES[selection]
page.app()