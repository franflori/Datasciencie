
import numpy as np
# EJERCICIO 1

# Crea una matriz con ayuda numpy:

# 1) Cuya matriz contenga 4 filas por 4 columnas de ceros

# 2) Apartir de la matriz de ceros crea la matriz identidad

nueva=np.zeros((4,4), int)
print (nueva)

def identidad(matriz):
    for i in range(0,matriz.shape[1]):
        matriz[i,i]=1
    return matriz


print(identidad(nueva))
   


# EJERCICIO 2

# Crea una matriz con ayuda numpy:

# Primera fila contenga: 3, 6, 8
# Segunda fila contenga: 20, 5, 7
# Tercera fila contenga: 10, 14, 1

# 1) Crea la transpuesta de esta matriz

# 2) Muestra el tamaño de la matriz

# 3) Muestra las dimensiones

# 4) ¿La matriz tiene valores menores de 0?

# 5) ¿La matriz tiene algún valor mayor de 10?

# 6) Coge una muestra de 5 valores de esa matriz usando linespace

# 7) La matriz contiene el valor 7

# 8) Crea una copia de esa matriz en una única dimensión

# 9) Crea una copia de esa matriz en una única dimensión, en este caso usando un bucle y una lista vacia

# 10) Realiza a esta última matriz creada con flatten la potencia de 3


A = np.array([[ 3, 6, 8], [20, 5, 7], [10, 14, 1]])

print ("matriz",A)
print ("Traspuesta",A.T)
print ("tamaño",A.size)
print ("dimesion",A.shape)
if np.all(A<0) :
    print ("Tienes valores mmenores que cero")
else :
    print (" NO Tienes valores mmenores que cero")

if np.any(A>10) :
    print ("Tiene algún valor mayor de 10")
else :
    print (" NO Tiene algún valor mayor de 10")

def valoresMuestra(matriz,valores):
    return np.linspace(matriz.min(),matriz.max(),valores)

nuevo=valoresMuestra(A,5)
print (nuevo)

if np.any(A==7) :
    print ("Tiene algún valor 7")
else :
    print (" NO Tiene algún valor 7")
print ("matriz",A)
if 7 in A :
    print ("Tiene algún valor 7")
else :
    print (" NO Tiene algún valor 7")
print (A.flatten())


def crear_lista(matriz):
    lista=[]
    for i in range(len(matriz[0])):
        for j in range(len(matriz[1])):
            lista.append(matriz[i][j])
    return lista

listaMat=crear_lista(A)
print (np.array(listaMat))

print(pow(A.flatten(),3))


