import streamlit as st
import pandas as pd
from entrenamiento import Entrenamiento

def funcion(totalcolumna,extaer,cadena):
    print(extaer)
    totalcolumna[cadena]=extaer
    return totalcolumna


def calcularEntrenamiento(df ,opciones):
    ValoresX=pd.DataFrame()
    entrena=Entrenamiento()
    for opcion in opciones:
        st.write("El resultado de los números es: ", opcion)
        ValoresX=funcion(ValoresX,df[opcion],opcion)
       
    

    st.write(ValoresX)
    st.write(df.isnull().sum())
    #entrena=Entrenamiento(ValoresX,df["Survived"])
    entrena.cargarEntranamiento(ValoresX,df["Survived"])
    acc_DT=entrena.algoritmoDecisionTreeClassifier()
   
    st.write(acc_DT)

    acc_KN=entrena.algoritmoKNeighborsClassifier()
    
    st.write(acc_KN)

    acc_RF=entrena.algoritmoRandomForestClassifier()
  
    st.write(acc_RF)

    acc_NB=entrena.algoritmoGaussianNB()
   
    st.write(acc_NB)

    acc_SVC=entrena.SVC()
   
    st.write(acc_SVC)

    return entrena




opciones = st.multiselect("Datos de cabecera:", 
                          ["Age", "SibSp", "Parch","Fare","Sex_male","Pclass_2",
                          "Pclass_3","Embarked_Q","Embarked_S"])

st.write("Has elegido los siguientes frameworks: ", opciones)

if st.button("Realizar Estudio"):
    resulEntrenamiento=calcularEntrenamiento(st.session_state["df_datos"] ,opciones)
    if "Entrenamiento" not in st.session_state:
        st.session_state["Entrenamiento"] = ""
    st.session_state["Entrenamiento"]= resulEntrenamiento

    







