
import streamlit as st
import pandas as pd
from pasajero import Pasajero
from pantalla import Pantalla

def captardatos(pasajero):
   
  
    # entrada de texto
    
   
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
    #pasajero.setAge(st.number_input("Inserte un número: "))
    age = st.slider('Edad del pasajero', 0, 99, 25)
    pasajero.setAge(age)



    
   # pasajero.setSibsp(st.number_input("Inserte sibsp: "))
   # pasajero.setParch(st.number_input("Inserte un parch: "))
    
    

    hermano = st.slider('Hermanos', 0, 10, 0)
    pasajero.setSibsp(hermano)

    
    parche = st.slider('Numero de padres e hijos', 0, 6, 0)
    pasajero.setParch(parche)
   
    pasajero.setTicket (st.text_input("Identificador del Billete: "))
    #pasajero.setFare (st.number_input("Inserte Fare: "))
    precioparche = st.slider('Precios', 0.00, 200.01, 0.01)
    pasajero.setFare(precioparche)

 #   pasajero.setCabin (st.text_input("Inserte Cabin: "))
    
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


   # pasajero.setEmbarked (st.text_input("Inserte Embarquessss: "))
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

print(pantalla)
if(pantalla.getEntrenar()==1):
    pasajero=st.session_state["pasajero"]
    pasajero=captardatos(pasajero)
    print (pasajero)

    if "pasajero" not in st.session_state:
        st.session_state["pasajero"] = ""
    st.session_state["pasajero"]= pasajero

    def crearObjeto(nuevo,persona,opcion):
        nuevo[opcion]=[persona.SacarValorCorrecto(opcion)]
        return nuevo  

    opciones=st.session_state["opciones"]
    entrenamiento= st.session_state["Entrenamiento"] 

    eleccion=elegirValoresEntrenamiento(entrenamiento)
    print(eleccion)

    if st.button("Realizar Estudio"):
    
        nuevo=pd.DataFrame()
        for opcion in opciones:
            nuevo=crearObjeto(nuevo,pasajero,opcion)

        
        vivo=entrenamiento.predecir(eleccion,nuevo)
        valor=vivo[0]   
        pasajero.setSuvived(valor)
        print(pasajero)
        
        if "pasajero" not in st.session_state:
            st.session_state["pasajero"] = ""
        st.session_state["pasajero"]= pasajero
        pantalla.pulsarAnalisis()

        st.session_state["pantalla"] = pantalla
      
else:
    st.write("Error en la pantalla")

