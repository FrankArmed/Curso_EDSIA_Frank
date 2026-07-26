"""Prueba de integración del flujo principal del sistema IoT."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_integration_flow.py

from datetime import datetime

from semana2.eval1.alert_manager import AlertManager, AlertStrategy
from semana2.eval1.anomaly_detector import AnomalyDetector
from semana2.eval1.sensor_reading import SensorReading


class MemoryAlert(AlertStrategy):
    """Guarda alertas en memoria para comprobar el flujo."""

    def __init__(self) -> None:
        self.messages: list[str] = []

    def send(self, message: str) -> None:
        """Guarda el mensaje recibido."""
        self.messages.append(message)


def test_high_temperature_generates_alert() -> None:
    """Una temperatura elevada debe producir una alerta."""
    reading = SensorReading(
        sensor_id="TH-01",
        temperature=36.0,
        humidity=60.0,
        timestamp=datetime(2026, 7, 18, 10, 30),
    )
    detector = AnomalyDetector( ##Parte del codigo realizada con ayuda de la IA.
        temperature_limit=35.0,
        humidity_limit=80.0,
    )
    strategy = MemoryAlert()
    manager = AlertManager(strategy)

    anomalies = detector.detect(reading)

    for anomaly in anomalies:
        manager.send(f"ALERTA: {anomaly}")

    assert strategy.messages == ["ALERTA: TEMPERATURE"]