import streamlit as st
import controllers.userController as userController
import models.user as user
from pymongo.errors import DuplicateKeyError
import bcrypt
import mapa as mapa

mapa.config_page("Cadastro")

def cadastro():
    
    name          = st.sidebar.text_input(label = "Nome")
    cpf           = st.sidebar.text_input(label = "CPF")
    password      = st.sidebar.text_input(label = "Senha", type = "password")
    password_c    = st.sidebar.text_input(label = "Confirmação de senha", type = "password")

    submit = st.sidebar.button("Cadastrar")

    if submit:
        if password != password_c:
            st.sidebar.error("As senhas não coincidem. Por favor, digite novamente.")
            return
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        novo_usuario = user.Usuario(name=name, cpf=cpf, password=hashed)
        
        try:
            userController.create(novo_usuario)
            st.sidebar.success("Cadastro feito com sucesso.")
        except DuplicateKeyError:
            st.sidebar.error("CPF já cadastrado.")

st.sidebar.page_link("pages/cadastro.py", label="Cadastro")
st.sidebar.page_link("pages/login.py", label="Entrar")

mapa.init_map_visualization(-21.125877931976074,-44.26214575767518)

cadastro()