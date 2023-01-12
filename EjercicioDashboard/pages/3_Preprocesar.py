import streamlit as st
from preprocesar import Preprocesar
from pasajero import Pasajero
from pantalla import Pantalla
from grafico import Grafico




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
   
    return df,memaAge,stdAge,meanFare,stdFare

st.title("Preprocesar")

pantalla=st.session_state["pantalla"]


if(pantalla.getPreprocesar()==1):

    st.title("Datos Sin Modificación")
    st.dataframe(st.session_state["df_datos"])
   
    df,memaAge,stdAg,meanFare,stdFare=preprocesar(st.session_state["df_datos"])

    st.markdown("☑️Elimina columna nombre")

    st.markdown("☑️Elimina columna Ticket")
    st.markdown("☑️Elimina columna Cabin por falta de informacion")
    st.markdown("☑️Modificamos y Creamos tablas dummies hombre/mujer")
    st.markdown("☑️Modificamos y Creamos tablas dummies columnas con strings con 3 opciones \"Embarked\"")
    
    st.markdown("☑️Modificamos y Creamos tablas dummies columnas\"Pclass\" hace referenica a las 3 clases")
    st.markdown("☑️Elminiar valores nulos de la  Edad, Embarque por valores de la medias")



   
    if "df_datos_preprocesado" not in st.session_state:
        st.session_state["df_datos_preprocesado"] = ""
    st.session_state["df_datos_preprocesado"]= df
    pasajero= Pasajero()

    pasajero.setPassengerId(df.shape [0]+1)
    pasajero.setMemaAge(memaAge)
    pasajero.setStdAge(stdAg)
    pasajero.setMeanFare(meanFare)
    pasajero.SetStdFare(stdFare)
   
    pantalla.pulsarEntrenaminto()

   



  
    if "pasajero" not in st.session_state:
        st.session_state["pasajero"] = ""
    st.session_state["pasajero"]= pasajero
    

    st.session_state["pantalla"] = pantalla
st.title("Datos del Dataset Modificado")

st.dataframe(st.session_state["df_datos_preprocesado"])
pintarGrafico=Grafico()
cadena=["Age", "SibSp", "Parch","Fare","Sex_male","Pclass_2",
                            "Pclass_3","Embarked_Q","Embarked_S"]
pintarGrafico.iniciaGraficios(cadena,st.session_state["df_datos_preprocesado"],False)
