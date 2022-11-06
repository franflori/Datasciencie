# EJERCICIO 1

"""
    En 2007-2008, la altura promedio de un jugador de baloncesto profesional fue de 2,00 metros con una desviación estándar de 0,02 metros. 
    Harrison Barnes es un jugador de baloncesto que mide 2,03 metros. ¿Qué porcentaje de jugadores son más altos que Barnes?
"""

def caculoZscore(µ,x,s):
    return round((x-µ)/s,2)

µ=2.00
s=0.02
x=2.03
Zscore=caculoZscore(µ,x,s)
print(Zscore)


#Mirando la talba 1.5 nos da le 0.9032
x=0.9332
print(f"porcentaje de juegadores más alto es de {(1-x)*100}")
# EJERCICIO 2

# Chris Paul mide 1,83 metros. ¿Qué proporción de jugadores de baloncesto se encuentran entre las alturas de Paul y Barnes?


xPaul=1.83
ZscorePaul=caculoZscore(µ,xPaul,s)
print(ZscorePaul)
#Mirando la talba -8.5 nos da le 0
proporción=93.32-0
print("Jugadores se encuentra en ",proporción)

# EJERCICIO 3

"""
    El 92 % de los candidatos obtuvo una puntuación tan buena o peor que la de Steve.
    Si el puntuación promedio fue 55 con una desviación estándar de 6 puntos, ¿cuál fue el puntuación de Steve?
"""
# 92 -----> 1.41
#1.41=(x-55)/6 --> 1.41*6=x-55 -->
#x=(1.41*6)+55
Zscore=1.41
µ=55
s=6
def calculo(Zscore,µ,s):
    return (Zscore*s)+µ

print(f"Puntuacion Steve {calculo(Zscore,µ,s)}")
