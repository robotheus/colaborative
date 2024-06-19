import streamlit as st
import mapa as mapa

mapa.config_page("Site")

st.sidebar.page_link("pages/cadastro.py", label="Cadastro")
st.sidebar.page_link("pages/login.py", label="Entrar")

mapa.init_map_visualization(-21.125877931976074,-44.26214575767518)
