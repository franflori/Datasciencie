from fastapi import FastAPI, status, HTTPException
import pandas as pd 
import json
import csv
import os
from pydantic import BaseModel


# Creamos nuestra primera aplicación FastAPI:
app = FastAPI()

# doy la ruta donde se encuentra el dataset:
MEDIA_ROOT = "../../datos/Iris2.csv"

# Método GET a la url "/test/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get("/test/")
async def test_1():
     return "Bienvenido a FastAPI"


# Método GET a la url "/iris/"
# llamaremos a nuestra aplicación (<app name> + <método permitido>)
@app.get("/iris/")
async def iris():
    # Crear el dataframe con la información de iris:
    df = pd.read_csv(MEDIA_ROOT)
    # print(df)
    # lo transformamos a json para poder gestionarlo desde el front:
    data = df.to_json(orient="index")
    # cargar la información con formato Json:
    data = json.loads(data)
    return data


@app.get("/iris/describe/")
async def describe():
    # Crear el dataframe con la información de iris:
    df = pd.read_csv(MEDIA_ROOT)
    # print(df)
    valor=df.describe()
    # lo transformamos a json para poder gestionarlo desde el front:
    data = valor.to_json(orient="index")
    # cargar la información con formato Json:
    data = json.loads(data)
    return data

# TODO: Realizar los distintos metodos con el IRIS dataset:
# Método GET para mostrar la información.
# TODO: Método POST para insertar un dato al final del iris dataset.
# TODO: Método PUT actualizaremos el último dato insertado.
# TODO: Método DELETE para eliminar ese último dato del archivo.
