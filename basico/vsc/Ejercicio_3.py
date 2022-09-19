
#Importar librerias
import numpy as np

# EJERCICIO 1

"""
    Dada una lista de nombre "listado" y con valores: 10,20,30,40,50
"""
# 1) Crea un pequeño programa capaz de conseguir el orden inverso de los números de "listado"
# imprime nuevamente el listado para tenerlo "a mano"
# 10-20-30-40-50 (tengo)
# 50-40-30-20-10 (lo que busco)

def inversa(lista):
    listado_inverso = []
    for i in  range(1,len(lista)+1):
       listado_inverso.append(lista[-i]) 
    return listado_inverso


listado = [10,20,30,40,50]
print(listado)

print(inversa(listado))

# EJERCICIO 2

"""
    Programa que coge por teclado 5 números y los almacena en una lista

    Nota:

    debería estar en la misma celda

    Hazlo como puedas, discurre cómo sería..
"""
def lista_teclado():
    listado_teclado = []
    for i in np.arange(1,6,1):
        entrada = int(input("Escribe un número entero: "))
        listado_teclado.append(entrada)
    print("\n")

    return listado_teclado



print(lista_teclado())


# EJERCICIO 3

"""
    Programa que coge por teclado una frase y es capaz de decir cuántas vocales hay

    Nota: asume que son letras minúsculas sin tildes.
"""

# 1) Entrada de texto por teclado
# 2) Hazlo si puedes de varias formas
    # forma 1: contar vocales en palabra/frase
# 3) Hazlo de otra forma si se te ocurre..
    # forma 2   

def contar_vocales(frase):
    cont = 0 
    vocales = ["a", "e", "i", "o", "u"]
    for letra in frase:
        if letra.lower() in vocales:
            cont+=1
    return cont

def contar_vocales2(frase):
    cont = 0
    for letra in frase:
        if (letra.lower()=="a") | (letra.lower()=="e") | (letra.lower()=="i") | (letra.lower()=="o") | (letra.lower()=="u"):
            cont+=1
    return cont


frase=input("añade la fase que vas a contar las vocales:")

print ("solucion metodo1",contar_vocales(frase))
print ("solucion metodo2",contar_vocales2(frase))



# EJERCICIO 4

"""
    Tablas de multiplicar:

    Haz algo tal que:
"""

# 1) Pregunta al usuario que tabla quiere multiplicar: <1 al 10>

# 2) Muestra los resultados de esta forma:

"""
        2 x 1 = 2

        2 x 2 = 4

        ...

        2 x 10 = 20

"""
def tabla_multipicar(numero):
    for i in range(1,11):
        print( str(numero)+ " x "+ str(i)+ " = "+ str(numero*i))




tabla_multipicar(int(input("Elija un tabla multiplciaf 1 10 ")))

    