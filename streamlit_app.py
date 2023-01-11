#Importaciones
import streamlit as st
import pandas as pd
import numpy as np

#Texto
st.title ("Unidades Economicas de la Zona Metropolitana de Monterrey [Noviembre/2022]")
st.markdown("El objetivo es analizar las UE de la ZMM en un mapa")

#Mapa
df = pd.DataFrame(np.random.randn(900, 2) / [10, 10] + [25.72939591, -100.3622204],columns=['lat', 'lon'])
st.map(df)
