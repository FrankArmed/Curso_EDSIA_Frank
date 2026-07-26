# Sprint Retrospective — Evaluación 1

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026  
**Proyecto:** Sistema IoT para una bodega industrial

## Resultado del Sprint

Durante el Sprint se implementó el núcleo del sistema de monitoreo:

- Registro de lecturas mediante `SensorReading`.
- Detección de temperatura elevada.
- Detección de humedad elevada.
- Umbrales configurables mediante `AnomalyDetector`.
- Administración de estrategias de alerta.
- Alertas en consola.
- Alertas almacenadas en archivo.
- Prueba de integración del flujo principal.

Los componentes principales fueron desarrollados mediante el ciclo:

```text
Red → Green → Refactor