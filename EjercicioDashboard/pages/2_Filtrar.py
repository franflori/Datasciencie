import streamlit as st
from preprocesar import Preprocesar
from pasajero import Pasajero
from pantalla import Pantalla
from grafico import Grafico



def captardatos(pasajero):
   
  
    # entrada de texto
    
   

    ##Survive  sobrive
    SurviveTip = st.radio(
        "Sobrevive",
         ('NO', 'SI','No Aplicar'))

    if SurviveTip == 'NO':
       pasajero.setSuvived (0) 
    elif SurviveTip == 'SI':
        pasajero.setSuvived (1)
  
    else:
        pasajero.setSuvived ("") 


    claseEle = st.radio(
        "Clase del  Pasaje",
         ('1st', '2nd','3rd','No Aplicar'))

    if claseEle == '1st':
       pasajero.setPclass (1) 
    elif claseEle == '2nd':
        pasajero.setPclass (2)
    elif claseEle == '3rd':
        pasajero.setPclass (3)
    else:
        pasajero.setPclass ("") 

   # pasajero.setNName (st.text_input("Nombre y datos del pasajero : "))
   # pasajero.setSex (st.text_input("Sexo : "))

    sexoEle = st.radio(
        "Sexo del Pasajero",
         ('Hombre', 'Mujer', 'No Aplicar'))

    if sexoEle == 'Hombre':
       pasajero.setSex ("male") 
    elif sexoEle == 'Mujer':
        pasajero.setSex ("female")
    else:
        pasajero.setSex ("") 

    # entrada de números

    edad1, edad2 = st.columns(2)
    with edad1:
        filtraedad = st.selectbox(
        "Filtrad Edad del  Pasaje",
        ("No Aplicar", "Mayor", "Menor"))

    with edad2:
        age = st.slider('Edad del pasajero', 0, 99, 0)
        pasajero.setAge(age)




    colHer1, colHer2 = st.columns(2)
    with colHer1:
        filtraHermano = st.selectbox(
        "Filtra número de Hermanos",
        ("No Aplicar", "Mayor", "Menor"))

    with colHer2:
        hermano = st.slider('Hermanos', 0, 10, 0)
        pasajero.setSibsp(hermano)


    familia1, familia2 = st.columns(2)
    with familia1:
        filtrafamilia = st.selectbox(
         "Filtra número de familia",
        ("No Aplicar", "Mayor", "Menor"))

    with familia2:
        parche = st.slider('Numero de padres e hijos', 0, 6, 0)
        pasajero.setParch(parche)



   
    

    col1, col2 = st.columns(2)
    with col1:
        filtraPrecio = st.selectbox(
        "Filtrar Precio",
        ("No Aplicar", "Mayor", "Menor"))

    with col2:
        precioparche = st.slider('Precios', 0.00, 1000.01, 0.01)
        pasajero.setFare(precioparche)


    
    CabinEle = st.radio(
        "Puerto de Embarkation del  Pasajero",
         ('Cherbourg', 'Queenstown','Southampton','No Aplicar'))

    if CabinEle == 'Cherbourg':
       pasajero.setEmbarked ("C") 
    elif CabinEle == 'Queenstown':
        pasajero.setEmbarked ("Q")
    elif CabinEle == 'Southampton':
        pasajero.setEmbarked ("S")
    else:
        pasajero.setEmbarked ("") 


 
    
    return pasajero,filtraedad,filtraHermano,filtrafamilia,filtraPrecio
   


def filtrado (filtra,datos,filtraedad,filtraHermano,filtrafamilia,filtraPrecio):
    if(filtra.getSuvived()!=""):
        datos=datos.loc[datos.Survived==filtra.getSuvived()]
    if(filtra.getPclass()!=""):
        datos=datos.loc[datos.Pclass==filtra.getPclass()]
  
    if(filtra.getSex()!=""):
        datos=datos.loc[datos.Sex==filtra.getSex()]
    
  
    


    if filtraedad== "Mayor":
        datos=datos.loc[datos.Age>=filtra.getAge()]
    elif filtraedad== "Menor":
        datos=datos.loc[datos.Age<=filtra.getAge()]

    if filtraHermano== "Mayor":
        datos=datos.loc[datos.SibSp>=filtra.getSibsp()]
    elif filtraHermano== "Menor":
        datos=datos.loc[datos.SibSp<=filtra.getSibsp()]

    if filtrafamilia== "Mayor":
        datos=datos.loc[datos.Parch>=filtra.getParch()]
    elif filtrafamilia== "Menor":
        datos=datos.loc[datos.Parch<=filtra.getParch()]
    
    if filtraPrecio== "Mayor":
        datos=datos.loc[datos.Fare>=filtra.getFare()]
        st.write(filtra.getFare())
    elif filtraPrecio== "Menor":
        datos=datos.loc[datos.Fare<=filtra.getFare()]


    if(filtra.getEmbarked()!=""):
        datos=datos.loc[datos.Embarked==filtra.getEmbarked()]
   

    return datos




pantalla=st.session_state["pantalla"]





filtrapasajero= Pasajero()
filtrapasajero,filtraedad,filtraHermano,filtrafamilia,filtraPrecio=captardatos(filtrapasajero)
datos=st.session_state["df_datos"]

datos=filtrado(filtrapasajero,st.session_state["df_datos"],filtraedad,filtraHermano,filtrafamilia,filtraPrecio)

st.title("Datos del Dataset")
st.dataframe(datos)
        
        

pintarGrafico=Grafico()
cadena=["Pclass", "Sex", "Age","SibSp","Parch","Fare",
                           "Embarked"]
pintarGrafico.iniciaGraficios(cadena,datos,True)
pantalla.pulsaPrepocesar()

