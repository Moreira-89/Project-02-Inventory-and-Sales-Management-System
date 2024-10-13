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
        
    # Verifica se o usuário está autenticado
    if not st.session_state.authenticated:
        show_login()# Exibe a tela de login

    else: 

        st.sidebar.title("Aonde vamos?")# Título da barra lateral

        st.sidebar.markdown(" ")

        page = "Inicio" # Página inicial padrão

        # Botões de navegação na barra lateral
        if st.sidebar.button("Inicio", icon=":material/home:"):
            page = "Inicio"
        
        if st.sidebar.button("Clientes", icon=":material/people:"):
            page = "Clientes"
        
        if st.sidebar.button("Estoque", icon=":material/inventory:"):
            page = "Estoque"

        if st.sidebar.button("Relatórios", icon=":material/assessment:"):
            page = "Relatórios"

        # Navegação baseada na página selecionada
        match page:

            case "Inicio":
                show_dash()# Exibe o dashboard
            
            case "Clientes":
                show_clients()# Exibe a pagina de cliente

            case "Estoque":
                show_inventory()# Exibe a pagina do estoque
            
            case "Relatórios":
                show_reports()# Exibe a pagina de relatório
        
        # Botão de logout
        if st.sidebar.button("Sair", icon=":material/logout:"):
            st.session_state.authenticated = False# Atualiza o estado de autenticação
            st.rerun()# Reinicia a aplicação

if __name__ == "__main__":
    main()
