# EJERCICIO 1

"""
    Crear un pequeño programa que calcule la multiplicación de 2 números (x, y)

    x = 3, y = 5
    x = 7, y = 3
"""

# a) Con una función (por ejemplo funcion_multiplicar)




def multiplicar(x,y):
    return x*y


print(multiplicar(5,4))

# b) Con la función lambda (Tal vez puedes ir a repasarlo)

def multipiLamda(x,y):
    return (lambda x,y : x*y)(x,y)


print("landa",(lambda x,y : x*y)(3,5))

print("nuevos, ",multipiLamda(5,5))

# c) Realizarlo con entrada de teclado (input)

print(multiplicar(int(input("escriba un número: ")),int(input("escriba un número: "))))

# EJERCICIO 2

"""
    -A-

        Dado un string:

        "Level"

        ¿Es un palíndromo?
"""

"""
    -B-

        ¿Y este string?

        "level"

        Nota: "Es un palíndromo si se invierte el orden del string, el resultado es exactamente el mismo"
"""
def palidromo (cadena):
    inv=cadena[::-1]
    if (inv==cadena):
        return True
    else:
        return False
   
    

cadena=input("Escribe palabra comparar palidromo: ")
if palidromo(cadena):
    print("la palabra es palindromo",cadena)
else :
     print("la palabra NO es  palindromo",cadena)

# EJERCICIO 3

"""
    Dado 2 strings:

    S1 = "Hi!"
    S2 = "Hello!"

    Imprimir las letras que son comunes
"""

def letraComunes(cadena1,cadena2):
    solucion=[]
    for letra in cadena1:
        if letra in cadena2 and letra not in solucion:
            solucion.append(letra)
    return solucion



print(letraComunes(input("Escribe  1 palabra para comparar  "),
                       input("Escribe  2 palabra para comparar  ")) )


