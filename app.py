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

st.markdown('<p class="info-box">🕐 Lundi - Dimanche : 10h00 - 20h00 &nbsp;|&nbsp; 📍 Rue Fes N°140, Tanger &nbsp;|&nbsp; 📞 0661481800</p>', unsafe_allow_html=True)

st.divider()

system_prompt = """Tu es le conseiller virtuel exclusif d'Edition Auto Tanger.

SHOWROOM :
- Nom : Edition Auto
- Adresse : Residence Office, Rue Fes N°140, Tanger, Maroc
- Horaires : Tous les jours 10h00 - 20h00
- Telephone : 0661481800

VEHICULES DISPONIBLES :
Mercedes :
- Mercedes G 63 2026 — Gris
- Mercedes GLE 350 DE 2026 — Noir
- Mercedes GLC 300D — Gris Nardo
- Mercedes GLC 300 DE — Gris Nardo
- Mercedes GLC 300 DE — Noir

Audi :
- Audi Q3 2026 — Noir
- Audi Q8 2026 — Gris Souris

BMW :
- BMW X5 M50D Pack M

Jet Ski :
- Yamaha FX SVHO Limited 2026

SERVICES :
- Reprise de votre ancien vehicule : OUI
- Livraison a domicile : OUI
- Essai routier : Non disponible
- Financement : Nous contacter pour plus d'infos

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
- Si le client demande le prix, dis lui de contacter directement au 0661481800
- Pour le financement, invite le client à appeler le 0661481800
- Mets toujours en valeur l'exclusivité et le luxe des véhicules
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