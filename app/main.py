"""Aplicación principal de SensorHub."""

# Frank Asael Méndez García - 31/07/2026

from fastapi import FastAPI

from app.db import Base, engine
from app.routers import readings, sensors

# Crea las tablas si todavía no existen.
Base.metadata.create_all(bind=engine)

# Crea la aplicación de FastAPI.
app = FastAPI(
    title="SensorHub API",
    description="API para administrar sensores y lecturas.",
    version="0.2.0",
)

# Agrega los endpoints de sensores y lecturas.
app.include_router(sensors.router)
app.include_router(readings.router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Comprueba que la API está funcionando."""
    return {"status": "ok"}