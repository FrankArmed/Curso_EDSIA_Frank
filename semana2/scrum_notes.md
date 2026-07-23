# Apuntes de Scrum — Semana 2

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026  
**Proyecto:** Sistema de monitoreo IoT para una bodega industrial

---

## 1. Objetivo de estudio

El objetivo de esta actividad es comprender Scrum como un marco completo
de trabajo y aplicarlo al desarrollo de un sistema de monitoreo IoT.

Durante esta semana se utilizarán:

- Las tres responsabilidades de Scrum.
- Los cinco eventos.
- Los tres artefactos.
- Los compromisos asociados a los artefactos.
- Los cinco valores.
- Los tres pilares del empirismo.
- Un Product Backlog.
- Un Sprint Backlog.
- Una Definition of Done.
- Un GitHub Project para visualizar el trabajo.

---

## 2. ¿Qué es Scrum?

Scrum es un marco de trabajo ligero utilizado para generar valor mediante
soluciones adaptables a problemas complejos.

En lugar de planificar todo el proyecto detalladamente desde el principio,
el trabajo se organiza en periodos cortos llamados Sprints. Durante cada
Sprint se construye un resultado utilizable, se inspecciona el progreso y
se adapta el plan de acuerdo con lo aprendido.

Scrum no describe exactamente cómo programar. Establece responsabilidades,
eventos, artefactos y reglas que permiten organizar y revisar el trabajo.

---

## 3. Los tres pilares de Scrum

### 3.1 Transparencia

El trabajo y el proceso deben ser visibles y comprensibles para quienes
participan en el proyecto.

En este proyecto la transparencia se logrará mediante:

- Un repositorio público.
- Historias de usuario visibles como Issues.
- Un tablero de GitHub Projects.
- Commits descriptivos.
- Pull requests.
- Resultados de pruebas y cobertura.
- Una bitácora de uso de inteligencia artificial.

### 3.2 Inspección

El trabajo debe revisarse frecuentemente para identificar problemas,
desviaciones o nuevas necesidades.

En este proyecto se inspeccionarán:

- Los criterios de aceptación.
- El orden de los commits TDD.
- Los resultados de pytest.
- La cobertura.
- Los reportes de Ruff.
- Los reportes de mypy.
- El avance del Sprint Goal.

### 3.3 Adaptación

Cuando la inspección revela un problema, el proceso o el producto debe
ajustarse oportunamente.

Ejemplos de adaptación en este proyecto:

- Corregir una historia que tenga criterios vagos.
- Dividir una tarea que resulte demasiado grande.
- Añadir una prueba para un caso límite no contemplado.
- Modificar el Sprint Backlog si una tarea deja de contribuir al objetivo.
- Mejorar la Definition of Done después de detectar una omisión.

---

## 4. Los cinco valores de Scrum

### 4.1 Compromiso

Me comprometo a completar el Sprint Goal y a respetar el proceso TDD:
primero el test, después el código mínimo y finalmente el refactor.

### 4.2 Enfoque

Durante el Sprint trabajaré primero en las historias seleccionadas. Evitaré
añadir funciones que no contribuyan al objetivo de la Evaluación 1.

### 4.3 Apertura

Registraré los errores encontrados, las decisiones tomadas y el uso de
inteligencia artificial. No ocultaré tests fallidos que formen parte de la
evidencia del ciclo Red.

### 4.4 Respeto

Mantendré el código organizado, documentado y comprensible para que pueda
ser revisado por otras personas. También respetaré los criterios y reglas
de la actividad.

### 4.5 Valentía

Aceptar un test fallido será parte normal del proceso. Corregiré los
problemas sin evitar los casos difíciles y explicaré las decisiones
técnicas tomadas.

---

## 5. Las tres responsabilidades de Scrum

La Scrum Guide 2020 utiliza el término responsabilidades específicas
dentro del Scrum Team. Frecuentemente también se les llama roles.

### 5.1 Product Owner

El Product Owner es responsable de maximizar el valor del producto y de
administrar eficazmente el Product Backlog.

Sus actividades incluyen:

- Definir y comunicar el Product Goal.
- Crear y comunicar los elementos del Product Backlog.
- Ordenar los elementos según su valor.
- Mantener el Product Backlog visible y comprensible.
- Aclarar qué necesidades son más importantes.

#### Aplicación en este proyecto

Como Product Owner:

- Pensaré en las necesidades del operador y supervisor de la bodega.
- Priorizaré la detección de anomalías sobre las funciones visuales.
- Utilizaré MoSCoW para ordenar las historias.
- Seleccionaré historias que generen un núcleo funcional.
- Evitaré introducir funciones que no aporten valor al Sprint Goal.

### 5.2 Scrum Master

El Scrum Master es responsable de ayudar a establecer Scrum y mejorar la
efectividad del Scrum Team.

Sus actividades incluyen:

- Ayudar a comprender y aplicar Scrum.
- Facilitar los eventos.
- Ayudar a eliminar impedimentos.
- Promover la mejora continua.
- Proteger el enfoque en el Sprint Goal.

#### Aplicación en este proyecto

Como Scrum Master:

- Revisaré diariamente el tablero.
- Verificaré que las historias tengan criterios verificables.
- Confirmaré que el test preceda al código.
- Registraré los impedimentos encontrados.
- Comprobaré que cada historia cumpla la Definition of Done.
- Evitaré mover una historia a Done si todavía falta calidad o evidencia.

### 5.3 Developers

Los Developers son responsables de crear un Increment utilizable durante
el Sprint.

Sus actividades incluyen:

- Crear el Sprint Backlog.
- Construir el producto.
- Mantener la calidad.
- Adaptar diariamente su plan.
- Cumplir la Definition of Done.

#### Aplicación en este proyecto

Como Developer:

- Crearé los tests antes que las implementaciones.
- Utilizaré ramas por historia.
- Haré commits pequeños y descriptivos.
- Ejecutaré pytest, Ruff, mypy y cobertura.
- Abriré pull requests antes de integrar las historias.
- Mantendré el código sencillo y adecuado a mi nivel actual.

---

## 6. Los cinco eventos de Scrum

### 6.1 Sprint

El Sprint contiene todos los demás eventos. Durante el Sprint se trabaja
para alcanzar un Sprint Goal y crear un Increment utilizable.

#### Aplicación propuesta

- Duración: una semana.
- Inicio: lunes.
- Cierre: sábado antes de las 23:59.
- Producto: núcleo del sistema IoT.
- Incremento esperado: lectura, detección y alertas verificadas con tests.

### 6.2 Sprint Planning

Durante Sprint Planning se responde:

1. ¿Por qué este Sprint es valioso?
2. ¿Qué puede completarse durante el Sprint?
3. ¿Cómo se realizará el trabajo seleccionado?

#### Aplicación propuesta

En `sprint_planning.md` se documentarán:

- Sprint Goal.
- Cinco a siete historias seleccionadas.
- Justificación de cada historia.
- Story points.
- Tareas de máximo cuatro horas.
- Riesgos y dependencias.
- Definition of Done.

### 6.3 Daily Scrum

El Daily Scrum permite inspeccionar el progreso hacia el Sprint Goal y
adaptar el plan.

#### Aplicación individual

Cada día responderé:

1. ¿Qué completé desde la última revisión?
2. ¿Qué realizaré ahora?
3. ¿Qué impedimento tengo?
4. ¿Sigo avanzando hacia el Sprint Goal?

Registro propuesto:

| Día | Trabajo terminado | Trabajo siguiente | Impedimento |
|---|---|---|---|
| Lunes | Estudio y tablero | Crear backlog | Ninguno |
| Martes | Historias y Gherkin | Comenzar TDD | Pend |
| Miércoles | Pend | Pend | Pend |
| Jueves | Pend | Pend | Pend |
| Viernes | Pend | Pend | Pend |
| Sábado | Pend | Pend | Pend |

### 6.4 Sprint Review

En la Sprint Review se inspecciona el resultado construido y se analiza
qué hacer a continuación...

#### Aplicación propuesta

Durante la revisión comprobaré:

- Qué historias quedaron realmente terminadas.
- Qué criterios Gherkin fueron satisfechos.
- Si el sistema registra lecturas válidas.
- Si detecta temperatura y humedad fuera de rango.
- Si puede enviar alertas por consola y archivo.
- Si la cobertura alcanza al menos 80 %.
- Qué historias deben regresar al Product Backlog.

### 6.5 Sprint Retrospective

La Sprint Retrospective inspecciona cómo se realizó el trabajo y define
mejoras para el siguiente Sprint.

Se responderá:

- ¿Qué salió bien?
- ¿Qué salió mal o fue difícil?
- ¿Qué se puede mejorar?
- ¿Qué acción concreta se aplicará después?

---

## 7. Los tres artefactos y sus compromisos

### 7.1 Product Backlog

Es una lista ordenada y cambiante de todo lo que puede necesitar el producto.

Contendrá:

- Historias de usuario.
- Prioridad MoSCoW.
- Story points.
- Criterios de aceptación.
- Valor de cada historia.

### Product Goal

### Product Goal del sistema

Construir un sistema de monitoreo capaz de registrar lecturas de temperatura
y humedad, detectar anomalías mediante umbrales configurables y generar
alertas por diferentes medios.

### 7.2 Sprint Backlog

Contiene:

- El Sprint Goal.
- Las historias seleccionadas.
- El plan de tareas para completar esas historias.

#### Compromiso: Sprint Goal

### Sprint Goal propuesto (aun sujeto a cambios)

Construir mediante TDD el núcleo verificable de un sistema IoT que represente
lecturas de sensores, detecte anomalías con umbrales configurables y emita
alertas usando estrategias intercambiables.

### 7.3 Increment

#### Incremento esperado

- `SensorReading`.
- `AnomalyDetector`.
- `AlertManager`.
- `ConsoleAlert`.
- `FileAlert`.
- Tests de comportamiento.
- Cobertura mínima de 80 %.
- Ruff limpio.
- Mypy sin errores.
- Pull requests revisados.

#### Compromiso: Definition of Done

La definition of ddone establecerá las condiciones obligatorias para
considerar terminada una historia.

---

## 8. Diferencias importantes

### 8.1 Product Backlog y Sprint Backlog

El Product Backlog contiene todas las necesidades conocidas y futuras.

El Sprint Backlog contiene únicamente las historias elegidas para el Sprint,
el Sprint Goal y el plan para realizarlas.

Una historia puede existir en el Product Backlog sin estar seleccionada para
el Sprint actual.

### 8.2 Sprint Review y Sprint Retrospective

La Sprint Review inspecciona el producto y el valor entregado.

La Sprint Retrospective inspecciona cómo se realizó el trabajo y cómo puede
mejorarse el proceso.

### 8.3 Increment y entrega parcial sin terminar

Un conjunto de archivos no es automáticamente un Increment. Para considerarlo
Increment debe cumplir la Definition of Done y ser utilizable..

### 8.4 Scrum y una lista de tareas

- Un objetivo.
- Responsabilidades.
- Eventos de inspección y adaptación.
- Artefactos transparentes.
- Compromisos de calidad.
- Entrega incremental de valor.

---

## 9. Aplicación de Scrum siendo un solo desarrollador

Aunque el proyecto se realizará individualmente, separaré las tres
responsabilidades mentalmente. Cuando priorice valor actuaré como Owner.
Cuando revise el proceso, los impedimentos y la Definition of Done actuaré
como Scrum Master. Cuando escriba tests, código, documentación y pull requests actuaré como
Developer.

---

## 10. Contexto del producto

La bodega industrial cuenta con 10 sensores de temperatura y humedad.

Cada sensor envía una lectura cada 30 segundos.

Se considera inicialmente una anomalía cuando:

- La temperatura supera 35 °C.
- La humedad supera 80 %.

Estos valores deben ser configurables y no estar escritos directamente
dentro de la lógica del detector.

Las alertas deben poder enviarse mediante:

- Consola.
- Archivo.

El diseño debe permitir añadir otras estrategias en el futuro sin modificar
el administrador principal.

---

## 11. Supuestos iniciales del proyecto

- Cada lectura pertenece a un sensor identificado.
- La humedad válida se encuentra entre 0 y 100 %.
- Los valores iguales al umbral no se consideran anomalía.
- Una anomalía se produce solamente al superar el umbral.
- El sistema no se conectará todavía a sensores físicos.
- Los datos se crearán dentro de las pruebas.
- No se desarrollará una interfaz gráfica.
- No se utilizará una base de datos durante este Sprint.
- No se implementará comunicación por red.
- El objetivo será construir y verificar el núcleo del dominio.

---

## 12. Riesgos iniciales

### Riesgo 1: escribir código antes del test

**Respuesta:** revisar el historial antes de cada commit y mantener el orden
Red, Green y Refactor.

### Riesgo 2: criterios Gherkin demasiado generales

**Respuesta:** exigir resultados observables y valores concretos.

### Riesgo 3: seleccionar demasiadas historias

**Respuesta:** limitar el Sprint a entre cinco y siete historias.

### Riesgo 4: aumentar demasiado la complejidad

**Respuesta:** utilizar implementaciones sencillas que cumplan los criterios
sin agregar tecnologías no requeridas.

### Riesgo 5: confundir story points con horas

**Respuesta:** utilizar los puntos como estimación relativa y las horas
solamente para dividir tareas.

---

## 13. Conceptos obtenidos del curso de Atlassian

### Agile

Agile representa una forma de trabajar basada en entregas frecuentes,
colaboración, retroalimentación y adaptación.

### Scrum

Scrum es un marco concreto que organiza el trabajo en Sprints mediante
responsabilidades, eventos, artefactos y compromisos.

### Kanban

Kanban visualiza el flujo de trabajo y ayuda a controlar cuánto trabajo se
encuentra en progreso.

### Jira y GitHub Projects

Jira y GitHub Projects pueden utilizar tableros, estados y elementos de
trabajo para representar el avance.

Para esta evaluación se utilizará GitHub Projects porque está integrado con:

- Issues.
- Pull requests.
- Repositorio.
- Ramas.
- Historial de desarrollo.

### Backlog

El backlog debe permanecer ordenado y actualizarse cuando aparece nueva
información.

### Trabajo en progreso

Tener demasiadas historias en progreso aumenta el cambio de contexto. Por
eso se intentará trabajar en una historia principal a la vez.

### Estimación

La estimación no pretende predecir exactamente el tiempo. Permite comparar
el tamaño relativo, riesgo e incertidumbre de las historias.

---

## 14. Configuración del GitHub Project

**Nombre:** Semana 2 - Sprint 1 - IoT Bodega

**Repositorio predeterminado:** FrankArmed/Curso_EDSIA_Frank

**Visibilidad:** Pública

**Vista principal:** Sprint Board

**Enlace:** PENDIENTE_DE_REEMPLAZAR_CON_EL_ENLACE_REAL

### Estados del tablero

| Estado | Significado |
|---|---|
| Backlog | Historia disponible, pero no seleccionada |
| Sprint | Historia seleccionada para el Sprint |
| In Progress | Historia en desarrollo |
| Review | Historia con pull request o revisión pendiente |
| Done | Historia que cumple la Definition of Done |

### Reglas para mover historias

#### De Backlog a Sprint

La historia fue seleccionada y justificada durante Sprint Planning.

#### De Sprint a In Progress

Se creó su rama y comenzó el ciclo TDD.

#### De In Progress a Review

Los tests pasan, la calidad fue revisada y existe un pull request.

#### De Review a Done

La historia cumple todos los criterios y la Definition of Done.

---

## 15. Reflexión personal (pendiente)

### ¿Qué concepto de Scrum me pareció más importante?



### ¿Qué diferencia encontré entre Scrum y una lista de tareas?



### ¿Cómo aplicaré Scrum siendo el único desarrollador?



### ¿Qué espero mejorar durante la semana?



### ¿Cuál será la principal dificultad?


---
