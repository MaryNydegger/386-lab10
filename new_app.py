import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

st.title('Dynamic Graph Lab 10')

number = st.slider('Select a number ', 1, 10)
option = st.selectbox('Select an Option ', ['A', 'B', 'C'])

data = pd.DataFrame({
    'x': np.arange(1, number + 1),
    'y': np.random.randint(1, 100, size = number)
})

st.write(f'Displaying data for option {option}:')
st.write(data)

plt.figure(figsize = (8,6))
plt.bar(data['x'], data['y'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Dynamic Bar Chart')
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)

