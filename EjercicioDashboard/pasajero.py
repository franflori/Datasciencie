import numpy as np
class Pasajero():
    passengerId=""
    survived=""
    pclass=""
    nName=""
    sex=""
    age=0
    sibsp=0
    parch=0
    ticket=""
    fare=0
    cabin=""
    embarked=""
    meanAge=1
    stdAge=1
    meanFare=1
    staFare=1

    def __init__(self):
        passengerId=""
        survived=""
        pclass=""
        nName=""
        sex=""
        age=0
        sibsp=0
        parch=0
        ticket=""
        fare=0
        cabin=""
        embarked=""
        meanAge=1
        stdAge=1
        meanFare=1
        stdFare=1


    def cargarDatos(self, passengerId,survived,pclass,nName,sex,
                age,sibsp,parch,ticket,fare,cabin,embarked) :
        self.passengerId=passengerId
        self.survived=survived
        self.pclass=pclass
        self.nName=nName
        self.sex=sex
        self.age=age
        self.sibsp=sibsp
        self.parch=parch
        self.ticket=ticket
        self.fare=fare
        self.cabin=cabin
        self.embarked=embarked


    def setPassengerId(self,passengerId):
         self.passengerId=passengerId

    def setSuvived(self,survived):
        
        self.survived=survived

    def setPclass(self,pclass):
        self.pclass=pclass

    def setNName(self,nName):
        self.nName=nName

    def setSex(self,sex):
        self.sex=sex

    def setAge(self,age):
       self.age=age
    def setSibsp(self,sibsp):
        self.sibsp=sibsp
    def setParch(self,parch):
        self.parch=parch
  
    def setTicket(self,ticket):
        self.ticket=ticket
  
    def setFare(self,fare):
        self.fare=fare

    def setCabin(self,cabin):
        self.cabin=cabin
  
    def setEmbarked(self,embarked):
        self.embarked=embarked

    def setMemaAge(self,meanAge):
        self.meanAge=meanAge
    
    def setStdAge(self,stdAge):
        self.stdAge=stdAge
            
    def setMeanFare(self,meanFare):
        self.meanFare=meanFare
    def SetStdFare(self,stdFare):
        self.stdFare=stdFare

    def getPassengerId(self):
         return self.passengerId

    def getSuvived(self):
        return self.survived

    def getPclass(self):
        return self.pclass

    def getNName(self):
        return self.nName

    def getSex(self):
        return self.sex

    def getAge(self):
       return self.age
    
    def getSibsp(self):
        return self.sibsp
   
    def getParch(self):
        return self.parch
  
    def getTicket(self):
        return self.ticket
  
    def getFare(self):
         return self.fare

    def getCabin(self):
        return self.cabin
  
    def getEmbarked(self):
        return self.embarked

    def getMemaAge(self):
        return self.meanAge
    
    def setStdAge(self,stdAge):
        self.stdAge=stdAge
            
    def getMeanFare(self):
        return self.meanFare
    def getStdFare(self):
        return self.stdFare


    def __str__(self):
        return f"Datos Pasaje ({ self.passengerId},{ self.survived},{self.pclass},{self.nName},{self.sex},{self.age},{self.sibsp},{self.parch},{self.ticket},{self.fare},{self.cabin},{self.embarked},{self.meanAge},{self.stdAge},{self.meanFare},{self.stdFare})"

    

    def SacarValorCorrecto(self,cadena):
        #Escalado age
        valor=0
        if cadena=="Age" and self.age!="":
            
            valor=(self.age - self.meanAge) / self.stdAge
            return valor
        #Escalado Fare
        if cadena=="Fare":  
            
            valor=(self.fare -  self.meanFare) / self.stdFare 
            return valor
       
        if cadena=="Embarked_Q":
            if  self.embarked=="Q" or self.embarked=="q":
                return 1
            else :
                return 0

        if cadena=="Embarked_S":
            if  self.embarked=="S" or self.embarked=="s":
                return 1
            else :
                return 0
        
        if cadena=="Sex_male":
            if  self.sex=="male":
                return 1
            else :
                return 0
            
        if cadena=="Pclass_2":
            if  self.pclass=="2":
                return 1
            else :
                return 0
        if cadena=="Pclass_3":
            if  self.pclass=="2":
                return 1
            else :
                return 0
            
        if cadena=="SibSp" :
            return self.sibsp
        if cadena=="Parch":
            return self.parch

        return valor
