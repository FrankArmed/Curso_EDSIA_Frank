"""Acceso a las lecturas almacenadas."""

# Frank Asael Méndez García - 31/07/2026

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Reading


class ReadingRepository:
    """Realiza operaciones sobre la tabla readings."""

    def __init__(self, session: Session) -> None:
        """Guarda la sesión de base de datos."""
        self.session = session

    def create(self, reading: Reading) -> Reading:
        """Guarda una lectura."""
        self.session.add(reading)
        self.session.commit()
        self.session.refresh(reading)

        return reading

    def get_by_id(self, reading_id: int) -> Reading | None:
        """Busca una lectura por su identificador."""
        return self.session.get(Reading, reading_id)

    def list_all(
        self,
        offset: int = 0,
        limit: int = 20,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
    ) -> list[Reading]:
        """Devuelve lecturas paginadas y filtradas."""
        statement = select(Reading)

        # Aplica la fecha inicial cuando fue enviada.
        if start_date is not None:
            statement = statement.where(
                Reading.recorded_at >= start_date
            )

        # Aplica la fecha final cuando fue enviada.
        if end_date is not None:
            statement = statement.where(
                Reading.recorded_at <= end_date
            )

        statement = (
            statement
            .order_by(Reading.id)
            .offset(offset)
            .limit(limit)
        )

        readings = self.session.scalars(statement)

        return list(readings)