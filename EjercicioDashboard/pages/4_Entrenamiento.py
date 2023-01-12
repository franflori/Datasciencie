import streamlit as st
import pandas as pd
from entrenamiento import Entrenamiento
from pantalla import Pantalla

def funcion(totalcolumna,extaer,cadena):
    print(extaer)
    totalcolumna[cadena]=extaer
    return totalcolumna


def calcularEntrenamiento(df ,opciones):
    ValoresX=pd.DataFrame()
    entrena=Entrenamiento()
    for opcion in opciones:
       
        ValoresX=funcion(ValoresX,df[opcion],opcion)
       
    

   ## st.write(ValoresX)
   # st.write(df.isnull().sum())
    #entrena=Entrenamiento(ValoresX,df["Survived"])
    entrena.cargarEntranamiento(ValoresX,df["Survived"])
    entrena.algoritmoDecisionTreeClassifier()
   
    st.write("algoritmoDecisionTreeClassifier",entrena.getAcc_DT())

    entrena.algoritmoKNeighborsClassifier()
    
    st.write("algoritmoKNeighborsClassifier ",entrena.getAcc_KN())

    entrena.algoritmoRandomForestClassifier()
  
    st.write("algoritmoRandomForestClassifier",entrena.getAcc_RF())

    entrena.algoritmoGaussianNB()
   
    st.write("algoritmoGaussianNB",entrena.getAcc_NB())

    entrena.SVC()
   
    st.write("SVC",entrena.getAcc_SVC())

    return entrena


pantalla=st.session_state["pantalla"]

if(pantalla.getEntrenar()==1):
    col1, col2 = st.columns(2)
    with col1:

        opciones = st.multiselect("Eligues columnas para para realiza Entrenamiento :", 
                            ["Age", "SibSp", "Parch","Fare","Sex_male","Pclass_2",
                            "Pclass_3","Embarked_Q","Embarked_S"])

    with col2:       
        st.write("Has elegido los siguientes columnas: ", opciones)

    
    if st.button("Realizar Estudio"):
        print(opciones)
        if (opciones!=[]):
            resulEntrenamiento=calcularEntrenamiento(st.session_state["df_datos_preprocesado"] ,opciones)
       
       
       
            if "Entrenamiento" not in st.session_state:
                st.session_state["Entrenamiento"] = ""
            st.session_state["Entrenamiento"]= resulEntrenamiento

            if "opciones" not in st.session_state:
                st.session_state["opciones"] = ""
            st.session_state["opciones"]= opciones
            
            pantalla.pulsarAnalisis()

            st.session_state["pantalla"] = pantalla
        
        else:
            st.write("Eligue al menos una opciona")





else:
    st.write("Error en la pantalla .Debe ejecurtase antes las pantallas anteriores")










