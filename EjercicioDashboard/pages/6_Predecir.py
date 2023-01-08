import streamlit as st
import pandas as pd
from datos_get import Datos_get
from pantalla import Pantalla

from pasajero import Pasajero


def grabarDatos(pasajero):
    Datos_get().grabar_excel(pasajero)
pantalla=Pantalla()
pantalla=st.session_state["pantalla"]
print (pantalla.getAnalisis())
if(pantalla.getAnalisis()==1):
    pasajero=st.session_state["pasajero"]
    if st.button("Gruadar Estudio"):
        grabarDatos(pasajero)
   
   

else:
    st.write("Error en la pantalla")


st.session_state["pantalla"] = pantalla

