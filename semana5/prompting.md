# Semana 5 — Prompting efectivo

**Estudiante:** Frank Asael Méndez García
**Fecha:** 15/08/2026

## Objetivo

Comparar prompts sencillos con prompts mejor estructurados para observar cómo el contexto, las restricciones y el formato de entrega influyen en las respuestas generadas por una IA.

Los prompts sencillos indican qué tarea debe realizarse y para qué se utilizará, pero dejan varias decisiones abiertas.

Los prompts mejorados utilizan cuatro elementos:

* **Contexto:** dónde se utilizará la respuesta.
* **Tarea:** qué debe realizar exactamente la IA.
* **Restricciones:** qué condiciones debe respetar.
* **Formato:** cómo debe entregar el resultado.

---

# Tarea 1 — Generación de código

## Propósito

Generar una función sencilla que permita convertir temperaturas de Celsius a Fahrenheit para utilizarla como ejemplo dentro de SensorHub.

## Prompt sencillo

> Crea una función en Python para convertir una temperatura de Celsius a Fahrenheit. La función será utilizada en un proyecto relacionado con sensores de temperatura.

### Resultado del prompt sencillo

Pegar aquí el resultado generado por la IA.

### Análisis del prompt

El prompt explica qué función se necesita y dónde se utilizará, pero deja varias decisiones abiertas.

Por ejemplo, no indica:

* el nombre de la función;
* el tipo de los parámetros;
* el tipo de retorno;
* si el resultado debe redondearse;
* si se permiten librerías externas;
* el formato en que debe entregarse el código.

Por esta razón, el resultado puede funcionar, pero dependerá de decisiones tomadas automáticamente por la IA.

---

## Prompt mejorado

> **Contexto:** Estoy trabajando en SensorHub, una API desarrollada en Python 3.12 para administrar sensores y sus lecturas.
>
> **Tarea:** Crea una función pura llamada `celsius_to_fahrenheit(c: float) -> float` que convierta una temperatura de Celsius a Fahrenheit.
>
> **Restricciones:** Utiliza type hints completos, no agregues dependencias externas y redondea el resultado a dos decimales. El código debe ser sencillo y fácil de explicar.
>
> **Formato:** Devuelve únicamente el código Python de la función y agrega un docstring breve que explique su propósito.

### Resultado del prompt mejorado

Pegar aquí el resultado generado por la IA.

### Análisis del prompt

El segundo prompt reduce las decisiones que la IA debe tomar por su cuenta.

Se especifican:

* el proyecto donde se utilizará;
* la versión y lenguaje;
* el nombre de la función;
* sus tipos;
* la precisión esperada;
* las dependencias permitidas;
* el formato de entrega.

Esto facilita revisar y utilizar directamente el resultado.

---

# Tarea 2 — Refactorización de código

## Propósito

Revisar una función existente de SensorHub que prepara la dirección de conexión de la base de datos para SQLite y PostgreSQL.

## Código utilizado

```python
def get_database_url() -> str:
    url = os.getenv("DATABASE_URL", "sqlite:///./sensorhub.db")

    if url.startswith("postgres://"):
        return url.replace(
            "postgres://",
            "postgresql+psycopg://",
            1,
        )

    if url.startswith("postgresql://") and "+psycopg" not in url:
        return url.replace(
            "postgresql://",
            "postgresql+psycopg://",
            1,
        )

    return url
```

## Prompt sencillo

> Refactoriza esta función de SensorHub para que sea más clara. La función se utiliza para preparar la URL de conexión a SQLite o PostgreSQL antes de crear la conexión con SQLAlchemy.
>
> ```python
> def get_database_url() -> str:
>     url = os.getenv("DATABASE_URL", "sqlite:///./sensorhub.db")
>
>     if url.startswith("postgres://"):
>         return url.replace(
>             "postgres://",
>             "postgresql+psycopg://",
>             1,
>         )
>
>     if url.startswith("postgresql://") and "+psycopg" not in url:
>         return url.replace(
>             "postgresql://",
>             "postgresql+psycopg://",
>             1,
>         )
>
>     return url
> ```

### Resultado del prompt sencillo

Pegar aquí el resultado generado por la IA.

### Análisis del prompt

El objetivo de la refactorización está claro, pero no se especifica qué partes del comportamiento deben conservarse.

La IA podría:

* cambiar el valor SQLite predeterminado;
* agregar librerías;
* modificar la forma en que se reconocen las URLs;
* crear funciones o clases innecesarias;
* hacer el código más complejo aunque siga funcionando.

Esto demuestra que pedir únicamente una "mejora" puede provocar cambios que no eran necesarios.

---

## Prompt mejorado

> **Contexto:** Estoy trabajando en SensorHub, una API FastAPI desarrollada en Python 3.12. La aplicación utiliza SQLite como base de datos local y PostgreSQL mediante `psycopg` cuando se ejecuta con Docker o Render.
>
> **Tarea:** Revisa la función `get_database_url()` y refactorízala únicamente si puedes hacerla más clara sin modificar su comportamiento.
>
> **Restricciones:** Conserva `sqlite:///./sensorhub.db` como valor predeterminado. Debe continuar aceptando URLs que comiencen con `postgres://`, `postgresql://` y `postgresql+psycopg://`. No agregues dependencias ni clases nuevas. Mantén una solución sencilla y fácil de explicar.
>
> **Formato:** Devuelve primero el código propuesto. Después explica en un máximo de cuatro puntos qué modificaste. Si la implementación actual ya es suficientemente clara, indícalo y evita una refactorización innecesaria.
>
> ```python
> def get_database_url() -> str:
>     url = os.getenv("DATABASE_URL", "sqlite:///./sensorhub.db")
>
>     if url.startswith("postgres://"):
>         return url.replace(
>             "postgres://",
>             "postgresql+psycopg://",
>             1,
>         )
>
>     if url.startswith("postgresql://") and "+psycopg" not in url:
>         return url.replace(
>             "postgresql://",
>             "postgresql+psycopg://",
>             1,
>         )
>
>     return url
> ```

### Resultado del prompt mejorado

Pegar aquí el resultado generado por la IA.

### Análisis del prompt

El prompt mejorado establece claramente qué comportamiento no debe modificarse.

También evita que la IA agregue complejidad innecesaria únicamente para producir una solución diferente.

En una refactorización no siempre es necesario cambiar el código. Si la implementación actual es clara y cumple su objetivo, conservarla también puede ser una decisión válida.

---

# Tarea 3 — Explicación de código y arquitectura

## Propósito

Obtener una explicación de la arquitectura de SensorHub que pueda utilizarse para comprender y explicar el proyecto.

## Prompt sencillo

> Explícame cómo funciona la arquitectura en capas de SensorHub. Quiero entender cómo una petición realizada a FastAPI llega hasta la base de datos.

### Resultado del prompt sencillo

Pegar aquí el resultado generado por la IA.

### Análisis del prompt

El objetivo de la explicación es claro, pero no se establece qué nivel de conocimiento tiene la persona que recibirá la respuesta.

La IA podría:

* utilizar conceptos demasiado avanzados;
* generar una explicación muy extensa;
* explicar patrones que SensorHub no utiliza;
* asumir componentes que no existen en el proyecto.

La respuesta puede ser correcta de forma general, pero no necesariamente será la mejor explicación para este proyecto.

---

## Prompt mejorado

> **Contexto:** SensorHub es una API desarrollada con FastAPI y utiliza una arquitectura en capas formada principalmente por `routers`, `services`, `repositories`, `models` y `schemas`. SQLAlchemy administra la persistencia y Pydantic valida los datos.
>
> **Tarea:** Explica cómo viaja una petición desde un endpoint de FastAPI hasta la base de datos y cómo regresa posteriormente la respuesta al cliente.
>
> **Restricciones:** La explicación está dirigida a un estudiante que está aprendiendo arquitectura de software. Utiliza únicamente los componentes mencionados y evita conceptos avanzados que no sean necesarios. Explica también por qué conviene separar las responsabilidades.
>
> **Formato:** Explica el recorrido en un máximo de seis pasos. Después incluye un ejemplo sencillo utilizando la creación de una lectura de un sensor de temperatura.

### Resultado del prompt mejorado

Pegar aquí el resultado generado por la IA.

### Análisis del prompt

El prompt mejorado define tanto la arquitectura existente como el nivel esperado de la explicación.

Esto reduce la posibilidad de que la IA invente componentes que no forman parte del proyecto y permite obtener una explicación más fácil de estudiar y defender.

---

# Comparación general

Las tres pruebas muestran que un prompt sencillo puede comunicar correctamente la intención principal de una tarea, pero deja varias decisiones en manos de la IA.

Un prompt mejor estructurado disminuye esa ambigüedad mediante cuatro elementos:

```text
Contexto
Tarea específica
Restricciones
Formato de entrega
```

Esto no significa que una respuesta obtenida con un prompt detallado sea automáticamente correcta.

La respuesta todavía debe revisarse porque un modelo puede producir código o explicaciones que parecen razonables aunque contengan errores.

---

# Conclusiones

Después de comparar ambos tipos de prompts puedo establecer las siguientes conclusiones:

1. Un prompt no necesita ser extremadamente detallado para comunicar una tarea, pero demasiada ambigüedad obliga a la IA a tomar decisiones que deberían corresponder al desarrollador, pudiendo generar inconsistencias o errores.

2. Agregar contexto ayuda a obtener respuestas relacionadas con la arquitectura y tecnologías que realmente utiliza el proyecto.

3. Las restricciones son especialmente importantes al generar o refactorizar código porque permiten conservar comportamiento, dependencias y nivel de complejidad.

4. Especificar el formato facilita revisar el resultado y evita recibir información que no fue solicitada.

5. Una respuesta bien escrita o un código aparentemente correcto no garantiza que la solución sea correcta. El resultado generado debe comprobarse mediante revisión, pruebas y criterio propio.

Por lo tanto, la IA se utiliza como una herramienta de apoyo y no como sustituto de la revisión del desarrollador.
