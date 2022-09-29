#pip install scipy
#pip install statsmodels

import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
# Preprocesado y análisis
# ===================================================================================================
import statsmodels.api as sm
from scipy import stats
# Gráficos
# ===================================================================================================
import matplotlib.pyplot as plt

# EJERCICIO 1

# Dada estos valores: 15 16 17 16 21 22 15 16 15 17 16 22 14 13 14 14 15 15 14 15 16 10 19 15 15 22 24 25 15 16
df = pd.DataFrame({"X": [15, 16, 17, 16, 21 ,22, 15, 16, 15, 17, 16, 22, 14, 13, 14,
                         14, 15, 15, 14, 15, 16, 10, 19, 15, 15, 22, 24, 25, 15 ,16]})
print(df.head())

def pintarHistrograma(df,barra):
    plt.hist(df.X, bins=barra,
    color="green",
    histtype="bar",
    rwidth= 0.3)
    # cuadrícula
    plt.grid(True)
    # Etiqueta del eje de la X
    plt.xlabel("valores")
    # Etiqueta del eje de la Y
    plt.ylabel("Frecuencia")
    # titulo:
    plt.title("Histograma")
    # Mostrar el gráfico:
    plt.show()




# 1) Realiza un Histograma con tamaño de barra 2.

pintarHistrograma(df,2)

# 2) ¿Cuál es el número que más se repite?
print(df.X.value_counts())
print( df["X"].mode())

# 3) ¿Qué pasa si cambiamos a tamaño de barra 5?
pintarHistrograma(df,5)
# 4) ¿Qué pasa si cambiamos a tamaño de barra 20?


pintarHistrograma(df,20)

# 5) ¿Qué parece indicar el sesgo en la distribución?
#Segos positio a la derecha valorea atipoco a la derecha
