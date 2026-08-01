"""Reglas sencillas relacionadas con las lecturas."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: reading_service.py

from app.models import Reading
from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.schemas.reading import ReadingCreate


class SensorNotFoundError(Exception):
    """Error utilizado cuando el sensor no existe."""


class InvalidReadingError(Exception):
    """Error utilizado cuando una lectura no es válida."""


class ReadingService:
    """Comprueba las reglas antes de guardar una lectura."""

    def __init__( ##Apartado del codigo hecho con ayuda de la IA.
        self,
        reading_repository: ReadingRepository,
        sensor_repository: SensorRepository,
    ) -> None:
        """Recibe los repositorios necesarios."""
        self.reading_repository = reading_repository
        self.sensor_repository = sensor_repository

    def create_reading(self, data: ReadingCreate) -> Reading:
        """Valida y crea una lectura."""
        sensor = self.sensor_repository.get_by_id(data.sensor_id)

        if sensor is None:
            raise SensorNotFoundError(
                f"El sensor {data.sensor_id} no existe"
            )

        if data.unit != sensor.unit:
            raise InvalidReadingError(
                f"La unidad debe ser {sensor.unit}"
            )

        # Rango físico utilizado para sensores de temperatura.
        if sensor.sensor_type == "temperature":
            if data.value < -40 or data.value > 125:
                raise InvalidReadingError(
                    "La temperatura debe estar entre -40 y 125"
                )

        # Rango físico utilizado para sensores de humedad.
        if sensor.sensor_type == "humidity":
            if data.value < 0 or data.value > 100:
                raise InvalidReadingError(
                    "La humedad debe estar entre 0 y 100"
                )

        reading = Reading(
            sensor_id=data.sensor_id,
            value=data.value,
            unit=data.unit,
        )

        return self.reading_repository.create(reading)

    def list_readings(self) -> list[Reading]:
        """Solicita todas las lecturas al repositorio."""
        return self.reading_repository.list_all()