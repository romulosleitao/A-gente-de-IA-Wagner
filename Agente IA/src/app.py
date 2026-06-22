import sys
import os


caminho_src = os.path.dirname(os.path.abspath(__file__))
if caminho_src not in sys.path:
    sys.path.append(caminho_src)

import streamlit as st
from utils.agente import configurar_api, carregar_bases, criar_modelo

# ==========================================
# 1. INICIALIZAÇÃO E CONFIGURAÇÃO SEGURA
# ==========================================
if "GOOGLE_API_KEY" in st.secrets:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    GOOGLE_API_KEY = "CHAVE_NAO_CONFIGURADA"

configurar_api(GOOGLE_API_KEY)

import streamlit as st
from utils.agente import configurar_api, carregar_bases, criar_modelo


# 1. INICIALIZAÇÃO

if "GOOGLE_API_KEY" in st.secrets:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    GOOGLE_API_KEY = "CHAVE_NAO_CONFIGURADA"

configurar_api(GOOGLE_API_KEY)

df_transacoes, df_atendimento, perfil, produtos = carregar_bases()
model = criar_modelo(df_transacoes, df_atendimento, perfil, produtos)

#
# 2. INTERFACE
#
st.set_page_config(page_title="Consultor Wagner", page_icon="👓")

st.markdown("""
    <style>
    .stApp { background-color: #F5F5DC; }
    h1, p, div { color: #000000 !important; }
    .stChatMessage { border-left: 4px solid #FFA500; background-color: rgba(255, 255, 255, 0.5); }
    div[data-testid="stChatMessage"]:nth-child(even) { border-left: 4px solid #008000; }
    .stSpinner > div > div { border-top-color: #FF0000 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("👓 Assistente Financeiro IA")
st.markdown("Consulte seu fluxo de caixa e gestão de empresas.")

# ==========================================
# 3. LÓGICA DO CHAT
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Pergunte sobre as finanças da empresa..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Analisando dados..."):
            try:
                # Inicia a conversa com o modelo que foi configurado lá no utils
                chat = model.start_chat(history=[])
                resposta = chat.send_message(prompt).text
                st.markdown(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta})
            except Exception as e:
                st.error(f"Erro na API: {e}")