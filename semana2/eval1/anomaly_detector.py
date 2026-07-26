"""Detección sencilla de anomalías ambientales."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: anomaly_detector.py

from semana2.eval1.sensor_reading import SensorReading


class AnomalyDetector:
    """Detecta valores superiores a los límites configurados."""

    def __init__(
        self,
        temperature_limit: float, ##SE USA FLOAT PORQUE LOS LÍMITES PUEDEN SER DECIMALES
        humidity_limit: float,
    ) -> None:
        """Recibe los límites utilizados para detectar anomalías."""
        self.temperature_limit = temperature_limit
        self.humidity_limit = humidity_limit

    def detect(self, reading: SensorReading) -> list[str]:
        """Devuelve las anomalías encontradas en una lectura."""
        anomalies: list[str] = []

        if reading.temperature > self.temperature_limit:
            anomalies.append("TEMPERATURE")

        if reading.humidity > self.humidity_limit:
            anomalies.append("HUMIDITY")

        return anomalies