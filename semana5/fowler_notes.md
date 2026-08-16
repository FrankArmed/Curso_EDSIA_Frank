# Notas de arquitectura — Microservices y Monolith First

**Estudiante:** Frank Asael Méndez García  
**Semana:** 5

## Microservicios

Los microservicios dividen una aplicación en varios servicios que pueden
desplegarse y evolucionar de manera independiente.

Algunas características importantes son:

1. Los componentes se separan como servicios.
2. Se organizan alrededor de capacidades del negocio.
3. Cada servicio puede evolucionar de forma independiente.
4. Existe comunicación entre servicios.
5. La infraestructura necesita mayor automatización.
6. Los servicios deben estar preparados para fallos.

## Ventajas

- Permiten desplegar partes del sistema de forma independiente.
- Diferentes servicios pueden escalar de forma distinta.
- Ayudan cuando existen equipos grandes y responsabilidades bien separadas.

## Desventajas

- Aumentan la complejidad.
- Existe comunicación por red.
- Hay más servicios que desplegar y supervisar.
- Los errores pueden ser más difíciles de encontrar.
- La gestión de los datos puede complicarse.

## Monolith First

La idea de Monolith First es no comenzar automáticamente un proyecto
nuevo utilizando microservicios.

Al inicio todavía pueden no estar claros los límites entre los diferentes
módulos del sistema. Un monolito permite descubrir esos límites antes de
separarlos en servicios independientes.

## ¿Cuándo NO usar microservicios?

No los utilizaría cuando:

- la aplicación todavía es pequeña;
- trabaja un equipo pequeño;
- el dominio todavía está cambiando;
- no existen problemas reales de escalabilidad;
- los módulos todavía no tienen límites claros;
- la complejidad adicional sería mayor que el beneficio.

## Aplicación a SensorHub

Actualmente SensorHub no necesita microservicios.

La separación entre routers, servicios, repositorios y modelos permite
mantener el proyecto organizado sin necesidad de dividirlo en varias
aplicaciones.

Por ahora es más conveniente conservar SensorHub como un monolito
modular.

## Conclusión

Los microservicios no hacen automáticamente mejor una aplicación.

Primero debe existir un problema real que justifique la complejidad
adicional. Para el estado actual de SensorHub, mantener un monolito
modular es una decisión más sencilla y adecuada.