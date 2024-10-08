import streamlit as st
st.set_page_config(layout="centered")

def check_credentials(input_username, input_password):

    correct_username = "admin"
    correct_password = "123"


    return input_username == correct_username and input_password == correct_password


def show_login():

    # Tela de Login
    if not st.session_state.authenticated:

        col1, col2 = st.columns(2)

        with col1:
            st.image("assets\images\img_login.png")

        with col2:
            st.title("Bem Vindo!")
            username = st.text_input("Nome de Usuário", "")
            password = st.text_input("Senha", "", type="password")

            if st.button("Login"):

                if check_credentials(username, password):

                    st.session_state.authenticated = True
                    st.success("Login bem-sucedido!")
                    st.rerun()

                else:
                    st.error("Nome de usuário ou senha incorretos.")