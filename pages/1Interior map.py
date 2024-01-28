import streamlit as st
import streamlit.components.v1 as components

def situm():
    components.html(
        """
        <iframe
            id="map-viewer-iframe"
            style="width:100%; height:600px"
            src="https://map-viewer.situm.com?apikey=9c3d00ce080f2f9d4f08f9ceba78193fbf4a8a8f15172141d8ce6bd95dafb4c4">
        </iframe>
        """,
        height=610,
    )

st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
            }
        </style>
        """, unsafe_allow_html=True)

situm()