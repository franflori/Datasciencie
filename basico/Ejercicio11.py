"""
    Creado: Isabel Maniega
    Fecha: 08/09/2022
"""

# Importar las librerías
from pickle import FALSE
import pandas as pd
import matplotlib.pyplot as plt


# EJERCICIO 1

"""
    Escribe el código necesario en Python para:

    almacenar con una lista de nombre "clientes" los siguientes nombres:

    "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas",
    "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"
"""

listado_nombre=["Ana Pérez", "Juan García", "Andrés Álvarez",
"Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez",
"Alberto Delgado", "Susana Castro", "Luis González"]

def buscar_nombre(listado_nombre,cadena):
    for nombre in listado_nombre:
        if nombre.lower()==cadena.lower():
            return  f"el cliente '{cadena}'  se encuentra en mi Base de Datos de Cliente"
    return f"'{cadena}' NO se encuentra en mi Base de Datos de Clientes"

usuario = "Ana Perez"

print(buscar_nombre(listado_nombre, usuario))
# 1) Para ese listado de clientes imprime todos ellos, 1 a 1

"""
    2) Dentro de ese grupo de clientes..

    se pide buscar..al cliente de nombre: "Juan García" si es posible

    Si lo encuentra, debería imprimir un mensaje tal que así:

    "el cliente -nombre del cliente- se encuentra en mi Base de Datos de Clientes"

    Si no se le encuentra, debería salir un mensaje tal que así:

    "el cliente -nombre del cliente- NO se encuentra en mi Base de Datos de Clientes"

    Nota: Comprueba en el caso de llevar o no acento

    Para:

    Juan García

    Juan Garcia

    Ojo con la tilde..
"""
usuario = "Juan García"

print(buscar_nombre(listado_nombre, usuario))

usuario = "Juan Garcia"

print(buscar_nombre(listado_nombre, usuario))

"""
    3) Crea un DataFrame, de nombre df

    con esa información en base a la siguiente relación de clientes y tarifas contratadas (€)

    clientes: Ana Pérez, Juan García, Andrés Álvarez, Luis Ramos, Pedro Cadenas,
            Estefanía Miguélez, Alberto Delgado, Susana Castro, Luis González

    tarifas: 40,50,50,35,45,50,60,50,45
"""

tarifas=[40,50,50,35,45,50,60,50,45]


def CrearDataFrame(campo1,campo2):
    df=pd.DataFrame({"clientes":campo1, "tarifas": campo2})
    return df
    
df=CrearDataFrame(listado_nombre,tarifas)
print(df)




# 4) Imprime las primeras 5 filas del DataFrame de 2 formas distintas
print(df.head(5))

print (df.head())

def imprimirdf(df,valor):
    for i in range(valor):
        print (df.iloc[i])

imprimirdf(df,5)


# 5) De ese DataFrame, selecciona solamente la columna "tarifas" e imprímela
    # (con 1 forma es suficiente, pero si sabes 2 mejor)
def imprimirValor(df,valor):
    print(df[valor])
def imprimirValor2(df,valor):
    print(df[[valor]])

def imprimiTarifa(df):
    print(df.tarifas)


imprimirValor(df,"tarifas")
imprimirValor2(df,"tarifas")
imprimiTarifa(df)

# 6) Descomenta las siguientes líneas (algunos trucos y cosas útiles).
    # Ponlo en formato función!!

def pintaruno(df):
    df.tarifas.value_counts()

    df.tarifas.value_counts().plot(kind="bar")
    plt.show()

def pintardos(df):

  
    

    df.tarifas.plot(kind="bar")
    plt.show()

pintaruno(df)
print(df)
pintardos(df)

# 7) De ese DataFrame, selecciona solamente aquellos clientes con tarifa superior a 50 euros (50 no incluído)

def tarifasuperio50(df):
    return df[ df.tarifas>50]


print(tarifasuperio50(df))

# EJERCICIO 2

# Número par o impar

# Prueba para los números 6 y 3

# Realiza un algortimo para saber si son pares o impares

def numeroPar(valor):
    if(valor%2==0) :
        return True
    else :
        return False


valor=343412412
if(numeroPar(valor)):
    print(f"El numero {valor} es par ")
else :
    print(f"El numero {valor} es impar ")

# EJERCICIO 3

"""
    Intercambio de valores entre variables

    Siendo por ejemplo:

    x = 3 e y = 2
    Se pide hacer un pequeño algoritmo que me intercambie esos valores.

    Y que sea el resultado:

    x = 2 e y = 3
"""
x=3
y=2

# 1) Hazlo sin funciones

print (f"El valor x antes cambio {x} y el de y es {y}")
y,x=x,y
print (f"El valor x despues del  cambio {x} y el de y es {y}")

# 2) Hazlo mismo con una función

x=3
y=2

print (f"El valor x antes cambio {x} y el de y es {y}")
def cambiarvalor(x,y):
    return y,x

x,y=cambiarvalor(x,y)

print (f"El valor x despues del  cambio {x} y el de y es {y}")