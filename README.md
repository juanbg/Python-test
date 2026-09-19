# Python CRUD API

CRUD mínimo construido con FastAPI, sin base de datos.

Los datos se almacenan en una lista de Python para simular una tabla. Al reiniciar
el contenedor, los datos vuelven al estado inicial.

## Operaciones

| Método | Endpoint | Operación |
|---|---|---|
| POST | `/users` | Create |
| GET | `/users` | Read All |
| GET | `/users/{id}` | Read One |
| PUT | `/users/{id}` | Update |
| DELETE | `/users/{id}` | Delete |

También existe `GET /` como health check.

## Ejecutar con Docker Compose

```bash
docker compose up --build
```

API:

`http://localhost:8000`

Swagger / OpenAPI:

`http://localhost:8000/docs`

## Ejecutar solamente con Docker

```bash
docker build -t python-crud-api .
docker run --rm -p 8000:8000 python-crud-api
```

## Ejemplos

### Read All

```bash
curl http://localhost:8000/users
```

### Read One

```bash
curl http://localhost:8000/users/1
```

### Create

```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Pedro","email":"pedro@example.com"}'
```

### Update

```bash
curl -X PUT http://localhost:8000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana Actualizada","email":"ana.nueva@example.com"}'
```

### Delete

```bash
curl -i -X DELETE http://localhost:8000/users/1
```

## Arquitectura

`main.py` contiene la capa HTTP.

`models.py` contiene los modelos de entrada/salida.

`repository.py` simula la capa de acceso a datos. La idea es que después puedas
reemplazar este archivo por SQLAlchemy, PostgreSQL, MongoDB u otra persistencia
sin cambiar demasiado la API.
