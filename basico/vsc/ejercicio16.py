import pandas as pd
import matplotlib.pyplot as plt

# EJERCICIO 1

# 1) Lee con pandas el archivo train.csv correspondiente al titanic dataset

df = pd.read_csv("./datos/train.csv")

# Descomentar para ejecutar:
print(df)


"""
    2) Hacer un bucle for para automatizar las gráficas de pd.crosstab

    Se pide relacionar la columna Survived con Pclass, Sex y Embarked

    Nota:

    Se pide que dentro del bucle for se encuentre la gráfica requerida.

    Entonces, en una sola celda, tenemos 3 gráficas mostradas y todo automatizado.
"""


def pintar(df,campos):
    for campo in campos:
        figura=pd.crosstab(df[campo], df["Survived"]).plot(kind="bar")

 
        plt.show()
  
#pintar(df,["Pclass","Sex","Embarked"])
"""
    3) Hacer una función para automatizar las gráficas de pd.crosstab

    Se pide relacionar la columna Survived con Pclass, Sex y Embarked

    NOTA:

    Se pide definir una función (1 vez por ello)

    y hacer llamadas a la función (3 en este caso, para: Pclass, Sex, Embarked)
"""

# EJERCICIO 2

# Ejercicio de obtener los valores que muestra el pd.crosstab de Sex y Pclass sin usar el propio pd.crosstab

# 1) Imprime nuevamente los primeros 5 valores

print(df.head())
# 2) Usando value_counts() observa cuantos hombres y mujeres hay

    # (No hace falta plotear, simplemente mostrar los números de cada)
print(df.Sex.value_counts())

# 3) Sin usar value_counts() observa cuantos hombres y mujeres hay (con un algoritmo)
def contarSex(personas):
    total=0
    hombre=0
    mujer=0
    for persona in personas :
        total+=1
        if persona == "male":
            hombre+=1
        if persona=="female":
            mujer+=1
      

    return total,hombre,mujer


print(contarSex(df["Sex"]))
  

"""
    4) Ahora haz lo mismo de otra forma

    En esta ocasión se pide que:

    crees un dataframe con el formato del original,

    bajo la permisa que sea un dataframe con todo hombres (primeramente) y con todo mujeres (a continuación)

    (2 DataFrames por tanto)

    Y observes si el número de filas de ambos nuevos DataFrames coincide con los valores anteriores
"""

df_hombre=df[df.Sex=="male"]
df_mujer=df[df.Sex=="female"]
print (len(df_hombre),len(df_mujer))