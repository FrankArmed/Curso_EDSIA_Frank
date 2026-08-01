"""Acceso a los sensores almacenados."""

# Frank Asael Méndez García - 01/08/2026

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Sensor


class SensorRepository:
    """Realiza operaciones sobre sensors."""

    def __init__(self, session: Session) -> None:
        """Guarda la sesión."""
        self.session = session

    def create(self, sensor: Sensor) -> Sensor:
        """Guarda un sensor."""
        self.session.add(sensor)
        self.session.commit()
        self.session.refresh(sensor)

        return sensor

    def get_by_id(self, sensor_id: str) -> Sensor | None:
        """Busca un sensor por ID."""
        return self.session.get(Sensor, sensor_id)

    def list_all(
        self,
        offset: int,
        limit: int,
    ) -> list[Sensor]:
        """Devuelve sensores paginados."""
        statement = (
            select(Sensor)
            .order_by(Sensor.id)
            .offset(offset)
            .limit(limit)
        )

        return list(self.session.scalars(statement))

    def save(self, sensor: Sensor) -> Sensor:
        """Guarda los cambios de un sensor."""
        self.session.commit()
        self.session.refresh(sensor)

        return sensor

    def delete(self, sensor: Sensor) -> None:
        """Elimina un sensor."""
        self.session.delete(sensor)
        self.session.commit()