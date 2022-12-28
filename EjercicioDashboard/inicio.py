from contextlib import nullcontext
import streamlit as st
from datos_get import Datos_get
from pasajero import Pasajero
from entrenamiento import Entrenamiento
from preprocesar import Preprocesar
from pantalla import Pantalla
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pantalla=  Pantalla()
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
 

with tab2:
   st.header("A dog")
   

with tab3:
   st.header("An owl")
print (pantalla.cargarDatos,pantalla.preprocesar)

if (pantalla.cargarDatos): 
    boton = st.sidebar.button("boton1")
    if boton:
        print(boton)
        pantalla.pulsaCargaDatos()
      
    if (pantalla.preprocesar): 
        boton2 = st.sidebar.button("boton2")
        if boton2:
            print(boton2)
          

    if (pantalla.entrenar): 
        boton3 = st.sidebar.button("boton3")
        if boton3:
            print(boton3)
            pantalla.pulsarEntrenar()

    if (pantalla.guardar): 
        boton4 = st.sidebar.button("boton4")
