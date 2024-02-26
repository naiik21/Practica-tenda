from typing import Union
from fastapi import FastAPI

from Model.Product import Product

from db import clientPS
from db import productDB

app = FastAPI()
conn= clientPS.dbClient()

@app.get("/")
def red_root():
    clientPS.dbClient()
    return {"Hello":"World"}

@app.get("/product")
def getProducts():
    clientPS.dbClient()
    data= productDB.consulta()
    return data
    

@app.get("/product/{id}")
def getProductId(id):
    clientPS.dbClient()
    data=productDB.consultaId(id)
    return data


@app.post("/product/")
def createProduct(prod: Product):
    clientPS.dbClient()
    data=productDB.createProduct(prod)
    return data


@app.put("/product/"
         "/product/{id}")
def updateProduct(id:int):
    conn= clientPS.dbClient()
    return {"masseage":f"consulta producte {id}"}

@app.delete("/product/{id}")
def deleteProduct(id:int):
    conn= clientPS.dbClient()
    return {"masseage":f"consulta producte {id}"}


@app.get("/productAll")
def allProducts(id:int):
    conn= clientPS.dbClient()
    return {"masseage":f"consulta producte {id}"}