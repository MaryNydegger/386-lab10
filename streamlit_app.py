import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.sidebar.title('Interactive Controls')
user_input = st.sidebar.slider('Select a number:', 1, 10, 5)


data = np.random.randn(100, user_input)

st.write('### Random Data Generated:')
st.write(pd.DataFrame(data))

st.write('### Line Chart:')
plt.figure(figsize=(8, 6))
plt.plot(np.mean(data, axis=0))
st.pyplot()

st.write('This app generates random data based on user input and displays it in a DataFrame. It also plots a line chart of the mean of the generated data.')
