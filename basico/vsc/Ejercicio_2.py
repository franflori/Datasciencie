#Importar librerias
import pandas as pd

# EJERCICIO 1

"""
   Dado el siguiente listado: ["Python", "Matlab", "R", "VBA", "Julia", "C++"].

    Modifica con un algoritmo ese listado.

    Cuando encuentre Python debe poner un 1
    y cuando encuentre otro lenguaje de programacion, un 0
    es un simple ejemplo de modificación de valores en una lista.
"""
def cambiar_listado(listado):
    n=0
    for registro in listado:
        if registro=="Python":
            listado[n]=1
        else :
            listado[n]=0
        n+=1
    return listado
    
    


languages = ["Python", "Matlab", "R", "VBA", "Julia", "C++"]
print (languages)
print ("cambio",cambiar_listado(languages))
# EJERCICIO 2

"""
    Dada la siguiente lista:
    L = [10, None, 8, 5, None, 20]
"""
    # 1) Susitituir por -1 el valor None usando bucles y listas
    # 2) Creamos un dataframe con los valores de la lista y
    #     modificamos los "NaN" por un valor de -1 (Valores nulos, suma, etc..)
    # 3) Vuelve a escribir el listado con falta de valores (inicial),
    #     y sustituye por la media.
    # 4) Apendiza la columna con estos valores
    #     listado2 = [10, 20, 50, 30, 20, 0]
    # 5) Elimina la columna L


def eliminar_None(lista):
    for i in  range(0,len(lista)):
        if lista[i]==None:
            lista[i]=-1
    return lista



def sacarSumanValor_1(L):
    df=pd.DataFrame(L, columns=["listado"])
    print(df)
    df.listado=df.listado.fillna(-1)
    print(df)
    return df.listado.sum()


def sacarSumanValorMedia(L):
    df=pd.DataFrame(L, columns=["listado"])
    print(df)
    df.listado=df.listado.fillna(df.listado.mean())
    print(df)
    return df.listado.sum()

def apend(df):
    listado2 = [10, 20, 50, 30, 20, 0]
    df['listado2'] = listado2
    return df

def borrar(df):
    df = df.drop(["listado2"], axis=1)
    return df


lista = [10, None, 8, 5, None, 20]

print (lista)
print ("cambio",eliminar_None(lista))
lista = [10, None, 8, 5, None, 20]
print("suma con -1 es ",sacarSumanValor_1(lista))

print("solucion 2")
print("suma con media es ",sacarSumanValorMedia(lista))

df=pd.DataFrame(lista, columns=["listado"])
print("anadir2",apend(df))
print("borrar",borrar(df))



# EJERCICIO 3

"""
    Crear un listado con los siguientes numeros:
        10, 20, 30, 40 (nombra la lista con nombre: "listado")
"""
    # 1) Crea el listado e imprimelo:
    # 2) Apendiza el valor 50 ( si es posible)
    # 3) Modifica (si es posible) el valor 10 por 100

def listar(listado):
    return listado

def anadirvalor(listado):
    listado.append(50)
    return listado
def modificar(listado):
    listado[0] = 100
    return listado


listado = [10, 20, 30, 40 ]
print(listar(listado))
print(anadirvalor(listado))
print(modificar(listado))
# EJERCICIO 4

"""
    Da una lista de nombre "Temperatura" con valores: 10, 20, 30, 40, 50
"""
    # 1) Crea el listado e imprimelo:
    # 2) En este "Temperatura". ¿Cuál es el elemento en la posición (index) 1?
    # 3) ¿Y en la posición (index) 0?
    # 4) ¿Y en la posición (index) -1?

def print_posicion(listado,index):
        return listado[index]


Temperatura= [10, 20, 30, 40, 50]
print("Tenperatura",listar(Temperatura))
print ("indice 1",print_posicion(Temperatura,1))
print ("indice 0",print_posicion(Temperatura,0))
print ("indice -1",print_posicion(Temperatura,-1))


