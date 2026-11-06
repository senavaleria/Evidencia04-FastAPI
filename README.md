# Mini-API de Catálogo

API de solo lectura hecha con **FastAPI** para consultar el catálogo de una tienda.
Los productos se guardan en una lista en memoria, sin base de datos.

Evidencia **GA1-AA3-EV04**, Guía 1: APIs con FastAPI (SENA, ADSO).

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
# 1. Clonar el repositorio y entrar a la carpeta
git clone <URL-de-este-repo>
cd mini-api-catalogo

# 2. Crear el entorno virtual
python -m venv venv

# 3. Activarlo
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS

# 4. Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn main:app --reload
```

La API queda en http://127.0.0.1:8000

- Documentación interactiva (Swagger): http://127.0.0.1:8000/docs
- Documentación de lectura (ReDoc): http://127.0.0.1:8000/redoc

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Mensaje de bienvenida |
| GET | `/productos` | Lista completa de productos |
| GET | `/productos/{producto_id}` | Un producto por su id (404 si no existe) |
| GET | `/categorias` | Categorías distintas del catálogo |
| GET | `/buscar?nombre=texto` | Productos cuyo nombre contiene el texto |

### Ejemplo

`GET /productos/1`

```json
{
  "id": 1,
  "nombre": "Teclado mecanico",
  "precio": 120000,
  "categoria": "Perifericos"
}
```
