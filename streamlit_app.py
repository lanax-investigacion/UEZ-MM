import streamlit as st
import pandas as pd
import numpy as np

#Texto
st.title ("Unidades Economicas de la Zona Metropolitana de Monterrey [Noviembre/2022]")
st.markdown("El objetivo es analizar las UE de la ZMM en un mapa")

#Read the CSV
data = pd.read_csv("UE_ZMM_LAT_LON_11_2022.csv")

st.write(data)
st.dataframe(data)
st.map(data)
