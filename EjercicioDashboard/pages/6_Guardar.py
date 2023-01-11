import streamlit as st
import pandas as pd
from datos_get import Datos_get
from pantalla import Pantalla

from pasajero import Pasajero


def grabarDatos(pasajero):
    Datos_get().grabar_excel(pasajero)
    df=Datos_get().read_datos()
    if "df_datos" not in st.session_state:
        st.session_state["df_datos"] = ""
    st.session_state["df_datos"]= df
    return df




    
pantalla=Pantalla()
pantalla=st.session_state["pantalla"]

print (pantalla.getAnalisis())
df=st.session_state["df_datos"]

    

st.write(pantalla.getGuardar())
if(pantalla.getGuardar()==1):
    pasajero=st.session_state["pasajero"]
    
   
    if st.button("Guadar Estudio")& pantalla.getGuardar()==1:
        df=grabarDatos(pasajero)
        st.write("Se Guardado corectamente")        
        pantalla.pulsaIniciar() 
        st.write(pantalla.getGuardar())
        st.session_state["pantalla"] = pantalla
        st.write(pantalla)
    elif pantalla.getGuardar()==2:
        st.write("Se Guardado corectamente el dato")
        st.write(df)
        
    
  
   

elif pantalla.getGuardar()==0:
    st.write("Error en la pantalla")

elif pantalla.getGuardar()==2:
    st.write("Se Guardado corectamente")
    st.write(df)



