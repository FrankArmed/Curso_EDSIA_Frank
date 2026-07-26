# Sprint 1 Planning — Evaluación 1

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026  
**Proyecto:** Sistema IoT para una bodega industrial

## Duración

Una semana, de lunes a sábado.

## Product Goal

Construir un sistema capaz de registrar lecturas de temperatura y humedad,
detectar anomalías con umbrales configurables y generar alertas mediante
diferentes estrategias.

## Sprint Goal

Construir mediante TDD el núcleo verificable de un sistema IoT que permita
registrar lecturas, detectar valores fuera de los límites configurados y
enviar alertas por consola o archivo.

## Historias seleccionadas

| ID | Historia | Puntos | Justificación |
|---|---|---:|---|
| US-01 | Registrar una lectura | 3 | Es la información base del sistema |
| US-04 | Detectar temperatura elevada | 3 | Permite identificar riesgo térmico |
| US-05 | Detectar humedad elevada | 3 | Permite identificar exceso de humedad |
| US-06 | Configurar los umbrales | 5 | Evita límites fijos dentro del detector |
| US-07 | Administrar estrategias de alerta | 5 | Permite cambiar el medio de notificación |
| US-08 | Mostrar alertas en consola | 3 | Ofrece una alerta inmediata |
| US-09 | Guardar alertas en archivo | 5 | Conserva un historial de eventos |

**Total:** 27 story points.

US-02 y US-03 se trataron como validaciones necesarias de US-01:

- Identificador obligatorio.
- Humedad entre 0 y 100 %.

Por esta razón se implementaron junto con `SensorReading`, pero no se
contabilizan como historias adicionales dentro de las siete seleccionadas.

## Orden de implementación

1. `SensorReading`.
2. `AnomalyDetector`.
3. `AlertManager`.
4. `ConsoleAlert`.
5. `FileAlert`.
6. Prueba de integración.
7. Revisión de calidad y cobertura.

Este orden se eligió porque el detector necesita una lectura y el
administrador de alertas necesita primero conocer las anomalías encontradas.

## Tareas del Sprint

Todas las tareas tienen una duración estimada menor o igual a cuatro horas.

### SensorReading

| Tarea | Tiempo estimado |
|---|---:|
| Escribir los tests iniciales | 1 h |
| Implementar la dataclass | 1 h |
| Validar identificador y humedad | 1 h |
| Revisar Ruff, mypy y tests | 30 min |

### AnomalyDetector

| Tarea | Tiempo estimado |
|---|---:|
| Escribir tests de temperatura y humedad | 1 h |
| Implementar la detección básica | 1 h |
| Permitir umbrales configurables | 1 h |
| Revisar calidad | 30 min |

### AlertManager

| Tarea | Tiempo estimado |
|---|---:|
| Escribir tests de las estrategias | 1 h |
| Crear la estrategia abstracta | 45 min |
| Implementar ConsoleAlert | 30 min |
| Implementar FileAlert | 1 h |
| Implementar AlertManager | 45 min |
| Revisar calidad | 30 min |

### Integración y cierre

| Tarea | Tiempo estimado |
|---|---:|
| Crear prueba del flujo completo | 1 h |
| Ejecutar todos los tests | 30 min |
| Revisar cobertura | 30 min |
| Actualizar documentación | 1 h |

## Estrategia TDD

Para las tres partes principales se utilizó:

```text
Red → Green → Refactor