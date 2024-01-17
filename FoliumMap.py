import pandas as pd
import folium
import streamlit as st
from streamlit_folium import folium_static
from streamlit_js_eval import get_geolocation # api for getting location
import json
import codecs
import requests

import streamlit.components.v1 as components


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


    st.header("Map of TUL")
   # st.write(route_nodes)
    #st.write(routejson)
    if st.checkbox("Navigation"):
        location = get_geolocation()
        # location = get_user_location()

        if location:
            location_tuple = [location['coords']['latitude'], location['coords']['longitude']]
            folium.Marker(
                location = location_tuple, tooltip="TO TY"
            ).add_to(m)

    
    folium_static(m, width=700, height=600)

    situm()


def situm():
    components.html(
        """
        <iframe
            id="map-viewer-iframe"
            style="width:100%; height:600px"
            src="https://map-viewer.situm.com?apikey=9c3d00ce080f2f9d4f08f9ceba78193fbf4a8a8f15172141d8ce6bd95dafb4c4">
        </iframe>
        """,
        height = 600,
        width = 700,
    )

if __name__ == "__main__":
    main()