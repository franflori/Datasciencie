import pandas as pd

# EJERCICIO 1


# 1) Crea una lista de nombre "Concursante" que contenga los siguientes valores:
    # "Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"

Concursante=["Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"]
# 2) Crea una lista de nombre "Resultados" que contenga los siguientes valores:
    # 20, 30, 50, 20, 10, 5, 60, 40

Resultados=[20, 30, 50, 20, 10, 5, 60, 40]

# 3) Crea un diccionario con los concursantes y los resultados.
diccionario={"Concursantes":Concursante,"Resutaldos":Resultados}
print(diccionario)

# 4) Crea un dataframe vacio y apendiza los concursantes y los resultados mediante el empleo de un bucle for


def recorrer(diccionario):
    df=pd.DataFrame()
    for  key in diccionario:
        print(key)
        print(diccionario[key])
        df[key]=diccionario[key]  
    return df      

dfconcursante=recorrer(diccionario)

print(dfconcursante)



# 5) Con ayuda de loc filtra los resultados obtenidos desde Pedro hasta Lara.

def buscar_indice(df,cadena):
    return df.loc[df.Concursantes==cadena]


df_primero=buscar_indice(dfconcursante,"Pedro")
df_segundo=buscar_indice(dfconcursante,"Lara")
print (df_primero.index[0],df_segundo.index[0])
valor1=df_primero.index[0]
valor2=df_segundo.index[0]
print(dfconcursante.loc[valor1:valor2,:])


# 6) Con ayuda de loc filtra los resultados obtenidos mayores o iguales a 40

print(dfconcursante.loc[dfconcursante["Resutaldos"] >= 40])

# 7) Muestra el concursante con la mayor puntuación
print(dfconcursante.Resutaldos.max())
print(dfconcursante.max())

# 8) Muestra el concursante con la menor puntuación
print(dfconcursante.min())

# 9) Modifica con la ayuda de loc los valores 20 por 0
dfconcursante.loc[dfconcursante["Resutaldos"] == 20, 'Resutaldos'] = 0

print(dfconcursante)

# 10) Modifica Concursante "Juan" su puntuación por "None" con ayuda de .loc


dfconcursante.loc[dfconcursante["Concursantes"] == "Juan",'Resutaldos']=None

print(dfconcursante)

# EJERCICIO 2 (3)

"""
    Escribe un programa que pida dos palabras y diga si riman o no.
    Si coinciden las tres últimas letras tiene que decir que riman.
    Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
"""

def compararCadena(cadena1,cadena2):
    Cadena="No rima"
    valcadena1=len(cadena)
    valcadena2=len(cadena2)
    if(cadena1[valcadena1-1]== cadena2[valcadena2-1]) &  (cadena1[valcadena1-2]== cadena2[valcadena2-2]) &  (cadena1[valcadena1-3]== cadena2[valcadena2-3]):
        Cadena="Rima"
    elif(cadena1[valcadena1-1]== cadena2[valcadena2-1]) &  (cadena1[valcadena1-2]== cadena2[valcadena2-2]):
        Cadena="Rima un poco"
    return Cadena
    

cadena=input("Introduce primera palabra: ")
cadena2=input("Introduce segunda palabra: ")

valorcadena1=len(cadena)
valorcadena2=len(cadena2)
if(valorcadena1<3 or valorcadena2<3) :
    print("No se puede comprobar las cadenas menor 3",cadena)
else :
    print(compararCadena(cadena,cadena2))