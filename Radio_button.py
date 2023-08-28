import streamlit as st
st.title('Usando el radio button')
selected_class = st.radio("Seleccione una clase", titanic_data['class'].unique())
st.write("Clase seleccionada:", selected_class)

