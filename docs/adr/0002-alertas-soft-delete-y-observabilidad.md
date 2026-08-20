# ADR 0002: Alertas con estado, baja lógica y observabilidad básica

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026  
**Estado:** Aceptado

## Contexto

El proyecto final exige alertas gestionables, que los sensores no se borren físicamente en producción y que el sistema pueda diagnosticarse mediante logs, healthcheck y métricas.

## Decisión

- Los sensores usan `is_active`; `DELETE /sensors/{id}` solo los desactiva.
- Las alertas tienen estados `open`, `acknowledged` y `resolved`.
- Una alerta se clasifica como `WARNING` cuando supera el umbral y como `CRITICAL` cuando supera en más de 20% el umbral.
- Se registra cada petición como JSON y se exponen contadores básicos en `/metrics`.
- Las migraciones Alembic se ejecutan antes de arrancar Uvicorn en Docker/Render.

## Consecuencias

- Se conserva el historial del sensor y de sus lecturas.
- Las alertas dejan de ser solo registros y tienen un ciclo de vida.
- La observabilidad ayuda a diagnosticar errores sin entrar al contenedor.
- Las métricas son locales al proceso y no sustituyen un sistema completo de monitorización.
