# ADR 0001: Arquitectura en capas para SensorHub

**Autor:** Frank Asael Méndez García  
**Estado:** Aceptado  
**Fecha:** 15/08/2026

## Contexto

SensorHub necesita administrar sensores y lecturas mediante una API
FastAPI sin colocar todas las responsabilidades directamente en los
endpoints.

El sistema necesita validar datos, aplicar reglas de negocio,
consultar la base de datos y representar sus tablas.

Si toda esta lógica estuviera dentro de los routers, el código sería
más difícil de probar, mantener y modificar.

Además, los esquemas de Pydantic se utilizan para validar los datos que entran y salen de la API.

Cada parte tiene una responsabilidad clara:

routers: reciben las peticiones HTTP y devuelven respuestas.
services: contienen las reglas y validaciones del negocio.
repositories: realizan las operaciones con la base de datos.
models: representan las tablas mediante SQLAlchemy.
schemas: validan los datos mediante Pydantic.

## Alternativas consideradas

Toda la lógica en los routers.
Se descartó porque mezclaría demasiadas responsabilidades en los mismos archivos y haría más difíciles las pruebas.

## Microservicios

También se descartaron por ahora. SensorHub sigue siendo un proyecto pequeño y no necesita varios servicios desplegados de forma independiente.
Usar microservicios en este momento agregaría más configuración, comunicación por red y mantenimiento sin resolver un problema real.

## Consecuencias

Positivas:

El código queda mejor organizado.
Cada capa tiene una responsabilidad clara.
Las pruebas son más sencillas de realizar.
Es más fácil modificar una parte sin afectar todo el sistema.

Negativas:

Hay más archivos que en una aplicación pequeña.
Una operación puede pasar por varias capas antes de llegar a la base de datos.

## Conclusión

Para el tamaño actual de SensorHub, una arquitectura en capas dentro de un monolito modular es suficiente.
Si en el futuro algunas partes necesitaran escalar o desplegarse de manera distinta o independiente, se podría volver a evaluar el uso de microservicios.