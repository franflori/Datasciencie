# EJERCICIO 1
class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
      
    
    def cumpleaños(self):
        self.edad+=1
    
    def __str__(self):
        return f"Datos persona ({self.nombre},{self.edad})"


persona=Persona("Juan",18)
print(persona)
persona.cumpleaños()
print(persona)


"""
    Crea una clase persona. Sus atributos deben ser su nombre y su edad.
    Además crea un método cumpleaños, que aumente en 1 la edad de la persona.
"""

# EJERCICIO 2

"""
    Para la clase anterior definir el método str.
    Debe retornar al menos el nombre de la persona.
"""

# EJERCICIO 3

"""
    Extender la clase persona agregando un atributo saldo y un método transferencia(self, persona2, monto).
    El saldo representa el dinero que tiene la persona.
    El método transferencia hace que la Persona que llama el método le transfiera la cantidad monto al objeto persona2.
    Si no tiene el dinero suficiente no se ejecuta la acción.
"""
class PersonaExt(Persona):
    def __init__(self,nombre,edad,saldo):
        super().__init__(nombre,edad)
        self.saldo=saldo
   
    
    def transferencia(self,persona,monto):
        if(self.saldo>monto):
            self.saldo=self.saldo-monto
            persona.saldo=persona.saldo+monto
        else:
            print("No tiene saldo suficiente")

persona1=PersonaExt("Juan",18,25)
persona2=PersonaExt("Luis",20,25)
print(persona1)
print(persona2)
persona1.transferencia(persona2,20)
print(persona1)
print(persona2)
persona1.transferencia(persona2,20)
print(persona1)
print(persona2)

    