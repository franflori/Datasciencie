# EJERCICIO 1

"""
    Dado este listado de números:

    -3, 150, 0, 499, 500, 1200, -350, 0, 750, 25

    Haz un pequeño algoritmo que haga lo siguiente:

    Si el número es negativo debe imprimir lo siguiente el valor es negativo
    Si es 0 debe imprimir un mensaje que indique: 0
    Si se encuentra entre 0 (no incluido) y 200 (si incluido), imprime 0,200
    Si se encuentra entre 200 (no incluido) y 500 (no incluido), debe imprimir (200, 500)
    Si es 500 debe continuar sin hacer nada
    Si se encuentra entre 500 (no incluido) y 1000 (no incluido) debe saltar automaticamente y dejar de testear (parar)
    Para el resto de números, debe decir: valor demasiado grande, desde 1000, en adelante

"""

# 1) Escribir en formato lista
listados=[-3, 150, 0, 499, 500, 1200, -350, 0, 750, 25]

# 2) Haz el propio ejercicio de programación planteado
def cambiarvalores(lista):
    cont=0
    for elemento in lista:
        if ( elemento<0):
            lista[cont]="El valor negativo"
        elif(elemento==0):
            lista[cont]="0"
        elif(elemento>0 and  elemento <=200 ):
            lista[cont]="0,200"
        elif(elemento>2000 and  elemento <500):
            lista[cont]=" (200, 500)"
        elif(elemento==500):
            continue
        elif(elemento>500 and  elemento <=1000):
            lista[cont]="saltar automaticamente y dejar de testear"
            break
        else:
            lista[cont]="valor demasiado grande, desde 1000, en adelante"




        cont+=1


    return lista

print(cambiarvalores(listados))

# EJERCICIO 2

# Dada la lista de nombre "listado" y de valores: 10, 20, 20, 30, 40, 40, 40

# 1) Crea la lista e imprimela

# 2) Haz un set de esa lista

# 3) Trata de buscar los números NO REPETIDOS de esa lista (sin usar set)

# Pista: Puedes almacenar todo en una nueva lista

listados=[-3, 150, 0, 499, 500, 1200, -350, 0, 750, 25]
listaset=set(listados)

def listaNoRepetidio(listado):
    lista=[]
    for elemento in listado:
        if elemento not in lista:
            lista.append(elemento)
    return lista

print (listaset)
print(listaNoRepetidio(listados))



# EJERCICIO 3

# Dados estos clientes:

# Usando el continue/break

# Trata de averiguar si un cliente concreto se encuentra en la BBDD (Base de Datos)

# "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"

listado_nombre=["Ana Pérez", "Juan García", "Andrés Álvarez",
"Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez",
"Alberto Delgado", "Susana Castro", "Luis González"]

def buscar_nombre(listado_nombre,cadena):
    for nombre in listado_nombre:
        if nombre==cadena:
            return True
    return False

cadena="Ana Pérez"
if(buscar_nombre(listado_nombre,cadena)) :
    print("SI se encuentra base datos",cadena)
else :
   print("NO se encuentra base datos",cadena)

cadena="Ana Perez"
if(buscar_nombre(listado_nombre,cadena)) :
    print("SI se encuentra base datos",cadena)
else :
   print("NO se encuentra base datos",cadena )