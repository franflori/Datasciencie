# EJERCICIO 1

# Calcula la Z score para los siguientes casos:

# 1) µ = 54, s= 12, x = 68

# 2) µ= 25, s = 3.5, x = 20

# 3) µ = 0.01, s = 0.002, x = 0.01

def caculoz(µ,s,x):
    return round((x-µ)/s,2)

print(caculoz(54,12,68))
print(caculoz(25,3.5,20))
print(caculoz(0.01,0.002,0.01))



# EJERCICIO 2

"""
    El GPA promedio de los estudiantes en una escuela de secundaria local es 3.2 con una desviación estándar de 0.3.
    Jenny tiene GPA de 2.8 ¿A cuántas desviaciones estándar de la media está el GPA de Jenny?
"""

µ = 3.2
x = 2.8
s =0.3
print("ejercicio2",caculoz(µ,s,x))


µ = 3.2
x = 2.8
s =0.3
ZscoreJenny = round((x - µ)/ s, 2)
print("GPA Jenny",ZscoreJenny)

# EJERCICIO 3

"""
    Jenny está tratando de demostrarles a sus padres que le va mejor en la escuela que a su prima.
    Su prima asiste a una escuela de secundaria diferente donde el GPA promedio es 3.4 con una desviación estándar de 0.2.
    El prima de Jenny tiene un GPA de 3.0.¿se está desempeñando Jenny mejor que su prima según los puntajes estándar?
"""

µ = 3.4
x = 3
s =0.2
ZscorePrima = caculoz(µ,s,x)
print("Resultado prima",ZscorePrima)


# EJERCICIO 4

"""
    La puntuación de Kyle en una prueba de matemáticas reciente fue de 2.3 desviaciones estándar de la puntuación media del 78%.
    Si la desviación estándar de los puntajes de la prueba fue del 8%. ¿Qué puntaje obtuvo kyle en su prueba?
"""
µ = 0.78
Zscore = 2.3
s =0.08

x=(Zscore*s)+µ
print("Puntuaje kyle",x)
