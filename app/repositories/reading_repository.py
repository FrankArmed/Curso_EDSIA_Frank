"""Acceso a las lecturas almacenadas."""

# Frank Asael Méndez García - 01/08/2026

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Reading


class ReadingRepository:
    """Realiza operaciones sobre readings."""

    def __init__(self, session: Session) -> None:
        """Guarda la sesión."""
        self.session = session

    def create(self, reading: Reading) -> Reading:
        """Guarda una lectura."""
        self.session.add(reading)
        self.session.commit()
        self.session.refresh(reading)

        return reading

    def get_by_id(self, reading_id: int) -> Reading | None:
        """Busca una lectura por ID."""
        return self.session.get(Reading, reading_id)

    def list_for_sensor(
        self,
        sensor_id: str,
        offset: int,
        limit: int,
        from_date: datetime | None,
        to_date: datetime | None,
    ) -> list[Reading]:
        """Lista lecturas de un sensor."""
        statement = select(Reading).where(
            Reading.sensor_id == sensor_id
        )

        if from_date is not None:
            statement = statement.where(
                Reading.recorded_at >= from_date
            )

        if to_date is not None:
            statement = statement.where(
                Reading.recorded_at <= to_date
            )

        statement = (
            statement
            .order_by(Reading.id)
            .offset(offset)
            .limit(limit)
        )

        return list(self.session.scalars(statement))

    def save(self, reading: Reading) -> Reading:
        """Guarda los cambios de una lectura."""
        self.session.commit()
        self.session.refresh(reading)

        return reading

    def delete(self, reading: Reading) -> None:
        """Elimina una lectura."""
        self.session.delete(reading)
        self.session.commit()