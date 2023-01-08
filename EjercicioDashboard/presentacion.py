import streamlit as st
from datos_get import Datos_get
from pasajero import Pasajero
from entrenamiento import Entrenamiento
from preprocesar import Preprocesar
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df=Datos_get().read_datos()
datos_orginales=df
ValoresX=pd.DataFrame()
valor=0
memaAge=0
stdAge=1 
meanFare=0
stdFare=1
valormaximo=0

entrena=Entrenamiento()
pasajero = Pasajero()




def pintarDatos():
    st.title("Gráfica con Streamlit .............s")

    # head()
    st.write("Vamos a imprimir los primeros 5 valores del dataset")
    st.write(df.head())

    # tail()
    st.write("Vamos a imprimir los últimos 5 valores del dataset")
    st.write(df.tail())
    return df


    







# wide mode: modo apaisado:
st.set_page_config(layout="wide")

st.sidebar.title("1. Data")

# multiselect: opcion multiple
opciones = st.sidebar.multiselect("Datos de cabecera:", 
                          ["Age", "SibSp", "Parch","Fare","Sex_male","Pclass_2",
                          "Pclass_3","Embarked_Q","Embarked_S"])

st.write("Has elegido los siguientes frameworks: ", opciones)

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
    return df

def funcion(totalcolumna,extaer,cadena):
    print(extaer)
    totalcolumna[cadena]=extaer
    return totalcolumna
check = st.sidebar.checkbox("Debes procesar los datos")

if not check:
    st.write("Buena elección")
else:
    df=preprocesar(df)
        



if st.button("Realizar Estudio"):

    ValoresX=pd.DataFrame()
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

def crearObjeto(nuevo,persona,opcion):
   
    
    nuevo[opcion]=[persona.SacarValorCorrecto(opcion)]
   
    return nuevo
               
def captardatos(pasajero,valor):
   
  
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
    pasajero.setMemaAge(memaAge)
    pasajero.setStdAge(stdAge)
    pasajero.setMeanFare(meanFare)
    pasajero.SetStdFare(stdFare)
   


    print (pasajero)

    if st.button("Coger datos"):
        print (pasajero)
        nuevo=pd.DataFrame()
        for opcion in opciones:
            st.write("El resultado de los números es: ", opcion)
           
         
            nuevo=crearObjeto(nuevo,pasajero,opcion)
        st.write(nuevo)
       
        vivo=entrena.predecir("DecisionTree",nuevo)
        valor=vivo[0]
        if valor ==1 : 
            print ("Vivo")
            pasajero.setSuvived(1)
            return 1
        if valor==0 :
            print ("muerto")
            pasajero.setSuvived(0)
            return 0
      
    
        st.write("El resultado de los números es: ",valor)
        return  valor
    
   


def grabarDatos(pasajero,vivo):
    print (pasajero) 
    print (vivo)    
    if st.button("Guardar datos"):
           
            
            Datos_get().grabar_excel(pasajero)



# checkbox
check = st.sidebar.checkbox("Quieres que se cage los datos")

if not check:
    st.write("Buena elección")
else:
    df=pintarDatos()
    fig, ax = plt.subplots()
    
    ax.hist(datos_orginales.Sex)
    st.pyplot(fig)
   

   

    
    # me creo una figura
    fig= plt.figure()
    # 3 subplots
    # 1 fila 3 columnas - gráfica 1
    ax1 = fig.add_subplot(131)
    # 1 fila 3 columnas - gráfica 2
    #ax2 = fig.add_subplot(132)
    # 1 fila 3 columnas - gráfica 3
    #ax3 = fig.add_subplot(133)
    # violinplot
    sns.violinplot(x="Embarked", y="Age", hue="Survived", data=df, ax=ax1)
   # sns.violinplot(x="Pclass", y="Age", hue="Survived", data=df, ax=ax2)
   # sns.violinplot(x="Sex", y="Age", hue="Survived", data=df, ax=ax3)
   
  
    st.pyplot(fig)








checknuevo = st.sidebar.checkbox("Sacar datos")

if not checknuevo:
    st.write("Buena elección")
else:
   
   valor=captardatos(pasajero,valor)


checkGrabardatos = st.sidebar.checkbox("Grabar Datos")
if not checkGrabardatos:
    st.write("Buena elección")
else:
    print("Nodiicacion",valor)
    grabarDatos(pasajero,valor)