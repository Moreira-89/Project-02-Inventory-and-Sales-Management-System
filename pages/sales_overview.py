import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import os

st.set_page_config(layout="wide")

st.sidebar.title("Navegação")
st.sidebar.page_link("pages/clients_overview.py", label="Clientes", icon=":material/person:")
st.sidebar.page_link("pages/inv_overview.py", label="Estoque", icon=":material/inventory:")
st.sidebar.page_link("pages/order_overview.py", label="Pedidos", icon=":material/orders:")
st.sidebar.page_link("pages/reports_overview.py", label="Relatorios", icon=":material/lab_profile:")
st.sidebar.page_link("app.py", label="Voltar para inicio", icon=":material/home:")

# Título da página
st.title("Vendas")

# Caminho para os arquivos de vendas e estoque
sales_file_path = "assets/data/data_sales.csv"
inventory_file_path = "assets/data/data_inventory.csv"

# Carregar os dados de vendas e estoque
if os.path.exists(inventory_file_path):
    inventory_df = pd.read_csv(inventory_file_path, sep=";")
else:
    st.error(f"Arquivo de estoque '{inventory_file_path}' não encontrado!")

if os.path.exists(sales_file_path):
    sales_df = pd.read_csv(sales_file_path, sep=",")
else:
    st.error(f"Arquivo de vendas '{sales_file_path}' não encontrado!")


# --> Cadastro de vendas
@st.dialog("Formulário para cadastro da venda")
def register_sale():
   
    customer_name = st.text_input("Nome do Cliente", placeholder="Insira o nome do cliente")
    product_name = st.selectbox("Produto", inventory_df["produto"].tolist())  # Lista de produtos do estoque
    quantity = st.number_input("Quantidade", min_value=1, max_value=10, step=1)  # Quantidade do produto
    sale_date = st.date_input("Data da Venda", pd.to_datetime("today"))
    
    # Obter o valor do produto a partir do estoque
    product_price = inventory_df[inventory_df["produto"] == product_name]["valor"].values[0]
    total_value = product_price * quantity  # Valor total da venda
    
    if st.button("Registrar Venda"):
        if customer_name and product_name and quantity > 0:
            # Adicionando a venda ao DataFrame de vendas
            new_sale = {
                "Cliente": customer_name,
                "Produto": product_name,
                "Quantidade": quantity,
                "Valor Total": total_value,
                "Data": sale_date
            }
            sales_df = sales_df.append(new_sale, ignore_index=True)
            
            # Atualizar estoque (diminuir a quantidade do produto)
            inventory_df.loc[inventory_df["Nome"] == product_name, "Quantidade"] -= quantity

            st.success(f"Venda registrada com sucesso!")
            st.rerun()  # Atualiza a página para refletir a nova venda
        else:
            st.warning("Por favor, preencha todos os campos corretamente!")


# --> Exibição das Vendas
search_input = st.text_input("Pesquisar Vendas", placeholder="Pesquisar por cliente ou produto")

# Exibir o formulário de cadastro de venda
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("Cadastrar Nova Venda"):
        register_sale()

# Filtro de vendas com base na pesquisa
with col1:
    if search_input:
        filtered_sales = sales_df[sales_df.apply(lambda row: row.astype(str).str.contains(search_input, case=False).any(), axis=1)]
        st.table(filtered_sales)
    else:
        st.table(sales_df)