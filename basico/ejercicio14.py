import pandas as pd

# EJERCICIO 1

"""
    Cada número es la suma de los 2 anteriores:

    0-1-1-2-3-5-8-13-21-34...

    Se pide programar esa secuencia con Python.

    Nota:

    Apendiza elementos hasta tener 10 primeros resultados.

    (los 10 números indicados desde 0 hasta 34)

    Si sabes, hazlo de varias formas diferentes
"""

def fibonacci(numero):
    lista=[]
    valor1=0
    valor2=1
    lista=[]
    lista.append(valor1)
    lista.append(valor2)
    for i in range(2,numero):
       
        valor1,valor2=valor2,valor1+valor2
        lista.append(valor2)
    return lista

print(fibonacci(10))


def fibonacciRecusivo(numero,valor1,valor2,lista):
    if(numero==0):
        return  lista.appen(valor1+valor2)
    else :
        fibonacciRecusivo(numero-1,valor2,valor1+valor2,lista)







#lista=[]
#lista.append(0)
#lista.append(1)
#lista=fibonacciRecusivo(10,0,1,lista)
#print (lista)


# EJERCICIO 2

# Cada número es la suma de los 2 anteriores:

# 0-1-1-2-3-5-8-13-21-34...

# Se pide programar para los números de fibonacci mayores de 1000

# Primero muestra los valores de 0 hasta 1000000, crea una lista
# con ese listado crea una segunda lista con los mayores de 1000


def fibonacciMayoresque(numero,mayores):
    lista=[]
    valor1=0
    valor2=1
    i=0
    
    while i<numero:
       
        valor1,valor2=valor2,valor1+valor2
        if(valor2>mayores):
            lista.append(valor2)
            i+=1
    return lista

print(fibonacciMayoresque(10,1000))


# EJERCICIO 3

# Se pide crear un NUEVO dataframe para cada uno de los siguientes casos

# planteados y que están relacionados con el Titanic DataSet

# (antes debéis de cargar el archivo como df)

# 1) Leer el archivo train.csv del titanic dataset

df = pd.read_csv("./basico/datos/train.csv")

# Descomentar para ejecutar:
print(df)

# 2) Crear un dataframe de nombre df_sobreviven refiriéndose a un dataframe en el que todos los pasajeros sobreviven

df_sobreviven=df[df.Survived ==1]
print  (df_sobreviven.head)
print  (df_sobreviven.count())
    # NOTA: si al principio no estás seguro del resultado, puedes usar value_counts() para comprobar tu resultado

# 3) Crear un dataframe de nombre df__no_sobreviven refiriéndose a un dataframe en el que NINGUNO de los pasajeros sobrevive
df_no_sobreviven=df[df.Survived ==0]

print (df_no_sobreviven)
# 4) DataFrame de hombres que no sobrevivieron en el titanic
df_No_sobrevive_hombre=df_no_sobreviven[df_no_sobreviven.Sex=="male"]

print (df_No_sobrevive_hombre)
# 5) DataFrame de hombres qudf_no_sobrevivene si sobrevivieron en el titanic
df_SI_sobrevive_hombre=df_sobreviven[df_sobreviven.Sex=="male"]
print (df_SI_sobrevive_hombre)
# 6) DataFrame de mujeres que no sobrevivieron en el titanic
df_No_sobrevive_mujer=df_no_sobreviven[df_no_sobreviven.Sex=="female"]
print (df_No_sobrevive_mujer)
# 7) DataFrame de mujeres que si sobrevivieron en el titanic
df_SI_sobrevive_mujer=df_sobreviven[df_sobreviven.Sex=="female"]
print (df_SI_sobrevive_mujer)