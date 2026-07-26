"""Pruebas TDD para las estrategias de alerta."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_alert_manager.py

from pathlib import Path

from semana2.eval1.alert_manager import (
    AlertManager,
    AlertStrategy,
    ConsoleAlert,
    FileAlert,
)


class MemoryAlert(AlertStrategy): ##Parte del codigo realizado con ayuda de la IA.
    """Estrategia sencilla utilizada solamente en las pruebas."""

    def __init__(self) -> None:
        self.messages: list[str] = []

    def send(self, message: str) -> None:
        """Almacena el mensaje recibido."""
        self.messages.append(message)


def test_manager_uses_selected_strategy() -> None:
    """Debe enviar el mensaje mediante la estrategia recibida."""
    strategy = MemoryAlert()
    manager = AlertManager(strategy)

    manager.send("Temperatura fuera de rango")

    assert strategy.messages == ["Temperatura fuera de rango"]


def test_console_alert_prints_message(capsys: object) -> None:
    """Debe mostrar el mensaje en la consola."""
    alert = ConsoleAlert()

    alert.send("Humedad fuera de rango")

    output = capsys.readouterr()  # type: ignore[attr-defined]
    assert output.out.strip() == "Humedad fuera de rango"


def test_file_alert_saves_message(tmp_path: Path) -> None:
    """Debe guardar un mensaje en un archivo."""
    file_path = tmp_path / "alerts.txt"
    alert = FileAlert(file_path)

    alert.send("Temperatura fuera de rango")

    assert file_path.read_text(encoding="utf-8") == (
        "Temperatura fuera de rango\n"
    )


def test_file_alert_appends_messages(tmp_path: Path) -> None:
    """Debe agregar mensajes sin borrar los anteriores."""
    file_path = tmp_path / "alerts.txt"
    alert = FileAlert(file_path)

    alert.send("Primera alerta")
    alert.send("Segunda alerta")

    assert file_path.read_text(encoding="utf-8").splitlines() == [
        "Primera alerta",
        "Segunda alerta",
    ]