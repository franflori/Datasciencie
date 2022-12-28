import streamlit as st
from preprocesar import Preprocesar
from pasajero import Pasajero
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


st.write("final")

print (st.session_state["df_datos"])
df,memaAge,stdAg,meanFare,stdFare=preprocesar(st.session_state["df_datos"])

st.write("Vamos a imprimir los primeros 5 valores del dataset")
st.write(df.tail())

if "df_datos" not in st.session_state:
    st.session_state["df_datos"] = ""
st.session_state["df_datos"]= df
pasajero= Pasajero()


if "memaAge" not in st.session_state:
    st.session_state["memaAge"] = ""
st.session_state["memaAge"]= memaAge

if "stdAg" not in st.session_state:
    st.session_state["stdAg"] = ""
st.session_state["stdAg"]= stdAg

if "meanFare" not in st.session_state:
    st.session_state["meanFare"] = ""
st.session_state["meanFare"]= meanFare
if "meanFare" not in st.session_state:
    st.session_state["stdFare"] = ""
st.session_state["stdFare"]= stdFare
 
pasajero.setMemaAge(memaAge)
pasajero.setStdAge(stdAg)
pasajero.setMeanFare(meanFare)
pasajero.SetStdFare(stdFare)


if "pasajero" not in st.session_state:
    st.session_state["pasajero"] = ""
st.session_state["pasajero"]= pasajero