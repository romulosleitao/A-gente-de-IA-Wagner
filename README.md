# 💼 Wagner - Agente Financeiro Inteligente

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B.svg)
![Gemini](https://img.shields.io/badge/Google_Gemini-AI-orange.svg)

## 📌 Sobre o Projeto
Este repositório contém o desenvolvimento do **Wagner**, um **Agente Financeiro baseado em Inteligência Artificial**. O sistema foi projetado para atuar como um consultor financeiro analítico e direto, cruzando dados históricos de transações, faturamento e perfil de investimento para oferecer respostas rápidas e auxiliar na tomada de decisão sobre capital de giro e gestão de caixa.

O projeto foi construído utilizando **Python**, **Streamlit** para a interface interativa e a API do **Google Gemini** como motor de processamento de linguagem natural.

## 🚀 Funcionalidades Principais
* **Análise Rápida de Caixa:** Leitura e interpretação de dados financeiros (entradas e saídas) a partir de bases locais (`.csv` e `.json`).
* **Consultoria Personalizada:** Recomendação de produtos financeiros (como CDBs e LCIs) alinhados às metas e ao perfil do usuário.
* **Sistema Anti-Alucinação:** Implementação de *System Prompts* rigorosos que impedem a IA de inventar dados ou responder sobre escopos fora das informações fornecidas.
* **Interface Intuitiva:** Dashboard amigável construído em Streamlit, permitindo interação fluida via chat diretamente com o Wagner.

## 📂 Arquitetura e Estrutura de Pastas
O projeto segue as melhores práticas de modularização de software, incluindo um template estrutural para o gerenciamento seguro de credenciais:

```text
📦 Agente IA
 ┣ 📂 .streamlit/         # Diretório de configurações do framework
 ┃ ┗ 📜 secrets.toml      # Template de credenciais (contém chave genérica de exemplo)
 ┣ 📂 data/               # Bases de conhecimento locais (transacoes.csv, perfil.json)
 ┣ 📂 docs/               # Documentação completa (pitch, métricas, prompts, etc.)
 ┣ 📂 src/                # Código-fonte principal
 ┃ ┣ 📂 utils/
 ┃ ┃ ┣ 📜 __init__.py     # Inicializador do módulo
 ┃ ┃ ┗ 📜 agente.py       # Lógica de conexão com o Gemini e carregamento de dados
 ┃ ┗ 📜 app.py            # Interface gráfica e execução do Streamlit
 ┣ 📜 .gitignore          # Proteção contra upload de ambientes virtuais e chaves reais
 ┗ 📜 README.md           # Documentação principal do repositório
