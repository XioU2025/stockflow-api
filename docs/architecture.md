# Arquitectura

El sistema utiliza arquitectura de API REST con FastAPI.

Componentes:

Cliente
API
Servicios
Almacenamiento en memoria

## Diagrama

```mermaid
graph TD
User --> API
API --> ProductService
API --> MovementService
ProductService --> Database
MovementService --> Database