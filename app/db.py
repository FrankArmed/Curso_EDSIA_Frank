"""Configuración de la base de datos de SensorHub."""

# Frank Asael Méndez García - 01/08/2026

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = "sqlite:///./sensorhub.db"

# Conexión con la base SQLite.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Crea nuevas sesiones.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    """Base utilizada por los modelos."""


def get_db() -> Generator[Session, None, None]:
    """Entrega y cierra una sesión."""
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()