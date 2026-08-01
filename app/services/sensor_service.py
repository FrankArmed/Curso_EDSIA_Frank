"""Reglas relacionadas con los sensores."""

# Frank Asael Méndez García - 31/07/2026

from app.models import Sensor
from app.repositories.sensor_repository import SensorRepository
from app.schemas.sensor import SensorCreate


class SensorAlreadyExistsError(Exception):
    """Error utilizado cuando el sensor ya existe."""


class InvalidSensorUnitError(Exception):
    """Error utilizado cuando la unidad no coincide con el tipo."""


class SensorService:
    """Comprueba las reglas antes de guardar un sensor."""

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

        # Cada tipo de sensor utiliza una unidad específica.
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

    def list_sensors(self) -> list[Sensor]:
        """Solicita todos los sensores al repositorio."""
        return self.repository.list_all()