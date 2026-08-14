# Cierre 

## Objetivo

Preparar SensorHub para ejecutarse de forma reproducible, validar los cambios automáticamente y desplegar la aplicación en producción.

## Trabajo realizado

Durante la semana se incorporaron:

- Docker con Python 3.12 slim.
- Docker Compose con API y PostgreSQL.
- Variables de entorno para la configuración.
- Alembic para migraciones.
- GitHub Actions con Ruff, mypy y pytest.
- Despliegue de SensorHub en Render.
- Health check mediante `/health`.
- Despliegue automático desde `main`.

## Producción

- API: https://sensorhub-api-frank.onrender.com
- Health: https://sensorhub-api-frank.onrender.com/health
- Swagger: https://sensorhub-api-frank.onrender.com/docs

## Flujo

```text
Cambio
  ↓
GitHub Actions
  ↓
Ruff + mypy + pytest
  ↓
Docker
  ↓
Render
  ↓
FastAPI + PostgreSQL
```

## Rollback

Si una versión causa problemas, se puede revertir el commit:

```powershell
git log --oneline
git revert ID_DEL_COMMIT
git push
```

Esto crea un nuevo commit que deshace el cambio sin borrar el historial.

## Resultado

SensorHub quedó funcionando localmente, con Docker Compose y en producción, con pruebas automáticas, migraciones y despliegue continuo.
