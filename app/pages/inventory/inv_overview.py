import streamlit as st
import pandas as pd


def show_inventory():

    st.title("Estoque")

    # Importacao dos dados
    try:
        df = pd.read_csv(r"assets\data\data_inventory.csv", sep=";")
    except FileNotFoundError:
        st.error("Impossivel encontrar os dados!")


    # Campo para realizar a pesquisa
    search_input = st.text_input(label="Pesquisar produto (nome, código, etc.)",
                            placeholder="Digite sua pesquisa")
    
    
    if st.button("Pesquisar"):

        if not search_input:
            st.warning("Por favor, insira um termo na pesquisa!")

        # Realiza a filtragem dos dados com tratamento de erro
        else:
            try:
                df_filtered = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
                st.table(df_filtered)

            except Exception as e:
                st.error(f"Ocorreu um erro durante a filtragem: {e}")

    # Exibi a tabela mesmo sem o filtro
    else:
        st.table(df)