# Base de Conhecimento

A estratégia de dados adotada foi o uso de arquivos locais (CSV e JSON) carregados diretamente na memória da aplicação via Pandas e injetados no contexto do LLM.

**Arquivos utilizados:**
1. `transacoes.csv`: Histórico de entradas e saídas (vendas e pagamentos de fornecedores).
2. `historico_atendimento.csv`: Consultas passadas para manter o contexto das necessidades de crédito.
3. `perfil_investidor.json`: Faturamento médio e metas financeiras da ótica.
4. `produtos_financeiros.json`: Catálogo de Renda Fixa para gestão do caixa.