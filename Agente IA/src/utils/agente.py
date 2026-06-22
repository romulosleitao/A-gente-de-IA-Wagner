import pandas as pd
import json
import streamlit as st
import google.generativeai as genai


def configurar_api(api_key):
    """Configura a chave da API do Google Gemini"""
    genai.configure(api_key=api_key)


@st.cache_data
def carregar_bases():
    """Carrega todos os arquivos locais da pasta data"""
    try:
        df_transacoes = pd.read_csv("data/transacoes.csv")
        df_atendimento = pd.read_csv("data/historico_atendimento.csv")

        with open("data/perfil_investidor.json", "r", encoding="utf-8") as f:
            perfil = json.load(f)
        with open("data/produtos_financeiros.json", "r", encoding="utf-8") as f:
            produtos = json.load(f)

        return df_transacoes, df_atendimento, perfil, produtos
    except Exception as e:
        return None, None, None, None


def criar_modelo(df_transacoes, df_atendimento, perfil, produtos):
    """Constrói o prompt de sistema e inicializa o modelo da IA"""
    system_prompt = f"""
    Você é o consultor financeiro exclusivo da WD Soluções Ópticas. 
    Sua personalidade é direta, analítica e focada em manter a saúde financeira da empresa.

    REGRAS OBRIGATÓRIAS (Anti-Alucinação):
    1. Você só pode responder com base nos dados fornecidos abaixo.
    2. Se perguntarem algo fora dos dados, diga: "Como consultor da empresa, não tenho acesso a essa informação no momento."
    3. Ajude a analisar as transações e o perfil do usuário para uma gestão inteligente do fluxo de caixa.

    DADOS DO CLIENTE (PERFIL):
    {json.dumps(perfil, indent=2, ensure_ascii=False) if perfil else "Sem dados."}

    HISTÓRICO DE TRANSAÇÕES RECENTES:
    {df_transacoes.to_string() if df_transacoes is not None else "Sem transações."}

    HISTÓRICO DE ATENDIMENTOS ANTERIORES:
    {df_atendimento.to_string() if df_atendimento is not None else "Sem histórico."}

    PRODUTOS FINANCEIROS DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False) if produtos else "Sem produtos."}
    """

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        system_instruction=system_prompt
    )
    return model