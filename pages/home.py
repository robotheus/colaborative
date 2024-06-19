import mapa as mp
import streamlit as st
import controllers.userController as userController
import os 

from streamlit_cookies_manager import EncryptedCookieManager

mp.config_page("Mapa")

cookies = EncryptedCookieManager(
    password=os.environ.get("COOKIES_PASSWORD", "mapacpf123") 
)

if not cookies.ready():
    st.stop()

def init_home():

    selected_cat = mp.categories()
    mp.init_map_interactive(-21.125877931976074,-44.26214575767518, selected_cat)

def remove_cookie():
    cookies.__delitem__('cpf')
    cookies.save()
        
if 'cpf' in st.session_state:
    userdata = userController.read(st.session_state['cpf'])
    
    cookies['cpf'] = str(userdata['cpf'])
    cookies.save()
else:
    cpf = cookies.get('cpf')
    print(cpf)
    
    if cpf:
        userdata = userController.read(str(cpf))
    else:
        st.switch_page("pages/login.py")

st.sidebar.title("Olá, " + str(userdata['nome']))

selec_cat = mp.categories()
mp.init_map_interactive(-21.125877931976074,-44.26214575767518, selec_cat)

st.sidebar.button("Sair", on_click=remove_cookie)


