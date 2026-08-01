"""Reglas relacionadas con las lecturas."""

# Frank Asael Méndez García - 31/07/2026

from datetime import datetime

from app.models import Reading
from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.schemas.reading import ReadingCreate


class SensorNotFoundError(Exception):
    """Indica que el sensor no existe."""


class ReadingNotFoundError(Exception):
    """Indica que la lectura no existe."""


class InvalidReadingError(Exception):
    """Indica que la lectura no es válida."""


class InvalidDateRangeError(Exception):
    """Indica que el rango de fechas es incorrecto."""


class ReadingService:
    """Valida y administra lecturas."""

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

        if sensor.sensor_type == "temperature":
            if data.value < -40 or data.value > 125:
                raise InvalidReadingError(
                    "La temperatura debe estar entre -40 y 125"
                )

        if sensor.sensor_type == "humidity":
            if data.value < 0 or data.value > 100:
                raise InvalidReadingError(
                    "La humedad debe estar entre 0 y 100" ##Fin del apartado del codigo hecho con ayuda de la IA. 
                )

        reading = Reading(
            sensor_id=data.sensor_id,
            value=data.value,
            unit=data.unit,
        )

        # Usa la fecha enviada cuando está disponible.
        if data.recorded_at is not None:
            reading.recorded_at = data.recorded_at

        return self.reading_repository.create(reading)

    def get_reading(self, reading_id: int) -> Reading:
        """Devuelve una lectura existente."""
        reading = self.reading_repository.get_by_id(reading_id)

        if reading is None:
            raise ReadingNotFoundError(
                f"La lectura {reading_id} no existe"
            )

        return reading

    def list_readings(
        self,
        offset: int,
        limit: int,
        start_date: datetime | None,
        end_date: datetime | None,
    ) -> list[Reading]:
        """Devuelve lecturas paginadas y filtradas."""
        if (
            start_date is not None
            and end_date is not None
            and start_date > end_date
        ):
            raise InvalidDateRangeError(
                "La fecha inicial no puede ser posterior a la final"
            )

        return self.reading_repository.list_all(
            offset=offset,
            limit=limit,
            start_date=start_date,
            end_date=end_date,
        )