#import
import numpy as np
from time import sleep

# EJERCICIO 1

"""
    Dado: "np.arange(2,10)"

    sigue los siguientes pasos:

    1) Escribe esa instrucción y asígnaselo a la variable "a"
"""
def crear():
    return np.arange(2,10)

a=crear()

print (a)



# 2) ¿Es equivalente a "np.arange(2,10,1)"?

def crear2():
    return np.arange(2,10,1)

b=crear2()
print (b)



# 3) Se pide quedarse con aquellos números menores de 5.

    # hazlo con numpy si puedes para la variable "a"

def devolver(valor):
    return valor

resulta=devolver(a[(a<5)])
print (resulta)


# 4) Hazlo pasando esa información (de "a") a una lista

lista=list(resulta)
print (lista)

# 5) En base a los resultados..

    # ¿Es posible recorrer 1 a 1 un array de numpy?

# 6) Haz el mismo proceso programando una sola línea (toma "a" como referencia)

lista2=list(a[(a<5)])
print (lista2)


# EJERCICIO 2

"""
    Para estos valores (v de valores por abreviar):

    v1 = 4

    v2 = 5

    v3 = 7

    v4 = 8

    El objetivo será calcular la media de estos valores

    Para ello sigue los siguientes pasos:

"""

# 1) Imprime los valores de esas variables v1,v2,v3,v4
v1 = 4

v2 = 5

v3 = 7

v4 = 8
print(v1,v2,v3,v4)


# 2) Descomenta las 2 líneas siguientes para aprender..

    # que es posible asignar varios valores en la misma línea

    # Y la asignación de valores a variables se hace de forma consecutiva.

#3) Descomenta la línea siguiente para aprender una posible forma de calcular la media.

    #  Usamos nuevamente numpy..

# 4) Calcula la media sin usar numpy

    # Si el resultado no sale bien, razona cómo debería hacerse..
media_numpy = np.mean([v1,v2,v3,v4])
print( "media mumpy",media_numpy)
media=(v1+v2+v3+v4)/4

print( "media ",media)
# EJERCICIO 3

"""
    Factorial de un número

    Nota:

    El Factorial de 5, por ejemplo:

    5! = 5 * 4 * 3 * 2 * 1 = 120

    y el de 3:

    3! = 3 * 2 * 1 = 6

    y así para todos..

    PASOS A SEGUIR Y COSAS A TENER EN CUENTA

    Pide por teclado el número del cual quieres calcular el factorial.

    Para que no sea muy grande te recomendamos:

    3,4 o 5 (para hacer las pruebas)

    si ya no lo recuerdas o nunca lo viste, no te preocupes..

    3! es: 3 * 2 * 1 = 6

    4! es: 4 * 3 * 2 * 1 = 24

    5! es: 5 * 4 * 3 * 2 * 1 = 120

    (esto es lo que se pide, en esencia)
"""

def solicitud_numero():
    return int(input("dígame su número para calcuar facoria: <No valen decimales>..."))


def factorial(numero):
    total=1
    for i in range(2,numero+1):
        total=total*i
    return total
num=solicitud_numero()

print( "El factorial es :",factorial(num))


# EJERCICIO 4

"""
    Haz un cronómetro en Python:

    Obviamente:

    Horas - Minutos - Segundos

    Debes usar lo siguiente (from time import sleep)

    NOTA: Si quieres puedes usar sleep(0.000001)

    en vez de sleep(1) -> 1 segundo

    (para no esperar 1 segundo a ver los cambios)

    Para poder pararlo en poco tiempo,

    imprime mientras horas<2, cuando llegue a 2 debería parar la ejecución.

    Debería ejecutarse en unos 2 minutos aprox.
"""

def cronometro():
    segundos=np.arange(0,60)
    minutos=np.arange(0,60)
    horas=np.arange(0,24)
    segundos=np.arange(0,60)

    print("HH"+":"+"MM"+":"+"SS")
    for elementohora in horas:
        if(elementohora==2):
            break 
        for elementominuto in minutos:
        
            for elementosegundo in segundos:
                sleep(0.000001)
                print(str(elementohora)+ " : "+str(elementominuto)+" : "+str(elementosegundo))
                
              
cronometro()