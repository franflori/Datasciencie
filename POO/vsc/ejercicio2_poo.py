# EJERCICIO 1
"""
    Crea una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    mostrar(): Muestra los datos de la persona.
    esMayorDeEdad(): Devuelve un valor indicando si es mayor de edad.
"""
class Persona:
    def __init__(self,nombre,edad,DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
        
    def mostrar(self):
        return print ("Datos",self.nombre,self.edad,self.DNI)
    def esMayorDeEdad(self):
        if(self.edad>=18):
            return True
        return False

persona1=Persona("Pepe",28,"52012309120")
persona1.mostrar()
if persona1.esMayorDeEdad():
    print("Es mayor de edad ",persona1.nombre)
else :
    print("Es menor de edad ",persona1.nombre)
    

# EJERCICIO 2
"""
    Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
    Construye los siguientes métodos para la clase:

    Un constructor, donde los datos pueden estar vacíos.
    El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    mostrar(): Muestra los datos de la cuenta.
    ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos si es saldo negativo.
"""
class Cuenta:
    titular=""
    _cantidad=0.0
    def __init__(self,titular,cantidad) :
        self.titular=titular
        self._cantidad=cantidad
    
    def mostrar(self):
        return "Cliente :",self.titular,self._cantidad
    
    def ingresar(self,cantidad):
        if(cantidad>0):
            self._cantidad+=cantidad
        else:
            return print("no se puede ingresar numero negativos")

    def retirar(self,cantidad):
        self._cantidad-=cantidad
        if (self._cantidad<0):
            return  print("Estas en número rojos")
    


cliente1=Cuenta("Pepep",53.23)
print(cliente1.mostrar())




# 1) Ingresar en positivo
cliente1.ingresar(20)
print(cliente1.mostrar())
# 2) Ingresar negativo
cliente1.ingresar(-23)
print(cliente1.mostrar())
# 3) Retirar dinero
cliente1.retirar(60)
print(cliente1.mostrar())
# 4) Retirar dinero en número rojos
cliente1.retirar(160)
print(cliente1.mostrar())

# EJERCICIO 3

"""
    Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior.
    Cuando se crea esta nueva clase, además del titular y la cantidad se
    debe guardar una bonificación que estará expresada en tanto por ciento.
    Construye los siguientes métodos para la clase:
    Un constructor.
    En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad,
    por lo tanto hay que crear un método esTitularValido() que devuelve verdadero
    si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
    Además la retirada de dinero sólo se podrá hacer si el titular es válido.
    El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
    Piensa los métodos heredados de la clase madre que hay que reescribir.
"""
class CuentaJoven(Cuenta):
    edad=0
    bonificacion=0
    def __init__(self,titular,cantidad,edad,bonificacion):
        super().__init__(titular,cantidad)
        self.edad=edad
        self.bonificacion=bonificacion

    def mostrar(self):
        return "Cliente Cuenta Joven:",self.titular,self._cantidad,self.edad



    def esTitulaValido(self):
        if self.edad>=18 and self.edad<25:
            return True
        return False

    def retirar(self,ingreso):
        if(self.esTitulaValido()):
            print("puede retirar")
            super().retirar(ingreso)
        else:
            return print ("no puede retirar no tiene la edad")

cliente2=CuentaJoven("Pepep",53.23,22,22)
print(cliente2.mostrar())
cliente2.retirar(100)
cliente2.ingresar(20)
print(cliente2.mostrar())
# 1) Mayor de edad

# 2) Menor de edad

cliente3=CuentaJoven("nene",53.23,10,22)
cliente3.mostrar()


cliente3.retirar(23)