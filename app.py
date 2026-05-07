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
        background-color: #0a0a0a;
        color: #gold;
    }
    .stChatMessage {
        background-color: #1a1a1a;
    }
    h1 {
        color: #CFB53B;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    p {
        color: #CFB53B;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🏎️ Tanger Luxury Motors")
st.markdown("*Votre conseiller virtuel exclusif — Karim*")
st.divider()

system_prompt = """Tu es Karim, conseiller virtuel de Tanger Luxury Motors.

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
- Si le client ecrit en darija, tu reponds OBLIGATOIREMENT en darija marocaine
- Si le client ecrit en francais, tu reponds en francais
- Si le client ecrit en anglais, tu reponds en anglais
- Tu es toujours elegant et professionnel
- Tu appelles toujours le client Monsieur ou Madame
- Tu proposes toujours un essai routier ou rendez-vous
- Jamais de langage familier ou Hhhh
- Maximum 1 emoji par reponse
- Style conseiller Ferrari ou Rolls Royce
- Ne mentionne jamais que tu es une IA
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Écrivez votre message..."):
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