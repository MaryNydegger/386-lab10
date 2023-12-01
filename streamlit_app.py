import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a Streamlit app
st.title('Dynamic Graph based on User Input')

# Create interactive elements
number = st.slider('Select a number', 1, 10)
option = st.selectbox('Select an option', ['A', 'B', 'C'])

# Generate data based on user input
data = pd.DataFrame({
    'x': np.arange(1, number + 1),
    'y': np.random.randint(1, 100, size=number)
})

# Display the data
st.write(f"Displaying data for option {option}:")
st.write(data)

# Create a dynamic graph
plt.figure(figsize=(8, 6))
plt.bar(data['x'], data['y'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Dynamic Bar Chart')
st.pyplot()

# Save the Streamlit app
st.set_option('deprecation.showPyplotGlobalUse', False)
