# Product Backlog — Sistema IoT para bodega

**Autor:** Frank Asael Méndez García  
**Fecha:** 24/07/2026

## Product Goal

Construir un sistema capaz de registrar lecturas de temperatura y humedad,
detectar anomalías mediante límites configurables y generar alertas por
consola o archivo.

## Escalas utilizadas de el backlogg

**Story points:** 1, 2, 3, 5, 8, 13.

**MoSCoW:**

- Must: indispensable.
- Should: importante.
- Could: opcional.
- Won't: no se realizará en este Sprint.

---

## US-01 — Registrar una lectura

**Como** operador de la bodega,  
**quiero** registrar una lectura de temperatura y humedad,  
**para** analizar las condiciones de cada sensor.

**Valor:** proporciona los datos principales del sistema.  
**MoSCoW:** Must  
**Story points:** 3

```gherkin
Escenario: Registrar una lectura válida
  Dado el sensor "TH-01"
  Y una temperatura de 25 °C
  Y una humedad de 60 %
  Cuando se crea la lectura
  Entonces debe conservar el identificador "TH-01"
  Y debe conservar la temperatura de 25 °C
  Y debe conservar la humedad de 60 %
```

---

## US-02 — Validar el identificador

**Como** operador de la bodega,  
**quiero** rechazar lecturas sin identificador,  
**para** saber qué sensor produjo cada dato.

**Valor:** mantiene la trazabilidad.  
**MoSCoW:** Must  
**Story points:** 2

```gherkin
Escenario: Rechazar identificador vacío
  Dado un identificador formado solo por espacios
  Cuando se intenta crear una lectura
  Entonces la lectura debe ser rechazada
  Y el mensaje debe indicar que el identificador es obligatorio
```

---

## US-03 — Validar la humedad

**Como** operador de la bodega,  
**quiero** rechazar valores de humedad inválidos,  
**para** evitar datos físicamente incorrectos.

**Valor:** protege la calidad de los datos.  
**MoSCoW:** Must  
**Story points:** 2

```gherkin
Esquema del escenario: Rechazar humedad inválida
  Dado una humedad de <valor> %
  Cuando se intenta crear una lectura
  Entonces la lectura debe ser rechazada
  Y el mensaje debe indicar que la humedad debe estar entre 0 y 100

Ejemplos:
  | valor |
  | -1    |
  | 101   |
```

---

## US-04 — Detectar temperatura elevada

**Como** supervisor de la bodega,  
**quiero** detectar temperaturas superiores al límite,  
**para** actuar antes de que los productos sufran daños.

**Valor:** permite reaccionar ante temperaturas peligrosas.  
**MoSCoW:** Must  
**Story points:** 3

```gherkin
Escenario: Detectar temperatura elevada
  Dado un límite de temperatura de 35 °C
  Y una lectura de 35.1 °C
  Cuando se analiza la lectura
  Entonces debe detectarse una anomalía de temperatura
```

```gherkin
Escenario: Aceptar el límite exacto
  Dado un límite de temperatura de 35 °C
  Y una lectura de 35 °C
  Cuando se analiza la lectura
  Entonces no debe detectarse una anomalía de temperatura
```

---

## US-05 — Detectar humedad elevada

**Como** supervisor de la bodega,  
**quiero** detectar humedades superiores al límite,  
**para** reducir el riesgo de deterioro de los productos.

**Valor:** permite reaccionar ante humedad peligrosa.  
**MoSCoW:** Must  
**Story points:** 3

```gherkin
Escenario: Detectar humedad elevada
  Dado un límite de humedad de 80 %
  Y una lectura de 80.1 %
  Cuando se analiza la lectura
  Entonces debe detectarse una anomalía de humedad
```

---

## US-06 — Configurar los umbrales

**Como** supervisor de la bodega,  
**quiero** configurar los límites de temperatura y humedad,  
**para** adaptar el sistema a diferentes productos.

**Valor:** evita límites escritos directamente en el código.  
**MoSCoW:** Must  
**Story points:** 5

```gherkin
Escenario: Utilizar límites personalizados
  Dado un límite de temperatura de 30 °C
  Y un límite de humedad de 70 %
  Y una lectura de 31 °C y 71 %
  Cuando se analiza la lectura
  Entonces debe detectarse una anomalía de temperatura
  Y debe detectarse una anomalía de humedad
```

---

## US-07 — Administrar estrategias de alerta

**Como** responsable del sistema,  
**quiero** seleccionar una estrategia de alerta,  
**para** cambiar el medio de notificación sin modificar el administrador.

**Valor:** permite utilizar diferentes tipos de alerta.  
**MoSCoW:** Must  
**Story points:** 5

```gherkin
Escenario: Enviar una alerta con una estrategia
  Dado un administrador con una estrategia de alerta
  Y el mensaje "Temperatura fuera de rango"
  Cuando se envía la alerta
  Entonces la estrategia debe recibir exactamente una vez el mensaje
```

---

## US-08 — Mostrar alertas en consola

**Como** operador de la bodega,  
**quiero** visualizar las alertas en consola,  
**para** conocer inmediatamente una condición anómala.

**Valor:** ofrece una notificación inmediata.  
**MoSCoW:** Should  
**Story points:** 3

```gherkin
Escenario: Mostrar una alerta
  Dado el mensaje "Humedad fuera de rango"
  Cuando se utiliza la alerta de consola
  Entonces la consola debe mostrar exactamente el mensaje indicado
```

---

## US-09 — Guardar alertas en archivo

**Como** supervisor de la bodega,  
**quiero** guardar las alertas en un archivo,  
**para** conservar un historial de anomalías.

**Valor:** proporciona evidencia de los eventos.  
**MoSCoW:** Should  
**Story points:** 5

```gherkin
Escenario: Guardar dos alertas
  Dado un archivo de alertas vacío
  Cuando se guardan dos mensajes
  Entonces el archivo debe conservar ambos mensajes
  Y cada mensaje debe ocupar una línea diferente
```

---

## US-10 — Conservar fecha y hora

**Como** supervisor de la bodega,  
**quiero** conocer la fecha y hora de cada lectura,  
**para** identificar cuándo ocurrió una anomalía.

**Valor:** permite relacionar datos con un momento específico.  
**MoSCoW:** Should  
**Story points:** 2

```gherkin
Escenario: Conservar la fecha indicada
  Dado la fecha y hora "2026-07-18 10:30:00" como ejemploo
  Cuando se crea una lectura
  Entonces la lectura debe conservar exactamente esa fecha y hora
```