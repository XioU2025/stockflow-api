# Simulación de base de datos en memoria

products_db = []
movements_db = []

def get_products():
    return products_db

def add_product(product):
    products_db.append(product)
    return product

def find_product(product_id):
    for p in products_db:
        if p.id == product_id:
            return p
    return None


def update_product_status(product_id, status):
    product = find_product(product_id)
    if product:
        product.status = status
        return product
    return None


def get_movements():
    return movements_db


def add_movement(movement):
    movements_db.append(movement)
    return movement