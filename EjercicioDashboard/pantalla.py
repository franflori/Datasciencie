class Pantalla():

    
    def __init__(self):
        self.iniciacion=0
        self.preprocesar=0
        self.entrenar=0
        self.analisis=0
        self.predecir=0
    
    def pulsaPrepocesar(self):
        self.iniciacion=1
        self.preprocesar=1
        self.entrenar=0
        self.analisis=0
        self.predecir=0

    def pulsarEntrenaminto(self):
        self.iniciacion=2
        self.preprocesar=2
        self.entrenar=1
        self.analisis=0
        self.predecir=0
       
    def pulsarAnalisis(self):
        self.iniciacion=2
        self.preprocesar=2
        self.entrenar=2
        self.analisis=1
        self.predecir=0

    
    def pulsaPredecir(self):
        self.iniciacion=2
        self.preprocesar=2
        self.entrenar=2
        self.analisis=2
        self.predecir=1
       
    def getIniciacion(self):
        return self.iniciacion
    
    def getPreprocesar(self):
        return self.preprocesar
    def getEntrenar(self):
        return self.entrenar
    
    def getAnalisis(self):
        return self.analisis
    def getPredecir(self):
        return self.predecir
    
    def __str__(self):
        return f"Datos Pantalla ({self.iniciacion},{self.preprocesar},{self.entrenar},{self.analisis},{self.predecir})"
 
        
      
    