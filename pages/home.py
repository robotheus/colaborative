import streamlit as st
import folium
from streamlit_folium import st_folium
import controllers.coordsController as coordsController

def create_map():
    m = folium.Map(location=map_center, zoom_start=16.5, width="100%", height=800)
    if st.session_state.clicked_coords:
        folium.Marker(location=st.session_state.clicked_coords, popup="teste").add_to(m)
    return m

st.set_page_config(page_title="Mapa Interativo", layout="wide")

cat = ["cat1", "cat2", "cat3", "cat4", "cat5", "cat6", "cat7"]
selected_cat = st.sidebar.radio("Selecione uma categoria:", cat)

map_center = [-21.1258328, -44.2633711]

if 'clicked_coords' not in st.session_state:
    st.session_state.clicked_coords = None

m = create_map()
clicked_location = st_folium(m, width="100%", height=800)

savebtn = st.sidebar.button("Salvar coordenadas")

if clicked_location and clicked_location['last_clicked']:
    aux = clicked_location['last_clicked']
    lat = aux['lat']
    lng = aux['lng']

    st.session_state.clicked_coords = [lat, lng]

    m = create_map()
    st_folium(m, width="100%", height=800)

    st.success(f'Coordenadas {lat} e {lng} selecionadas')

if savebtn and st.session_state.clicked_coords:
    lat, lng = st.session_state.clicked_coords
    
    coordsController.create(selected_cat, lat, lng)
    
    st.success("Coordenadas salvas no banco.")
    
    st.session_state.clicked_coords = None
    
    # aqui em vez de criar o mapa vazio novamente vamos tentar criar o mapa com a nova marcação salva
    # para isso vai ser preciso criar um read para o coordController
    m = create_map()
    st_folium(m, width="100%", height=800)
