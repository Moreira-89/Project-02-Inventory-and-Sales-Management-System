import streamlit as st

def update_search():
    st.session_state['search_term'] = st.session_state['search_input']
