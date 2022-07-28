

# EJERCICIO 1

"""
    Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
    Escribir una tercera función que reciba un diccionario con los precios
    y porcentajes de una cesta de la compra, y una de las funciones anteriores, 
    y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
    Ejemplo de diccionario: {1000:20, 500:10, 100:1}
"""
def apply_discount(price, discount):
    return price - price * discount / 100

def apply_IVA(price, percentage):
    
    return price + price * percentage / 100
    

def price_basket(basket, function):
    
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

   
    

iva = {1000:20, 500:10, 100:1}
descuento= {1000:20, 500:40, 100:11}



print('El precio de la compra tras aplicar los descuentos es: ', price_basket(descuento, apply_discount))
print('El precio de la compra tras aplicar el IVA es: ', price_basket(iva, apply_IVA))












# EJERCICIO 2


def aplica_funcion_lista(funcion, lista):
    nueva=[]
    for elemento in lista:
        nueva.append(funcion(elemento))
   
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





lista=[1,2,4,6,8,10,23,12,3]
print (lista)
print(aplica_funcion_lista(cuadrado,lista))





# EJERCICIO 4

"""
    Escribir una función reciba una lista de notas y
    devuelva la lista de calificaciones correspondientes a esas notas.
    Suspenso < 5
    Aprobado = 5
    Suficiente entre 5 - 7
    Notable 7-9
    Sobresaliente > 9
"""


def calificacion(lista):
    nueva_lista=[]
    for x in lista:
     
        if x<5:
           nueva_lista.append("SUSPENSO")
        elif  x==5 :
            nueva_lista.append("APROBADO")
        elif x>5 or x<7 :
             nueva_lista.append("SUFICIENTE")
        elif x>=7 or x<9 :
            nueva_lista.append("NOTABLE")
        elif x>9:
             nueva_lista.append("SOBRESALIENTE")
    return nueva_lista

listaNotas=[5,3,5,8,6,10]
print(calificacion(listaNotas))



# EJERCICIO 5

"""
    Escribir una función que reciba un diccionario con las asignaturas y
    las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas
    y las calificaciones correspondientes a las notas.
"""

def sacar_notas(dicionario):
    for valor, lista_valor in dicionario.items():
        if(valor=="Asignatura"):
            listaNota=lista_valor
        else :
            lista_letra=calificacion(lista_valor)
        
    print("mayuscula: ", listaNota)
    print("letra: ", lista_letra)
    listaMayuscula=[]
    for mayuscula in listaNota:
        listaMayuscula.append(mayuscula.upper())
   
    return  {"Asignatura": listaMayuscula, "Notas": lista_letra}


asignanturas = ["Lengua", "Matematica", "Programacion", "Ingles"]
notas = [1, 8, 6,3]
diccionario = {"Asignatura": asignanturas, "Notas": notas}
print("antes modificacion",diccionario)
nuevo_diccionario=sacar_notas(diccionario)
print("despues modificacion",nuevo_diccionario)


# EJERCICIO 6




"""
    Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
    pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
    por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
""" 
password=input("Intrudocir pass.....")

nuevaPass=input("Intrudocir pass nueva.....")

if(password.upper()==nuevaPass.upper()):
    print ("coincide")
else :
    print ("no coincide")

