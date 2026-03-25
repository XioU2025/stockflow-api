# StockFlow API

MVP técnico de un sistema de inventario desarrollado con FastAPI.

## Problema
Muchas pequeñas empresas no tienen control claro de su inventario.

## Solución
Una API que permite:
- Registrar productos
- Registrar movimientos
- Consultar inventario
- Cambiar estado de productos

## Tecnologías
- Python
- FastAPI
- Uvicorn
- Pydantic

## Ejecutar proyecto

Instalar dependencias:

pip install fastapi uvicorn

Ejecutar:

uvicorn app.main:app --reload

Abrir documentación:

http://127.0.0.1:8000/docs