# Curso EDSIA — Frank Asael Méndez García

[![CI](https://github.com/FrankArmed/Curso_EDSIA_Frank/actions/workflows/ci.yml/badge.svg)](https://github.com/FrankArmed/Curso_EDSIA_Frank/actions/workflows/ci.yml)

Repositorio de trabajo del curso **EDSIA**, enfocado en el desarrollo progresivo de software.

El proyecto comenzó con ejercicios pequeños de Python y diseño de software, y evolucionó hasta **SensorHub**, una API REST con persistencia, pruebas automatizadas, contenedores, integración continua y despliegue en producción.

<p align="center">
  <img src="gifrecurse.gif" width="200" height="200">
</p>

---

## SensorHub API

SensorHub permite administrar sensores y sus lecturas mediante una API construida con FastAPI.

### Producción

- **API:** https://sensorhub-api-frank.onrender.com
- **Health check:** https://sensorhub-api-frank.onrender.com/health
- **Swagger:** https://sensorhub-api-frank.onrender.com/docs

---

## Progreso del curso

Las carpetas `semana0/`, `semana1/` y `semana2/` conservan los ejercicios y evaluaciones iniciales. Desde la **Semana 3**, SensorHub se desarrolla como producto dentro de `app/` y los archivos de infraestructura se encuentran en la raíz del repositorio.

---

## Arquitectura actual

SensorHub utiliza una arquitectura en capas:

```text
Cliente / Swagger
    Routers
    Services
 Repositories
    Models
 Base de datos
```

Responsabilidades principales:

- `routers/`: recibe las peticiones HTTP y genera las respuestas.
- `services/`: contiene las reglas y validaciones del negocio.
- `repositories/`: concentra el acceso a los datos.
- `models/`: representa las tablas mediante SQLAlchemy.
- `schemas/`: valida la entrada y salida mediante Pydantic.

La decisión de utilizar esta arquitectura se documenta en `docs/adr/`.

---

## Tecnologías utilizadas

- Python 3.12+
- FastAPI
- Pydantic
- SQLAlchemy 2.x
- SQLite para ejecución local sencilla
- PostgreSQL para Docker Compose y producción
- Alembic para migraciones
- pytest y pytest-cov
- Ruff
- mypy
- Docker
- Docker Compose
- GitHub Actions
- Render

---

## Estructura principal

```text
Curso_EDSIA_Frank/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── main.py
│   ├── db.py
│   ├── routers/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   └── schemas/
├── docs/
│   └── adr/
├── migrations/
│   └── versions/
├── semana0/
├── semana1/
├── semana2/
├── tests/
├── AI_LOG.md
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── render.yaml
└── requirements.txt
```

---

## Instalación local

Desde la raíz del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

---

## Ejecutar SensorHub localmente

Sin definir `DATABASE_URL`, la aplicación utiliza SQLite como base local.

```powershell
uvicorn app.main:app --reload
```

Direcciones principales:

```text
API:      http://127.0.0.1:8000
Health:   http://127.0.0.1:8000/health
Swagger:  http://127.0.0.1:8000/docs
```

Respuesta esperada de `/health`:

```json
{
  "status": "ok"
}
```

---

## Ejecutar con Docker Compose

Docker Compose levanta:

```text
api → SensorHub con FastAPI
db  → PostgreSQL
```

Primero crea el archivo local `.env` a partir del ejemplo:

```powershell
Copy-Item .env.example .env
```

Después:

```powershell
docker compose up --build -d
```

Comprobar los servicios:

```powershell
docker compose ps
```

Ver logs:

```powershell
docker compose logs api
```

Detener los contenedores:

```powershell
docker compose down
```

Los datos de PostgreSQL se mantienen en un volumen persistente.

Para eliminar también el volumen de desarrollo:

```powershell
docker compose down -v
```

---

## Migraciones con Alembic

Las tablas ya no se crean automáticamente al iniciar FastAPI. Alembic administra el esquema mediante migraciones versionadas.

Aplicar todas las migraciones:

```powershell
alembic upgrade head
```

Consultar la migración actual:

```powershell
alembic current
```

En Docker y Render, las migraciones se aplican antes de iniciar Uvicorn.

---

## Endpoints principales

### Sensores

| `POST` | `/sensors` | Crear un sensor |
| `GET` | `/sensors` | Listar sensores |
| `GET` | `/sensors/{sensor_id}` | Consultar un sensor |
| `PATCH` | `/sensors/{sensor_id}` | Actualizar un sensor |
| `DELETE` | `/sensors/{sensor_id}` | Eliminar un sensor |

### Lecturas

| `POST` | `/sensors/{sensor_id}/readings` | Crear una lectura |
| `GET` | `/sensors/{sensor_id}/readings` | Listar lecturas de un sensor |
| `GET` | `/readings/{reading_id}` | Consultar una lectura |
| `PATCH` | `/readings/{reading_id}` | Actualizar una lectura |
| `DELETE` | `/readings/{reading_id}` | Eliminar una lectura |

La API también incluye paginación y filtros de lecturas por rango de fechassss.

---

## Pruebas y calidad

Ejecutar la suite:

```powershell
python -m pytest
```

Revisar calidad:

```powershell
ruff check app tests
mypy app
```

---

## Integración continua

El workflow `.github/workflows/ci.yml` se ejecuta automáticamente en Pull Requests y cambios enviados a `main`.

---

## Despliegue continuo

La infraestructura de producción se define en `render.yaml`.

Render administra:

- un Web Service basado en Docker;
- una base PostgreSQL;
- `DATABASE_URL` mediante variables de entorno;
- `/health` como health check;
- despliegue automático después de que los checks configurados terminan correctamente.

---

## Seguridad de configuración

El repositorio no debe contener credenciales reales.

La configuración sensible se entrega mediante variables de entorno:

```text
DATABASE_URL
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
```

El archivo `.env` es únicamente local y permanece ignorado por Git. El repositorio puede incluir `.env.example` porque contiene únicamente valores de ejemploooo.

---

## Trabajo realizado por semana

### Semana 0 — Preparación

Se configuró el entorno de desarrollo y se verificaron las herramientas principales. También se realizó el primer ejercicio mínimo de sensor acompañado por una prueba automatizada.

### Semana 1 — Diseño de software y comunicaciones

Se trabajaron conceptos de programación orientada a objetos mediante una máquina de estados y ejemplos de SOLID. Después se desarrolló un pequeño sistema UART con configuración, parsers y persistencia.

Como extensión se incorporaron:

- parser CAN;
- buffer circular;
- protección concurrente mediante `Lock`.

### Semana 2 — Scrum y TDD

Se organizó el trabajo mediante Scrum:

- Product Backlog;
- historias de usuario;
- criterios Gherkin;
- prioridades MoSCoW;
- story points;
- Sprint Planning;
- Definition of Done.

El desarrollo principal se realizó mediante TDD con:

- `SensorReading`;
- `AnomalyDetector`;
- `AlertManager`;
- estrategias de alerta por consola y archivo.

### Semana 3 — SensorHub como producto

El proyecto dejó de ser únicamente una colección de ejercicios y pasó a utilizar `app/` como producto principal.

Se incorporaron:

- FastAPI y Swagger;
- CRUD de sensores y lecturas;
- esquemas Pydantic;
- SQLAlchemy 2.x;
- patrón repositorio;
- capa de servicios;
- paginación;
- filtros por fecha;
- validaciones físicas;
- pruebas con `TestClient`;
- revisión por pares.

### Semana 4 — Docker y CI/CD

SensorHub se preparó para ejecutarse de forma reproducible y desplegarse automáticamente.

Se incorporaron:

- imagen basada en `python:3.12-slim`;
- Docker Compose;
- PostgreSQL;
- volúmenes persistentes;
- configuración mediante variables de entorno;
- migraciones con Alembic;
- GitHub Actions;
- Ruff, mypy y pytest automáticos;
- comprobación de construcción de Docker en CI;
- despliegue público en Render;
- health checks;
- despliegue continuo.

---

## Bitácora

`AI_LOG.md` documenta consultas, decisiones, problemas encontrados, correcciones y aprendizajes obtenidos durante el curso.

También se conservan documentos de arquitectura y evidencias relacionadas con revisiones por pares dentro de `docs/`.

---

## Autor

**Frank Asael Méndez García**  
Ingeniería en Instrumentación Electrónica
