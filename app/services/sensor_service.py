"""Reglas relacionadas con los sensores."""

# Frank Asael Méndez García - 31/07/2026

from app.models import Sensor
from app.repositories.sensor_repository import SensorRepository
from app.schemas.sensor import SensorCreate


class SensorAlreadyExistsError(Exception):
    """Indica que el sensor ya existe."""


class SensorNotFoundError(Exception):
    """Indica que el sensor no existe."""


class InvalidSensorUnitError(Exception):
    """Indica que la unidad es incorrecta."""


class SensorService:
    """Valida y administra sensores."""

    def __init__(self, repository: SensorRepository) -> None:
        """Recibe el repositorio de sensores."""
        self.repository = repository

    def create_sensor(self, data: SensorCreate) -> Sensor:
        """Valida y crea un sensor."""
        existing_sensor = self.repository.get_by_id(data.id)

        if existing_sensor is not None:
            raise SensorAlreadyExistsError(
                f"El sensor {data.id} ya existe"
            )

        expected_unit = "C"

        if data.sensor_type == "humidity":
            expected_unit = "%"

        if data.unit != expected_unit:
            raise InvalidSensorUnitError(
                f"La unidad para {data.sensor_type} debe ser {expected_unit}"
            )

        sensor = Sensor(
            id=data.id,
            sensor_type=data.sensor_type,
            unit=data.unit,
        )

        return self.repository.create(sensor)

    def get_sensor(self, sensor_id: str) -> Sensor:
        """Devuelve un sensor existente."""
        sensor = self.repository.get_by_id(sensor_id)

        if sensor is None:
            raise SensorNotFoundError(
                f"El sensor {sensor_id} no existe"
            )

        return sensor

    def list_sensors(
        self,
        offset: int,
        limit: int,
    ) -> list[Sensor]:
        """Devuelve sensores paginados."""
        return self.repository.list_all(offset, limit)