# Curso EDSIA — Frank Asael Méndez García

Este repositorio contiene las actividades realizadas durante el curso EDSIA.

Las carpetas `semana0/`, `semana1/` y `semana2/` se conservan como historial.
Desde la Semana 3, la aplicación principal vive en `app/`.

---

# SensorHub API — Semana 3

API REST para administrar sensores y lecturas mediante FastAPI, Pydantic,
SQLAlchemy y SQLite.

## Funciones principales

- Crear, consultar, actualizar y eliminar sensores.
- Crear, consultar, actualizar y eliminar lecturas.
- Validar tipos de sensor, unidades y rangos físicos.
- Paginar resultados con `offset` y `limit`.
- Filtrar lecturas por rango de fechas.
- Mostrar documentación automática en Swagger.

## Arquitectura

La aplicación utiliza cuatro capas:

```text
routers → services → repositories → models
```

- `routers/`: recibe peticiones HTTP y devuelve respuestas.
- `services/`: contiene las reglas del negocio.
- `repositories/`: realiza operaciones con la base de datos.
- `models/`: representa las tablas de SQLAlchemy.
- `schemas/`: valida la entrada y salida con Pydantic.

La decisión de arquitectura se documenta en:

```text
docs/adr/0001-layered-architecture.md
```

## Estructura principal

```text
app/
├── main.py
├── db.py
├── routers/
├── services/
├── repositories/
├── models/
└── schemas/

tests/
docs/adr/
requirements.txt
pyproject.toml
```

## Requisitos

- Python 3.12 o superior.
- Dependencias indicadas en `requirements.txt`.

## Instalación

Desde la raíz del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecutar la API

Desde la raíz del repositorio:

```powershell
uvicorn app.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

Swagger estará disponible en:

```text
http://127.0.0.1:8000/docs
```

## Comprobar el estado

```text
GET /health
```

Respuesta esperada:

```json
{
  "status": "ok"
}
```

## Endpoints de sensores

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/sensors` | Crear un sensor |
| GET | `/sensors` | Listar sensores |
| GET | `/sensors/{sensor_id}` | Consultar un sensor |
| PATCH | `/sensors/{sensor_id}` | Actualizar un sensor |
| DELETE | `/sensors/{sensor_id}` | Eliminar un sensor |

### Crear un sensor

```text
POST /sensors
```

Cuerpo de ejemplo:

```json
{
  "id": "TH-01",
  "sensor_type": "temperature",
  "unit": "C"
}
```

Respuesta esperada:

```text
201 Created
```

### Actualizar un sensor

```text
PATCH /sensors/TH-01
```

Cuerpo de ejemplo:

```json
{
  "sensor_type": "humidity",
  "unit": "%"
}
```

### Listar sensores con paginación

```text
GET /sensors?offset=0&limit=20
```

## Endpoints de lecturas

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/sensors/{sensor_id}/readings` | Crear una lectura |
| GET | `/sensors/{sensor_id}/readings` | Listar lecturas de un sensor |
| GET | `/readings/{reading_id}` | Consultar una lectura |
| PATCH | `/readings/{reading_id}` | Actualizar una lectura |
| DELETE | `/readings/{reading_id}` | Eliminar una lectura |

### Crear una lectura

Primero debe existir el sensor indicado.

```text
POST /sensors/TH-01/readings
```

Cuerpo de ejemplo:

```json
{
  "value": 25.5,
  "unit": "C",
  "recorded_at": "2026-08-01T10:00:00"
}
```

Respuesta esperada:

```text
201 Created
```

### Listar lecturas con paginación

```text
GET /sensors/TH-01/readings?offset=0&limit=20
```

### Filtrar lecturas por fechas

```text
GET /sensors/TH-01/readings?from=2026-08-01T00:00:00&to=2026-08-01T23:59:59
```

### Actualizar una lectura

```text
PATCH /readings/1
```

Cuerpo de ejemplo:

```json
{
  "value": 30.0
}
```

### Eliminar una lectura

```text
DELETE /readings/1
```

Respuesta esperada:

```text
204 No Content
```

## Reglas de validación

| Tipo de sensor | Unidad | Rango permitido |
|---|---|---|
| `temperature` | `C` | -40 a 125 |
| `humidity` | `%` | 0 a 100 |

La API también rechaza:

- Identificadores vacíos.
- Tipos de sensor desconocidos.
- Unidades desconocidas.
- Sensores duplicados.
- Lecturas asociadas a sensores inexistentes.
- Rangos de fechas invertidos.

## Códigos HTTP utilizados

| Código | Significado |
|---|---|
| 200 | Consulta o actualización correcta |
| 201 | Recurso creado |
| 204 | Recurso eliminado |
| 400 | Rango de fechas incorrecto |
| 404 | Recurso inexistente |
| 409 | Sensor duplicado |
| 422 | Datos que no cumplen las validaciones |

## Ejecutar las pruebas

```powershell
python -m pytest
```

## Verificar cobertura

```powershell
python -m pytest --cov=app --cov-report=term-missing
```

La cobertura mínima requerida es de 80 %.

## Verificar calidad

```powershell
ruff check .
mypy app
```

## Base de datos

La aplicación utiliza SQLite.

El archivo local:

```text
sensorhub.db
```

no se incluye en Git porque está registrado en `.gitignore`.

## :D
