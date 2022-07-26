import pandas as pd
# EJERCICIO 1

"""
    Escriba una función es_bisiesto() que determine si un año determinado es un año
    bisiesto. Un año bisiesto es divisible por 4, pero no por 100.
    También es divisible por 400.
"""

def es_bisiesto(anio):

    if (anio%4==0 and anio%100!=0) or anio%400==0:
        return True
    
    return False

# EJERCICIO 2

"""
    Haz un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años.
    Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos
    esos años si cada año se aplica la tasa de interés introducida.
    Recordar que un capital C dolares a un interés del x por cien durante n años
    se convierte en C * (1 + x/100)elevado a n (años). Probar el programa
    sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""

def hipoteca(dolares,interes,anio):

    total=dolares*(1+interes/100)**anio
    
    return total
   

# EJERCICIO 3

"""
    Este programa muestra primero el listado de categorías de películas
    y pide al usuario que introduzca el código de la categoría de la película
    y posterior a ello pide que el usuario introduzca el número de días de atraso,
    y así se muestra al final el total a pagar.
"""

# CATEGORIA     PRECIO  CODIGO  RECARGO/DIA DE ATRASO
# FAVORITOS      2.50      1          0.50
# NUEVOS         3.00      2          0.75
# ESTRENOS       3.50      3          1.00
# SUPER ESTRENOS 4.00      4          1.50

def main(codCategoria,dias):

    categoria=["FAVORITOS","NUEVOS","ESTRENOS","SUPER ESTRENOS"]
    precio=[2.50,3.00,3.50,4.00]
    codigo=[1,2,3,4]
    recargo=[0.50,0.75,1.00,1.50]
    df = pd.DataFrame({"categorias": categoria, "precios": precio,"codigos": codigo,"recargos": recargo})
    print(df)
    resultado=0 
    
    while True:
        df_selecionada=df[df.codigos==codCategoria]
    
    
        if(len(df_selecionada)>0):
            resultado=float(df_selecionada.recargos*dias)
            break
        else :
            print("No existe ningun el codigo ")
            codCategoria=int(input(" Introduczca Codigo de categoria "))



    
    return resultado

def comprobar_error_teclado( texto,type):
    while True:
        try:
            valor=type(input(texto))
            return valor
        except Exception as e:
            print("Error: %s" % str(e))


"""
print(comprobar_error("Prueba ",int))

print(comprobar_error("Prueba  float",float))
"""

#num=int(input("Introduzca el año si quiere saber si es bisiesto "))

num=comprobar_error_teclado("Introduzca el año si quiere saber si es bisiesto ",int)
if(es_bisiesto(num)):
    print("El años es bisisiteso",num)
else :
    print("El años NO  es bisisiteso",num)




#dolares=int(input("Introduzca cantidad de dolares "))
#interes=float(input("Introduzca tasa de interé  "))
#anio=int(input("Número de años "))
dolares=comprobar_error_teclado("Introduzca cantidad de dolares ",int)
interes=comprobar_error_teclado("Introduzca tasa de interés ",float)
anio=comprobar_error_teclado("Número de años ",int)
print("Capital Total ",hipoteca(dolares,interes,anio))

#codCategoria=int(input("Codigo de categoria "))
#dias=int(input("Número de dias  "))
codCategoria=comprobar_error_teclado("Codigo de categoria ",int)
dias=comprobar_error_teclado("Número de dias ",int)
print(" Total a pagar....",main(codCategoria,dias))


