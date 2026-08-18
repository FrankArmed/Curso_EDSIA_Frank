# Peer Review — Semana 5

**Estudiante:** Frank Asael Méndez García  
**Semana:** 5  

## Cómo instalar y ejecutar el proyecto

Desde la raíz del repositorio:

```powershell
git clone <URL_DEL_REPOSITORIO>
cd Curso_EDSIA_Frank
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Ejecutar con SQLite

```powershell
alembic upgrade head
uvicorn app.main:app --reload
```

La documentación Swagger queda disponible en:

```text
http://127.0.0.1:8000/docs
```

### Ejecutar con Docker y PostgreSQL

Copia `.env.example` como `.env` y completa las variables necesarias.

```powershell
Copy-Item .env.example .env
docker compose up --build -d
docker compose ps
```

Para detener los contenedores:

```powershell
docker compose down
```

## Validaciones antes del review

```powershell
python -m pytest
ruff check app tests semana5
mypy app semana5
```
