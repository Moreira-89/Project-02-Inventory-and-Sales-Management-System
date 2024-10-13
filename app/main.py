import streamlit as st
from pages.authentication.login import show_login
from pages.dashboard.dash_overview import show_dash
from pages.reports.reports_overview import show_reports
from pages.customers.clients_overview import show_clients
from pages.inventory.inv_overview import show_inventory

def main():

    # Armazena o estado de autenticação
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        
    # Tela de login
    if not st.session_state.authenticated:
        show_login()

    else: 

        st.sidebar.title("Aonde vamos?")

        st.sidebar.markdown(" ")

        page = "Inicio"

        if st.sidebar.button("Inicio"):
            page = "Inicio"
        
        if st.sidebar.button("Clientes"):
            page = "Clientes"
        
        if st.sidebar.button("Estoque"):
            page = "Estoque"

        if st.sidebar.button("Relatórios"):
            page = "Relatórios"

        match page:

            case "Inicio":
                show_dash()
            
            case "Clientes":
                show_clients()

            case "Estoque":
                show_inventory()
            
            case "Relatórios":
                show_reports()
        
        if st.sidebar.button("Sair"):
            st.session_state.authenticated = False
            st.rerun()

if __name__ == "__main__":
    main()
