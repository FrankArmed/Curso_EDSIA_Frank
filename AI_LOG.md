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

```text
42 tests de Semana 1 aprobados
43 tests aprobados incluyendo Semana 0
Cobertura total: 91 %
Ruff: sin errores
Mypy: sin errores