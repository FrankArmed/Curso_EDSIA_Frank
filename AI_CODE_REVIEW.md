# AI Code Review — Semana 5

**Estudiante:** Frank Asael Méndez García
**Archivo revisado:** `app/services/reading_service.py`

## Objetivo

Utilizar una herramienta de IA para revisar código real de SensorHub y evaluar sus recomendaciones con criterio propio antes de modificar el proyecto.

El análisis se centró en casos borde, validaciones, seguridad, mantenibilidad y posibles pruebas faltantes.

---

## Hallazgo 1 — Tipos de sensores desconocidos

**Propuesta de la IA:**
Agregar una validación para evitar que `validate_reading()` acepte silenciosamente un tipo de sensor diferente de `temperature` o `humidity`.

**Veredicto:** ACEPTADO CON AJUSTES.

**Decisión:**
Los esquemas de entrada ya restringen los tipos de sensores permitidos, por lo que el problema no ocurre normalmente desde la API. Sin embargo, se decidió agregar una comprobación sencilla en la capa de servicio para evitar aceptar datos incorrectos si el servicio recibe directamente un objeto `Sensor` inválido.

No se utilizará un diccionario de configuración porque para dos tipos de sensores la estructura actual sigue siendo más sencilla de explicar.

---

## Hallazgo 2 — Validación de `offset` y `limit`

**Propuesta de la IA:**
Agregar al servicio validaciones para impedir valores negativos, cero o límites demasiado grandes.

**Veredicto:** RECHAZADO COMO CAMBIO DE CÓDIGO.

**Decisión:**
El router ya valida estos parámetros mediante FastAPI:

* `offset >= 0`
* `limit >= 1`
* `limit <= 100`

Repetir las mismas condiciones en el servicio añadiría validación duplicada sin aportar una mejora importante para el flujo actual.

Se agregarán pruebas para demostrar que estas restricciones realmente funcionan.

---

## Hallazgo 3 — Fechas futuras en `recorded_at`

**Propuesta de la IA:**
Evitar que una lectura pueda guardarse con una fecha futura.

**Veredicto:** ACEPTADO.

**Decisión:**
`recorded_at` representa el momento en que fue registrada una medición. Para este proyecto se considera inválido guardar una lectura cuya fecha todavía no ha ocurrido.

Se agregará una función pequeña de validación y se utilizará tanto al crear como al actualizar una lectura.

---

## Hallazgo 4 — `sensor_id` vacío

**Propuesta de la IA:**
Validar nuevamente en `ReadingService` que `sensor_id` no sea una cadena vacía.

**Veredicto:** RECHAZADO.

**Decisión:**
El identificador se recibe principalmente como parámetro de ruta y los sensores creados por la API ya tienen restricciones de longitud.

La IA también mencionó una posible inyección, pero las consultas se realizan mediante SQLAlchemy y repositorios, por lo que esa observación no justifica agregar esta validación al servicio.

---

## Hallazgo 5 — Comentario de IA dentro del código

**Propuesta de la IA:**
Eliminar el comentario que indica que `list_for_sensor()` fue realizado con ayuda de IA.

**Veredicto:** ACEPTADO.

**Decisión:**
Se eliminará el comentario, pues se puede considerar que no es muy importante este tipo de comentarios, y se dejará únicamente un docstring breve que describa la responsabilidad del método.

---

## Hallazgo 6 — Validaciones adicionales en filtros de fecha

**Propuesta de la IA:**
Rechazar fechas de filtro futuras o demasiado antiguas.

**Veredicto:** RECHAZADO.

**Decisión:**
Una consulta con una fecha futura puede devolver una lista vacía sin representar un error. De la misma forma, consultar información antigua puede ser completamente válido.

La validación importante ya existente es impedir que la fecha inicial sea posterior a la fecha final.

---

## Hallazgo 7 — Consulta adicional al sensor en `update_reading()`

**Propuesta de la IA:**
Consultar el sensor únicamente cuando cambien el valor o la unidad.

**Veredicto:** RECHAZADO.

**Decisión:**
La optimización propuesta es válida técnicamente, pero no representa un problema significativo para el alcance actual de SensorHub.

Mantener el flujo actual hace que el método sea más sencillo y evita agregar condiciones únicamente por una optimización prematura.

---

## Hallazgo 8 — Validación defensiva de retornos del repositorio

**Propuesta de la IA:**
Comprobar manualmente que los métodos del repositorio devuelvan objetos válidos.

**Veredicto:** RECHAZADO.

**Decisión:**
Los repositorios implementan contratos tipados mediante `Protocol`. Agregar comprobaciones adicionales en cada operación duplicaría responsabilidades y haría más complejo el servicio.

Los errores de los repositorios deben ser detectados mediante sus propios tests y mediante el análisis de tipos.

---

# Cambios aceptados

Después de revisar las recomendaciones de la IA se decidió implementar únicamente cambios que aportan valor sin aumentar innecesariamente la complejidad:

1. Rechazar tipos de sensores no soportados desde `ReadingService`.
2. Rechazar fechas futuras en `recorded_at`.
3. Eliminar un comentario de trazabilidad de IA del código de producción.
4. Agregar nuevas pruebas de casos borde.

---

# Conclusión

La revisión demostró que los hallazgos de una IA no deben implementarse automáticamente.

Algunas recomendaciones identificaron casos que si aplican, mientras que otras ignoraron validaciones existentes en otras capas o proponían optimizaciones que no son necesarias para el alcance actual.

El criterio final se tomó revisando la arquitectura completa, el comportamiento existente y la complejidad del proyecto, contemplando que no soy alguien con mucho conocimiento de programación, pero quieriendo abarcar y tomar en cuenta nuevos conocimientos referentes al curso.
 