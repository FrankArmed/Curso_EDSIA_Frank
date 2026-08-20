"""Modelo SQLAlchemy para las alertas."""

# Frank Asael Méndez García - 15/08/2026

from datetime import datetime, timezone

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Alert(Base):
    """Representa una alerta generada por una lectura."""

    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(primary_key=True)

    sensor_id: Mapped[str] = mapped_column(
        ForeignKey("sensors.id"),
        index=True,
    )

    reading_id: Mapped[int] = mapped_column(
        ForeignKey("readings.id"),
        index=True,
    )

    value: Mapped[float]
    threshold: Mapped[float]
    message: Mapped[str] = mapped_column(String(200))

    level: Mapped[str] = mapped_column(String(20))
    status: Mapped[str] = mapped_column(
        String(20),
        default="open",
    )

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )