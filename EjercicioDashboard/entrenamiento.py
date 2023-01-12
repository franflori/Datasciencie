

#Defino el algoritmo a utilizar
from pandas import DataFrame
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

class Entrenamiento():

    clf_DT=DecisionTreeClassifier()
    clf_KN = KNeighborsClassifier()
    clf_NB = GaussianNB()
    clf_RF = RandomForestClassifier()
    clf_SVC = SVC()
    X_train=DataFrame()
    X_test=DataFrame()
    y_train=DataFrame()
    y_test=DataFrame()
    acc_KN=DataFrame()
    acc_DT=DataFrame()
    acc_RF=DataFrame()
    acc_NB=DataFrame()
    acc_SVC=DataFrame()

    def cargarEntranamiento(self, X,y):
    
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.X_train=X_train
        self.X_test=X_test
        self.y_train=y_train
        self.y_test=y_test
        print(type(self.X_train))

    # KNeighborsClassifier

    def algoritmoKNeighborsClassifier(self):
      
        self.clf_KN.fit(self.X_train, self.y_train)
        y_pred = self.clf_KN.predict(self.X_test)
        self.acc_KN = accuracy_score(self.y_test, y_pred)
       #return self.acc_KN

    def algoritmoDecisionTreeClassifier(self):
        #DecisionTreeClassifier
        
        self.clf_DT.fit(self.X_train, self.y_train)
        y_pred = self.clf_DT.predict(self.X_test)
        self.acc_DT = accuracy_score(self.y_test, y_pred)
       
        #return self.acc_DT
    
    def algoritmoRandomForestClassifier(self):
        # RandomForestClassifier
        
        self.clf_RF.fit(self.X_train, self.y_train)
        y_pred = self.clf_RF.predict(self.X_test)
        self.acc_RF = accuracy_score(self.y_test, y_pred)
        #return self.acc_RF 
    
    def  algoritmoGaussianNB(self):

        #GaussianNB
       
        self.clf_NB.fit(self.X_train, self.y_train)
        y_pred = self.clf_NB.predict(self.X_test)
        self.acc_NB = accuracy_score(self.y_test, y_pred)
        #return self.acc_NB
    
    def  SVC(self):

        
        self.clf_SVC.fit(self.X_train, self.y_train)
        y_pred = self.clf_SVC.predict(self.X_test)
        self.acc_SVC = accuracy_score(self.y_test, y_pred)
        #return self.acc_SVC
    

    def predecir(self,algoritmo,valorx):

       
        if  algoritmo=="DecisionTree" :
            resultado= self.clf_DT.predict(valorx)        
            
        elif algoritmo=="KNeighbors":
            resultado= self.clf_KN.predict(valorx) 
        elif algoritmo=="GaussianNB":
            resultado= self.clf_NB.predict(valorx) 
        elif algoritmo=="RandomForest":
            resultado= self.clf_RF.predict(valorx)
        else:
            resultado= self.clf_SVC.predict(valorx)
       


        return resultado
   
    def getAcc_KN(self):
        return self.acc_KN
    def getAcc_DT(self):
        return self.acc_DT
    def getAcc_RF(self):
        return self.acc_RF
    def getAcc_NB(self):
        return self.acc_NB
    
    def getAcc_SVC(self):
        return self.acc_SVC
    
    
   
