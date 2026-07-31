"""Esquemas Pydantic para las lecturas de sensores."""

# Frank Asael Méndez García - 18/07/2026

from pydantic import BaseModel, Field


class ReadingCreate(BaseModel):
    """Datos que el cliente debe enviar para registrar una lectura."""

    sensor_id: str = Field(min_length=1, max_length=50)
    value: float
    unit: str = Field(min_length=1, max_length=10)


class ReadingResponse(ReadingCreate):
    """Lectura devuelta por la API con su identificador."""

    id: int ##Esto sirve para que el cliente pueda identificar la lectura registrada en la base de datos. 