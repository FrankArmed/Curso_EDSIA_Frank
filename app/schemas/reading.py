"""Esquemas que validan los datos de las lecturas."""

# Frank Asael Méndez García - 31/07/2026

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ReadingCreate(BaseModel):
    """Datos necesarios para registrar una lectura."""

    sensor_id: str = Field(min_length=1, max_length=50)
    value: float
    unit: str = Field(min_length=1, max_length=10)

    # La fecha es opcional. Si no se envía, se genera automáticamente.
    recorded_at: datetime | None = None

    @field_validator("unit")
    @classmethod
    def validate_unit(cls, value: str) -> str:
        """Rechaza unidades desconocidas."""
        if value not in {"C", "%"}:
            raise ValueError("La unidad debe ser C o %")

        return value


class ReadingResponse(BaseModel):
    """Formato de una lectura devuelta por la API."""

    # Permite usar objetos de SQLAlchemy como respuesta.
    model_config = ConfigDict(from_attributes=True)

    id: int
    sensor_id: str
    value: float
    unit: str
    recorded_at: datetime