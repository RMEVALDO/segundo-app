Atue como um desenvolvedor Python sênior especializado em Streamlit e didática de Vibe Coding.

Preciso de uma aplicação web intermediária em Python chamada "Simulador de Custos e Orçamento". O objetivo é praticar filtros interativos, cálculos acumulados e alertas dinâmicos.

Requisitos da aplicação:
1. Barra Lateral (Sidebar):
   - Um controle deslizante (st.slider) para definir o "Orçamento Total Disponível" (de R$ 5.000 a R$ 50.000, padrão R$ 20.000, passo de R$ 500).
   - Um filtro de seleção múltipla (st.multiselect) para escolher quais categorias exibir (ex: Matéria-Prima, Mão de Obra, Logística, Energia, Ferramentas).
2. Base de Dados Interna:
   - Crie internamente um DataFrame do Pandas com 8 a 12 despesas simuladas contendo: "Item", "Categoria", "Valor (R$)" e "Prioridade" (Alta, Média, Baixa).
3. Área Principal:
   - Título e subtítulo organizados.
   - Painel de 3 métricas no topo (st.columns e st.metric):
     1. Orçamento Definido.
     2. Gasto Filtrado (total da soma dos itens filtrados).
     3. Saldo Restante (com indicador delta positivo ou negativo).
   - Alerta visual condicional:
     - Se o Gasto for menor ou igual ao Orçamento: mensagem de sucesso (st.success) informando que o projeto está dentro da meta.
     - Se ultrapassar o Orçamento: mensagem de aviso/erro (st.error) alertando o valor excedido.
   - Gráfico de pizza ou barras horizontais agrupando o total de gastos por Categoria.
   - Tabela (st.dataframe) exibindo apenas os itens correspondentes aos filtros selecionados.
4. Resiliência:
   - Todo o código deve estar em um único arquivo chamado `app.py`.
   - Utilizar apenas `streamlit` e `pandas` (sem dependências pesadas de gráficos para evitar falhas de deploy).

Por favor, forneça:
1. O código completo do arquivo `app.py`.
2. O conteúdo exato para o arquivo `requirements.txt`.
3. Instruções rápidas de como rodar no terminal do GitHub Codespaces.
