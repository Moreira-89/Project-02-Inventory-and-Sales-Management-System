import streamlit as st#type: ignore
import pandas as pd#type: ignore
import os

st.set_page_config(layout="wide")

st.sidebar.image("assets/images/user_photo.png")

st.sidebar.write("Nome: Mauricio")
st.sidebar.write("Cargo: Administrador") 

st.sidebar.markdown("---")

st.sidebar.title("Navegação")
st.sidebar.page_link("pages/inv_overview.py", label="Estoque", icon=":material/inventory:")
st.sidebar.page_link("pages/order_overview.py", label="Pedidos", icon=":material/orders:")
st.sidebar.page_link("pages/sales_overview.py", label="Vendas", icon=":material/point_of_sale:")
st.sidebar.page_link("pages/reports_overview.py", label="Relatorios", icon=":material/lab_profile:")
st.sidebar.page_link("app.py", label="Voltar para inicio", icon=":material/home:")


st.title("Clientes")  

# ---> Importacao dos dados
file_path = "assets/data/data_clients.csv"

if os.path.exists(file_path):
    try:

        df = pd.read_csv(file_path, sep=",")

    except Exception as e:

        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
    
else:
    st.error(f"Arquivo '{file_path}' não encontrado!")
    
# ---> Campo para realizar a pesquisa
search_input = st.text_input(label="Pesquisar cliente (nome, e-mail, etc.)",
                        placeholder="Digite sua pesquisa")

# ---> Etapa de criacao da caixa para cadastro de clientes
@st.dialog("Formulário de Cadastro")
def register():
    
    client_name = st.text_input(label="Nome:",
                        placeholder="Insira o nome do cliente")
    
    client_phone = st.text_input(label="Telefone:",
                        placeholder="Insira o telefone para contato")
    client_email = st.text_input(label="E-mail:")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        client_log = st.text_input(label="Logradouro",
                            placeholder=" ")

        client_num = st.text_input(label="Nº:",
                            placeholder=" ")
        
    with col2:
        client_district = st.text_input(label="Bairro:",
                            placeholder=" ")
        client_city = st.text_input(label="Cidade:",
                            placeholder=" ")
        siglas_estados_brasileiros = [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
        "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
        "SP", "SE", "TO"]

        client_sigla = st.selectbox(
            "Estado:",
            options=siglas_estados_brasileiros,
            index=None,
            placeholder=" "
        )

    if st.button("Cadastrar"):

        if client_name and client_phone and client_email and client_log and client_num and client_district and client_city and client_sigla:

            # Simulacao de cadastro de produto
            st.session_state.products.append({

                "Nome": client_name,
                "Telefone": client_phone,
                "Email": client_email,
                "Logradouro": client_log,
                "Nº": client_num,
                "Bairro": client_district,
                "Cidade": client_city,
                "Estado": client_sigla
            })

            st.success(f"Cliente '{client_name}' cadastrado com sucesso!")
            st.rerun()  # Reinicia a aplicação para atualizar a tabela
            
        else:
            st.warning("Por favor, preencha todos os campos!")


if 'clients' not in st.session_state:
    st.session_state.clients = []

col1, col2 = st.columns([3, 1])

with col2:
    if st.button("Cadastrar cliente"):
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