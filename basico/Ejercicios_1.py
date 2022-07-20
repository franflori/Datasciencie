#Importar librerias

#Ejercicio 1
"""
    Describe una variable con nombre "notas" que tenga el valor de -3, muestra su valor.
"""
notas = -3
print(notas)

#Ejercicio 2
""""

Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida: El valor de "s" es "valor de s" y el valor de y es
"valor de y"
"""
s = 25
y = 10
print(f'el valor de s es {s} y el valor de y es {y}')
print('el valor de s es ' + str(s) + ' y el valor de y es ' + str(y))
print('el valor de s es ', s, ' y el valor de y es ', y)
print(f'el valor de s es %s y el valor de y es %s' %(s, y))

#Ejercicio 7
#Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)

L = [3, -6, 4, -10, 2.6666]
print(L)
print(max(L),min(L))


#Ejercicio 8
"""Tratar de reemplazar los valores que faltan en este listado --> por un -1
L = [10, None, 8, 5, None, 20]
1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores."""

L = [10, None, 8, 5, None, 20]
L[1] = -1
L[-2] = -1
print(L)

""""2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])"""
"""
import pandas as pd
nuevo=[10, None, 8, 5, None, 20]
df=pd.DataFrame(nuevo)
print(df)


"""
import pandas as pd
nuevo=[10, None, 8, 5, None, 20]
df=pd.DataFrame(nuevo)
print(df)