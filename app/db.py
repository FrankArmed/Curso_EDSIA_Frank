"""Configuración de la base de datos de SensorHub."""

# Frank Asael Méndez García - 07/08/2026

import os
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


def get_database_url() -> str:
    """Obtiene la conexión desde el entorno o usa SQLite local."""
    url = os.getenv(
        "DATABASE_URL",
        "sqlite:///./sensorhub.db",
    )

    # Algunos proveedores usan postgres://.
    if url.startswith("postgres://"):
        return url.replace(
            "postgres://",
            "postgresql+psycopg://",
            1,
        )

    # Agrega el driver psycopg cuando sea necesario.
    if url.startswith("postgresql://") and "+psycopg" not in url:
        return url.replace(
            "postgresql://",
            "postgresql+psycopg://",
            1,
        )

    return url


DATABASE_URL = get_database_url()

# SQLite necesita esta opción; PostgreSQL no.
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
else:
    engine = create_engine(DATABASE_URL)

# Crea nuevas sesiones para trabajar con la base de datos.
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    """Base utilizada por los modelos."""


def get_db() -> Generator[Session, None, None]:
    """Entrega una sesión y la cierra al terminar."""
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()