"""Configuración compartida para las pruebas de la API."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: conftest.py

from collections.abc import Generator

import pytest

from app.routers.readings import reading_store ##importa el almacenamiento de lecturas


@pytest.fixture(autouse=True)
def clear_reading_store() -> Generator[None, None, None]:
    """Limpia las lecturas antes y después de cada prueba."""
    reading_store.clear()

    yield

    reading_store.clear()