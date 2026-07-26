"""Estrategias sencillas para enviar alertas."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: alert_manager.py

from abc import ABC, abstractmethod
from pathlib import Path


class AlertStrategy(ABC):
    """Contrato común para todas las estrategias de alerta."""

    @abstractmethod
    def send(self, message: str) -> None:
        """Envía un mensaje de alerta."""
        raise NotImplementedError


class ConsoleAlert(AlertStrategy):
    """Muestra las alertas en la consola."""

    def send(self, message: str) -> None:
        """Imprime el mensaje recibido."""
        print(message)


class FileAlert(AlertStrategy):
    """Guarda las alertas en un archivo de texto."""

    def __init__(self, file_path: str | Path) -> None: ##Parte del codigo hecho con ayuda de la IA.
        self.file_path = Path(file_path)

    def send(self, message: str) -> None:
        """Agrega el mensaje como una línea nueva."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("a", encoding="utf-8") as file:
            file.write(message + "\n")


class AlertManager:
    """Envía alertas utilizando una estrategia seleccionada."""

    def __init__(self, strategy: AlertStrategy) -> None:
        self.strategy = strategy

    def send(self, message: str) -> None:
        """Entrega el mensaje a la estrategia."""
        self.strategy.send(message)