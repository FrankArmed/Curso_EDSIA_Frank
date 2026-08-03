# Peer Review — Ronda 1

**Autor:** Frank Asael Méndez García  
**Semana:** 3  
**Proyecto:** SensorHub API

## Motivo

El Pull Request original fue fusionado accidentalmente antes de recibir la
revisión por pares.

Esta nueva rama se utiliza para completar correctamente la ronda de revisión
antes de realizar otro merge.

## Archivos que deben revisarse

- `app/`
- `tests/`
- `docs/adr/0001-layered-architecture.md`
- `README.md`
- `requirements.txt`
- `pyproject.toml`

## Comandos de verificación

```powershell
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
python -m pytest
ruff check .
mypy app

Swagger:

http://127.0.0.1:8000/docs