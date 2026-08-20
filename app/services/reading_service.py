"""Lista lecturas con paginación y filtros de fecha."""

# Frank Asael Méndez García - 15/08/2026

from datetime import datetime
from typing import Any

from app.models import Reading, Sensor
from app.repositories.protocols import (
    ReadingRepositoryProtocol,
    SensorRepositoryProtocol,
)
from app.schemas.reading import ReadingCreate, ReadingUpdate


class SensorNotFoundError(Exception):
    """Indica que el sensor no existe."""


class ReadingNotFoundError(Exception):
    """Indica que la lectura no existe."""


class InvalidReadingError(Exception):
    """Indica que la lectura no es válida."""


class InvalidDateRangeError(Exception):
    """Indica que las fechas son incorrectas."""


class ReadingService:
    """Valida y administra lecturas."""

    def __init__(
        self,
        reading_repository: ReadingRepositoryProtocol,
        sensor_repository: SensorRepositoryProtocol,
    ) -> None:
        """Recibe los repositorios."""
        self.reading_repository = reading_repository
        self.sensor_repository = sensor_repository

    def get_sensor(self, sensor_id: str) -> Sensor:
        """Devuelve el sensor asociado."""
        sensor = self.sensor_repository.get_by_id(sensor_id)

        if sensor is None:
            raise SensorNotFoundError(
                f"El sensor {sensor_id} no existe"
            )

        return sensor

    def validate_reading(
        self,
        sensor: Sensor,
        value: float,
        unit: str,
    ) -> None:
        """Valida unidad y rango físico."""
        if unit != sensor.unit:
            raise InvalidReadingError(
                f"La unidad debe ser {sensor.unit}"
            )

        if sensor.sensor_type == "temperature":
            if value < -40 or value > 125:
                raise InvalidReadingError(
                    "La temperatura debe estar entre -40 y 125"
                )

        elif sensor.sensor_type == "humidity":
            if value < 0 or value > 100:
                raise InvalidReadingError(
                    "La humedad debe estar entre 0 y 100"
                )

        else:
            raise InvalidReadingError(
                "Tipo de sensor no soportado"
            )

    def _validate_recorded_at(
        self,
        recorded_at: datetime,
    ) -> None:
        """Rechaza fechas futuras."""
        now = datetime.now(tz=recorded_at.tzinfo)

        if recorded_at > now:
            raise InvalidReadingError(
                "La fecha de la lectura no puede ser futura"
            )

    def create_reading(
        self,
        sensor_id: str,
        data: ReadingCreate,
    ) -> Reading:
        """Valida y crea una lectura."""
        sensor = self.get_sensor(sensor_id)

        self.validate_reading(
            sensor,
            data.value,
            data.unit,
        )

        reading = Reading(
            sensor_id=sensor_id,
            value=data.value,
            unit=data.unit,
        )

        if data.recorded_at is not None:
            self._validate_recorded_at(data.recorded_at)
            reading.recorded_at = data.recorded_at

        return self.reading_repository.create(reading)

    def get_reading(self, reading_id: int) -> Reading:
        """Devuelve una lectura."""
        reading = self.reading_repository.get_by_id(reading_id)

        if reading is None:
            raise ReadingNotFoundError(
                f"La lectura {reading_id} no existe"
            )

        return reading

    def list_for_sensor( ##Se agregó la función list_for_sensor para listar las lecturas de un sensor con paginación y filtrado por fechas. 
        self,
        sensor_id: str,
        offset: int,
        limit: int,
        from_date: datetime | None,
        to_date: datetime | None,
    ) -> list[Reading]:
        """Lista lecturas de un sensor."""
        self.get_sensor(sensor_id)

        if (
            from_date is not None
            and to_date is not None
            and from_date > to_date
        ):
            raise InvalidDateRangeError(
                "La fecha inicial no puede ser posterior a la final"
            )

        return self.reading_repository.list_for_sensor(
            sensor_id,
            offset,
            limit,
            from_date,
            to_date,
        )

    def update_reading(
        self,
        reading_id: int,
        data: ReadingUpdate,
    ) -> Reading:
        """Actualiza parcialmente una lectura."""
        reading = self.get_reading(reading_id)
        sensor = self.get_sensor(reading.sensor_id)

        new_value = reading.value
        new_unit = reading.unit

        if data.value is not None:
            new_value = data.value

        if data.unit is not None:
            new_unit = data.unit

        self.validate_reading(
            sensor,
            new_value,
            new_unit,
        )

        reading.value = new_value
        reading.unit = new_unit

        if data.recorded_at is not None:
            self._validate_recorded_at(data.recorded_at)
            reading.recorded_at = data.recorded_at

        return self.reading_repository.save(reading)

    def delete_reading(self, reading_id: int) -> None:
        """Elimina una lectura."""
        reading = self.get_reading(reading_id)
        self.reading_repository.delete(reading)

    def get_statistics(self, sensor_id: str) -> dict[str, Any]:
        """Obtiene las estadísticas de las lecturas de un sensor."""
        return self.reading_repository.get_statistics(sensor_id)