"""Esquemas de entrada y salida para lecturas."""

# Frank Asael Méndez García - 01/08/2026

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ReadingCreate(BaseModel):
    """Datos necesarios para crear una lectura."""

    value: float
    unit: str = Field(min_length=1, max_length=10)
    recorded_at: datetime | None = None

    @field_validator("unit")
    @classmethod
    def validate_unit(cls, value: str) -> str:
        """Valida la unidad."""
        if value not in {"C", "%"}:
            raise ValueError("La unidad debe ser C o %")

        return value


class ReadingUpdate(BaseModel):
    """Datos opcionales para actualizar una lectura."""

    value: float | None = None
    unit: str | None = Field(
        default=None,
        min_length=1,
        max_length=10,
    )
    recorded_at: datetime | None = None

    @field_validator("unit")
    @classmethod
    def validate_unit(
        cls,
        value: str | None,
    ) -> str | None:
        """Valida la unidad cuando fue enviada."""
        if value is not None:
            if value not in {"C", "%"}:
                raise ValueError("La unidad debe ser C o %")

        return value


class ReadingResponse(BaseModel):
    """Formato de una lectura devuelta por la API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    sensor_id: str
    value: float
    unit: str
    recorded_at: datetime