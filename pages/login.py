import streamlit as st
import controllers.userController as userController
import bcrypt
import mapa as mapa

mapa.config_page("Entrar")

def login():
    cpf           = st.sidebar.text_input(label = "CPF")
    password      = st.sidebar.text_input(label = "Senha", type = "password")
    
    userdata = userController.read(cpf)
    login = st.sidebar.button("Entrar")

    if login:
        if not userdata:
            st.sidebar.error("CPF não cadastrado.")
            
            return

        hashed_password_from_db = userdata["senha"]
        
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password_from_db):
            st.session_state['cpf'] = userdata['cpf']
            st.switch_page("pages/home.py")
        else:
            st.sidebar.error("Senha incorreta.")

st.sidebar.page_link("pages/cadastro.py", label="Cadastro")
st.sidebar.page_link("pages/login.py", label="Entrar")

mapa.init_map_visualization(-21.125877931976074,-44.26214575767518)

login()