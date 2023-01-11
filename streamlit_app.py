#Importaciones
import streamlit as st
import pandas as pd
import numpy as np

#Texto
st.title ("Unidades Economicas de la Zona Metropolitana de Monterrey [Noviembre/2022]")
st.markdown("El objetivo es analizar las UE de la ZMM en un mapa")

#Grafica
df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df
