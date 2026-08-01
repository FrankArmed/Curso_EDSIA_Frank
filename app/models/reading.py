"""Modelo SQLAlchemy para las lecturas."""

# Frank Asael Méndez García - 30/07/2026

from datetime import datetime, timezone

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Reading(Base):
    """Representa una lectura almacenada en la base de datos."""

    __tablename__ = "readings"

    # SQLAlchemy generará automáticamente este identificador.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Una lectura por sensor existente.
    sensor_id: Mapped[str] = mapped_column(
        ForeignKey("sensors.id"),
        index=True,
    )

    value: Mapped[float]
    unit: Mapped[str] = mapped_column(String(10))

    # Cuando no se envía una fecha, se utiliza la fecha actual.
    recorded_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )