import streamlit as st
import streamlit.components.v1 as components

def situm():
    components.html(
        """
        <iframe
            id="map-viewer-iframe"
            style="width:100%; height:600px;"
            src="https://map-viewer.situm.com?apikey=9c3d00ce080f2f9d4f08f9ceba78193fbf4a8a8f15172141d8ce6bd95dafb4c4">
        </iframe>
        """,
        height=600,
    )

st.markdown(
    """
    <style>
    .st-emotion-cache-sy3zga {
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        display: table-cell;
        color: black;
    }
    </style>    
    """, 
    unsafe_allow_html=True)

selected_building = st.selectbox(
    label="Building selector:",
    options = ("IFE", "Language center"),
    index = None,
    placeholder ="Select building",
    label_visibility="hidden"
)

if selected_building == "IFE":
    situm()
elif selected_building == "Language center":
    st.write("CJ")