import streamlit as st#type: ignore
import pandas as pd
from pages.authentication.login import show_login
from pages.dashboard.dash_overview import show_dash
from pages.reports.reports_overview import show_reports
from pages.customers.clients_overview import show_clients
from pages.inventory.inv_overview import show_inventory
from pages.orders.order_overview import show_orders

def main():


    # Armazena o estado de autenticação
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        
    # Verifica se o usuário está autenticado
    if not st.session_state.authenticated:
        show_login()# Exibe a tela de login

    else: 

        st.sidebar.title("Aonde vamos?")# Título da barra lateral

        st.sidebar.markdown(" ")

        page = st.sidebar.radio("",

            (":house: Inicio", 
            ":busts_in_silhouette: Clientes", 
            ":package: Estoque", 
            ":shopping_trolley: Pedidos", 
            ":bar_chart: Relatórios")
        )

        # Navegação baseada na página selecionada
        match page:

            case ":house: Inicio":
                show_dash()# Exibe o dashboard
            
            case ":busts_in_silhouette: Clientes":
                show_clients()# Exibe a pagina de cliente

            case ":package: Estoque":
                show_inventory()# Exibe a pagina do estoque

            case ":shopping_trolley: Pedidos":
                show_orders()# Exibe a pagina de pedidos
            
            case ":bar_chart: Relatórios":
                show_reports()# Exibe a pagina de relatório
        
        st.sidebar.markdown("---")
        # Botão de logout
        if st.sidebar.button("Sair", icon=":material/logout:"):
            st.session_state.authenticated = False# Atualiza o estado de autenticação
            st.rerun()# Reinicia a aplicação

if __name__ == "__main__":
    main()
