import pandas as pd
from csv import writer
from pasajero import Pasajero
class Datos_get():
 

    def read_datos(self):
        df = pd.read_csv("train.csv")
        return df
    

    




    def grabar_excel(self,pasajero):
        #PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

        list_data= [pasajero.getPassengerId(),pasajero.getSuvived(),pasajero.getPclass()
                ,pasajero.getNName(),pasajero.getSex(),pasajero.getAge(),pasajero.getSibsp(),
                pasajero.getParch(),pasajero.getTicket(),pasajero.getFare(),pasajero.getCabin(),pasajero.getEmbarked()]
        print ("grabar----",list_data)
        with open('train.csv', 'a', newline='') as f_object:  
            # Pass the CSV  file object to the writer() functio
            writer_object = writer(f_object)
            # Result - a writer object
           
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow(list_data)  
            # Close the file object
            f_object.close()

        print("finalizar")



