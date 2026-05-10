import streamlit as st
from anthropic import Anthropic

client = Anthropic()

st.set_page_config(
    page_title="Edition Auto Tanger",
    page_icon="🏎️",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0a0a0a;
        background-image: url('https://images.unsplash.com/photo-1617814076367-b759c7d7e738?w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.88);
        z-index: 0;
    }
    .main > div {
        position: relative;
        z-index: 1;
    }
    h1 {
        color: #C0C0C0 !important;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 2.2em !important;
        letter-spacing: 4px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    }
    .subtitle {
        color: #C0C0C0;
        text-align: center;
        font-style: italic;
        font-size: 1em;
        margin-bottom: 5px;
    }
    .welcome-box {
        background: rgba(192, 192, 192, 0.1);
        border: 1px solid #C0C0C0;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        color: #C0C0C0;
        margin: 10px 0 20px 0;
        font-size: 0.95em;
    }
    .info-box {
        color: #C0C0C0;
        text-align: center;
        font-size: 0.85em;
        opacity: 0.8;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🏎️ EDITION AUTO")
st.markdown('<p class="subtitle">Votre conseiller virtuel exclusif</p>', unsafe_allow_html=True)

st.markdown("""
<div class="welcome-box">
    ✨ Bienvenue chez Edition Auto Tanger !<br>
    Je suis votre conseiller personnel.<br>
    Posez-moi vos questions en français, darija, anglais ou español.
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="info-box">🕐 Tous les jours : 10h00 - 20h00 &nbsp;|&nbsp; 📍 Rue Fes N°140, Tanger &nbsp;|&nbsp; 📞 0661481800</p>', unsafe_allow_html=True)

st.divider()

system_prompt = """Tu es le conseiller virtuel exclusif d'Edition Auto Tanger.

SHOWROOM :
- Nom : Edition Auto
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
  * Direction arrière (ultra rare)
  * Suspension Adaptive M
  * Pack Carbone intégral intérieur
  * Tableau de bord, console et portières carbone
  * Volant M Sport chauffant
  * Jantes M 21 pouces
  * Sièges cuir rouge chauffants ventilés mémoire
  * Toit panoramique Sky Lounge LED
  * Éclairage LED ambiance multicolore
  * Soft Close portes automatiques
  * Coffre électrique
  * Head-Up Display
  * Caméra 360 + Park Assist
  * Apple CarPlay / Android Auto
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
- Etat : Neuf — 0 km — Importée Allemagne
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
  * Éclairage ambiance LED multicolore
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
- Etat : Neuf — Importée
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
- Etat : Neuf — Importée
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
- Financement : Nous contacter pour plus d'infos au 0661481800

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
- Pour les prix, invite le client à appeler le 0661481800
- Pour le financement, invite le client à appeler le 0661481800
- Mets toujours en valeur l exclusivité et le luxe des véhicules
- Si le client demande une voiture non disponible, propose les alternatives disponibles
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