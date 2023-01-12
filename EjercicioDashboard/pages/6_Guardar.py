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


df=st.session_state["df_datos"]

    

st.markdown(" Almacenarán los datos que nos den los usuarios, para ir enriqueciendo nuestros datos.")

st.markdown("")
st.markdown("")
st.markdown("")
if(pantalla.getGuardar()==1):
    pasajero=st.session_state["pasajero"]
    
   
    if st.button("Guadar Estudio")& pantalla.getGuardar()==1:
        df=grabarDatos(pasajero)
        st.write("Se Guardado corectamente")        
        pantalla.pulsaIniciar() 
     
        st.session_state["pantalla"] = pantalla
        st.dataframe(df)
        
    elif pantalla.getGuardar()==2:
        st.write("Se Guardado corectamente el dato")
       
        st.dataframe(df)
        
    
  
   

elif pantalla.getGuardar()==0:
    st.write("Error en la pantalla .Debe ejecurtase antes las  pantallas anteriores")

elif pantalla.getGuardar()==2:
    st.write("Se Guardado corectamente")
    st.dataframe(df)



