import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import os

st.set_page_config(layout="wide")

st.sidebar.title("Navegação")
st.sidebar.page_link("pages/clients_overview.py", label="Clientes", icon=":material/person:")
st.sidebar.page_link("pages/inv_overview.py", label="Estoque", icon=":material/inventory:")
st.sidebar.page_link("pages/order_overview.py", label="Pedidos", icon=":material/orders:")
st.sidebar.page_link("app.py", label="Voltar para inicio", icon=":material/home:")

# Título da página
st.title("Relatórios")

# ---> Importacao dos dados
file_path = "assets\data\data_reports.csv"

if os.path.exists(file_path):
    try:

        data = pd.read_csv(file_path, sep=",")

    except Exception as e:

        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
    
else:
    st.error(f"Arquivo '{file_path}' não encontrado!")

# Criando o DataFrame
df = pd.DataFrame(data)
df["Data"] = pd.to_datetime(df["Data"])

# Filtros na tela principal (fora da sidebar)
st.write("Filtros para Geração de Relatórios")

col1, col2= st.columns(2)

with col1:
    produto_servico = st.selectbox("Selecione o Produto/Serviço", options=df["Produto \ Servico"].unique())

with col2:
    cliente = st.selectbox("Selecione o Cliente", options=df["Cliente"].unique())

# Filtro de Data (opcional)
data_inicial = st.date_input("Data Inicial", df["Data"].min())
data_final = st.date_input("Data Final", df["Data"].max())

if st.button("Aplicar Filtros"):
    # Filtrando os dados com base nos critérios
    filtered_df = df[
        (df["Produto \ Servico"] == produto_servico) &
        (df["Cliente"] == cliente) &
        (df["Data"] >= pd.to_datetime(data_inicial)) &
        (df["Data"] <= pd.to_datetime(data_final))
    ]
    
    # Exibindo o relatório filtrado
    if not filtered_df.empty:
        st.subheader(f"Relatório de Vendas - {produto_servico} para {cliente} entre {data_inicial} e {data_final}")
        st.dataframe(filtered_df)
    else:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")

    # Botão para exportar para Excel
    if st.button("Exportar Relatório para Excel"):
        # Salvando o relatório filtrado em Excel
        filtered_df.to_excel("relatorio.xlsx", index=False)
        st.success("Relatório exportado com sucesso!")
