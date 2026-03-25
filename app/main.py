from fastapi import FastAPI, HTTPException
from .models import Product, Movement
from .database import (
    get_products,
    add_product,
    find_product,
    update_product_status,
    get_movements,
    add_movement
)

app = FastAPI(title="StockFlow API")

@app.post("/products")
def create_product(product: Product):
    return add_product(product)

@app.get("/products")
def list_products():
    return get_products()

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = find_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@app.put("/products/{product_id}/status")
def change_status(product_id: int, status: str):
    product = update_product_status(product_id, status)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Estado actualizado"}

@app.post("/movements")
def create_movement(movement: Movement):
    return add_movement(movement)

@app.get("/movements")
def list_movements():
    return get_movements()