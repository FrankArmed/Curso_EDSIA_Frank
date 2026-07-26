# Definition of Done — Semana 2

**Autor:** Frank Asael Méndez García  
**Fecha:** 18/07/2026

Una historia se considera terminada cuando cumple todas las condiciones
siguientes:

1. Cumple sus criterios de aceptación en Gherkin.
2. El test fue escrito y ejecutado antes que el código.
3. El historial muestra primero el commit `test` y después el commit `feat`.
4. Todos los tests relacionados pasan.
5. La cobertura total de Semana 2 es de al menos 80 %.
6. Ruff no reporta errores.
7. Mypy no reporta errores.
8. El código utiliza nombres claros y anotaciones de tipos.
9. No existe duplicación evidente o complejidad innecesaria.
10. La historia fue desarrollada en una rama independiente.
11. Se creó y revisó un pull request.
12. Los cambios fueron integrados correctamente en `main`.
13. La documentación fue actualizada cuando fue necesario.
14. La historia se encuentra en la columna `Done` del tablero.
15. El repositorio local está sincronizado con GitHub.

## Comandos de verificación

```powershell
python -m pytest
ruff check semana2
mypy -p semana2.eval1
git status