import math

# EJERCICIO 1

"""
    Una población distribuida normalmente tiene una media de 100 y una desviacion estándar de 20.
    ¿ Cuál es la puntuación Z de una media muestral de 110, tomada de una muestra de tamaño 4?
"""



def calculoDesviacion(s,muestra):
    return s/math.sqrt(muestra)

def caculoz(µ,x,s):
    return round((x-µ)/s,2)
    

µ = 100
s = 20
x = 110
n = 4
desviacion=calculoDesviacion(s,n)

print(desviacion)

Zscore=caculoz(µ,x,desviacion)
print(Zscore)

# EJERCICIO 2

"""
    El tiempo medio conocido que se tarda en entregar una pizza es de 22.5 minutos con una desviación estándar de 2 minutos.
    Pedí pizza todas las semanas durante las últimas 10 semanas y obtuve un tiempo de 21.5 minutos.
    ¿Cuál es la probabilidad de obtener este promedio?
"""

µ = 22.5
s = 2
x = 21.5
n = 10

desviacionPiza=calculoDesviacion(s,n)

print("Pizza",desviacionPiza)



ZscorePi=caculoz(µ,x,desviacionPiza)
print(ZscorePi)

# EJERCICIO 3

# Si sigo pidiendo pizzas por la toda la eternidad. ¿A qué nivel puedo esperar que se acerque este promedio?