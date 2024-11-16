import streamlit as st
from pages.login import show_login

def main():

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # Verifica se o usuário está autenticado
    if st.session_state.authenticated:

        st.title("Página Principal")
        st.write("Bem-vindo ao dashboard!") 

        st.sidebar.title("Navegação")
        st.sidebar.page_link("pages/clients_overview.py", label="Clientes", icon=":material/person:")
        st.sidebar.page_link("pages/inv_overview.py", label="Estoque", icon=":material/inventory:")
        st.sidebar.page_link("pages/order_overview.py", label="Pedidos", icon=":material/orders:")
        st.sidebar.page_link("pages/reports_overview.py", label="Relatorios", icon=":material/lab_profile:")
        
        st.sidebar.markdown("---")
        
        if st.sidebar.button("Sair", icon=":material/logout:"):
            st.session_state.authenticated = False
            st.rerun()
    else:
        show_login()

if __name__ == "__main__":
    main()