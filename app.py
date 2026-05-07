import streamlit as st
from anthropic import Anthropic

client = Anthropic()

st.set_page_config(
    page_title="Tanger Luxury Motors",
    page_icon="🏎️",
    layout="centered"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #0a1628;
        background-image: url('https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=1920&q=80');
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
        background: rgba(10, 22, 40, 0.85);
        z-index: 0;
    }
    .main > div {
        position: relative;
        z-index: 1;
    }
    h1 {
        color: #CFB53B !important;
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 2.5em !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        letter-spacing: 3px;
    }
    .subtitle {
        color: #CFB53B;
        text-align: center;
        font-style: italic;
        font-size: 1.1em;
        margin-bottom: 5px;
    }
    .welcome-box {
        background: rgba(207, 181, 59, 0.1);
        border: 1px solid #CFB53B;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        color: #CFB53B;
        margin: 10px 0 20px 0;
        font-size: 0.95em;
    }
    .hours-box {
        color: #CFB53B;
        text-align: center;
        font-size: 0.85em;
        opacity: 0.8;
    }
    .stChatMessage {
        background-color: rgba(10, 22, 40, 0.8) !important;
        border: 1px solid rgba(207, 181, 59, 0.3);
        border-radius: 10px;
    }
    .stChatInput {
        border-color: #CFB53B !important;
    }
    hr {
        border-color: #CFB53B !important;
        opacity: 0.3;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🏎️ TANGER LUXURY MOTORS")
st.markdown('<p class="subtitle">Votre conseiller virtuel exclusif — Karim</p>', unsafe_allow_html=True)

st.markdown("""
<div class="welcome-box">
    ✨ Bienvenue chez Tanger Luxury Motors — Mrhba bik !<br>
    Je suis Karim, votre conseiller personnel.<br>
    Posez-moi vos questions en français, darija ou anglais.
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="hours-box">🕐 Lundi - Samedi : 9h00 - 19h00 &nbsp;|&nbsp; 📍 Boulevard Mohammed VI, Tanger</p>', unsafe_allow_html=True)

st.divider()

system_prompt = """Tu es Karim, conseiller virtuel exclusif de Tanger Luxury Motors.

SHOWROOM :
- Adresse : Boulevard Mohammed VI, Tanger
- Horaires : Lundi-Samedi 9h-19h
- Telephone : 05 39 XX XX XX

STOCK :
- Mercedes GLE 2024 : 1 250 000 DH
- Mercedes G-Wagon 2024 : 2 900 000 DH
- BMW X5 2024 : 950 000 DH
- BMW X7 2024 : 1 250 000 DH
- Porsche Cayenne 2024 : 1 350 000 DH
- Range Rover Sport 2024 : 1 500 000 DH

SERVICES :
- Essai routier gratuit
- Financement et leasing disponible
- Reprise ancien vehicule
- Garantie 3 ans incluse

COMPORTEMENT :
- Si le client ecrit en darija, reponds en darija naturelle et simple
- Si le client ecrit en francais, reponds en francais
- Si le client ecrit en anglais, reponds en anglais
- Tu es toujours elegant et professionnel
- Tu appelles toujours le client Monsieur ou Madame
- Tu proposes toujours un essai routier ou rendez-vous
- Jamais de langage familier
- Maximum 1 emoji par reponse
- Style conseiller Ferrari ou Rolls Royce
- Ne mentionne jamais que tu es une IA
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Écrivez votre message en français, darija ou anglais..."):
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