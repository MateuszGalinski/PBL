import folium
import streamlit as st
from streamlit_folium import folium_static
import codecs

import streamlit.components.v1 as components

st.markdown("""
    <style>
        iframe {
            width: 100%;
            min-height: 400px;
            height: 100%:
        }
            
        [data-testid=stSidebarNavLink] span {
            color: #ffffff !important;
        }   
    </style>
""", unsafe_allow_html=True)

POLI_CENTRUM = [51.749444, 19.453957]
WEEIA = [51.752759, 19.453395]
IFE = [51.7551228632686, 19.45145719746805]
INDEKS = [51.751980, 19.452478]

def read_html(html_file_name):
    html_file = codecs.open(html_file_name, 'r')
    iframe = html_file.read()
    html_file.close()
    return iframe

def main():
    m = folium.Map(location = POLI_CENTRUM, zoom_start=16)

    weeia_logo = folium.features.CustomIcon('WEEIA.png', icon_size=(30,30))
    ife_logo = folium.features.CustomIcon('IFE.png', icon_size=(30,30))
    entrance_left_logo = folium.features.CustomIcon('entrance_left.png', icon_size=(10,10))
    entrance_bottom_logo = folium.features.CustomIcon('entrance_bottom.png', icon_size=(10,10))
    # piwo = folium.features.CustomIcon('piwo.png', icon_size=(30,30))
    # door = folium.features.CustomIcon('door.png', icon_size=(15,15))

    weeia_popup = folium.Popup(read_html("popupHTML.html"), max_width = 2500)
    ife_popup = folium.Popup(read_html("ifeHTML.html"), max_width=2500)

    folium.Marker(
        WEEIA, popup = weeia_popup, tooltip = "WEEIA faculty", icon = weeia_logo
    ).add_to(m)

    folium.Marker(
        IFE, popup = ife_popup, tooltip = "IFE faculty", icon = ife_logo
    ).add_to(m)

    folium.Marker(
        [51.752628, 19.452957], icon=entrance_left_logo, tooltip=None
    ).add_to(m)

    st.title("Map of TUL")
    
    folium_static(m, width=700, height=400)


if __name__ == "__main__":
    main()