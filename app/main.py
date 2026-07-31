"""Aplicación principal de la API SensorHub."""

# Frank Asael Méndez García - 18/07/2026

from fastapi import FastAPI

from app.routers import readings

## Este objeto representa la aplicación completa de FastAPI.
app = FastAPI(
    title="SensorHub API",
    description="API para registrar y consultar lecturas de sensores.",
    version="0.1.0",
)

## Eto conecta las rutas de lecturas con la aplicación principal.
app.include_router(readings.router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Confirma que la API está funcionando."""
    return {"status": "ok"}