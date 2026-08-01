"""Acceso a los sensores almacenados en la base de datos."""

# Frank Asael Méndez García - 30/07/2026

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Sensor


class SensorRepository:
    """Realiza operaciones sencillas sobre la tabla sensors."""

    def __init__(self, session: Session) -> None:
        """Guarda la sesión que utilizará el repositorio."""
        self.session = session

    def create(self, sensor: Sensor) -> Sensor:
        """Guarda un sensor en la base de datos."""
        self.session.add(sensor)
        self.session.commit()
        self.session.refresh(sensor)

        return sensor

    def get_by_id(self, sensor_id: str) -> Sensor | None:
        """Busca un sensor mediante su identificador."""
        return self.session.get(Sensor, sensor_id)

    def list_all(self) -> list[Sensor]:
        """Devuelve todos los sensores."""
        statement = select(Sensor).order_by(Sensor.id)
        sensors = self.session.scalars(statement)

        return list(sensors)