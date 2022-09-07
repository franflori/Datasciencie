import pandas as pd

import numpy as np
import time

# EJERCICIO 1

# Calcula la longitud de una cadena de texto sin usar la instruccion len(cadena)

# 1) Cadena de texto: hola como estas?

    # Nombre de la variable: "cadena"
cadena = "hola como estas?"

# Descomentar para ejecutar:
# print(cadena)

# 2) Longitud de la cadena de texto

# Descomentar para ejecutar:
# print(len(cadena))

# 3) Longitud de la cadena de texto calculada con un bucle

def longitud(cadena):
    contador = 0
    for letra in cadena:
        contador += 1
    return contador

# Descomentar para ejecutar:
print(longitud(cadena))


# EJERCICIO 2

# Crea un diccionario que tenga la nota de 3 asignaturas y

# haz un pequeño algoritmo que calcule la nota media

# CURSO         -> Nota
# ---------------------
# Python        ->  10
# Big Data      ->  8
# NLP           ->  6

notas = {"Python": 10, "Big Data": 8, "NLP": 6}
print(notas)

values = [value for value in notas.values()]
# Descomentar para ejecutar:
print("notas",values)

media = sum(values) / len(values)
# Descomentar para ejecutar:
print(media)


# 1) Muestra el valor de las claves

def claves(diccionario):
    return diccionario.keys()

# Descomentar para ejecutar:
print(claves(notas))

# 2) Muestra el valor de los valores del diccionario

def valores(diccionario):
    return diccionario.values()

# Descomentar para ejecutar:
print(valores(notas))





# 3) Apendiza en el diccionario un nuevo elemento:
def anadirValor(diccionario,clave,valor):
    diccionario[clave] = valor
    return diccionario

print (notas)
notas=anadirValor(notas,"Machine Learning",9)
print (notas)

    # Machine Learning --> 9

# 4) Haciendo uso un bucle muestra la clave y el valor del diccionario, cuyo resultado final sean listas anidadas.
def imprimir_dicionario(notas):
   
    for clave in notas:
        valor = notas[clave]
        print(clave,valor)
    # [["clave1", valor1], ["clave2", valor2]]

def anidad(nota):
    lista =[]
    for key,value in nota.items():
        lista_info=[]
        lista_info.append(key)
        lista_info.append(value)
        print(lista_info)
        lista.append(lista_info)
    return lista

imprimir_dicionario(notas)
lista=anidad(notas)
print(lista)


# 5) Reconvierte el diccionario para transformarlo en un dataframe y busca la asignatura con la nota más alta

def CrearDataFrame(diccionario):
    
    df=pd.DataFrame(list(diccionario.items()),columns=['Asignaturas', 'Notas'])
    return df

df=CrearDataFrame(notas)




def notaMax_min(df):
    return df.Notas.max(),df.Notas.min()
print(notaMax_min(df))

# 6) ¿y la nota más baja?

# 7) Ordena el dataframe en orden descendente:

def ordenar(df,valor):
    return df.sort_values(by=valor,ascending=False)

print(ordenar(df,"Notas"))

# EJERCICIO 3

"""
Dadas 2 funciones:

Determina cual de ellas ejecuta mas rápido.

Si sabes, hazlo de 2 formas.

función a

def main(): for i in range(10**8): pass

main()

función b

def main(): for i in np.arange(10**8): pass

main()

de 2 formas
"""

def main():
    for i in range(10**8):
        pass

def main2():
    for i in np.arange(10**8): 
         pass 


def tiempo1():
    tiempo_inicial = time.time()
    main()
    tiempo_final=time.time()
    return tiempo_final-tiempo_inicial

def tiempo2():
    tiempo_inicial = time.time()
    main2()
    tiempo_final=time.time()
    return tiempo_final-tiempo_inicial

print("tiempo de ejecución: main() = ", tiempo1())
print("tiempo de ejecución: main2()", tiempo2())


# EJERCICIO 4

# Dada:

# Una matriz tal que así:

# A = np.array([[1,2,3], [4,5,6], [7,8,9]])

# se pide:

# 1) Escribe ese código en Python

# 2) Escribe la matriz transpuesta.

    # Nota, puedes usar numpy, si quieres. Si sabes más de una forma puedes usar varias.

# 3) Se pide que hagas lo mismo, pero con un bucle.

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(A)
print (A.T)
print (np.transpose(A))

def transpues(A):
    B=np.empty((A.shape[1], A.shape[0]), int)
    for columna in range(A.shape[1]):
        for fila in range(A.shape[0]):
            B[columna,fila]=A[fila,columna]
    return B

print ( transpues(A))
