# ADR 0001 — Arquitectura en capas

**Autor:** Frank Asael Méndez García  
**Fecha:** 01/08/2026  
**Estado:** Aceptada

## Contexto

SensorHub necesita administrar sensores y lecturas sin colocar todas las
responsabilidades dentro de los endpoints.

## Decisión

La aplicación utiliza cuatro capas:

```text
routers → services → repositories → models

Los routers reciben peticiones HTTP.
Los servicios contienen las reglas del negocio.
Los repositorios acceden a la base de datos.
Los modelos representan las tablas.

Los esquemas Pydantic validan la entrada y salida de la API.

Los servicios dependen de contratos Protocol, por lo que pueden probarse
con repositorios fake sin utilizar SQLite. 