"""Esquemas que validan los datos de los sensores."""

# Frank Asael Méndez García - 30/07/2026

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SensorCreate(BaseModel):
    """Datos necesarios para crear un sensor."""

    id: str = Field(min_length=1, max_length=50)
    sensor_type: str = Field(min_length=1, max_length=20)
    unit: str = Field(min_length=1, max_length=10)

    @field_validator("sensor_type")
    @classmethod
    def validate_sensor_type(cls, value: str) -> str:
        """Acepta solamente los tipos de sensor conocidos."""
        allowed_types = {"temperature", "humidity"}

        if value not in allowed_types:
            raise ValueError("El tipo debe ser temperature o humidity")

        return value

    @field_validator("unit")
    @classmethod
    def validate_unit(cls, value: str) -> str:
        """Acepta solamente las unidades utilizadas por el proyecto."""
        allowed_units = {"C", "%"}

        if value not in allowed_units:
            raise ValueError("La unidad debe ser C o %")

        return value


class SensorResponse(SensorCreate):
    """Formato utilizado para devolver un sensor."""

    # Permite convertir un objeto SQLAlchemy en una respuesta Pydanticc.
    model_config = ConfigDict(from_attributes=True)