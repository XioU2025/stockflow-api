from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    stock: int
    status: str

class Movement(BaseModel):
    id: int
    product_id: int
    type: str
    quantity: int