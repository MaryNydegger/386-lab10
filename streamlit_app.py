import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Lab 10- Streamlit')
Apple = pd.read_csv('AppleData.csv')

prices = st.sidebar.slider('Select Price: ', min_value = 0.0, max_value = 20.0, value = (0.0, 20.0))
genres = Apple['prime_genre'].unique()
genre = st.sidebar.multiselect('Select Genre: ', genres, default = genres)

apple_filtered = Apple[(Apple['prime_genre'].isin(genre)) & (Apple['price'] >= prices[0]) & (Apple['price'] <= prices[1])]

if st.checkbox('View Data'):
    st.subheader('raw Data')
    st.write(apple_filtered)

st.subheader('Top 5 Apps')
top_five = apple_filtered.sort_values(by = 'rating_count_tot', ascending = False).head(5)
st.bar_chart(top_five.set_index('track_name')['rating_count_tot'], use_container_width=True)

st.write('This app generates data from the Apple Store for the top 5 apps and their ratings')
