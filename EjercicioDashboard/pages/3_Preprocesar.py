import streamlit as st
from preprocesar import Preprocesar
from pasajero import Pasajero
from pantalla import Pantalla

st.title("Pre procesar")


def preprocesar(df):
    #Eliminar columnas
    preprocesar= Preprocesar()
    df=preprocesar.name_process(df)
    df=preprocesar.ticket_process(df)
    df=preprocesar.cabin_process(df)
    df=preprocesar.eliminaColumna(df,"PassengerId")
    df=preprocesar.age_process(df,"Mean")
    df=preprocesar.embarked_process(df,"S")


    #"Sex", "Pclass", "Embarked"
    df=preprocesar.dummies_crear(df,"Sex")
    df=preprocesar.dummies_crear(df,"Pclass")
    df=preprocesar.dummies_crear(df,"Embarked")
    df,memaAge,stdAge=preprocesar.escalado_Age(df)
    df,meanFare,stdFare=preprocesar.escalado_Fare(df)
    st.write(df.head())

    st.write(df.isnull().sum())
    return df,memaAge,stdAge,meanFare,stdFare



pantalla=st.session_state["pantalla"]


if(pantalla.getIniciacion()==0):
    st.write("final")

    print (st.session_state["df_datos"])
    df,memaAge,stdAg,meanFare,stdFare=preprocesar(st.session_state["df_datos"])

    st.write("Vamos a imprimir los primeros 5 valores del dataset")
    st.write(df.tail())

    if "df_datos" not in st.session_state:
        st.session_state["df_datos"] = ""
    st.session_state["df_datos"]= df
    pasajero= Pasajero()

    pasajero.setPassengerId(df.shape [0]+1)
    pasajero.setMemaAge(memaAge)
    pasajero.setStdAge(stdAg)
    pasajero.setMeanFare(meanFare)
    pasajero.SetStdFare(stdFare)

    print(pasajero)
    if "pasajero" not in st.session_state:
        st.session_state["pasajero"] = ""
    st.session_state["pasajero"]= pasajero
    pantalla.pulsaPrepocesar()

    st.session_state["pantalla"] = pantalla

else:
    st.write("Error en la pantalla")
