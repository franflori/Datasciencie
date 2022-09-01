#Importar librerias
import pandas as pd
#Ejercicio 1
"""
    Describe una variable con nombre "notas" que tenga el valor de -3, muestra su valor.
"""
def sacar_notas( valor  ):
    return -3

notas=sacar_notas(-3)
print("el valor de notas",notas)

#Ejercicio 2
""""

Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida: El valor de "s" es "valor de s" y el valor de y es
"valor de y"
"""

def sacarListado(s,y):
    print(f'el valor de s es {s} y el valor de y es {y}')
    print('el valor de s es ' + str(s) + ' y el valor de y es ' + str(y))
    print('el valor de s es ', s, ' y el valor de y es ', y)
    print(f'el valor de s es %s y el valor de y es %s' %(s, y))

sacarListado(25,10)
# EJERCICIO 3

"""
    Declarar una variable con nombre "name",
    que tenga el valor de Juan "El profesor"
"""
def imprimir_comilla(cadena):

    print(cadena)

name="Juan 'El profesor'"
imprimir_comilla(name)
name2="Juan \"El profesor\""
imprimir_comilla(name2)
name3='Juan "El profesor"'
imprimir_comilla(name3)
# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""

def concantena(cadena1,cadena2):
    return cadena1+ " "+cadena2

print( "Resultado :"+concantena("Juan","'El profesor'"))

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""
def tranformacionFrase(cadena,num):
    if num==1 :
        return cadena.title() 
    elif num== 2:
        return cadena.upper()
    elif num==3:
        return cadena.lower()
    else :
        return cadena
    
print(" primera mayusucula "+tranformacionFrase("no cuentes los días, haz que los días cuente",1))
print(" mayusucula "+tranformacionFrase("no cuentes los días, haz que los días cuente",2))
print(" minusculas "+tranformacionFrase("no cuentes los días, haz que los días cuente",3))
print(" igual "+tranformacionFrase("no cuentes los días, haz que los días cuente",41))
# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""
def operacion(num1,num2,tipo):
    if tipo == 1 :
        return num1+num2
    elif tipo == 2 :
        return num1+num2

    elif tipo == 3 :
        return 2+num1*num2
    
    elif tipo == 4:
        return num1**num2
    elif tipo == 5:
        return round(num1,num2)
    else :
        return 0


print("suma ",operacion(26,35,1))
print("multiplicacion",operacion(26,35,2))
print("operacion",operacion(26,35,3))
numelevado=operacion(3,9,4)
print("elevado",numelevado)
print ("redondeo",operacion(numelevado,2,5))
valor=type(numelevado)
print ("tipo " ,valor)


numelevado=-numelevado
print ("valor y su valos absolto",numelevado,abs(numelevado))


    
    



#Ejercicio 7
#Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)


def max_min(lista):
    return(max(lista),min(lista))



L = [3, -6, 4, -10, 2.6666]
print("Lista",L)
print("maxi y mino",max_min(L))


#Ejercicio 8
"""Tratar de reemplazar los valores que faltan en este listado --> por un -1
L = [10, None, 8, 5, None, 20]
1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores.
 2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])

"""





def cambiar_valores(L):
    L[1] = -1
    L[-2] = -1
    return L

lista = [10, None, 8, 5, None, 20]
print(lista)

print(cambiar_valores(lista))


def sacadDaaFrame(L):
    return pd.DataFrame(L, columns=["listadoA"])

L = [10, None, 8, 5, None, 20]
print (sacadDaaFrame(L))
