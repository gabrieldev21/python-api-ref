from fastapi import FastAPI
from models.product import Product

app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/{nome}")
def ola(nome: str):
    if not nome:
        pass
    return {"Olá": nome}


data = [
    Product(id=1, name="MeuNome", description="descrição", price=1.29),
    Product(id=2, name="SegundoNome", description="descrição2", price=2.29),
    Product(id=3, name="TerceiroNome", description="descrição3", price=3.29),
    Product(id=4, name="QuartoNome", description="descrição4", price=4.29),
]


@app.get("/api/products")
def get_products():
    return data


@app.get("/api/products/{id}")
def get_products_by_id(id: int):
    for product in data:
        if product.id == id:
            return product
    return {"message": "There are no products with this ID!"}
