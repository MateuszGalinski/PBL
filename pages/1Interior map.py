import streamlit as st
import streamlit.components.v1 as components

def IFE():
    components.html(
        """
        <iframe
            id="map-viewer-iframe"
            style="width:100%; height:600px"
            src="https://map-viewer.situm.com?apikey=9c3d00ce080f2f9d4f08f9ceba78193fbf4a8a8f15172141d8ce6bd95dafb4c4&lng=en-GB&buildingid=15332&floorid=49421">
        </iframe>
        """,
        height=610,
    )

def LC():
    components.html(
        """
        <iframe
            id="map-viewer-iframe"
            style="width:100%; height:600px"
            src="https://map-viewer.situm.com?apikey=9c3d00ce080f2f9d4f08f9ceba78193fbf4a8a8f15172141d8ce6bd95dafb4c4&lng=en-GB&buildingid=15331&floorid=49418">
        </iframe>
        """,
        height=610,
    )
# https://map-viewer.situm.com/?apikey=9c3d00ce080f2f9d4f08f9ceba78193fbf4a8a8f15172141d8ce6bd95dafb4c4&lng=en-GB&buildingid=15332&floorid=49421
# https://map-viewer.situm.com/?apikey=9c3d00ce080f2f9d4f08f9ceba78193fbf4a8a8f15172141d8ce6bd95dafb4c4&lng=en-GB&buildingid=15331&floorid=49418
st.markdown("""
        <style>
            [data-testid=stSidebarNavLink] span {
                color: #ffffff !important;
            }
            .block-container {
                padding-top: 1rem;
            }
        </style>
        """, unsafe_allow_html=True)

selected_building = st.selectbox(
    label="Building selector:",
    options = ("IFE", "Language center"),
    index = None,
    placeholder ="Select building",
    label_visibility="hidden"
)

if selected_building == "IFE":
    IFE()
elif selected_building == "Language center":
    LC()
