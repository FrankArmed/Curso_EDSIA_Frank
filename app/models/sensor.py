"""Modelo SQLAlchemy para los sensores."""

# Frank Asael Méndez García - 28/07/2026, actualización 20/08/2026

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Sensor(Base):
    """Representa un sensor almacenado en la base de datos."""

    __tablename__ = "sensors"

    id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True,
    )

    sensor_type: Mapped[str] = mapped_column(String(20))
    unit: Mapped[str] = mapped_column(String(10))
    location: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="sin especificar",
    )

    # Indica si el sensor sigue activo.
    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )

    # Si es None, el sensor no genera alertas por umbral.
    alert_threshold: Mapped[float | None] = mapped_column(
        nullable=True,
        default=None,
    )