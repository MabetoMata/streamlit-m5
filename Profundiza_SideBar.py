import streamlit as st
st.title('Mi primera App con streamlite')
sidebar = st.sidebar
# Agregar la barra lateral
sidebar.title('Esta es la barra lateral')
sidebar.write('Aquí van los elementos de entrada')
st.header('Información sobre el conjunto de datos')
st.header('Descripción de datos')
st.write('''Este es in simple ejemplo de una app para predecir
¡Esta app predice mis datos''')
