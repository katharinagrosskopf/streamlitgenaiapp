# user_persona.py
import streamlit as st

def app():
    st.title('Zielgruppenpersona')

    # Eingabefelder für grundlegende Informationen der User Persona
    with st.form(key='user_persona_form'):
        name = st.text_input("Name und Vorname")
        alter = st.slider("Alter", 16, 100, 30)  # Min, Max, Default
        geschlecht = st.selectbox("Geschlecht", ["Männlich", "Weiblich", "Andere"])

        # Psychografische Daten
        interessen = st.text_area("Interessen und Hobbys", placeholder= "z.B. Sport, Reisen, Kochen")
        werte = st.text_area("Vorlieben und Abneigungen", placeholder="z.B. Humor, prägnante Inhalte, keine langen Erklärvideos")

        # Verhaltensdaten
        einkaufsgewohnheiten = st.text_area("Bevorzugte Tik Tok Inhalte", placeholder="z.B. Fashion, Beauty, Comedy, DIY")
        nutzung_sozialer_medien = st.selectbox("Nutzung Sozialer Medien",["Nie","0h-2h Täglich","2h-4h Täglich","Öfter"])
        markenpraferenzen = st.text_area("Lieblingschannels und Influencer")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Persona speichern")

        if submit_button:
            # Speichern der Persona-Daten im session_state
            st.session_state['persona_data'] = {
                "name": name,
                "alter": alter,
                "geschlecht": geschlecht,
                "interessen": interessen,
                "werte": werte,
                "einkaufsgewohnheiten": einkaufsgewohnheiten,
                "nutzung_sozialer_medien": nutzung_sozialer_medien,
                "markenpraferenzen": markenpraferenzen
            }

            st.success("User Persona erfolgreich erstellt!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
