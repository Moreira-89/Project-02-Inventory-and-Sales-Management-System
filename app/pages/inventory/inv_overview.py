import streamlit as st
import pandas as pd
import os


def show_inventory():

    st.title("Estoque")

# ---> Importacao dos dados
    file_path = "assets/data/data_inventory.csv"

    if os.path.exists(file_path):
        try:
    
            df = pd.read_csv(file_path, sep=";")

        except Exception as e:

            st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
            return
        
    else:
        st.error(f"Arquivo '{file_path}' não encontrado!")
        return

# ---> Campo para realizar a pesquisa
    search_input = st.text_input(label="Pesquisar produto (nome, código, etc.)",
                            placeholder="Digite sua pesquisa")

# ---> Etapa de criacao da caixa para cadastro do produto
    @st.dialog("Formulário de Cadastro")
    def register():

        product_name = st.text_input(label="Nome do produto:",
                            placeholder="Insira o nome do produto")
        
        quantity_product = st.text_input(label="Quantiadade do produto:",
                            placeholder="Insira a quantidade do produto")

        product_value = st.text_input(label="Valor do produto:",
                            placeholder="Insira o valor do produto")

        product_code = st.text_input(label="Codigo do produto:",
                            placeholder="Insira o codigo do produto")

        if st.button("Cadastrar"):

            if product_name and quantity_product and product_value and product_code:

                # Simulacao de cadastro de produto
                st.session_state.products.append({

                    "Nome": product_name,
                    "Quantidade": quantity_product,
                    "Valor": product_value,
                    "Código": product_code
                })

                st.success(f"Produto '{product_name}' cadastrado com sucesso!")
                st.rerun()  # Reinicia a aplicação para atualizar a tabela
                
            else:
                st.warning("Por favor, preencha todos os campos!")
    

    if 'products' not in st.session_state:
        st.session_state.products = []

    col1, col2 = st.columns([3, 1])

    with col2:
        if st.button("Cadastrar produto"):
            register()

# ---> Realizacao do filtro de pesquisa

    with col1:
        if st.button("Pesquisar"):

            if not search_input:
                st.warning("Por favor, insira um termo na pesquisa!")

            # Realiza a filtragem dos dados com tratamento de erro
            else:
                try:
                    data_filtered = df[df.apply(lambda row: row.astype(str).str.contains(search_input, case=False).any(), axis=1)]
                    st.table(data_filtered)

                except Exception as e:
                    st.error(f"Ocorreu um erro durante a filtragem: {e}")

        # Exibi a tabela mesmo sem o filtro
        else:
            st.table(df)