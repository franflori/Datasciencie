import streamlit as st
from preprocesar import Preprocesar
from pasajero import Pasajero
from pantalla import Pantalla




def captardatos(pasajero):
   
  
    # entrada de texto
    
   

    ##Survive  sobrive
    SurviveTip = st.radio(
        "Sobrevive",
         ('NO', 'SI','NS/NC'))

    if SurviveTip == 'NO':
       pasajero.setSuvived (0) 
    elif SurviveTip == 'SI':
        pasajero.setSuvived ("1")
  
    else:
        pasajero.setSuvived ("") 


    claseEle = st.radio(
        "Clase del  Pasaje",
         ('1st', '2nd','3rd','NS/NC'))

    if claseEle == '1st':
       pasajero.setPclass ("1") 
    elif claseEle == '2nd':
        pasajero.setPclass ("2")
    elif claseEle == '3rd':
        pasajero.setPclass ("3")
    else:
        pasajero.setPclass ("") 

    pasajero.setNName (st.text_input("Nombre y datos del pasajero : "))
   # pasajero.setSex (st.text_input("Sexo : "))

    sexoEle = st.radio(
        "Sexo del Pasajero",
         ('Hombre', 'Mujer', 'NS/NC'))

    if sexoEle == 'Hombre':
       pasajero.setSex ("male") 
    elif sexoEle == 'Mujer':
        pasajero.setSex ("female")
    else:
        pasajero.setSex ("") 

    # entrada de números

    age = st.slider('Edad del pasajero', 0, 99, 25)
    pasajero.setAge(age)




    
    

    hermano = st.slider('Hermanos', 0, 10, 0)
    pasajero.setSibsp(hermano)

    
    parche = st.slider('Numero de padres e hijos', 0, 6, 0)
    pasajero.setParch(parche)
   
    pasajero.setTicket (st.text_input("Identificador del Billete: "))
  
    precioparche = st.slider('Precios', 0.00, 200.01, 0.01)
    pasajero.setFare(precioparche)


    
    CabinEle = st.radio(
        "Puerto de Embarkation del  Pasajero",
         ('Cherbourg', 'Queenstown','Southampton','NS/NC'))

    if CabinEle == 'Cherbourg':
       pasajero.setCabin ("C") 
    elif CabinEle == 'Queenstown':
        pasajero.setCabin ("Q")
    elif CabinEle == 'Southampton':
        pasajero.setCabin ("S")
    else:
        pasajero.setCabin ("") 


  
    return pasajero
   


def filtrado (filtra,datos):
   
  if(filtra.getSuvived()!=""):
    datos=datos.loc[datos.Survived==filtra.getSuvived()]


    return datos




pantalla=st.session_state["pantalla"]





if(pantalla.getIniciacion()==0):
    filtrapasajero= Pasajero()
    filtrapasajero=captardatos(filtrapasajero)

    if st.button("Realizar Filtado"):

        datos=filtrado(filtrapasajero,st.session_state["df_datos"])
        st.write(datos)


