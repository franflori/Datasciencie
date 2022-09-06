
#import
import pandas as pd


# EJERCICIO 1

# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

# 1) Escribe el listado e ímprimelo

from csv import list_dialects


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

print ("menor - sin ordena",listaOrdena)
lismenor= ordenaSort(listaOrdena)
print ("menor",lismenor)
listaOrdena=[30, 20, 10, 50, 40]
print ("menor -sin ordena",listaOrdena)
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

print ("MAYOR  sin ordena",listaOrdena)
listaMayo= ordenaSortM(listaOrdena)
print ("MAYOR",listaMayo)
listaOrdena=[30, 20, 10, 50, 40]
print ("MAYOR sin ordena",listaOrdena)
listamax=ordenarBucleMaxMin(listaOrdena)
print ("MAYOR",listamax)




# EJERCICIO 5
"""
    Escribe el código necesario en Python para:
    * almacenar con una lista de nombre "módulos" las siguientes materias de un programa de Ciencia de Datos:
    * Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP.
"""

def imprimir(lista):
    for registro in lista:
        print( "Asignatura",registro)


modulos=["Big Data", "Python", "Algoritmos", "Machine Learning", "Deep Learning", "NLP"]
print (modulos)

# 1) Para ese listado imprime todas ellas, 1 a 1

imprimir(modulos)

"""
    2) dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas.
    y que forman la base de conocimientos iniciales para afrontar con éxito el resto de un programa.
    Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas)
    Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales" (por ejemplo)
    Imprime ese listado al terminar de almacenarlos.
"""
def asignatura_esencia(lista):
    esensiales=[]
    for registro in lista:
        if(registro=="Python")|(registro=="Algoritmos"):
            esensiales.append(registro)
    return esensiales


esensiales=asignatura_esencia(modulos)
imprimir(esensiales)


"""
    3) Crea un DataFrame, de nombre df con esa información en base
    a la siguiente relación de módulos y horas de clase módulos:
    Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP
    horas: 25, 15, 5, 15, 5, 10
"""
horas=[25, 15, 5, 15, 5, 10]

def CrearDataFrame(campo1,campo2):
    df=pd.DataFrame({"Modulos":campo1, "Horas": campo2})
    return df
    
df=CrearDataFrame(modulos,horas)
print(df)



# 4) De ese DataFrame, selecciona solamente la columna "horas" e imprímela
def ImprimirData(valor):
    print (valor)

print("LIstado 1")
ImprimirData(df.Horas)
print("LIstado 2")
ImprimirData(df["Horas"])
print("LIstado 3")
ImprimirData(df[["Horas"]])
# 5) Muestra el gráfico (plot) para la columna "horas"
pintarHoras =df["Horas"] 


def pintar(pintar):
  
    import matplotlib.pyplot as plt
    figure = pintar.plot(kind="bar")
    plt.show()

pintar(pintarHoras)


# 6) De ese DataFrame, selecciona solamente aquellas materias que tienen 20 o más horas de dedicación
print("tienen 20 o más horas")
ImprimirData(df[df["Horas"]>=20])

# 7) De ese DataFrame, selecciona solamente aquellas materias que tienen menos de 10 horas de dedicación

print("tienen 20 o más horas")
ImprimirData(df[df["Horas"]<=10])

# 8) De ese DataFrame, selecciona solamente (si fuera posible)
    # aquellas materias que tienen mas de 26 horas de dedicación
print("tienen mas de 26 horas")
ImprimirData(df[df["Horas"]>26])

# 9) Apendiza, (si puedes), una nueva columna llamada "docente" con el instructor encargado de la materia.

    # Y cuyos nombres serán: Enrique, Susana, Juan, Ana, Laura, Patricia

def AnadirDataFrame(df,lista,literal):
    df[literal]=lista
    return df


df=AnadirDataFrame(df,["Enrique", "Susana", "Juan", "Ana", "Laura", "Patricia"],"Docente")
print(df)




