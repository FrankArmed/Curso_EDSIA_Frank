"""Lógica para detectar anomalías y generar alertas."""

# Frank Asael Méndez García - 15/08/2026

from app.models import Alert, Reading, Sensor
from app.repositories.protocols import AlertRepositoryProtocol
from app.services.notification import NotificationStrategy


class AlertService:
    """Evalúa lecturas y genera alertas cuando es necesario."""

    def __init__(
        self,
        alert_repository: AlertRepositoryProtocol,
        notification_strategy: NotificationStrategy,
    ) -> None:
        """Recibe el repositorio y la estrategia de notificación."""
        self.alert_repository = alert_repository
        self.notification_strategy = notification_strategy

    def evaluate(
        self,
        sensor: Sensor,
        reading: Reading,
    ) -> Alert | None:
        """Genera una alerta si la lectura supera el umbral."""
        threshold = sensor.alert_threshold

        # Sin umbral configurado no existe una anomalía que evaluar.
        if threshold is None:
            return None

        if reading.value <= threshold:
            return None

        difference = reading.value - threshold

        level = "WARNING"

        if difference >= 10:
            level = "CRITICAL"

        alert = Alert(
            sensor_id=sensor.id,
            reading_id=reading.id,
            value=reading.value,
            threshold=threshold,
            level=level,
            status="open",
            message=(
                f"Lectura {reading.value} {reading.unit} "
                f"supera el umbral {threshold} {sensor.unit}"
            ),
        )

        saved_alert = self.alert_repository.create(alert)

        self.notification_strategy.notify(saved_alert)

        return saved_alert

    def list_alerts(
        self,
        offset: int,
        limit: int,
    ) -> list[Alert]:
        """Devuelve las alertas almacenadas."""
        return self.alert_repository.list_all(
            offset,
            limit,
        )