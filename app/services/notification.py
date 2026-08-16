"""Estrategias utilizadas para notificar alertas."""

# Frank Asael Méndez García - 15/08/2026

from typing import Protocol

from app.models import Alert


class NotificationStrategy(Protocol):
    """Define cómo debe enviarse una notificación."""

    def notify(self, alert: Alert) -> None: ...


class ConsoleNotificationStrategy:
    """Muestra las alertas en la consola."""

    def notify(self, alert: Alert) -> None:
        """Imprime el mensaje de la alerta."""
        print(f"ALERTA: {alert.message}")