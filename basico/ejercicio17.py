# EJERCICIO 1

"""
    Crea la clase "matematicas" y dentro de esa clase crea las funciones suma y resta,
    en dichas funciones nos deberán devolver el resultado de la suma y de la resta, siguiendo los siguientes pasos:
"""

# Crea la clase matematicas
# crea la funcion suma en la cual se le pase un valor (x):
#           y = 10 + x
#           retornar el resultado
# crea la funcion resta en la cual se le pase un valor(x):
#           y = 10- x
#           retornar el resultado
# Imprime el resultado de la función suma y de la funcion resta para un valor de x = 5, x = 10

class Matematicas:
    
    def suma(x):
        return 10+x
    
    def resta(x):
        return 10-x
    


print(Matematicas.suma(5))
print(Matematicas.suma(10))

class Mat2:
    
    def inicializar(self,x):
        self.x=x

    def suma(self):
        a=10+int(self)
        print (a)
        return a
    
    def resta(self):
        b=10-self
        return b



"""
ma=Mat2 ()
ma.inicializar(5)
a=str(ma.resta(ma.x))
"""


# EJERCICIO 2

"""
    Crea dos clases una llamala "libros" y otra clase "materias".

    A la clase libros declara una función con nombre "tipos" y dentro de clase materias declara una función con nombre "asignaturas".

    A la función tipos retorne el valor name = "Data Science" y la función asignaturas retorne nombre = "Big Data"
"""
# 1) Prueba a retornar el resultados de la clase libros y la función tipos

# 2) Prueba a retornar el resultados de la clase materias y la función asignaturas

# 3) Prueba a retornar el resultados de la clase materias y la función tipos
    # ¿ Qué es lo que observas ?

class Libros:
    def tipos():
        return "Data Science"

class Materias:
    def asignaturas():
        return "Big Data"

print ("imprime a clase libros y la función tipo"+ Libros.tipos())

print ("imprime a clase materias y la función asignaturas"+ Materias.asignaturas())