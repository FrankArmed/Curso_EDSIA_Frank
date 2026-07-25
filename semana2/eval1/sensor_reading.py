"""Representación de una lectura de temperatura y humedad."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: sensor_reading.py

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SensorReading:
    """Almacena la lectura producida por un sensor."""

    sensor_id: str
    temperature: float
    humidity: float
    timestamp: datetime

    def __post_init__(self) -> None:
        """Valida los datos principales de la lectura."""
        clean_id = self.sensor_id.strip() ##PARA ESTA PARTE SE USO IA DADO EL ESCASO CONOCIMIENTO DE ESTOS TEMAS

        if not clean_id:
            raise ValueError("el identificador es obligatorio")

        if not 0 <= self.humidity <= 100:
            raise ValueError("la humedad debe estar entre 0 y 100")

        # Al ser una dataclass congelada, se usa object.__setattr__.
        object.__setattr__(self, "sensor_id", clean_id)