
from fastapi import FastAPI, status,Response
from modelos import User



# Crear un listado:
database = [{"id": 1, "name": "Juan Perez", "age": 25, "profesion": "Ingeniero"},
 {"id": 2, "name": "Susana Ruiz", "age": 45, "profesion": "Profesora"}]

tags_metadata=[
    {
        "name":"TEST",
        "description":"Bienvenida"
    },
    {
        "name":"Users",
        "description":"Muestra los gestión de los usuarios"
    }
]

app = FastAPI (title="DataScienci Coruse", openapi_tags=tags_metadata)


@app.get("/test/",tags=["TEST"],description="Mostar la informacion de la Web")
async def info():
     return {"msg":"Bienvenido a nuestra Api Rest"}



# TODO:Mostrar el listado: GET
@app.get("/getData/",status_code=status.HTTP_200_OK,tags=["Users"],description="Mostar todos los usuarios")
async def show():
    return database
    




# TODO:Mostrar el listado: GET
@app.get("/getData/{item_id}" , status_code=status.HTTP_200_OK,tags=["Users"],description="Mostar un usuario")
async def show(id: int,response: Response):
    for i in range(0,len(database)):
        if database[i]["id"]== id:
            response.status_code=status.HTTP_200_OK
            return database[i]
    response.status_code=status.HTTP_404_NOT_FOUND
    return {"id":id, "msg":"User Not Found"}



# TODO:Insertar un dato en es listado: POST
@app.post("/postData/", status_code=status.HTTP_201_CREATED,tags=["Users"],description="Insertar un usuario")
async def insert(item: User):   
    database.append(item.dict())
    return item


# TODO:Actualizaréis un dato del listado: PUT


@app.put("/putData/{id}", status_code=status.HTTP_200_OK,tags=["Users"],description="Actualizado  un usuario")
async def updateData(id: int, item:User,response:Response):
    for i in range(0,len(database)):
        if database[i]["id"]== id:
            database[i]=item.dict()
            response.status_code=status.HTTP_200_OK
            return item
    response.status_code=status.HTTP_404_NOT_FOUND
    return {"id":id, "msg":"User Not Found"}



# Eliminareis un dato: Delete

@app.delete("/deleteData/{id}",tags=["Users"],description="Eliminar  un usuario")
async def deleteData(id: int,response:Response):
    for value in database:
        if value["id"]== id:
            database.remove(value)
            response.status_code=status.HTTP_200_OK
            return {"item_id":id,"msg":"Eliminado"}
    response.status_code=status.HTTP_404_NOT_FOUND
    return {"id":id, "msg":"User Not Found"}


#Eliminareis todos

@app.delete("/deleteData/",tags=["Users"],description="Eliminar  todos usuario")
async def deleteData(response:Response):
    database.clear()
    response.status_code=status.HTTP_200_OK
    return {"msg":"Eliminado todos"}
    