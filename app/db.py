"""Configuración de la base de datos de SensorHub."""

# Frank Asael Méndez García - 30/07/2026

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# SQLite guardará los datos en sensorhub.db, en la raíz del proyecto.
DATABASE_URL = "sqlite:///./sensorhub.db"

# Esta opción permite que FastAPI use SQLite desde diferentes hilos.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# SessionLocal crea sesiones para leer y guardar datos.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    """Clase base de todos los modelos de SQLAlchemy."""


def get_db() -> Generator[Session, None, None]:
    """Entrega una sesión y la cierra al terminar la petición."""
    with SessionLocal() as session:
        yield session