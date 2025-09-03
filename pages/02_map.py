import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'lat': [37.50, 37.52, 37.48],
    'lon': [126.91, 126.89, 126.93]
})
st.map(df)