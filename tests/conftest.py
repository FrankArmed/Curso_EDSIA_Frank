"""Configuración compartida para las pruebas."""

# Frank Asael Méndez García - 31/07/2026

from collections.abc import Generator
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db import Base, get_db
from app.main import app


@pytest.fixture
def client(tmp_path: Path) -> Generator[TestClient, None, None]:
    """Crea un cliente con una base temporal."""

    # Crea una base diferente para cada prueba.
    database_path = tmp_path / "sensorhub_test.db"

    test_engine = create_engine(
        f"sqlite:///{database_path}",
        connect_args={"check_same_thread": False},
    )

    # Crea sesiones conectadas a la base temporal.
    TestSession = sessionmaker(
        bind=test_engine,
        autoflush=False,
        expire_on_commit=False,
    )

    # Crea las tablas necesarias.
    Base.metadata.create_all(bind=test_engine)

    def override_get_db() -> Generator[Session, None, None]:
        """Entrega una sesión temporal."""
        with TestSession() as session:
            yield session

    # Sustituye la base real durante las pruebas.
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    # Limpia la configuración al finalizar.
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=test_engine)