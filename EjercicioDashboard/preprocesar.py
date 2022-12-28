import pandas as pd
import numpy as np

class Preprocesar():

    def name_process(self,df):
       
        df = df.drop(["Name"], axis=1)
        return df
    
    def ticket_process(self,df):
        
        df = df.drop(["Ticket"], axis=1)
        return df
    def cabin_process(self,df):
    
        df = df.drop( ["Cabin"], axis=1)
        return df
    
    def age_process(self,df,opcion):
        if opcion == "Mean":
            age_avg = df['Age'].mean()
            df['Age'] = df['Age'].fillna(age_avg)
        elif opcion == "Median":
            age_mediana = age_avg = df['Age'].median()
            df['Age'] = df['Age'].fillnafillna(age_mediana)
        return df
    
    def embarked_process(self,df,opcion):
        if (opcion =="S") | (opcion =="C") |(opcion =="Q"):
            df["Embarked"] = df["Embarked"].fillna(opcion)
        else :
            df["Embarked"] = df["Embarked"].fillna("S")
        return df
    
            
    def dummies_crear(self,df,cadena):
        df = pd.get_dummies(df, columns=[cadena], drop_first=True)
        return df
    
    def eliminaColumna(self,df,cadena):
        
        df = df.drop([cadena], axis=1)
        return df
    

    def escalado_Age(self,df):
       
        df.Age = (df.Age - np.mean(df.Age, axis=0)) / (np.std(df.Age, axis=0))
        return df,np.mean(df.Age, axis=0),np.std(df.Age, axis=0)
    
    def escalado_Fare(self,df):
        df.Fare = (df.Fare - np.mean(df.Fare, axis=0)) / (np.std(df.Fare, axis=0))

       
        return df,np.mean(df.Fare, axis=0),np.std(df.Fare, axis=0)
