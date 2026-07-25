"""Pruebas TDD para la detección de anomalías."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_anomaly_detector.py

from datetime import datetime

from semana2.eval1.anomaly_detector import AnomalyDetector
from semana2.eval1.sensor_reading import SensorReading


def create_reading(
    temperature: float,
    humidity: float,
) -> SensorReading:
    """Crea una lectura sencilla para las pruebas.""" ##DADO ALGUNAS COMPLEJIDADES SE REALIZO CON AYUDA DE IA. 
    return SensorReading(
        sensor_id="TH-01",
        temperature=temperature,
        humidity=humidity,
        timestamp=datetime(2026, 7, 18, 10, 30),
    )


def test_detect_high_temperature() -> None:
    """Debe detectar una temperatura superior al límite."""
    detector = AnomalyDetector(
        temperature_limit=35.0,
        humidity_limit=80.0,
    )

    anomalies = detector.detect(create_reading(35.1, 60.0))

    assert anomalies == ["TEMPERATURE"]


def test_detect_high_humidity() -> None:
    """Debe detectar una humedad superior al límite.""" 
    detector = AnomalyDetector(
        temperature_limit=35.0,
        humidity_limit=80.0,
    )

    anomalies = detector.detect(create_reading(25.0, 80.1))

    assert anomalies == ["HUMIDITY"]


def test_exact_limits_are_not_anomalies() -> None:
    """Los valores iguales a los límites deben aceptarse."""
    detector = AnomalyDetector(
        temperature_limit=35.0,
        humidity_limit=80.0,
    )

    anomalies = detector.detect(create_reading(35.0, 80.0))

    assert anomalies == []


def test_use_custom_limits() -> None:
    """Debe utilizar los límites entregados al detector."""
    detector = AnomalyDetector(
        temperature_limit=30.0,
        humidity_limit=70.0,
    )

    anomalies = detector.detect(create_reading(31.0, 71.0))

    assert anomalies == ["TEMPERATURE", "HUMIDITY"]