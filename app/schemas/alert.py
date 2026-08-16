"""Esquemas de salida para alertas."""

# Frank Asael Méndez García - 15/08/2026

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AlertResponse(BaseModel):
    """Formato de una alerta devuelta por la API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    sensor_id: str
    reading_id: int
    value: float
    threshold: float
    message: str
    created_at: datetime