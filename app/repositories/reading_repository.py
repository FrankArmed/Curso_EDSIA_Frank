"""Acceso a las lecturas almacenadas en la base de datos."""

# Frank Asael Méndez García - 31/07/2026

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Reading


class ReadingRepository:
    """Realiza operaciones sencillas sobre la tabla readings."""

    def __init__(self, session: Session) -> None:
        """Guarda la sesión utilizada por el repositorio."""
        self.session = session

    def create(self, reading: Reading) -> Reading:
        """Guarda una lectura en la base de datos."""
        self.session.add(reading)
        self.session.commit()
        self.session.refresh(reading)

        return reading

    def list_all(self) -> list[Reading]:
        """Devuelve todas las lecturas."""
        statement = select(Reading).order_by(Reading.id)
        readings = self.session.scalars(statement)

        return list(readings)