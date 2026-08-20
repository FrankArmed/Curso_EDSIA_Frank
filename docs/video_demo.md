# Guion para video demo — 3 a 5 minutos

## 0:00–0:30 — Problema

"SensorHub es una API de telemetría IoT. Recibe lecturas de sensores, las valida, las almacena y genera alertas cuando un valor supera el umbral configurado."

## 0:30–1:10 — Arquitectura

Mostrar el diagrama Mermaid del README y explicar:

`Swagger -> Routers -> Services -> Repositories -> PostgreSQL`

Mencionar DIP y el dominio puro de telemetría.

## 1:10–2:20 — Demo funcional

1. Abrir `/docs`.
2. Crear un sensor con ubicación y umbral.
3. Enviar una lectura normal.
4. Enviar una lectura que supere el umbral.
5. Consultar `/alerts` y mostrar `WARNING` o `CRITICAL`.
6. Cambiar la alerta a `acknowledged` y después a `resolved`.

## 2:20–3:00 — Estadísticas y observabilidad

Mostrar `/sensors/{sensor_id}/statistics`, `/health` y `/metrics`.

## 3:00–3:40 — Calidad de ingeniería

Mostrar GitHub Actions en verde, cobertura superior a 80%, Docker y Alembic.

## 3:40–4:00 — Cierre

"El sistema queda desplegado con CI/CD, configuración por variables de entorno, migraciones versionadas, logs estructurados y pruebas de integración."
