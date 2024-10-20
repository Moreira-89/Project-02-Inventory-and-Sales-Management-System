import streamlit as st#type: ignore
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

        page = st.sidebar.radio(
            "Navegação",
            ("Inicio", "Clientes", "Estoque", "Pedidos", "Relatórios")
        )

        # Navegação baseada na página selecionada
        match page:

            case "Inicio":
                show_dash()# Exibe o dashboard
            
            case "Clientes":
                show_clients()# Exibe a pagina de cliente

            case "Estoque":
                show_inventory()# Exibe a pagina do estoque

            case "Pedidos":
                show_orders()# Exibe a pagina de pedidos
            
            case "Relatórios":
                show_reports()# Exibe a pagina de relatório
        
        st.sidebar.markdown("---")
        # Botão de logout
        if st.sidebar.button("Sair", icon=":material/logout:"):
            st.session_state.authenticated = False# Atualiza o estado de autenticação
            st.rerun()# Reinicia a aplicação

if __name__ == "__main__":
    main()
