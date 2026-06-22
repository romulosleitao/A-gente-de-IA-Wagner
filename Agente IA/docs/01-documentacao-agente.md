# Documentação do Agente Financeiro

## 1. Caso de Uso
**Problema:** Dificuldade na gestão rápida de fluxo de caixa, controle de despesas com fornecedores de armações e planejamento financeiro para reposição de estoque.
**Solução:** Um agente financeiro de IA que cruza o histórico de transações com o perfil corporativo da WD Soluções Ópticas para responder rapidamente sobre a saúde do caixa e sugerir produtos financeiros adequados.

## 2. Persona e Tom de Voz
**Persona:** Um consultor financeiro corporativo, sênior e analítico.
**Tom de voz:** Direto, profissional e focado em resultados. Não usa jargões desnecessários e foca na liquidez e segurança da empresa.

## 3. Arquitetura Simples
Usuário -> Interface (Streamlit) -> Processamento (Python/Pandas lendo CSV/JSON) -> LLM (Google Gemini 1.5 Flash) -> Resposta validada ao Usuário.

## 4. Segurança e Anti-Alucinação
- O agente tem uma instrução rígida (System Prompt) para **não inventar** dados.
- Ele só pode calcular e responder com base nos arquivos locais de transações e perfil.
- Para assuntos fora do escopo, ele utiliza uma frase de escape padrão: "Como consultor da empresa, não tenho acesso a essa informação no momento."