import pandas as pd
class Datos_get():
 

    def read_datos(self):
        df = pd.read_csv("train.csv")
        return df
    


