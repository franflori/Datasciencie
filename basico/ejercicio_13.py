from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# EJERCICIO 1

# NO HACE FALTA HACERLO EN FORMATO FUNCIÓN!

# Se pide por tanto:

# -1- Leer el archivo train.csv de Titanic dataset con pandas (carpeta src)

# -2- Imprimir algunas filas de la parte de arriba y otras de la parte del final

# -3- Imprimir algunos parámetros estadísticos

# -4- Ver si en todas las columnas tenemos el mismo número de datos (solo verlo)

# -5- Ver el número de hombres y mujeres que hay

# -6- Hacer alguna gráfica con pandas relativa al número de hombres y mujeres que hay

# Si quieres hacer alguna cosa más también puedes

def leer():
    df = pd.read_csv("../datos/train.csv")
    return df
#df=leer()

def pintar(df,cadena):
    df[cadena].value_counts()

    df[cadena].value_counts().plot(kind="bar")
    plt.show()


def tarea(df):

    print("CAbecera",df.head())
    print("Pine",df.tail())
    print(df.describe())
    print(df.describe(include = 'all'))
    print(len(df), df.shape)
    print(df.Sex.value_counts())
    pintar(df,"Sex")








#tarea(df)
# EJERCICIO 2
"""
    Dadas estas matrices:

    * m1 = [[1, 10, 20], [30, 40, 50]]
    * m2 = [[60, 80, 90,]]
    * m3 = [[-2, 3, 5], [8, 6, 2]]
"""

# 1) Comprueba si todos los valores de las matrices son mayores de 0

# 2) Si en la matriz m2 se encuentra el valor 80

# 3) Selecciona de m1 las dos últimas columnas

# 4) Concatena la m1 con m2, cuyo nombre de la matriz resultante sea m4

# 5) Convierte m1 y m3 en "np.matrix" asignando el nombre de matriz_1 y matriz_3, respectivamente

# 6) Realiza la resta, suma y producto de la matriz_1 y matriz_3

# 7) Realiza las traza de la matriz de m4
m1 = np.array([[1, 10, 20], [30, 40, 50]])
m2 = np.array([[60, 80, 90,]])
m3 = np.array([[-2, 3, 5], [8, 6, 2]])

print(m1)
print(m2)

print(m3)

def mayores0(matriz):
    return np.all(matriz>0)

print (mayores0(m2))   
print (mayores0(m1))
print (mayores0(m3))

def tienevalor80(matriz):
    return np.any(matriz==80)
print (tienevalor80(m2))   
print (tienevalor80(m1))
print (tienevalor80(m3))

def tienevalor80Otra(matriz):
    return 80 in matriz

print (tienevalor80Otra(m2))

print (m1[:,[1,2]])
print (m1[:,[1,2]])

m4 = np.concatenate((m1, m2), axis=0)

print(m4)

matriz_1 = np.matrix(m1)
print(matriz_1)

matriz_3 = np.matrix(m3)
print(matriz_3)
print("suma")
print(matriz_1+matriz_3 )
print("resta")
print(matriz_1-matriz_3 )
print("producto")
print(matriz_1*matriz_3.T)

matriz=np.matrix(m4)
print(np.trace(matriz))

# EJERCICIO 3

"""
    * Numeros Primos: Crear un listado de los numeros primos menores de 30

    Explicación inicial teórica

    (véase Tema_7..)

    Nota:

    si quieres apendiza el número 2,

    y a partir de ahí crea el algoritmo para apendizar los demas

    (menores de 30 en todo caso)

"""

# 1) Pide por teclado un número y di si es o no primo
def numeroPrimo(numero):
    cont=2
    while (cont<numero):
        if(numero%cont==0):
            return False
        cont=cont+1
    return True

numero = int(input("Introduce nume que quiera sea primo.."))
if(numeroPrimo(numero)):
    print(f"El numero {numero}  es primo")
else:
     print(f"El  numero {numero} NO es primo")

# 2) Escribe los números primos menores de 30

def entreNumeroPrimo(desde,hasta):
    lista=[]
    for i in range(desde,hasta):
        if numeroPrimo(i):
            lista.append(i)
    return lista

def menorqueNumero(numero):
    return entreNumeroPrimo(2,numero)

print(menorqueNumero(30))


# 3) Numeros Primos: Crear un listado de los numeros primos menores de 200


print(menorqueNumero(200))

# 4) Números Primos: Haz un listado de números primos entre 50 y 100

print(entreNumeroPrimo(50,100))

# 5) Numeros Primos: Haz un listado de los 10 primeros números primos
    # Si puedes hazlo de más de una forma, no necesario aun así
cont=1
buscaPrimo=2
listaPrimo=[]
while (cont<=10):
    if(numeroPrimo(buscaPrimo)):
        listaPrimo.append(buscaPrimo)
        cont=cont+1
        
    buscaPrimo=buscaPrimo+1
print(listaPrimo)