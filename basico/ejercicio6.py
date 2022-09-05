# EJERCICIO 1

# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

listado = [30,20,10,50,40]


def muestra_max_min(lista):
    return max(lista),min(lista)

print("El maximo, y minimo lista son",listado,muestra_max_min(listado))

def  minimo(listado):
    numero=listado[0]
    for i in listado:
        if(numero>i):
            numero=i
    return numero

print (listado,min(listado))
print( "El minino del listado es ", minimo(listado))

# 2) Prueba con min(listado)

# 3) Realiza lo mismo pero con bucles y condicionales


# EJERCICIO 2

# Máximo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

# 2) Prueba con max(listado)

# 3) Realiza lo mismo pero con bucles y condicionales


def  maximo(listado):
    numero=listado[0]
    for i in listado:
        if(numero<i):
            numero=i
    return numero

print (listado,max(listado))
print( "El máximo del listado es ", maximo(listado))



# EJERCICIO 3

# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales

listaOrdena=[30, 20, 10, 50, 40]
def ordenarBucleMinMaxi(lista):
    ordenafinal=[]
    copia=lista
   
    maximo=len(lista)
    while maximo>0:
        ordenafinal.append(min(copia))
        copia.remove(min(copia))
        maximo=maximo-1


    return ordenafinal

def ordenaSort(lista):
    lista.sort(reverse=False)
    return lista

print ("menor",listaOrdena)
lismenor= ordenaSort(listaOrdena)
print ("menor",lismenor)
listaOrdena=[30, 20, 10, 50, 40]
print ("menor",listaOrdena)
listamin=ordenarBucleMinMaxi(listaOrdena)
print ("menor",listamin)




# EJERCICIO 4

# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# 1) Escribe el listado e ímprimelo

# 2) Prueba a usar sort()

# 3) Realiza lo mismo pero con bucles y condicionales



listaOrdena=[30, 20, 10, 50, 40]
def ordenarBucleMaxMin(lista):
    ordenafinal=[]
    copia=lista
   
    maximo=len(lista)
    while maximo>0:
        ordenafinal.append(max(copia))
        copia.remove(max(copia))
        maximo=maximo-1


    return ordenafinal

def ordenaSortM(lista):
    lista.sort(reverse=True)
    return lista

print ("MAYOR",listaOrdena)
listaMayo= ordenaSortM(listaOrdena)
print ("MAYOR",listaMayo)
listaOrdena=[30, 20, 10, 50, 40]
print ("MAYOR",listaOrdena)
listamax=ordenarBucleMaxMin(listaOrdena)
print ("MAYOR",listamax)





# EJERCICIO 5
"""
    Pendiente
"""