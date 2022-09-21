# EJERCICIO 1
"""
    1) Crea el siguiente programa:
    Una clase de nombre Librería
    Inicia los siguientes atributos: nombre, sección, editorial y año
    Crea una segunda clase con nombre Rosalia que herede la clase librería.
    En esta clase Rosalia, crea una función "result" cuyo resultado sea los datos de los libros.
    declara los Objetos siguientes:
    libro1 --> Oceanarium, Ciencia, Impedimenta, 2021
    libro2 --> 33 Botones, Novela negra, Atlantis, 2022
    libro3 --> Venganza en Compostela, Historia, Universo de letras, 2022
"""
class Librería:
   

    def __init__(self, nombre,sección,editorial,año):
        self.nombre=nombre
        self.sección=sección
        self.editorial=editorial
        self.año=año

class Rosalia(Librería):
    def result(self):
        return f"El libro nombre {self.nombre} seccion {self.sección} editorial {self.editorial} de {self.año} "


libro1 = Rosalia("Oceanarium", "Ciencia", "Impedimenta", 2021)
print("El libro 1",libro1.result())


libro2 = Rosalia(" 33 Botones", "Novela negra", "Atlantis", 2022)
libro3 = Rosalia("Venganza en Compostela", "Historia", " Universo de letras", 2022)
print("El libro 2",libro2.result())
print("El libro 3",libro3.result())


# EJERCICIO 2
"""
    2) Crea otra libraría de nombre MiLibro, que corresponde a una nueva clase,
    define una función de nombre misLibros, cuyo resultado sea los datos de los libros:
    libro4 --> Mi primera Novela, Novela, Bruño, 2019
    libro5 --> Gatos, Literatura, Listado, 2018
"""

class MiLibro (Librería):
    def misLibros(self):
        return f"libro biblioteca MiLibro {self.nombre} seccion {self.sección} editorial {self.editorial} de {self.año} "

   
        
libro4=MiLibro("Mi primera Novela", "Novela", "Bruño", 2019)
libro5=MiLibro("Gatos", "Literatura", "Listado", 2018)     
def media(lista):
    return sum(lista)/len(lista)  

print(libro4.misLibros())
print(libro5.misLibros())
operacion=media([libro4.año,libro5.año])
print("La operacios es",operacion)



