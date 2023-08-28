# Import streamlit and pandas
import streamlit as st 
import pandas as pd 

# Print title
st.title('Streamlit con cache y 100')

# Set dataset url
DATA_URL = 'dataset.csv'

@st.cache
def load_data(nrows):
    # Create dataframe data, con n rows
    data = pd.read_csv(DATA_URL, nrows=nrows)
    # Return dataframe
    return data

# preint text loading
data_load_state = st.text('Loading data...')
# Call function load_data
data = load_data(101)
# Print text done
data_load_state.text("Done !")

# Print dataframe
st.dataframe(data)
