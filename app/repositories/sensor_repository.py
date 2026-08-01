"""Acceso a los sensores almacenados."""

# Frank Asael Méndez García - 31/07/2026

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Sensor


class SensorRepository:
    """Realiza operaciones sobre la tabla sensors."""

    def __init__(self, session: Session) -> None:
        """Guarda la sesión de base de datos."""
        self.session = session

    def create(self, sensor: Sensor) -> Sensor:
        """Guarda un sensor."""
        self.session.add(sensor)
        self.session.commit()
        self.session.refresh(sensor)

        return sensor

    def get_by_id(self, sensor_id: str) -> Sensor | None:
        """Busca un sensor por su identificador."""
        return self.session.get(Sensor, sensor_id)

    def list_all(
        self,
        offset: int = 0,
        limit: int = 20,
    ) -> list[Sensor]:
        """Devuelve sensores con paginación."""
        statement = (
            select(Sensor)
            .order_by(Sensor.id)
            .offset(offset)
            .limit(limit)
        )

        sensors = self.session.scalars(statement)

        return list(sensors)