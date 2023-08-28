# Importar extenciones correspondientes
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

st.title('Reto # 5 Análsisi de trabajadores')
DATA_URL = ('Employees.csv')

# Ver la tabla usando cache con 500 elementos
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data  
data = load_data(500)

# Crear y poner título al sidebar
sidebar = st.sidebar
sidebar.title("Trabajadores sidebar")

# Si dan el checkbox se ve la tabla
if sidebar.checkbox('Mostrar la tabla'):
    st.subheader('Primeros 500 trabajadores usando cache')
    st.write(data)

# Buscar Employee_ID
buscar = sidebar.text_input('Escribe el # de emplaeado')
@st.cache
def load_data_byname(buscar):
    filtered_data_byrange = data[data['Employee_ID'].str.upper().str.contains(buscar.upper())]
    return filtered_data_byrange
if sidebar.button('Buscar por ID'):
    filterbyname = load_data_byname(buscar)
    st.subheader('Tabla de coincidencias por número de trabajador')
    st.dataframe(filterbyname)


# Filtrar por nivel educativo
@st.cache
def filter_data_by_NE(NE):
    filtered_data_NE = data[data['Education_Level'] == NE]
    return filtered_data_NE

selected_NE = st.sidebar.selectbox("Seleccionar nievel educativo", data['Education_Level'].unique())
btnFilterbyNE= st.sidebar.button('Filtrar nivel educativo')

if (btnFilterbyNE):
   filterbyNE = filter_data_by_NE(selected_NE)
   count_row = filterbyNE.shape[0]  # Gives number of rows
   st.write(f"Total de trabajadores en el nivel {selected_NE} es: {count_row}")
   st.dataframe(filterbyNE)


# Filtrar por ciudad
@st.cache
def filter_data_by_CD(CD):
    filtered_data_CD = data[data['Hometown'] == CD]
    return filtered_data_CD

selected_CD = st.sidebar.selectbox("Seleccionar la ciduad", data['Hometown'].unique())
btnFilterbyCD= st.sidebar.button('Filtrar por ciudad')

if (btnFilterbyCD):
   filterbyCD = filter_data_by_CD(selected_CD)
   count_row = filterbyCD.shape[0]  # Gives number of rows
   st.write(f"Total de trabajadores en la ciudad {selected_CD} es: {count_row}")
   st.dataframe(filterbyCD)


# Filtrar por Unit
@st.cache
def filter_data_by_Unit(Unit):
    filtered_data_Unit = data[data['Unit'] == Unit]
    return filtered_data_Unit

selected_Unit = st.sidebar.selectbox("Seleccionar Unit", data['Unit'].unique())
btnFilterbyUnit= st.sidebar.button('Filtrar Unit ')

if (btnFilterbyUnit):
   filterbyUnit = filter_data_by_Unit(selected_Unit)
   count_row = filterbyUnit.shape[0]  # Gives number of rows
   st.write(f"Total de trabajadores en la unidad {selected_Unit} es: {count_row}")
   st.dataframe(filterbyUnit)

# Seaborn histograma
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.histplot(x=data['Age'], bins=[19,24,29,34,39,44,49,54,59,64,69])
st.pyplot()
# Seaborn gráfico de frecuencias
sns.barplot(x=data.index, y=data['Unit'])
st.pyplot()
st.subheader('El rubro más grande es Security')
# Analizar deserción por ciudad
sns.boxplot(x=data['Hometown'],y=data["Attrition_rate"])
st.pyplot()
st.subheader('La mayor deserción la tiene Franklin y la menor Lebanon')
# Analizar edad y deserción
sns.lineplot(x=data['Age'],y=data["Attrition_rate"])
st.pyplot()
st.subheader('Se ve una ligera disminución conforme avanza la edad')
# Gráfica de correlación
sns.scatterplot(x=data['Time_of_service'],y=data["Attrition_rate"], hue = data['Age'])
st.pyplot()
st.subheader('Se ve una ligera disminución conforme avanza el tiempo de servicio y la edad')