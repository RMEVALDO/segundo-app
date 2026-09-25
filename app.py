import pandas as pd
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Simulador de Custos e Orçamento",
    page_icon="💰",
    layout="wide",
)


# 1. Base de Dados Interna (Cached para performance)
@st.cache_data
def carregar_dados():
    dados = [
        {"Item": "Aço e Chapas", "Categoria": "Matéria-Prima", "Valor (R$)": 4500.00, "Prioridade": "Alta"},
        {"Item": "Componentes Eletrônicos", "Categoria": "Matéria-Prima", "Valor (R$)": 3200.00, "Prioridade": "Alta"},
        {"Item": "Desenvolvedores Python", "Categoria": "Mão de Obra", "Valor (R$)": 7500.00, "Prioridade": "Alta"},
        {"Item": "Designer UX", "Categoria": "Mão de Obra", "Valor (R$)": 2800.00, "Prioridade": "Média"},
        {"Item": "Frete Internacional", "Categoria": "Logística", "Valor (R$)": 2100.00, "Prioridade": "Média"},
        {"Item": "Distribuição Local", "Categoria": "Logística", "Valor (R$)": 950.00, "Prioridade": "Baixa"},
        {"Item": "Energia Fabril", "Categoria": "Energia", "Valor (R$)": 1800.00, "Prioridade": "Alta"},
        {"Item": "Servidores Cloud", "Categoria": "Energia", "Valor (R$)": 600.00, "Prioridade": "Alta"},
        {"Item": "Licença IDEs", "Categoria": "Ferramentas", "Valor (R$)": 400.00, "Prioridade": "Baixa"},
        {"Item": "Equipamentos de Teste", "Categoria": "Ferramentas", "Valor (R$)": 1500.00, "Prioridade": "Média"},
    ]
    return pd.DataFrame(dados)


df = carregar_dados()

# 2. Barra Lateral (Sidebar)
st.sidebar.header("⚙️ Configurações do Projeto")

orcamento_total = st.sidebar.slider(
    "Orçamento Total Disponível (R$)",
    min_value=5000,
    max_value=50000,
    value=20000,
    step=500,
    format="R$ %d",
)

categorias_disponiveis = df["Categoria"].unique().tolist()
categorias_selecionadas = st.sidebar.multiselect(
    "Filtrar por Categoria",
    options=categorias_disponiveis,
    default=categorias_disponiveis,
)

# Aplicar filtro de categoria ao DataFrame
if categorias_selecionadas:
    df_filtrado = df[df["Categoria"].isin(categorias_selecionadas)]
else:
    df_filtrado = df.iloc[0:0]  # DataFrame vazio caso nada seja selecionado

# 3. Área Principal
st.title("💰 Simulador de Custos e Orçamento")
st.caption("Acompanhe e simule os custos do projeto em tempo real com filtros interativos.")

# Cálculos
gasto_total = df_filtrado["Valor (R$)"].sum()
saldo = orcamento_total - gasto_total

# Painel de Métricas (Top Bar)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Orçamento Definido", f"R$ {orcamento_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

with col2:
    st.metric("Gasto Filtrado", f"R$ {gasto_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

with col3:
    st.metric(
        "Saldo Restante",
        f"R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        delta=f"R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        delta_color="normal",
    )

st.divider()

# Alerta Visual Condicional
if saldo >= 0:
    st.success(f"✅ **Projeto sob controle!** Você ainda tem **R$ {saldo:,.2f}** dentro do limite estipulado.")
else:
    st.error(f"⚠️ **Atenção!** O orçamento foi excedido em **R$ {abs(saldo):,.2f}**. Ajuste os filtros ou o limite.")

# Seção Visual: Gráfico nativo + Tabela
st.subheader("📊 Distribuição de Gastos por Categoria")

if not df_filtrado.empty:
    col_grafico, col_tabela = st.columns([1, 1.2])

    with col_grafico:
        # Agrupamento por Categoria (Gráfico nativo de barras do Streamlit)
        gastos_por_cat = df_filtrado.groupby("Categoria")["Valor (R$)"].sum()
        st.bar_chart(gastos_por_cat)

    with col_tabela:
        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Valor (R$)": st.column_config.NumberColumn(
                    "Valor (R$)",
                    format="R$ %.2f",
                )
            },
        )
else:
    st.info("Nenhuma categoria selecionada no menu lateral.")
