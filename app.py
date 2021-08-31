import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.title('Simple App')
    col1, col2 = st.columns(2)
    with col1:
        lat = st.number_input('Latitude', value=40.74)
    with col2:
        long = st.number_input('Longitude', value=-73.99)
    n_points = st.slider('Number of points', 1, 1000, 100)
    df = pd.DataFrame(
        np.random.randn(n_points, 2) / [100, 100] + [lat, long],
        columns=['lat', 'lon'])
    st.map(df)
    st.caption('This is just a random distribution of points at the latitude and longitude you chose. Pretty fun!')


if __name__ == '__main__':
    app()
