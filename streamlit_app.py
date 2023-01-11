import streamlit as st
import pandas as pd

# Allow the user to upload the file
file = st.file_uploader("UE_ZMM_LAT_LON_11_2022.csv")

#Read the CSV
data = pd.read_csv(file)

#Display the dataframe
st.dataframe(data)
