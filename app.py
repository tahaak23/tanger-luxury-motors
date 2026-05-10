import streamlit as st
from anthropic import Anthropic

client = Anthropic()

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
        text-shadow: none;
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

    .stChatMessage {
        background: linear-gradient(135deg, rgba(42, 37, 32, 0.9), rgba(58, 53, 48, 0.9)) !important;
        border: 1px solid rgba(201, 168, 76, 0.2) !important;
        border-radius: 12px !important;
    }

    .stChatInput textarea {
        background-color: #2a2520 !important;
        color: #C9A84C !important;
        border: 1px solid rgba(201, 168, 76, 0.4) !important;
        border-radius: 10px !important;
    }

    hr {
        border-color: rgba(201, 168, 76, 0.3) !important;
    }

    p, div {
        color: #C9A84C;
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
  * Tableau de bord console et portières carbone
  * Volant M Sport chauffant
  * Jantes M 21 pouces
  * Sièges cuir rouge chauffants ventilés mémoire
  * Toit panoramique Sky Lounge LED
  * Éclairage LED ambiance multicolore
  * Soft Close portes automatiques
  * Coffre électrique
  * Head-Up Display
  * Caméra 360 + Park Assist
  * Apple CarPlay Android Auto
  * Système audio Harman Kardon premium
  * BMW Laser Light
  * Attache remorque électrique

2. Yamaha FX SVHO Limited 2026 - Jet Ski
- Couleur : Noir Mat
- Etat : Neuf
- Moteur : 1.8L Supercharged
- Options principales :
  * Écran digital multifonction
  * Système audio intégré Yamaha
  * Cruise Control
  * Modes Eco et Sport
  * Marche arrière électronique
  * Clé intelligente
  * Grand espace de rangement
  * Selle confort premium
  * Bouée tractable Yamaha incluse
  * Housse de protection incluse
  * Remorque incluse

3. Mercedes GLE Coupé 350DE 4MATIC AMG Line Plus 2026
- Couleur : Noir Obsidienne Métallisé
- Intérieur : Cuir Rouge Bordeaux
- Etat : Neuf 0 km Importée Allemagne
- Motorisation : Hybride Diesel Rechargeable
- Puissance : 333 ch
- Boite : 9G-TRONIC automatique
- Transmission : 4MATIC intégrale
- Options principales :
  * Pack AMG Line Plus extérieur complet
  * Pack Night noir brillant
  * Jantes AMG 22 pouces Black Design
  * Digital Light Multibeam LED
  * Feux arrière LED 3D signature Mercedes
  * Cuir Rouge Bordeaux perforé premium
  * Pack Carbone et Aluminium AMG intérieur
  * Sièges Sport AMG chauffants ventilés multicontours mémoire
  * Sièges arrière chauffants
  * Volant AMG Nappa chauffant
  * Toit panoramique Full Glass
  * Climatisation 4 zones
  * Double écran HD MBUX 2026
  * Navigation réalité augmentée
  * Apple CarPlay Android Auto sans fil
  * Burmester Surround 3D
  * Caméra 360 HD
  * Chargeur induction
  * Assistant vocal Hey Mercedes
  * Suspension AIRMATIC adaptive
  * Direction arrière des roues
  * DISTRONIC PLUS régulateur adaptatif

4. Audi Q3 2026 S Line Diesel Full Options
- Couleur : Noir Métallisé
- Intérieur : Noir Alcantara
- Etat : Neuf Importée
- Motorisation : Diesel
- Boite : S Tronic automatique
- Options principales :
  * Pack S Line intérieur et extérieur
  * Sièges sport Alcantara
  * Virtual Cockpit Audi
  * Écran tactile MMI dernière génération
  * Caméra recul + radars 360
  * Toit panoramique
  * LED Matrix
  * Climatisation automatique multi-zones
  * Jantes sport design

5. Mercedes GLC 300DE 4MATIC Coupé AMG Line Plus 2026
- Couleur : Gris Nardo
- Intérieur : Rouge Sport
- Etat : Neuf Importée
- Motorisation : Hybride Diesel Plug-in
- Transmission : 4MATIC intégrale
- Options principales :
  * Pack Carbone Intérieur Luxe
  * Suspensions pilotées
  * Direction arrière des roues
  * Toit panoramique
  * Multibeam LED
  * Système MBUX dernière génération
  * Sièges Sport AMG
  * Caméra 360 + Parking Assist
  * Chargeur induction
  * Son Burmester

SERVICES :
- Reprise de votre ancien vehicule : OUI
- Livraison a domicile : OUI
- Essai routier : Non disponible
- Financement : Nous contacter pour plus d infos au 0661481800

COMPORTEMENT :
- Tu parles français, darija, anglais et espagnol automatiquement
- Tu détectes la langue du client et réponds dans la même langue
- Tu es toujours élégant, raffiné et ultra professionnel
- Tu appelles toujours le client Monsieur ou Madame
- Tu proposes toujours une visite au showroom ou un rendez-vous
- Jamais de langage familier
- Maximum 1 emoji par réponse
- Style conseiller Rolls Royce ou Bentley
- Ne mentionne jamais que tu es une IA
- Pour les prix invite le client à appeler le 0661481800
- Pour le financement invite le client à appeler le 0661481800
- Mets toujours en valeur l exclusivité et le luxe des véhicules
- Si le client demande une voiture non disponible propose les alternatives disponibles
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

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