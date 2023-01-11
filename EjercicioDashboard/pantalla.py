class Pantalla():

    
    def __init__(self):
        self.iniciacion=0
        self.preprocesar=0
        self.entrenar=0
        self.analisis=0
        self.guardar=0
    
    def pulsaIniciar(self):
        self.iniciacion=1
        self.preprocesar=0
        self.entrenar=0
        self.analisis=0
        self.guardar=2

    def pulsaPrepocesar(self):
        self.iniciacion=1
        self.preprocesar=1
        self.entrenar=0
        self.analisis=0
        self.guardar=0

    def pulsarEntrenaminto(self):
        self.iniciacion=1
        self.preprocesar=1
        self.entrenar=1
        self.analisis=0
        self.guardar=0
       
    def pulsarAnalisis(self):
        self.iniciacion=1
        self.preprocesar=1
        self.entrenar=1
        self.analisis=1
        self.guardar=0

    
    def pulsaGuardar(self):
        self.iniciacion=1
        self.preprocesar=1
        self.entrenar=1
        self.analisis=1
        self.guardar=1
       
    def getIniciacion(self):
        return self.iniciacion
    
    def getPreprocesar(self):
        return self.preprocesar
    def getEntrenar(self):
        return self.entrenar
    
    def getAnalisis(self):
        return self.analisis
    def getGuardar(self):
        return self.guardar
    
    def __str__(self):
        return f"Datos Pantalla ({self.iniciacion},{self.preprocesar},{self.entrenar},{self.analisis},{self.guardar})"
 
        
      
    