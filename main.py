import streamlit as st
from auth.login import show_login

def main():

    # Armazena o estado de autenticação
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        
    # Tela de login
    if not st.session_state.authenticated:
        show_login()

    else:
        
        st.title("Página Principal")
        st.write("Bem-vindo ao dashboard!")
       
        if st.button("Sair"):
            st.session_state.authenticated = False
            st.rerun()

if __name__ == "__main__":
    main()
