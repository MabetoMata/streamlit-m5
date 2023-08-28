import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Netflix práctica')
DATA_URL = ('movies.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data  
data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text('Done ! using cache...')


# crear title de la app web
sidebar = st.sidebar
sidebar.title("Películas recuperadas")

if sidebar.checkbox('Mostrar todos los films'):
    st.subheader('Todos los filmes')
    st.write(data)

# Poner 
buscar = sidebar.text_input('Escribe le nombre del filme')
@st.cache
def load_data_byname(buscar):
    filtered_data_byrange = data[data['name'].str.upper().str.contains(buscar.upper())]
    return filtered_data_byrange

if sidebar.button('Buscar'):
    # create filterbyname dataframe
    filterbyname = load_data_byname(buscar)
    st.dataframe(filterbyname)

# Buscar director
buscar_director = sidebar.selectbox('Selecciona el Director',data['director'].unique())
