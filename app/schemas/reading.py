"""Esquemas que validan los datos de las lecturas."""

# Frank Asael Méndez García - 30/07/2026

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator


class ReadingCreate(BaseModel):
    """Datos necesarios para registrar una lectura."""

    sensor_id: str = Field(min_length=1, max_length=50)
    value: float
    unit: str = Field(min_length=1, max_length=10)

    @field_validator("unit")
    @classmethod
    def validate_unit(cls, value: str) -> str:
        """Rechaza las unidades desconocidas."""
        if value not in {"C", "%"}:
            raise ValueError("La unidad debe ser C o %")

        return value


class ReadingResponse(ReadingCreate):
    """Formato utilizado para devolver una lectura."""

    # Permite crear la respuesta desde un modelo SQLAlchemy.
    model_config = ConfigDict(from_attributes=True)

    id: int
    recorded_at: datetime