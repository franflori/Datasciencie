import streamlit as st
from datos_get import Datos_get


def pintarDatos():
    st.title("Gráfica con Streamlit .............s")
    df=Datos_get().read_datos()
    datos_orginales=df
    # head()
    st.write("Vamos a imprimir los primeros 5 valores del dataset")
    st.write(df.head())

    # tail()
    st.write("Vamos a imprimir los últimos 5 valores del dataset")
    st.write(df.tail())


# wide mode: modo apaisado:
st.set_page_config(layout="wide")

st.sidebar.title("1. Data")

# multiselect: opcion multiple
opciones = st.sidebar.multiselect("Datos de cabecera:", 
                          ["Pclass", "Name", "Sex", "Age","SibSp","Parch","Ticket"
                          "Fare","Cabin","Embarke"])

st.write("Has elegido los siguientes frameworks: ", opciones)


# checkbox
check = st.sidebar.checkbox("Quieres que se cage los datos")

if not check:
    st.write("Buena elección")
else:
    pintarDatos()

   
  


