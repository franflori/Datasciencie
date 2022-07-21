# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""



def max(x,y):
    if (x>=y):
        return x
    else :
        return y

# EJERCICIO 2

"""
    Definir una función max_de_tres(), 
    que tome tres números como argumentos y 
    devuelva el mayor de ellos.
"""

def max_de_tres(num1,num2,num3):
    numMaximo=num1
    if (num1<num2):
        numMaximo=num2
    if(numMaximo<num3):
        numMaximo=num3
    return numMaximo 
    
    
    

# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista 
    o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, 
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud(cadena):
    cont=0
    for i in cadena:
        cont+=1
    

    return cont


# EJERCICIO 4

"""
    Escribir una función que tome un carácter y devuelva True si es una vocal,
     de lo contrario devuelve False.
"""

def es_vocal(valor):
    if(valor[0].upper()=="A" or valor[0].upper()=="E" or  valor[0].upper()=="I" or 
    valor[0].upper()=="O" or valor[0].upper()=="U"):
        return True
    else :
        return False

# EJERCICIO 5

"""
   5) - Escribir una función sum() y una función multip() que sumen y 
   multipliquen respectivamente todos los números de una lista. 
   Por ejemplo: sum([1,2,3,4])
    debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
def suma(lista):

    resultado=0
    for x in lista:
        resultado=resultado+x
    return resultado

def multip(lista):
    resultado=1
    for x in lista:
        resultado=resultado*x
    return resultado

   




numero1=0
while True:
        try:
            numero1 = int(input("Elija  primero número comparar "))
          
            break
        except Exception as e:
            print("No es un número")
           
    


numero2=0
while numero2==0:
        try:
            numero2 = int(input("Elija  segundo número comparar "))
          
            break
        except Exception as e:
            print("No es un número")



print("El numero mayor de es "+str(max(numero1,numero2)))

numero3=0
while numero3==0:
        try:
            numero3 = int(input("Elija  tercer número comparar "))
          
            break
        except Exception as e:
            print("No es un número")





print("El numero mayor de es "+str(max_de_tres(numero1,numero2,numero3)))


cadena=input("Introduzca la cadena medir la cadena ")

print("la longitud de la cadenas es "+str(longitud(cadena)))

caracter=input("Introduzca la cadena comapara ")

if(es_vocal(caracter)):
    print("Es una vocal",caracter )
else :
    print("No es una vocal", caracter)

listado = [1,4,7,3,21]
print("la longitud de la cadenas es "+str(longitud(listado)))


print(listado)
print("La suma del listado es "+(str(suma(listado))))
print("La producto del listado es "+(str(multip(listado))))

print("Enhorabuena acabaste los ejercicios")


