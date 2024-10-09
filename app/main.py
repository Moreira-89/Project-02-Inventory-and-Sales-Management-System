import streamlit as st
from pages.authentication.login import show_login
from pages.dashboard.dash import show_dash

def main():

    # Armazena o estado de autenticação
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        
    # Tela de login
    if not st.session_state.authenticated:
        show_login()

    else:
        show_dash()

if __name__ == "__main__":
    main()
