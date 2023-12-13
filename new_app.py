import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
In [2]:
st.title('Dynamic Graph Lab 10')

number = st.slider('Select a number ', 1, 10)
option = st.selectbox('Select an Option ', ['A', 'B', 'C'])

