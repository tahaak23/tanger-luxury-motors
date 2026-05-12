import streamlit as st
from anthropic import Anthropic
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

client = Anthropic()

# Google Sheets connection
def connect_google_sheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scope
    )
    client_gs = gspread.authorize(creds)
    sheet = client_gs.open("Edition Auto — Leads").sheet1
    return sheet

def save_lead(nom, telephone, vehicule, message, langue):
    try:
        sheet = connect_google_sheets()
        date = datetime.now().strftime("%d/%m/%Y %H:%M")
        sheet.append_row([date, nom, telephone, vehicule, message, langue, "Nouveau"])
    except Exception as e:
        print(f"Erreur Google Sheets: {e}")

st.set_page_config(
    page_title="Edition Auto Luxury Cars",
    page_icon="🏎️",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Raleway:wght@300;400&display=swap');

    .stApp {
        background: linear-gradient(135deg, #2C2C2C 0%, #1a1a1a 50%, #2C2C2C 100%);
    }
    .main > div {
        position: relative;
        z-index: 1;
    }
    .header-container {
        background: linear-gradient(180deg, #3a3530 0%, #2a2520 100%);
        border-bottom: 3px solid #C9A84C;
        padding: 30px 20px;
        text-align: center;
        margin-bottom: 20px;
        border-radius: 0 0 15px 15px;
        box-shadow: 0 4px 20px rgba(201, 168, 76, 0.3);
    }
    .logo-text {
        font-family: 'Playfair Display', serif;
        font-size: 3em;
        font-weight: 700;
        letter-spacing: 8px;
        background: linear-gradient(180deg, #FFD700 0%, #C9A84C 40%, #FFD700 60%, #C9A84C 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: block;
        margin-bottom: 5px;
    }
    .luxury-text {
        font-family: 'Raleway', sans-serif;
        font-size: 1em;
        letter-spacing: 6px;
        color: #C9A84C;
        font-weight: 300;
    }
    .gold-line {
        width: 100px;
        height: 2px;
        background: linear-gradient(90deg, transparent, #C9A84C, transparent);
        margin: 10px auto;
    }
    .welcome-box {
        background: linear-gradient(135deg, rgba(201, 168, 76, 0.1), rgba(201, 168, 76, 0.05));
        border: 1px solid rgba(201, 168, 76, 0.4);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        color: #C9A84C;
        margin: 10px 0 20px 0;
        font-family: 'Raleway', sans-serif;
        font-size: 0.95em;
        letter-spacing: 1px;
    }
    .info-box {
        color: #C9A84C;
        text-align: center;
        font-size: 0.85em;
        opacity: 0.8;
        font-family: 'Raleway', sans-serif;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-container">
    <span class="logo-text">EDITION AUTO</span>
    <div class="gold-line"></div>
    <span class="luxury-text">LUXURY CARS</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="welcome-box">
    ✦ Bienvenue chez Edition Auto Tanger ✦<br><br>
    Votre conseiller virtuel exclusif est à votre service.<br>
    Posez vos questions en français, darija, English ou Español.
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="info-box">🕐 Tous les jours : 10h00 — 20h00 &nbsp;✦&nbsp; 📍 Rue Fes N°140, Tanger &nbsp;✦&nbsp; 📞 0661481800</p>', unsafe_allow_html=True)

st.divider()

system_prompt = """Tu es le conseiller virtuel exclusif d'Edition Auto Luxury Cars Tanger.

SHOWROOM :
- Nom : Edition Auto Luxury Cars
- Adresse : Residence Office, Rue Fes N°140, Tanger, Maroc
- Horaires : Tous les jours 10h00 - 20h00
- Telephone : 0661481800

VEHICULES DISPONIBLES :

1. BMW X5 M50d Pack M Full Options Pack Carbone 2021
- Couleur : Noir
- Interieur : Cuir Rouge Pack M
- Kilometrage : 67 000 km
- Carburant : Diesel Quad-turbo
- Puissance : 400 ch
- Boite : Automatique Steptronic 8 rapports
- Transmission : xDrive intégrale
- Matriculation : Rabat
- Entretien : BMW SMEIA Tanger
- Options principales :
  * Direction arrière ultra rare
  * Suspension Adaptive M
  * Pack Carbone intégral intérieur
  * Volant M Sport chauffant
  * Jantes M 21 pouces
  * Sièges cuir rouge chauffants ventilés mémoire
  * Toit panoramique Sky Lounge LED
  * Head-Up Display
  * Caméra 360 + Park Assist
  * Apple CarPlay Android Auto
  * Système audio Harman Kardon premium

2. Yamaha FX SVHO Limited 2026 - Jet Ski
- Couleur : Noir Mat
- Etat : Neuf
- Moteur : 1.8L Supercharged
- Options : Écran digital, Audio Yamaha, Cruise Control,
  Modes Eco/Sport, Marche arrière électronique,
  Clé intelligente, Remorque incluse

3. Mercedes GLE Coupé 350DE 4MATIC AMG Line Plus 2026
- Couleur : Noir Obsidienne Métallisé
- Intérieur : Cuir Rouge Bordeaux
- Etat : Neuf 0 km Importée Allemagne
- Motorisation : Hybride Diesel Rechargeable 333 ch
- Boite : 9G-TRONIC automatique
- Options : Pack AMG Line Plus, Jantes AMG 22 pouces,
  Digital Light, Burmester 3D, Caméra 360,
  Hey Mercedes, Suspension AIRMATIC, DISTRONIC PLUS

4. Audi Q3 2026 S Line Diesel Full Options
- Couleur : Noir Métallisé
- Intérieur : Noir Alcantara
- Etat : Neuf Importée
- Options : Virtual Cockpit, MMI, Toit panoramique,
  LED Matrix, Climatisation multi-zones

5. Mercedes GLC 300DE 4MATIC Coupé AMG Line Plus 2026
- Couleur : Gris Nardo
- Intérieur : Rouge Sport
- Etat : Neuf Importée
- Options : Pack Carbone, MBUX, Sièges Sport AMG,
  Caméra 360, Burmester, Multibeam LED

SERVICES :
- Reprise vehicule : OUI
- Livraison domicile : OUI
- Essai routier : Non disponible
- Financement : Appeler le 0661481800

COMPORTEMENT :
- REGLE NUMERO 1 — PRIORITE ABSOLUE : Détecte la langue du PREMIER message du client. Si le client écrit en darija (mots comme salam, wash, bghit, 3andkom, chhal, kifach, nta, hna, daba, kayn, makaynch, mzyan, wakha, zwina, aji, bzzaf) REPONDS UNIQUEMENT ET TOUJOURS EN DARIJA pour toute la conversation. Ne passe JAMAIS au français si le client a commencé en darija. C'est une règle ABSOLUE et NON NEGOCIABLE.
- En darija utilise un langage élégant et professionnel
- Evite les mots trop familiers comme "tchkila", "zwina", "hhhh"
- Utilise plutôt : "collection", "véhicules", "modèles disponibles"
- Mélange le français et la darija de façon élégante
- Exemple correct : "3andna des modèles exceptionnels disponibles"
- Exemple incorrect : "3andna tchkila dial voitures"
- Si français réponds en français
- Si anglais réponds en anglais
- Si espagnol réponds en espagnol
- Tu es toujours élégant et ultra professionnel
- Tu appelles toujours le client Monsieur ou Madame
- Pour inviter le client au showroom dis toujours :
  "Le véhicule est disponible dans notre showroom au Rue Fes N°140, Tanger. Venez le découvrir en personne !"
- Ne jamais demander si le client est disponible
- C'est le client qui vient à toi — pas l'inverse
- Ton ton est assertif et confiant comme un showroom Ferrari
- Jamais de langage familier
- Maximum 1 emoji par réponse
- Ne mentionne jamais que tu es une IA
- Pour les prix appelle le 0661481800
- IMPORTANT : Après chaque conversation quand le client montre de l interet,
  demande son nom et telephone pour le rappeler
  - Si le client veut un rendez-vous demande :
  "Pour confirmer votre visite, puis-je avoir votre prénom et numéro de téléphone ?"
"""

if "messages" not in st.session_state:
    st.session_state.messages = []
if "lead_saved" not in st.session_state:
    st.session_state.lead_saved = False

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Écrivez votre message en français, darija, English ou Español..."):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        system=system_prompt,
        messages=st.session_state.messages
    )

    reply = response.content[0].text

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })
    with st.chat_message("assistant"):
        st.markdown(reply)

  # Sauvegarde automatique dans Google Sheets
import re

try:
   phone_pattern = r'(0[5-7][0-9]{8})'
phone_found = re.search(phone_pattern, str(prompt) if prompt else "")

    if phone_found:
        telephone = phone_found.group()
        
        langue = "Français"
        if any(word in str(prompt).lower() for word in ["salam", "wash", "bghit", "chhal", "kifach", "nta", "3andkom"]):
            langue = "Darija"
        elif any(word in str(prompt).lower() for word in ["hello", "hi", "what", "how"]):
            langue = "Anglais"
        elif any(word in str(prompt).lower() for word in ["hola", "que", "como"]):
            langue = "Espagnol"

        vehicule = "Non spécifié"
        vehicules = ["BMW", "Mercedes", "Audi", "GLE", "GLC", "Q3", "Q8", "X5", "Yamaha", "G63"]
        for v in vehicules:
            for msg in st.session_state.messages:
                if v.lower() in str(msg["content"]).lower():
                    vehicule = v
                    break

        nom = "Client Web"
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                content = str(msg["content"])
                if len(content.split()) <= 3 and not re.search(phone_pattern, content):
                    nom = content
                    break

        save_lead(nom, telephone, vehicule, str(prompt), langue)

except Exception as e:
    print(f"Erreur sauvegarde: {e}")