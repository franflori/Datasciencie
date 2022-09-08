import pandas as pd
import numpy as np

# EJERCICIO 1

"""
    1) Haz un programa que calcule los múltiplos de 3

    Para ello primero debe preguntarse al usuario cuántos múltiplos desea añadir.

    Nota: Puedes usar un bucle while si lo deseas

"""
def multiporwhile(numero):
    i=1
    lista=[]
    while i<=numero:
        print (f"3 * {i}= {i*3}")
        lista.append(i*3)
        i +=1
    return lista


lista=[]

#lista=multiporwhile(int(input("Numero multipo ")))


print(lista)

# 2) Haz lo mismo con np.arange
valor=1
#valor=int(input("Numero multipo "))
lista2=np.arange(3,3*valor+1,3).tolist()
print(lista2)


# EJERCICIO 2

"""
    Dado el listado del apartado 2

    Dada esta lista de variable "listado" y "valores": 10, 10, 20, 20, 20, 30, 40

    Se pide:
"""
listado=[10, 10, 20, 20, 20, 30, 40]
print (listado)

# 1) Crea un DataFrame con esa información e imprímelo
df=pd.DataFrame({"Listado":listado})

print(df)

# 2) Usa value_counts() para determinar cuántas repeticiones hay de cada número en esa columna

print ( df["Listado"].value_counts())

# 3) Haz un ".shape" a esa información del value_counts()

    # NOTA: Escribe: .shape justo al final
print ( df["Listado"].value_counts().shape)

# 4) A esa misma instrucción con value_counts() escribe al final ".values"

    # Y veras la información..

    # pasa esa información a lista si puedes

    # y guarda ese listado como "repeticiones"

repeticiones=df["Listado"].value_counts().values.tolist()
print ( df["Listado"].value_counts().values)
print(repeticiones)

# 5) A esa información de value_counts() añade al final ".index"

    # Y pasa posteriormente a lista esa información

    # y guarda ese listado con el nombre: "valores"
valores=df["Listado"].value_counts().index.tolist()
print(valores)

# 6) Crea un DataFrame con 2 columnas,

    # 1 para "valores"

    # 1 para "repeticiones"

    # llámalo: "df_value_counts" (por ejemplo)

    # Y observa..

df_value_counts=pd.DataFrame({"Valores":valores,"Repeticiones":repeticiones})

print (df_value_counts)

# 7) Haz lo siguiente: "df.value_counts()"
print(df.value_counts())

# 8) Observa si hay diferencias entre: "df" y "df_value_counts"

print(df_value_counts)

# EJERCICIO 3
"""
    Comparación de matrices

    Haz el código que testee si esas 2 matrices son iguales

    1)

    Dadas:

    matriz1 = np.array([[1,2],[3,4]])

    matriz2 = np.array([[1,2],[3,8]])

    PISTAS:
"""
matriz1 = np.array([[1,2],[3,4]])
matriz2 = np.array([[1,2],[3,8]])

def comparar_matriz(m1,m2):
    for i in range(2):
        for j in range (2):
            if m1[i,j]!=m2[i,j] :
                return False
    return True

if(comparar_matriz(matriz1,matriz2)):
    print ( " La matriz son iguales")
else :
    print ( " La matriz son distintas")


if(comparar_matriz(matriz1,matriz1)):
    print ( " La matriz son iguales")
else :
    print ( " La matriz son distintas")

   # -1- RECORRER MATRIZ1 Y MATRIZ2 CON LA PARAMETRIZACIÓN de i y j
  #  COMPROBAR: ( matriz1 [ i ][ j ] == matriz2 [ i ][ j ] )




   # -2- crear una variable contador (inicializada en 0)
   # y, cuando detecte, un número de una matriz en una posición concreta,

   # y sea diferente del número que tiene LA OTRA MATRIZ..entonces..

  #  -3- incremento 1 unidad en dicho contador:
  #  SI los números son DISTINTOS

   # --> entonces, que se incremente en 1 unidad..

  #  de tal manera que si ese contador=0 (al final)--> son todos iguales --> matriz1 = matriz2

  #  y si es distinto de 0 -> es que POR LO MENOS 1 vez encontró un número diferente

  #  matriz1 != matriz2

  #  -4- puedes usar np.arange( ) si lo deseas para las filas y para las columnas

 #   -5- recuerda el ejercicio del cronómetro para tener una referencia


def comparaM(m1,m2):
    return (m1==m2)
print(comparaM(matriz1,matriz2))
print(comparaM(matriz1,matriz2).all())