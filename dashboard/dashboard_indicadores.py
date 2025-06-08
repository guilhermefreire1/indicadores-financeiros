import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import sqlite3

st.set_page_config(
    page_title="Dashboard - Indicadores Econômicos",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Dashboard de Indicadores Econômicos")
st.markdown("Visualização interativa de **Selic, IPCA e Dólar Comercial** com dados reais da API SGS (BACEN).")

# Função para carregar os dados
@st.cache_data
def carregar_dados_sqlite(indicador):
    conn = sqlite3.connect("db/indicadores.db")
    query = f"""
        SELECT data, valor, indicador
        FROM indicadores
        WHERE indicador = '{indicador.lower()}'
    """
    df = pd.read_sql_query(query, conn, parse_dates=["data"])
    conn.close()
    return df

# Lista de indicadores disponíveis
indicadores = ["Selic", "IPCA", "Dolar"]

# Indicador principal
indicador_selecionado = st.selectbox("📌 Selecione o indicador principal", indicadores)

# Segundo indicador para comparação (opcional)
indicador_comparacao = st.selectbox("📊 Comparar com outro indicador?", ["Nenhum"] + [i for i in indicadores if i != indicador_selecionado])

# Carregar dados do indicador principal
df = carregar_dados_sqlite(indicador_selecionado)

# Opções de ano e mês
anos_disponiveis = df["data"].dt.year.sort_values().unique()
ano_selecionado = st.selectbox("📆 Filtrar por ano", anos_disponiveis)

meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}
mes_selecionado = st.selectbox("🗓️ Filtrar por mês (opcional)", ["Todos"] + list(meses.values()))

# Filtragem por ano e mês
df_filtrado = df[df["data"].dt.year == ano_selecionado]
if mes_selecionado != "Todos":
    numero_mes = [k for k, v in meses.items() if v == mes_selecionado][0]
    df_filtrado = df_filtrado[df_filtrado["data"].dt.month == numero_mes]

# Resumo estatístico
col1, col2, col3 = st.columns(3)
col1.metric("📈 Máximo", f"{df_filtrado['valor'].max():.2f}")
col2.metric("📉 Mínimo", f"{df_filtrado['valor'].min():.2f}")
col3.metric("📊 Média", f"{df_filtrado['valor'].mean():.2f}")

# Gráfico principal
fig = px.line(
    df_filtrado,
    x="data",
    y="valor",
    title=f"Evolução de {indicador_selecionado}",
    labels={"data": "Data", "valor": indicador_selecionado}
)
st.plotly_chart(fig, use_container_width=True)

# Gráfico comparativo (se selecionado)
if indicador_comparacao != "Nenhum":
    df_comp = carregar_dados_sqlite(indicador_comparacao)
    df_comp = df_comp[df_comp["data"].dt.year == ano_selecionado]
    if mes_selecionado != "Todos":
        df_comp = df_comp[df_comp["data"].dt.month == numero_mes]

    fig_comp = px.line()
    fig_comp.add_scatter(x=df_filtrado["data"], y=df_filtrado["valor"], mode="lines", name=indicador_selecionado)
    fig_comp.add_scatter(x=df_comp["data"], y=df_comp["valor"], mode="lines", name=indicador_comparacao)

    fig_comp.update_layout(
        title=f"📊 Comparativo: {indicador_selecionado} vs {indicador_comparacao}",
        xaxis_title="Data",
        yaxis_title="Valor",
    )
    st.plotly_chart(fig_comp, use_container_width=True)

# Tabela
st.markdown("### 📋 Tabela com dados filtrados")
st.dataframe(df_filtrado, use_container_width=True)
