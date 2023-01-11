import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

#Texto
st.title ("Unidades Economicas de la Zona Metropolitana de Monterrey [Noviembre/2022]")
st.markdown("El objetivo es analizar las UE de la ZMM en un mapa")

#Read the CSV
dm = pd.read_csv("UE_ZMM_LAT_LON_2022_v2.csv")

#st.map(data)


st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=25.7293,
        longitude=-100.3622,
        zoom=10,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=dm,
           get_position='[lon, lat]',
           radius=10,
           elevation_scale=5,
           elevation_range=[0, 100],
           pickable=True,
           extruded=True,
        ),
    ],
))
