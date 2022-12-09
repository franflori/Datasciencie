

#Defino el algoritmo a utilizar
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

class entrenamiento():






    # KNeighborsClassifier

    def algoritmoKNeighborsClassifier(self, X_train, y_train,X_test,y_test):
        clf = KNeighborsClassifier()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc_KN = accuracy_score(y_test, y_pred)
        return acc_KN,clf

    def algoritmoDecisionTreeClassifier(self, X_train, y_train,X_test,y_test):
        #DecisionTreeClassifier
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc_DT = accuracy_score(y_test, y_pred)
        return acc_DT,clf
    
    def algoritmoRandomForestClassifier(self, X_train, y_train,X_test,y_test):
        # RandomForestClassifier
        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc_RF = accuracy_score(y_test, y_pred)
        return acc_RF,clf 
    
    def  algoritmoGaussianNB(self, X_train, y_train,X_test,y_test):

        #GaussianNB
        clf = GaussianNB()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc_NB = accuracy_score(y_test, y_pred)
        return acc_NB,clf
    
    def prevision
  