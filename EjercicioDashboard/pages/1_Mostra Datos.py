import streamlit as st
from datos_get import Datos_get
import seaborn as sns
import matplotlib.pyplot as plt
from grafico import Grafico
import pandas as pd


from plotnine import *


from pantalla import Pantalla






st.title("Cargar Datos")
#df=Datos_get().read_datos()

df=st.session_state["df_datos"]
#if "df_datos" not in st.session_state:
 #   st.session_state["df_datos"] = ""
#st.session_state["df_datos"]= df
df=st.session_state["df_datos"]
if "pantalla" not in st.session_state:
    st.session_state["pantalla"] = ""

pantalla= Pantalla()
st.session_state["pantalla"] = pantalla


st.title("Datos del Dataset")
st.dataframe(df)
pintarGrafico=Grafico()
cadena=["Pclass", "Sex", "Age","SibSp","Parch","Fare",
                            "Embarked"]
pintarGrafico.iniciaGraficios(cadena,df,True)
pantalla.pulsaPrepocesar()











