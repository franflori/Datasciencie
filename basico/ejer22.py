

# EJERCICIO 1

"""
    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
    Escribir una tercera función que reciba un diccionario con los precios
    y porcentajes de una cesta de la compra, y una de las funciones anteriores, 
    y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
    Ejemplo de diccionario: {1000:20, 500:10, 100:1}
"""



def apply_discount(price, discount):
    descuento=price*discount[price]/100
    total=price-descuento
    return total

def apply_IVA(price, percentage):
    descuento=price*percentage[price]/100
    total=price+descuento
    return total
    

def price_basket(basket, funcion):


    return 

# EJERCICIO 2

"""
    Escribir una función que reciba otra función y una lista,
    y devuelva otra lista con el resultado de aplicar
    la función dada a cada uno de los elementos de la lista.
"""

def aplica_funcion_lista(funcion, lista):
    nueva=[]
    for elemento in lista:
        nueva.append(funcion(elemento))
    # TODO: recorrer la lista
    # TODO: apendizar los resultados de la función en una lista vacia
    # TODO: retorne la lista final
    return nueva

def cuadrado(n):
   return n*n

# EJERCICIO 3

"""
    Escribir una función que reciba una frase y
    devuelva un diccionario con las palabras que contiene y su longitud.
    Ejemplo: "Hola Mundo" --> {"Hola": 4, "Mundo": 5}
"""


class Palabra_leng:
    def __init__(self,palabra):
        self.palabra=palabra
        self.longitud=len(palabra)

    def imprimir():
        print ()

def convertir_lista(cadena):
  
    longitud=[]
    lista=cadena.split()
    for palabra in lista:
        longitud.append(len(palabra))

    print(lista)
    print (longitud)
    dict_from_list = dict(zip(lista, longitud))
  
    return dict_from_list


cadena=input("Intruduce cadena ")

print(convertir_lista(cadena))

precio = {1000:20, 500:10, 100:1}
descuento= {1000:20, 500:40, 100:11}

print()

lista=[1,2,4,6,8,10,23,12,3]
print (lista)
print(aplica_funcion_lista(cuadrado,lista))



