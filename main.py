from fastapi import FastAPI, HTTPException

app = FastAPI(title="Mini-API de Catálogo")

# "Base de datos" temporal en memoria
productos = [
    {"id": 1, "nombre": "Teclado mecanico", "precio": 120000, "categoria": "Perifericos"},
    {"id": 2, "nombre": "Mouse gamer", "precio": 85000, "categoria": "Perifericos"},
    {"id": 3, "nombre": "Monitor 24", "precio": 650000, "categoria": "Pantallas"},
]


# 1. Mensaje de bienvenida
@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la Mini-API de Catalogo"}


# 2. Lista completa de productos
@app.get("/productos")
def listar_productos():
    return productos


# 3. Buscar un producto por su id (recorremos la lista con un for)
@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    for producto in productos:
        if producto["id"] == producto_id:
            return producto
    # Si el for termina sin encontrarlo, respondemos 404 (no encontrado)
    raise HTTPException(status_code=404, detail="Producto no encontrado")


# 4. Lista de categorías distintas (sin repetir)
@app.get("/categorias")
def listar_categorias():
    categorias = []
    for producto in productos:
        if producto["categoria"] not in categorias:
            categorias.append(producto["categoria"])
    return categorias


# 5. Productos cuyo nombre contenga el texto buscado (sin importar mayúsculas)
@app.get("/buscar")
def buscar_productos(nombre: str = ""):
    resultado = []
    for producto in productos:
        if nombre.lower() in producto["nombre"].lower():
            resultado.append(producto)
    return resultado
