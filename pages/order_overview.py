import streamlit as st #type: ignore

st.set_page_config(layout="wide")

st.sidebar.title("Navegação")
st.sidebar.page_link("pages/clients_overview.py", label="Clientes", icon=":material/person:")
st.sidebar.page_link("pages/inv_overview.py", label="Estoque", icon=":material/inventory:")
st.sidebar.page_link("pages/reports_overview.py", label="Relatorios", icon=":material/lab_profile:")
st.sidebar.page_link("app.py", label="Voltar para inicio", icon=":material/home:")


st.title("Pedidos")
