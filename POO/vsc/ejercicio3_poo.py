# EJERCICIO 1

"""
    Crearemos una clase llamada NumeroComplejo.
    Este tipo tiene un atributo x para la coordenada en x e y para la coordenada en y.
    Representa un número complejo de la forma (x, y).
"""


class NumeroComplejo:
    x=0
    y=0

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    
    def imprimir(self):
        print(f"El numero x {self.x} y el numero y es {self.y}")

    def __str__(self):
       
        return f"El numero complejo es ({self.x},{self.y})"
    
    def comparar(self,num2):
        if self.x==num2.x and self.y==num2.y:
            return True
        return False
    


    
    
# EJERCICIO 2

"""
    Ahora defina dentro de la clase NumeroComplejo un función imprimir
    donde muestre los valores de x e y.
"""
 
  
# EJERCICIO 3

"""
    Define la función str para la clase NumeroComplejo
    para poder imprimir usando la función print.
"""

numero=NumeroComplejo(5,6)
print(numero.x)
print(numero.y)
numero.imprimir()
print(numero)


print(numero)

numer2=NumeroComplejo(5,6)
print(numer2)
print(numero.comparar(numer2))

num3=NumeroComplejo(4,6)

print(num3)
print(num3.comparar(numer2))

# EJERCICIO 4

"""
    Define una función que compara dos números complejos,
    ya que si dos objetos distintos tienen sus atributos iguales,y
    sino NO se consideran iguales.
"""

# EJERCICIO 5

"""
    Realiza un método que sume dos numeros complejos sin modificiar los objetos originales,
    ya que se retorna un nuevo numero NumeroComplejo.
"""