import streamlit as st
import pandas as pd

names_link = 'dataset.csv'
# Read CSV
names_data = pd.read_csv(names_link)

# Create title
st.title ('Streamlit and pandas')

# Print dataframe
st.dataframe(names_data)