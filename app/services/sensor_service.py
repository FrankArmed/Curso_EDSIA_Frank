"""Reglas relacionadas con los sensores."""

# Frank Asael Méndez García - 01/08/2026

from app.models import Sensor
from app.repositories.protocols import SensorRepositoryProtocol
from app.schemas.sensor import SensorCreate, SensorUpdate


class SensorAlreadyExistsError(Exception):
    """Indica que el sensor ya existe."""


class SensorNotFoundError(Exception):
    """Indica que el sensor no existe."""


class InvalidSensorUnitError(Exception):
    """Indica que la unidad es incorrecta."""


class SensorService:
    """Valida y administra sensores."""

    def __init__(
        self,
        repository: SensorRepositoryProtocol,
    ) -> None:
        """Recibe un repositorio."""
        self.repository = repository

    def validate_unit(
        self,
        sensor_type: str,
        unit: str,
    ) -> None:
        """Comprueba la unidad del sensor."""
        expected_unit = "C"

        if sensor_type == "humidity":
            expected_unit = "%"

        if unit != expected_unit:
            raise InvalidSensorUnitError(
                f"La unidad para {sensor_type} debe ser {expected_unit}"
            )

    def create_sensor(self, data: SensorCreate) -> Sensor:
        """Valida y crea un sensor."""
        existing_sensor = self.repository.get_by_id(data.id)

        if existing_sensor is not None:
            raise SensorAlreadyExistsError(
                f"El sensor {data.id} ya existe"
            )

        self.validate_unit(data.sensor_type, data.unit)

        sensor = Sensor(
            id=data.id,
            sensor_type=data.sensor_type,
            unit=data.unit,
            location=data.location,
            is_active=data.is_active,
            alert_threshold=data.alert_threshold,
        )

        return self.repository.create(sensor)

    def get_sensor(self, sensor_id: str) -> Sensor:
        """Devuelve un sensor."""
        sensor = self.repository.get_by_id(sensor_id)

        if sensor is None:
            raise SensorNotFoundError(
                f"El sensor {sensor_id} no existe"
            )

        return sensor

    def list_sensors( ##Apartado realizado con ayuda de la IA. Se agregó la función list_sensors para listar los sensores con paginación.
        self,
        offset: int,
        limit: int,
    ) -> list[Sensor]:
        """Devuelve sensores paginados."""
        return self.repository.list_all(offset, limit)

    def update_sensor(
        self,
        sensor_id: str,
        data: SensorUpdate,
    ) -> Sensor:
        """Actualiza parcialmente un sensor."""
        sensor = self.get_sensor(sensor_id)

        new_type = sensor.sensor_type
        new_unit = sensor.unit

        if data.sensor_type is not None:
            new_type = data.sensor_type

        if data.unit is not None:
            new_unit = data.unit

        self.validate_unit(new_type, new_unit)

        sensor.sensor_type = new_type
        sensor.unit = new_unit

        if data.location is not None:
            sensor.location = data.location

        if data.is_active is not None:
            sensor.is_active = data.is_active

        if data.alert_threshold is not None:
            sensor.alert_threshold = data.alert_threshold

        return self.repository.save(sensor)

    def delete_sensor(self, sensor_id: str) -> None:
        """Elimina un sensor."""
        sensor = self.get_sensor(sensor_id)
        self.repository.delete(sensor)