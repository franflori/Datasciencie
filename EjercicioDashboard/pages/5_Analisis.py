
import streamlit as st

def captardatos(pasajero):
   
  
    # entrada de texto
    
    pasajero.setPclass (st.text_input("Inserte clase: "))
    pasajero.setNName (st.text_input("Nombre : "))
    pasajero.setSex (st.text_input("Sexo : "))
    # entrada de números
    pasajero.setAge(st.number_input("Inserte un número: "))
    pasajero.setSibsp(st.number_input("Inserte sibsp: "))
    pasajero.setParch(st.number_input("Inserte un parch: "))
   
    pasajero.setTicket (st.text_input("Inserte Ticket: "))
    pasajero.setFare (st.number_input("Inserte Fare: "))
    pasajero.setCabin (st.text_input("Inserte Cabin: "))
    pasajero.setEmbarked (st.text_input("Inserte Embarquessss: "))
    return pasajero
   
   
   




pasajero=st.session_state["pasajero"]


pasajero=captardatos(pasajero)
print (pasajero)
    