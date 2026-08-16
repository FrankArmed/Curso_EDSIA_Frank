"""Esquemas de entrada y salida para sensores."""

# Frank Asael Méndez García - 01/08/2026

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SensorCreate(BaseModel):
    """Datos necesarios para crear un sensor."""

    id: str = Field(min_length=1, max_length=50)
    sensor_type: str = Field(min_length=1, max_length=20)
    unit: str = Field(min_length=1, max_length=10)
    alert_threshold: float | None = None

    @field_validator("sensor_type")
    @classmethod
    def validate_sensor_type(cls, value: str) -> str:
        """Valida el tipo de sensor."""
        if value not in {"temperature", "humidity"}:
            raise ValueError("El tipo debe ser temperature o humidity")

        return value

    @field_validator("unit")
    @classmethod
    def validate_unit(cls, value: str) -> str:
        """Valida la unidad."""
        if value not in {"C", "%"}:
            raise ValueError("La unidad debe ser C o %")

        return value


class SensorUpdate(BaseModel):
    """Datos opcionales para actualizar un sensor."""

    sensor_type: str | None = Field(
        default=None,
        min_length=1,
        max_length=20,
    )
    unit: str | None = Field(
        default=None,
        min_length=1,
        max_length=10,
    )
    alert_threshold: float | None = None

    @field_validator("sensor_type")
    @classmethod
    def validate_sensor_type(
        cls,
        value: str | None,
    ) -> str | None:
        """Valida el tipo cuando fue enviado."""
        if value is not None:
            if value not in {"temperature", "humidity"}:
                raise ValueError(
                    "El tipo debe ser temperature o humidity"
                )

        return value

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


class SensorResponse(SensorCreate):
    """Formato de un sensor devuelto por la API."""

    model_config = ConfigDict(from_attributes=True)