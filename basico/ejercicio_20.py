"""
    Basándote en la teoría explicada en clase sobre Python
    realiza los siguientes ejercicios
"""

# EJERCICIO 1

"""
    Definir una función generar_n_caracteres() que tome un entero n
    y devuelva el caracter multiplicado por n.
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

from signal import valid_signals


def generar_n_caracteres(n, caracter):
    final=""
    for num in range(1,n+1,1):
  
        final=final+caracter
       
    
    return final

# EJERCICIO 2

"""
    Definir un diagrama procedimiento() que tome una lista de números enteros
    e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7])
    debería imprimir lo siguiente:
"""
  

    # XXXX
    # XXXXXXXXX
    # XXXXXXX
def procedimiento(lista):
    for x in lista:
     
        cadena=""
        for num in range(0,x,1):
            cadena=cadena+"X"
        print(cadena)
  
    

# EJERCICIO 3

"""
    Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

def mas_larga(lista):
    maximo=0
    masLarga=""
    for x in lista:
       
        if(len(x)>maximo):
            maximo=len(x)
            masLarga=x
   
    return masLarga

def mas_larga_cadena(lista):
    maximo=0
    masLarga=[]
    for x in lista:
       
        if(len(x)>maximo):
            masLarga=[]
            maximo=len(x)
            masLarga.append(x)
        elif(len(x)==maximo):
            masLarga.append(x)


   
    return masLarga

# EJERCICIO 4

"""
    Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
    y devuelva las palabras que tengan mas de n caracteres.
"""

def filtrar_palabras(lista, n):
    salida=[]
    for x in lista:
        if(len(x)>=n):
            salida.append(x)

    
    return salida

# EJERCICIO 5

"""
    Escribir un programa que ingrese una cadena de texto.
    El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def c_mayusculas(cadena):
    numMayscula=0
    for num in range(0,len(cadena),1):
      
        if(cadena[num]==cadena[num].upper()):
            numMayscula+=1



    return numMayscula

# EJERCICIO 6

"""
    Definir una tupla con 10 edades de personas.
        * Imprimir la cantidad de personas con edades superiores a 20.
"""

def mayores(tup):
    cont=0
    for t in tup:
      
       if(t>=20):
        cont+=1

    return cont


# EJERCICIO 7

"""
    Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
    También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

def main(lista,buscar):
    salida=[]
    for x in lista:
        if(x[0].upper()==buscar.upper()):
            salida.append(x)

    
   
    
    
    return salida

# EJERCICIO 8

"""
    Crear una función contar_vocales(),
    que reciba una palabra y cuente cuantas letras "a" tiene,
    cuantas letras "e" tiene y así hasta completar todas las vocales.
    Se puede hacer que el usuario sea quien elija la palabra.
"""

def contar_letra(cadena,vocal):
    cont=0
    for num in range(0,len(cadena),1):

        if(cadena[num].upper()==vocal.upper()):
            cont+=1
        
    
    return cont


def contar_vocales(cadena):
   print(" Con la letra A ",contar_letra(cadena,"A"))
   print(" Con la letra E ",contar_letra(cadena,"E"))
   print(" Con la letra I ",contar_letra(cadena,"I"))
   print(" Con la letra O ",contar_letra(cadena,"O"))
   print(" Con la letra U ",contar_letra(cadena,"U"))



num=int(input("Introduzca numero repetir "))
caracter=input("Introduzca numero caracteres ")
print(generar_n_caracteres(num,caracter))


procedimiento([4, 0,9, 7])

palabras=["uno", "dos", "tres","cuatro"]
print (mas_larga(palabras))


palabras2=["uno", "dos","cuatra", "tres","cuatro"]
print (mas_larga_cadena(palabras2))



contar=int(input("minimo de palabra "))

print(filtrar_palabras(palabras2,contar))

cadena=input("Introduzca palabra contar Mayuscula ")
print(c_mayusculas(cadena))

edades = (20, 13, 30, 40,70,89,23,12,29)
print("El numero de mayores de 20 años  son",mayores(edades))


cadena=input("Introduzca palabra busca palabra")
print(main(palabras,cadena))


vocales=input("contral vocales.....")
contar_vocales(vocales)
