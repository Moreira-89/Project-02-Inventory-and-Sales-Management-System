import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import os

st.set_page_config(layout="wide")

st.sidebar.title("Navegação")
st.sidebar.page_link("pages/clients_overview.py", label="Clientes", icon=":material/person:")
st.sidebar.page_link("pages/inv_overview.py", label="Estoque", icon=":material/inventory:")
st.sidebar.page_link("pages/reports_overview.py", label="Relatorios", icon=":material/lab_profile:")
st.sidebar.page_link("app.py", label="Voltar para inicio", icon=":material/home:")


st.title("Pedidos")

# ---> Importacao dos dados
file_path = "assets/data/data_orders.csv"

if os.path.exists(file_path):
    try:

        df = pd.read_csv(file_path, sep=",")
        df["Data"] = pd.to_datetime(df["Data"])

    except Exception as e:

        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
    
else:
    st.error(f"Arquivo '{file_path}' não encontrado!")

# Filtros na tela de pedidos
st.write("Filtros para Pedidos")

# Filtro de Cliente
cliente = st.selectbox("Selecione o Cliente", options=["Todos"] + list(df["Cliente"].unique()))

# Filtro de Produto / Serviço
produto_servico = st.selectbox("Selecione o Produto/Serviço", options=["Todos"] + list(df["Produto / Servico"].unique()))

# Filtro de Data (intervalo)
data_inicial = st.date_input("Data Inicial", df["Data"].min())
data_final = st.date_input("Data Final", df["Data"].max())

# Botão para abrir o formulário
col1, col2 = st.columns([4, 1])

with col1:
    # Exibindo o botão para aplicar filtros
    if st.button("Aplicar Filtros"):
        # Filtrando os dados com base nos critérios
        filtered_df = df[
            (df["Cliente"] == cliente or cliente == "Todos") &
            (df["Produto / Servico"] == produto_servico or produto_servico == "Todos") &
            (df["Data"] >= pd.to_datetime(data_inicial)) &
            (df["Data"] <= pd.to_datetime(data_final))
        ]
        
        # Exibindo o relatório de pedidos filtrado
        if not filtered_df.empty:
            st.subheader("Pedidos Encontrados")
            st.dataframe(filtered_df)
        else:
            st.warning("Nenhum pedido encontrado com os filtros selecionados.")

# Função para abrir o formulário de cadastro de pedido
@st.dialog("Formulário de Cadastro de Pedido")
def register(df):
    cliente_name = st.selectbox("Selecione o Cliente", options=df["Cliente"].unique())
    produto_name = st.text_input("Produto / Serviço")
    quantidade = st.text_input("Quantidade")
    data_pedido = st.date_input("Data do Pedido")
    valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)

    if st.button("Cadastrar Pedido"):
        if cliente_name and produto_name and quantidade and valor > 0:
            # Simulando o cadastro do pedido
            new_order = {
                "Cliente": cliente_name,
                "Produto / Servico": produto_name,
                "Quantidade": quantidade,
                "Data": data_pedido,
                "Valor (R$)": valor
            }
            
            # Adicionando o novo pedido ao DataFrame
            df = df.append(new_order, ignore_index=True)
            st.success(f"Pedido de {cliente_name} cadastrado com sucesso!")
            st.rerun()  # Reinicia a aplicação para atualizar a tabela
        else:
            st.warning("Por favor, preencha todos os campos!")

if 'products' not in st.session_state:
    st.session_state.products = []

with col2:
    if st.button("Cadastrar Novo Pedido"):
        register(df)
