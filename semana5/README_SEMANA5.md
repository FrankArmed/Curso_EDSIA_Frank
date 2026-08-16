# Semana 5 — IA como copiloto profesional

Durante esta semana se utilizó IA como apoyo para generar, revisar y documentar código, manteniendo la decisión final y la validación en manos del desarrollador.

<p align="center">
  <img src="gifrecurse.gif" width="200" height="200">
</p>

---

## TDD de la feature de anomalías

La funcionalidad se desarrolló mediante ciclos RED → GREEN:

```text
RED 1   - pruebas del comportamiento de AlertService
GREEN 1 - implementación mínima de detección y estrategia de notificación
RED 2   - pruebas de integración con la API
GREEN 2 - persistencia, migración Alembic y GET /alerts
```

Una lectura normal no genera una alerta. Si el valor supera el umbral configurado para el sensor, SensorHub registra la anomalía y permite consultarla mediante la API.

## Arquitectura utilizada

```text
routers
services
repositories
models
base de datos
```

La decisión de mantener SensorHub se documenta en:

```text
docs/adr/0001-arquitectura-en-capas.md
```

## Validación

Para validar la aplicación principal:

```powershell
python -m pytest
ruff check app tests
mypy app
```

Para revisar individualmente los ejercicios de `semana5/`:

```powershell
python -m pytest semana5\test_conversions.py -v -o addopts="" --cov=semana5 --cov-report=term-missing
ruff check semana5
mypy semana5
```

## Criterio sobre el uso de IA

Las respuestas de IA no se aceptaron automáticamente. Cada cambio relevante fue revisado con código, pruebas y criterio propio antes de integrarse al proyecto. La comparación entre revisión humana e IA permitió identificar tanto recomendaciones útiles como sugerencias que no aplicaban al contexto real de SensorHub. :D
