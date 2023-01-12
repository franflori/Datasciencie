
import streamlit as st
import pandas as pd
from pasajero import Pasajero
from pantalla import Pantalla
from PIL import Image


def captardatos(pasajero):
   
  
    # entrada de texto
    
   
    claseEle = st.radio(
        "Clase del  Pasaje",
         ('1st', '2nd','3rd','NS/NC'))

    if claseEle == '1st':
       pasajero.setPclass (1) 
    elif claseEle == '2nd':
        pasajero.setPclass (2)
    elif claseEle == '3rd':
        pasajero.setPclass (3)
    else:
        pasajero.setPclass ("") 

    pasajero.setNName (st.text_input("Nombre y datos del pasajero : "))
 

    sexoEle = st.radio(
        "Sexo del Pasajero",
         ('Hombre', 'Mujer', 'NS/NC'))

    if sexoEle == 'Hombre':
       pasajero.setSex ("male") 
    elif sexoEle == 'Mujer':
        pasajero.setSex ("female")
    else:
        pasajero.setSex ("") 

  
    age = st.slider('Edad del pasajero', 0, 99, 25)
    pasajero.setAge(age)




    
    

    hermano = st.slider('Hermanos', 0, 10, 0)
    pasajero.setSibsp(hermano)

    
    parche = st.slider('Numero de padres e hijos', 0, 6, 0)
    pasajero.setParch(parche)
   
    pasajero.setTicket (st.text_input("Identificador del Billete: "))
   
    precioparche = st.slider('Precios', 0.00, 1000.01, 0.01)
    pasajero.setFare(precioparche)

    pasajero.setCabin (st.text_input("Cabina donde embarca: "))
    
    CabinEle = st.radio(
        "Puerto de Embarkation del  Pasajero",
         ('Cherbourg', 'Queenstown','Southampton','NS/NC'))

    if CabinEle == 'Cherbourg':
       pasajero.setEmbarked ("C") 
    elif CabinEle == 'Queenstown':
        pasajero.setEmbarked ("Q")
    elif CabinEle == 'Southampton':
        pasajero.setEmbarked ("S")
    else:
        pasajero.setEmbarked ("") 


   
    return pasajero
   
 
def elegirValoresEntrenamiento(entrenamiento):
    
    genre = st.radio(
        "Elegir uno de los entrenamiento",
         ('DecisionTree', 'KNeighbors', 'GaussianNB','RandomForest','SVC'))

    if genre == 'DecisionTree':
        return "DecisionTree"
    elif genre == 'KNeighbors':
        return "KNeighbors"
    elif genre == 'GaussianNB':
        return "GaussianNB"
    elif genre == 'RandomForest':
        return "RandomForest"
    elif genre == 'SVC':
        return "SVC"
   
   
   
   
   
  






pantalla=st.session_state["pantalla"]


if(pantalla.getAnalisis()==1):
    pasajero=st.session_state["pasajero"]
    pasajero=captardatos(pasajero)
   

    if "pasajero" not in st.session_state:
        st.session_state["pasajero"] = ""
    st.session_state["pasajero"]= pasajero

    def crearObjeto(nuevo,persona,opcion):
        nuevo[opcion]=[persona.SacarValorCorrecto(opcion)]
        return nuevo  

    opciones=st.session_state["opciones"]
    entrenamiento= st.session_state["Entrenamiento"] 



  


   
    valoresImprmir = {"DecisionTree":entrenamiento.getAcc_DT(), "KNeighbors":entrenamiento.getAcc_KN(), "GaussianNB":entrenamiento.getAcc_NB(), "RandomForest": entrenamiento.getAcc_RF(),"SVC": entrenamiento.getAcc_SVC()}
    

    algoritmo = list(valoresImprmir.keys())
    valores = list(valoresImprmir.values())
    diccionario = {"Algoritmo": algoritmo, "Valores": valores}

    valor1, valor2 = st.columns(2)
    with valor1:
         st.dataframe(pd.DataFrame(diccionario))
     
    with valor2:
        eleccion=elegirValoresEntrenamiento(entrenamiento)
        
    
    print(eleccion)
    print(valoresImprmir)
    if st.button("Realizar Estudio"):
    
        nuevo=pd.DataFrame()
        for opcion in opciones:
            nuevo=crearObjeto(nuevo,pasajero,opcion)

        
        vivo=entrenamiento.predecir(eleccion,nuevo)
        valor=vivo[0]   
        pasajero.setSuvived(valor)
        print(pasajero)
        
        if(valor==1):
            image = Image.open('image//viva.jpg')
            st.image(image, caption='VIVO')
            
        else:
            imagemuerto = Image.open('image//muerto.jpg')
            st.image(imagemuerto, caption='NO SOBREVIVIO')
           

        if "pasajero" not in st.session_state:
            st.session_state["pasajero"] = ""
        st.session_state["pasajero"]= pasajero
        pantalla.pulsaGuardar()

        st.session_state["pantalla"] = pantalla
      
else:
   st.write("Error en la pantalla .Debe ejecurtase antes pantallas anteriores")


