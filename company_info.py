# company_info.py
import streamlit as st

def app():
    st.title('Tik Tok Channel')

    # Eingabefelder für Unternehmensdaten
    with st.form(key='company_info_form'):
        unternehmensname = st.text_input("Channel Name")
        branche = st.text_input("Art des Channels", placeholder="z.B. Mode, Beauty, Technik")
        groesse = st.selectbox("Followeranzahl", ["0-1000 Follower", "1000-5000 Follower", "5000-10000 Follower", "Mehr als 10000 Follower"])

        # Informationen zu USPs und Zielen
        usps = st.text_area("USPs (Unique Selling Points)")
        ziele = st.text_area("Zielsetzung der Texte", placeholder="z.B. Unterhaltung, Information, Inspiration")

        # Informationen zur Markenpersönlichkeit
        markenpersoenlichkeit = st.text_area("Creatorpersönlichkeit und -werte", placeholder="z.B. humorvoll, authentisch, kreativ")

        # Informationen zu Hauptzielgruppen
        hauptzielgruppen = st.text_area("Hauptzielgruppen des Channels", placeholder="z.B. Gen Alpha, Gen Z, Millennials")

        # Knopf zum Absenden des Formulars
        submit_button = st.form_submit_button("Channeldaten speichern")

        if submit_button:
            # Speichern der Unternehmensdaten im session_state
            st.session_state['company_data'] = {
                "Channel Name": unternehmensname,
                "Art des Channels": branche,
                "groesse": groesse,
                "usps": usps,
                "ziele": ziele,
                "markenpersoenlichkeit": markenpersoenlichkeit,
                "hauptzielgruppen": hauptzielgruppen
            }

            st.success("Channeldaten erfolgreich gespeichert!")

# Dieser Teil ist für Testzwecke, wenn Sie dieses Skript einzeln laufen lassen.
if __name__ == "__main__":
    app()
