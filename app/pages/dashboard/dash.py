import streamlit as st

def show_dash():

    # Armazena o estado de autenticação
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    st.title("Página Principal")
    st.write("Bem-vindo ao dashboard!")
    
    with st.sidebar:

        st.button("Clientes")
        st.button("Estoque")
        st.button("Pedidos")
        st.button("Relatorios")

        if st.button("Sair"):
            st.success("Até a próxima!")
            st.session_state.authenticated = False
            st.rerun()