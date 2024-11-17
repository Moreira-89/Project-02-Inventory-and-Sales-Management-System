import plotly.express as px
import streamlit as st
import pandas as pd
import os
from pages.login import show_login

def main():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # Verifica se o usuário está autenticado
    if st.session_state.authenticated:

        st.set_page_config(layout="wide")

        st.sidebar.image("assets/images/user_photo.png")

        st.sidebar.write("Nome: Mauricio")
        st.sidebar.write("Cargo: Administrador") 

        st.sidebar.markdown("---")

        st.sidebar.title("Navegação")
        st.sidebar.page_link("pages/clients_overview.py", label="Clientes", icon=":material/person:")
        st.sidebar.page_link("pages/inv_overview.py", label="Estoque", icon=":material/inventory:")
        st.sidebar.page_link("pages/sales_overview.py", label="Vendas", icon=":material/point_of_sale:")
        st.sidebar.page_link("pages/order_overview.py", label="Pedidos", icon=":material/orders:")
        st.sidebar.page_link("pages/reports_overview.py", label="Relatorios", icon=":material/lab_profile:")
        
        st.sidebar.markdown("---")
        
        if st.sidebar.button("Sair", icon=":material/logout:"):
            st.session_state.authenticated = False
            st.rerun()

        st.title('Dashboard de Gestão de Oficina Mecânica')

        # Caminho para os csv
        sales_file_path = "assets/data/data_sales.csv"
        inventory_file_path = "assets/data/data_inventory.csv"
        client_file_path = "assets/data/data_clients.csv"

        # Carregar os dados de vendas e estoque
        if os.path.exists(inventory_file_path):
            inventory_df = pd.read_csv(inventory_file_path, sep=";")
        else:
            st.error(f"Arquivo de estoque '{inventory_file_path}' não encontrado!")

        if os.path.exists(sales_file_path):
            sales_df = pd.read_csv(sales_file_path, sep=",")
        else:
            st.error(f"Arquivo de vendas '{sales_file_path}' não encontrado!")

        if os.path.exists(client_file_path):
            client_df = pd.read_csv(client_file_path, sep=",")
        else:
            st.error(f"Arquivo de clientes '{client_file_path}' não encontrado!")

        col1, col2 = st.columns(2)

        with col1:
            # 1. Relatório de Compras por Cliente
            st.write('Compras por Cliente')
            compras_cliente = sales_df.groupby('Cliente').size().reset_index(name='Compras')

            fig_compras_cliente = px.pie(compras_cliente, 
                                        names='Cliente', 
                                        values='Compras', 
                                        title='Número de Compras por Cliente')
            st.plotly_chart(fig_compras_cliente)

        with col2:
            # 2. Gráfico de Estoque de Produtos
            st.write('Estoque de Produtos')
            inventory_df_sorted = inventory_df.sort_values(by='quantidade', ascending=False)
            fig_estoque = px.bar(inventory_df_sorted, 
                                x='produto', 
                                y='quantidade', 
                                title='Estoque de Produtos', 
                                labels={'quantidade': 'Quantidade no Estoque', 'produto': 'Produto'})
            st.plotly_chart(fig_estoque)
        
        # 3. Gráfico de Vendas por Produto
        st.write('Vendas por Produto')
        vendas_produto = sales_df.groupby('Produto').agg({'Quantidade': 'sum', 'Valor Total': 'sum'}).reset_index()
        fig_vendas_produto = px.bar(vendas_produto, 
                                    x='Produto', 
                                    y='Valor Total', 
                                    title='Vendas por Produto', 
                                    labels={'Valor Total': 'Valor Total (R$)', 'Produto': 'Produto'})
        st.plotly_chart(fig_vendas_produto)

    else:
        show_login()

if __name__ == "__main__":
    main()