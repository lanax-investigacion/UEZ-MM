import streamlit as st
import pandas as pd
import folium

# Load the data
data = pd.read_csv("mexico_data.csv")

# Create a map
m = folium.Map(location=[data['lat'].mean(), data['lon'].mean()], zoom_start=6)

# Add markers to the map
for _, row in data.iterrows():
    folium.CircleMarker(location=[row['lat'], row['lon']], radius=5, color='red', fill=True, fill_color='red').add_to(m)

# Show the map
st.write(m)

# Add a select box to filter the data
selected_column = st.selectbox("Select a column to filter by", data.columns)
value = st.text_input("Enter a filter value")

# Show only the data that matches the filter
filtered_data = data[data[selected_column] == value]
st.dataframe(filtered_data)
