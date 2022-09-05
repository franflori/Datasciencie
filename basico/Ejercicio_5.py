
#libreria

import numpy as np


# EJERCICIO 1

# a) Declara la variable "test" como una lista con los siguientes componentes: 25, 8, 32, 20, 1.
    # Usa las formas que conozcas para crearla y el uso de type para asegurarte de que es una lista.

def defineLista():
    return [25, 8, 32, 20, 1]

def defineLista2():
    return list((25, 8, 32, 20, 1))

test=defineLista()
print(test, type(test))

test2=defineLista2()
print(test2, type(test2))

# b) Apendiza un valor de valor 20, 32, 25, 32
def anadir(lista,x):
    lista.append(x)

anadir(test,20)
anadir(test,32)
anadir(test,25)
anadir(test,32)


print(test)



# c) Elimina el valor 8 de la lista

def elimina(lista,valor):
    lista.remove(valor)

elimina(test,8)
print(test)  

# d) Elimina los duplicados que haya en la lista test

def eliminaduplicado(lista):
    return list(set(lista))

test=eliminaduplicado(test)
print(test)


# e) Crea una segunda lista de nombre "info" que contenga los valores:
    #  25, 100, 10, 20, 5, 25, 30, 200
def defineLista3():
    return [25, 100, 10, 20, 5, 25, 30, 200]

info=defineLista3()
print(info)

# f) ¿Cuántos valores se repiten entre las listas?

def contar_repetidos(lista,lista2):
    cont=0
    for elemento in lista:
        
            if elemento in lista2 :
                print ("Numero esta en la lista ",elemento)
                cont+=1
    return(cont)

print("Aparecen elemento lista", contar_repetidos(info,test))



# g) Muéstrame el maximo y mínimo en las dos listas

def muestra_max_min(lista):
    return max(lista),min(lista)

print("El maximo, y minimo lista son",info,muestra_max_min(info))
print("El maximo, y minimo lista son",test,muestra_max_min(test))


# h) Crea una nueva variable de nombre "matriz" transformando la lista test en matriz

def convertir(lista):
    return np.array(lista)

matriz=convertir(test)
print(matriz)

# i) Crea una función que se llame "funcion_división" donde se divida
    # el test con valor 32 entre info con valor 5 y muestra el resto de la división

def funcion_division(n,s):
    return test[n] % info[s]


def buscar_valor(lista,valor):
    cont=0
    for i in lista:
        if i==valor:
            break;
        cont+=1
    return cont

print(buscar_valor(test,32),buscar_valor(info,5))
print("resultado",funcion_division(buscar_valor(test,32),buscar_valor(info,5)))


# j) Con ayuda de reverse() muestra la inversa de test

def invertir(lista):
    return lista.reverse()

print(test)  
list=invertir(test)
print(list)
# k) Con el listado info utiliza un bucle for con la ayuda de enumerate(),
    # para mostrar posición y valor y crea un diccionario de nombre "newDict"

def nuevo_dicionario(info):
    newDict = {}
    for key, value in enumerate(info):
        newDict[key] = value
    return newDict

newDict= nuevo_dicionario(info)
print(newDict)

# l) Crea un nuevo listado con nombre "info2" donde los valores: 25 se sustituya por "María",
    # el valor 20 por "Juan" y el valor 10 por "Pedro"

def nueva_listado(info):
    informacion=[]
    for i in info:
        if i == 25:
            informacion.append("María")
        elif i == 20:
            informacion.append("Juan")
        elif i == 10:
            informacion.append("Pedro")
        else:
            informacion.append(i)
    return informacion
infonuevo=nueva_listado(info)
print(infonuevo)



# m) Sustituye en el listado test los multiplos de 2 por "Dos"

def sustituye(test):
    cont=0
    for i in test:
        if i%2==0:
            test[cont]="dos"
        cont+=1

sustituye(test)
print(test)
    

# EJERCICIO 2

"""
    Escribe un programa que imprima los números desde 1 hasta 100

    Pero:

    * Para los múltiplos de 3 escribe "Hello"
    * Para los múltiplos de 5 escribe "World"
    * Para los múltiplos de ambos (3 y 5) escribe "Hello World"
    (en vez de los números correspondientes)
"""

lista = np.arange(0,101,1)
lista = lista.tolist()
print(np.array(lista))

def elimina(lista):
    for numero in lista:
        if (numero%3==0) and (numero%5==0):
            lista[numero]="Hello World"
        elif (numero%3==0):
            lista[numero]="Hello "
        elif (numero%5==0):
            lista[numero]="World "

elimina(lista)
print(np.array(lista))
         
       
