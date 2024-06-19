import streamlit as st
import folium
from streamlit_folium import st_folium
import controllers.coordsController as coordsController

ICON_COLOR_DICT = {
    "Categoria 1": {"icon": "glyphicon glyphicon-ok", "color": "red"},
    "Categoria 2": {"icon": "glyphicon glyphicon-remove", "color": "blue"},
    "Categoria 3": {"icon": "glyphicon glyphicon-star", "color": "green"},
    "Categoria 4": {"icon": "glyphicon glyphicon-heart", "color": "purple"},
    "Categoria 5": {"icon": "glyphicon glyphicon-home", "color": "orange"},
    "Categoria 6": {"icon": "glyphicon glyphicon-flag", "color": "darkred"},
    "Categoria 7": {"icon": "glyphicon glyphicon-map-marker", "color": "cadetblue"}
}

def create_map(lat, lng, selected_cat=None, clicked_coords=None, markers=None):
    m = folium.Map(location=[lat, lng], zoom_start=16.5)

    if clicked_coords and selected_cat:
        folium.Marker(
            location=clicked_coords,
            popup=selected_cat,
            icon=folium.Icon(icon=ICON_COLOR_DICT[selected_cat]['icon'], color=ICON_COLOR_DICT[selected_cat]['color'])
        ).add_to(m)

    if markers:
        for marker in markers:
            cat = marker['cat']
            folium.Marker(
                location=[marker['lat'], marker['lng']],
                popup=cat,
                icon=folium.Icon(icon=ICON_COLOR_DICT[cat]['icon'], color=ICON_COLOR_DICT[cat]['color'])
            ).add_to(m)

    return m

def config_page(title: str):
    st.set_page_config(
        page_title=title,
        layout="wide"
    )
    st.markdown("""
        <style>
            .main {
                padding: 0;
                overflow: hidden;
                height: 100vh;
            }
            #root > div:nth-child(1) > div > div > div > div > section > div {
                padding: 0;
            }
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

def categories():
    cat = ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7"]
    selected_cat = st.sidebar.radio("Selecione uma categoria:", cat)
    return selected_cat

def init_map_interactive(lat: float, lng: float, selected_cat: str):
    map_center = [lat, lng]

    if 'clicked_coords' not in st.session_state:
        st.session_state.clicked_coords = None

    initial_center = map_center if st.session_state.clicked_coords is None else st.session_state.clicked_coords
    markers = coordsController.read()

    m = create_map(initial_center[0], initial_center[1], selected_cat, st.session_state.clicked_coords, markers)
    clicked_location = st_folium(m, width="100%", height=1000)

    if clicked_location and clicked_location['last_clicked']:
        aux = clicked_location['last_clicked']
        lat, lng = aux['lat'], aux['lng']
        st.session_state.clicked_coords = [lat, lng]

        markers = coordsController.read()
        m = create_map(lat, lng, selected_cat, st.session_state.clicked_coords, markers)
        st_folium(m, width="100%", height=1000)

    if st.sidebar.button("Salvar coordenadas"):
        if st.session_state.clicked_coords:
            lat, lng = st.session_state.clicked_coords
            coordsController.create(selected_cat, lat, lng)

            markers = coordsController.read()
            m = create_map(lat, lng, selected_cat, st.session_state.clicked_coords, markers)
            st_folium(m, width="100%", height=1000)
        else:
            st.sidebar.error("Selecione um local no mapa.")

def init_map_visualization(lat: float, lng: float):
    markers = coordsController.read()
    m = create_map(lat, lng, markers=markers)
    st_folium(m, width="100%", height=1000)

if __name__ == "__main__":
    config_page("Mapa Interativo")
    selected_cat = categories()
    init_map_interactive(-23.55052, -46.633308, selected_cat)
