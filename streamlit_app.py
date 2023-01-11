import streamlit as st
import pandas as pd

#Read the CSV
data = pd.read_csv("UE_ZMM_LAT_LON_11_2022.csv")

#Display the dataframe
st.dataframe(data)
