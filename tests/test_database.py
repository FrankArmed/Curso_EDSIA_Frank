"""Pruebas sencillas de persistencia con SQLAlchemy."""

# Frank Asael Méndez García - 01/08/2026

from pathlib import Path

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from app.db import Base
from app.models import Reading, Sensor


def test_save_sensor_in_database(tmp_path: Path) -> None:
    """Debe guardar y recuperar un sensor."""
    database_path = tmp_path / "sensorhub_test.db"
    test_engine = create_engine(f"sqlite:///{database_path}")

    try:
        Base.metadata.create_all(test_engine)

        with Session(test_engine) as session:
            sensor = Sensor(
                id="TH-01",
                sensor_type="temperature",
                unit="C",
            )

            session.add(sensor)
            session.commit()

            saved_sensor = session.scalar(
                select(Sensor).where(Sensor.id == "TH-01")
            )

            assert saved_sensor is not None
            assert saved_sensor.sensor_type == "temperature"
            assert saved_sensor.unit == "C"
    finally:
        test_engine.dispose()


def test_save_reading_in_database(tmp_path: Path) -> None:
    """Debe guardar una lectura."""
    database_path = tmp_path / "sensorhub_test.db"
    test_engine = create_engine(f"sqlite:///{database_path}")

    try:
        Base.metadata.create_all(test_engine)

        with Session(test_engine) as session:
            sensor = Sensor(
                id="HU-01",
                sensor_type="humidity",
                unit="%",
            )
            session.add(sensor)

            reading = Reading(
                sensor_id="HU-01",
                value=65.0,
                unit="%",
            )
            session.add(reading)
            session.commit()

            saved_reading = session.scalar(select(Reading))

            assert saved_reading is not None
            assert saved_reading.sensor_id == "HU-01"
            assert saved_reading.value == 65.0
            assert saved_reading.unit == "%"
    finally:
        test_engine.dispose()