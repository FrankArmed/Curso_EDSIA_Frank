"""Aplicación principal de SensorHub."""

# Frank Asael Méndez García - 31/07/2026

from fastapi import FastAPI

from app.routers import alerts, readings, sensors

# Crea la aplicación principal de FastAPI.
app = FastAPI(
    title="SensorHub API",
    description="API para administrar sensores y lecturas.",
    version="0.2.0",
)

# Agrega los endpoints de sensores y lecturas.
app.include_router(sensors.router)
app.include_router(readings.router)
app.include_router(alerts.router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Comprueba que la API está funcionando."""
    return {"status": "ok"}

@app.get("/metrics", tags=["metrics"])
def metrics() -> dict[str, int]:
    """Devuelve métricas básicas de la API."""
    return {"requests_total": 0}