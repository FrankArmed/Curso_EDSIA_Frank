"""Pruebas de servicios con repositorios fake."""

# Frank Asael Méndez García - 01/08/2026

from datetime import datetime

import pytest

from app.models import Sensor
from app.schemas.reading import ReadingCreate
from app.schemas.sensor import SensorCreate
from app.services.reading_service import (
    InvalidReadingError,
    ReadingService,
)
from app.services.sensor_service import SensorService
from tests.fakes import (
    FakeReadingRepository,
    FakeSensorRepository,
)


def test_sensor_service_without_database() -> None:
    """Debe crear un sensor usando memoria."""
    repository = FakeSensorRepository()
    service = SensorService(repository)

    sensor = service.create_sensor(
        SensorCreate(
            id="TH-01",
            sensor_type="temperature",
            unit="C",
        )
    )

    assert sensor.id == "TH-01"
    assert repository.get_by_id("TH-01") is sensor


def test_reading_service_without_database() -> None:
    """Debe crear una lectura usando memoria."""
    sensor_repository = FakeSensorRepository()
    reading_repository = FakeReadingRepository()

    sensor_repository.create(
        Sensor(
            id="TH-01",
            sensor_type="temperature",
            unit="C",
        )
    )

    service = ReadingService(
        reading_repository,
        sensor_repository,
    )

    reading = service.create_reading(
        "TH-01",
        ReadingCreate(
            value=25.5,
            unit="C",
            recorded_at=datetime(2026, 8, 1, 10, 0),
        ),
    )

    assert reading.id == 1
    assert reading.value == 25.5


def test_reading_service_rejects_invalid_value() -> None:  ##Apartado hecho con ayuda de la IA. Se ha modificado para que cumpla con el protocolo.
    """Debe rechazar una temperatura inválida."""
    sensor_repository = FakeSensorRepository()
    reading_repository = FakeReadingRepository()

    sensor_repository.create(
        Sensor(
            id="TH-01",
            sensor_type="temperature",
            unit="C",
        )
    )

    service = ReadingService(
        reading_repository,
        sensor_repository,
    )

    with pytest.raises(InvalidReadingError):
        service.create_reading(
            "TH-01",
            ReadingCreate(
                value=150,
                unit="C",
            ),
        )


##Apartado extra.
def test_reading_service_rejects_unknown_sensor_type() -> None:
    """Debe rechazar un tipo de sensor no soportado."""
    sensor_repository = FakeSensorRepository()
    reading_repository = FakeReadingRepository()

    sensor_repository.create(
        Sensor(
            id="PR-01",
            sensor_type="pressure",
            unit="C",
        )
    )

    service = ReadingService(
        reading_repository,
        sensor_repository,
    )

    with pytest.raises(InvalidReadingError):
        service.create_reading(
            "PR-01",
            ReadingCreate(
                value=20.0,
                unit="C",
            ),
        )