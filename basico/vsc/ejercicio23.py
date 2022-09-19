import pandas as pd
# Ejercicio 1



"""
    Desarrolla el siguiente ejercicios de POO:

   * Alumnos  -> Es la clase.
   * __init__ -> Es el método init
   * nombre, edad, asignatura y nota son las propiedades
   * Instanciamos..
   * los posibles alumnos (alumno1, alumno2, alumno3..) --> son los "objetos"
   * y el.__init__ los inicializa

   A continuación muestra la edad del alumno 2 y el alumno 3 y sus notas
"""
class Alumno:
    def __init__(self, nombre,edad,asignatura,nota):
        self.nombre=nombre
        self.edad=edad
        self.asignatura=asignatura
        self.nota=nota
    
    def getEdad(self):
        return self.edad
    
    def getNota(self):
        return self.nota


alumno1=Alumno("Pepe",21,"Matematica",5)
alumno2=Alumno("Juan",221,"Historia",10)
alumno3=Alumno("Luis",11,"Matematica",5)
print( "Notas, y edad",alumno2.getEdad(),alumno2.getNota())
print( "Notas, y edad",alumno3.getEdad(),alumno3.getNota())


# Ejercicio 2


"""
    Escribir un programa que pregunte al usuario su edad
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
edad=int(input("Que edad tienes...."))

for i in range(1,edad+1):
    print("has cumplido ----",i)



# Ejercicio 3

"""
    Escribir un programa que pida al usuario una palabra y
    luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

def invetir_cadena(cadena):
    return cadena[::-1]

cadena=input("Invertira cadena....")
print(" la innvertida es ",invetir_cadena(cadena))


# Ejercicio 4

"""
    Escribir un programa que pregunte el nombre completo del usuario en la consola y
    después muestre por pantalla el nombre completo del usuario tres veces,
    una con todas las letras minúsculas,
    otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
    El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
cadena=input("Escribre tu nombre....")
print("Maysucula",cadena.upper())
print("Minuscula",cadena.lower())
print("Primera maysuca",cadena.title())

# Ejercicio 5

"""
    Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
def sacartelefono(telefono):
    telefono=telefono.strip()
    guion=telefono.index("-")
    
  # +34-913724710-56
    nuevo=telefono[guion+1:len(telefono)]
    final_guion=nuevo.index("-")
  
    final=nuevo[0:final_guion]

    return final




telefono=input("Introducaza telefono....")


print  ( "telefono final",sacartelefono(telefono))



# Ejercicio 6

"""
    Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
    y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
cadena=input("Introducaza cadena....")
vocal=input("Intrudzca vocal....")

print(cadena.replace(vocal.lower(),vocal.upper()))

# Ejercicio 7

"""
    Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
    y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
numero=float(input("Introduce euros...."))
parte_entera=int(numero)
print("Entero",parte_entera)
partedecimal=numero-parte_entera
print("Decimal",int(round(partedecimal,2)*100))

# Ejercicio 8

"""
    Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:

    Mes Ventas Gastos

    Enero 30500 22000

    Febrero 35600 23400

    Marzo 28300 18100

    Abril 33900 20700
"""
def imprimir_df(df):
    print("    Mes    Ventas  Gastos")
    for i in df.index: 
     print(" "+ df["Mes"][i]+ " "+str(df["Ventas"][i])+ " "+str(df["Gastos"][i]))

mes = ["Enero", "Febrero", "Marzo", "Abril"]
ventas = [30500, 35600, 28300,33900]
gastos =[22000, 23400, 18100,20700] 

df = pd.DataFrame({"Mes": mes, "Ventas": ventas,"Gastos": gastos})
print (df)
imprimir_df(df)

# Ejercicio 9

"""
    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
"""

def balance(df,lista_mes):
    lista_balance=[]
    total=0
    for mes in lista_mes:
        df_selecionada=df[df.Mes==mes]
        if(len(df_selecionada)>0):
            total=total+int(df_selecionada.Ventas-df_selecionada.Gastos)
            lista_balance.append(int(df_selecionada.Ventas-df_selecionada.Gastos))
        else :
             lista_balance.append(int(0))
    return lista_balance,total

mes_solicitar=["Febrero", "Marzo", "Abril","Diciembre"]
lista_meses,total=balance(df,mes_solicitar)
print("Balance de meses",mes_solicitar,lista_meses)
print("Total",total)
# Ejercicio 10

"""
    Escribir un programa que almacene las asignaturas de un curso
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
    pregunte al usuario la nota que ha sacado en cada asignatura,
    y después las muestre por pantalla con el mensaje "Has sacado ASIGNATURA la nota de NOTA"
    donde es cada una de las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.
"""
def solicitud(listasAsignatura):
    nota=[]
    for asignatura in listasAsignatura:
       
        numero=int(input(" Introduca la nota de "+asignatura+"  es :"))
        nota.append(numero)
   

    df = pd.DataFrame({"Asignatura": listasAsignatura, "Nota":nota })
    return (df)
    
def imprimir(df):
    for i in df.index: 
     print("Has sacado "+ df["Asignatura"][i]+ " la nota de "+str(df["Nota"][i]))



listasAsignatura=["Matemáticas", "Física", "Química", "Historia" ,"Lengua"]
df=solicitud(listasAsignatura)
imprimir(df)