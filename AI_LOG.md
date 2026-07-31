# Bitácora de uso de inteligencia artificial

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026

Esta bitácora documenta usos específicos de herramientas de inteligencia artificial, internet, entre otras, durante el desarrollo de la Semana 1.

---

## Entrada 1 — Organización inicial del proyecto

**Objetivo:**  
Definir una estructura ordenada para los archivos de la máquina de estados, los ejemplos SOLID y el driver UART.

**Cambios realizados por el estudiante:**  
Se creó la estructura desde PowerShell y se añadieron archivos separados para configuración, analizadores, dispositivo, registrador y buffer.

**Aprendizaje:**  
Separar los componentes desde el inicio facilita las pruebas y permite realizar commits atómicos.

---

## Entrada 2 — Comprensión de los principios SOLID

**Objetivo:**  
Comprender SRP, OCP, LSP, ISP y DIP mediante ejemplos relacionados con sensores.

**Consulta realizada:**  
Se solicitaron ejemplos de cada principio, acompañados de explicaciones y pruebas.

**Aprendizaje:**  
SOLID no busca aumentar innecesariamente la cantidad de clases, sino separar responsabilidades y reducir dependencias difíciles de modificar.

---

## Entrada 3 — Solución de errores en PowerShell

**Objetivo:**  
Resolver errores ocurridos durante las pruebas manuales de los analizadores Modbus, NMEA y CAN.

**Problema encontrado:**  
PowerShell interpretó el símbolo `$` de una sentencia NMEA como una variable y también produjo errores por el uso incorrecto de comillas.

**Consulta realizada:**  
Se pidió identificar por qué el parser rechazaba una sentencia que aparentemente comenzaba con `$`.

**Resultado recibido:**  
Se explicó la diferencia entre las comillas de PowerShell y las de Python, y se recomendó probar cada analizador por separado.

**Cambios realizados por el estudiante:**  
Se corrigieron los comandos de terminal y se verificaron individualmente los tres analizadores.

**Aprendizaje:**  
Un error mostrado durante una prueba no siempre se encuentra dentro del programa; también puede originarse en la forma en que la terminal interpreta el comando.

---

## Entrada 4 — Simplificación de los analizadores

**Objetivo:**  
Mantener el proyecto acorde con el nivel progresivo del curso.

**Consulta realizada:**  
Se pidió reducir la complejidad del código original de los analizadores.

**Resultado recibido:**  
Se eliminó temporalmente la validación completa de CRC Modbus y checksum NMEA, conservando las clases abstractas, el análisis básico y las validaciones principales.

**Cambios realizados por el estudiante:**  
Se utilizó la versión simplificada de `MessageParser`, `ModbusParser`, `NMEAParser` y `CANParser`.

**Aprendizaje:**  
Es preferible comenzar con una implementación clara y funcional antes de incorporar características avanzadas que pueden añadirse en semanas posteriores.

---

## Entrada 5 — Pruebas, cobertura y calidad

**Objetivo:**  
Comprobar que el proyecto cumpliera los requisitos técnicos de la Semana 1.

**Consulta realizada:**  
Se buscaron los comandos necesarios para ejecutar todos los tests, obtener cobertura y revisar Ruff y mypy.

**Resultados obtenidos:**

42 tests de Semana 1 aprobados
43 tests aprobados incluyendo Semana 0
Cobertura total: 91 %
Ruff: sin errores
Mypy: sin errores

--- 

# Semana 2

## Entrada 1 — Revisión del Product Backlog 

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026

**Objetivo:**  
Revisar que las historias del sistema IoT fueran claras y verificables.

**Consulta realizada:**  
Se solicitó revisar las historias, sus criterios Gherkin, story points y
prioridades MoSCoW.

**Cambios realizados:**  
Se crearon historias con criterios observables y medibles.

**Aprendizaje:**  
Una historia debe expresar valor para una persona y sus criterios deben
poder convertirse posteriormente en pruebas automáticas.

## Entrada 2 — Aplicación de TDD estricto

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026

**Objetivo:**  
Aplicar correctamente el ciclo Red, Green y Refactor en los componentes
principales de la Evaluación 1.

**Consulta realizada:**  
Se solicitó una guía paso a paso para escribir primero las pruebas de
`SensorReading`, `AnomalyDetector` y `AlertManager`.

**Resultado recibido:**  
Se propuso crear una rama por componente, escribir el test antes del archivo
de producción, ejecutar el fallo esperado y conservar commits separados.

**Decisiones tomadas:**  
Se mantuvo una implementación sencilla con clases pequeñas, validaciones
básicas y dependencias entregadas mediante el constructor.

**Cambios realizados:**  
Se crearon commits `test` antes de los commits `feat` y se utilizaron pull
requests para incorporar los cambios a `main`.

**Aprendizaje:**  
TDD no consiste en escribir pruebas después de programar. El test debe
definir primero el comportamiento y fallar por una razón conocida.

---

## Entrada 3 — Revisión de ramas, pruebas y cobertura

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026

**Objetivo:**  
Comprobar que todos los componentes estuvieran realmente integrados en
`main` y cumplieran los requisitos de calidad.

**Problema encontrado:**  
Pytest encontró solamente cuatro pruebas porque los pull requests de
`SensorReading` y `AnomalyDetector` seguían abiertos.

**Consulta realizada:**  
Se pidió identificar por qué los tests existían en el historial, pero no
aparecían al ejecutar las pruebas desde `main`.

**Resultado recibido:**  
Se revisaron las ramas, los commits y el estado de los pull requests. Después
se fusionaron las tres ramas en el orden correcto.

**Cambios realizados:**  
Se actualizaron los pull requests, se sincronizó `main` y se ejecutaron
pytest, Ruff, mypy y pytest-cov.

**Resultados finales:**


56 tests aprobados
Cobertura de Semana 2: 99 %
Ruff: sin errores
Mypy: sin errores

---

# Semana 3

## Entrada 1 — Estructura inicial de la API SensorHub

**Autor:** Frank Asael Méndez García  
**Fecha:** 30/07/2026

**Objetivo:**  
Crear una API inicial con FastAPI respetando la nueva estructura oficial
del repositorio.

**Consulta realizada:**  
Se solicitó una estructura sencilla y ordenada junto con Swagger y pruebas con TestClient.

**Decisión tomada:**  
Se separaron la aplicación principal, el router y los esquemas Pydantic.
Las lecturas se almacenaron temporalmente en memoria porque la persistencia
con SQLAlchemy corresponde a la actividad del martes.

**Cambios realizados:**  
Se crearon con ayuda de la IA `app/`, `tests/`, los endpoints iniciales y pruebas automáticas.

**Aprendizaje:**  
FastAPI utiliza los tipos y modelos Pydantic para validar datos y generar
automáticamente la documentación de los endpoints.