"""Pruebas TDD para las lecturas de sensores."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_sensor_reading.py

from datetime import datetime

import pytest

from semana2.eval1.sensor_reading import SensorReading


def test_create_valid_sensor_reading() -> None:
    """Debe crear una lectura válida y conservar sus datos."""
    timestamp = datetime(2026, 7, 18, 10, 30)

    reading = SensorReading(
        sensor_id="TH-01",
        temperature=25.0,
        humidity=60.0,
        timestamp=timestamp,
    )

    assert reading.sensor_id == "TH-01"
    assert reading.temperature == 25.0
    assert reading.humidity == 60.0
    assert reading.timestamp == timestamp


def test_reject_empty_sensor_id() -> None:
    """Debe rechazar un identificador formado solo por espacios."""
    with pytest.raises(ValueError, match="identificador es obligatorio"):
        SensorReading(
            sensor_id="   ",
            temperature=25.0,
            humidity=60.0,
            timestamp=datetime.now(),
        )


def test_reject_humidity_below_zero() -> None:
    """Debe rechazar humedad inferior a cero."""
    with pytest.raises(ValueError, match="entre 0 y 100"):
        SensorReading(
            sensor_id="TH-01",
            temperature=25.0,
            humidity=-1.0,
            timestamp=datetime.now(),
        )


def test_reject_humidity_above_one_hundred() -> None:
    """Debe rechazar humedad superior a cien."""
    with pytest.raises(ValueError, match="entre 0 y 100"):
        SensorReading(
            sensor_id="TH-01",
            temperature=25.0,
            humidity=101.0,
            timestamp=datetime.now(),
        )