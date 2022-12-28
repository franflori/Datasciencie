class Pantalla():

    
    def __init__(self):
        self.cargarDatos=True
        self.preprocesar=False
        self.entrenar=False
        self.guardar=False
    
    def pulsaCargaDatos(self):
        self.cargarDatos=True
        self.preprocesar=True
        self.entrenar=False
        self.guardar=False

    def pulsapreprocesar(self):
        self.cargarDatos=True
        self.preprocesar=True
        self.entrenar=True
        self.guardar=False

    def pulsarEntrenar(self):
        self.cargarDatos=True
        self.preprocesar=True
        self.entrenar=True
        self.guardar=True

    def __str__(self):
        return f"Datos Pasaje ({ self.passengerId},{ self.survived},{self.pclass},{self.nName},{self.sex},{self.age},{self.sibsp},{self.parch},{self.ticket},{self.fare},{self.cabin},{self.embarked})"


    