 #Ejercicio 1

"""
    Definir una función inversa() que calcule la inversion de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
"""

def inversa(cadena):
    solucion=""
    logintud=len(cadena)
    for num in range(logintud-1,-1,-1):
        solucion=solucion+cadena[num]
     

    return solucion


# Ejercicio 2

"""
    Definir una funcion es_palindromo() que reconoce palindromo 
    palabras  que tiene el mismo aspecto escritas invertidas), ejemplo: es_palindromo("radar")
    tendría que devolver True.
"""

def es_palindromo(candena):
    logintud=len(cadena)
    
    for num in range(0,logintud,1):
       
        if(candena[num]!=candena[-(num+1)]):
            return False
       
   
    return True

# Ejercicio 3

"""
    Definir una funcion superposicion() que tome dos listas y devuelva True si tiene al
    menos 1 elemento en común o devuelva False en caso contrario. Escribe la función usando el bucle for 
    aninado.
"""

def superposicion(lista1,lista2):

    for x in lista1:
       
        if(x in lista2):
            return True
    
    return False



cadena=input("Introduzca la cadena invertir la cadena ")
print("la cadena original es "+cadena + " y la inversa es " +inversa(cadena))

palabraPalindromo=input("Introduzca la cadena es palidromo ")

if (es_palindromo(palabraPalindromo)):
    print ("La palabra es un "+palabraPalindromo+ " palindromo")
else :
     print ("La palabra NO es un "+palabraPalindromo+  " palindromo")

listado = [1,4,7,3,21]
listado2 =[5,29,212]

if (superposicion(listado,listado2)):
    print ("Al menos tiene un elemento comun",listado,listado2)
else :
    print ("NO tiene ningun elemento comun las lista",listado,listado2)

listado = [1,4,7,3,21]
listado2 =[5,29,212,21]
if (superposicion(listado,listado2)):
    print ("Al menos tiene un elemento comun",listado,listado2)
else :
    print ("NO tiene ningun elemento comun las lista",listado,listado2)


