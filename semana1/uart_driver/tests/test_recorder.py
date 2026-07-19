"""Pruebas sencillas para el registrador JSON Lines."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_recorder.py

from pathlib import Path

from semana1.uart_driver.parsers import ParsedMessage
from semana1.uart_driver.recorder import JsonLinesRecorder


def test_recorder_saves_one_message(tmp_path: Path) -> None:
    """Debe guardar y recuperar un mensaje."""
    file_path = tmp_path / "messages.jsonl"
    recorder = JsonLinesRecorder(file_path)

    message = ParsedMessage(
        protocol="MODBUS",
        fields={
            "address": 1,
            "function_code": 3,
        },
    )

    recorder.record(message)
    records = recorder.read_all()

    assert len(records) == 1
    assert records[0]["protocol"] == "MODBUS"
    assert records[0]["fields"]["address"] == 1
    assert "timestamp" in records[0]


def test_recorder_appends_multiple_messages(
    tmp_path: Path,
) -> None:
    """Debe agregar mensajes sin borrar los anteriores."""
    file_path = tmp_path / "messages.jsonl"
    recorder = JsonLinesRecorder(file_path)

    first_message = ParsedMessage(
        protocol="NMEA",
        fields={"talker": "GP"},
    )
    second_message = ParsedMessage(
        protocol="CAN",
        fields={"identifier": 0x123},
    )

    recorder.record(first_message)
    recorder.record(second_message)

    records = recorder.read_all()

    assert len(records) == 2
    assert records[0]["protocol"] == "NMEA"
    assert records[1]["protocol"] == "CAN"


def test_recorder_returns_empty_list_when_file_is_missing(
    tmp_path: Path,
) -> None:
    """Debe devolver una lista vacía cuando el archivo no existe."""
    file_path = tmp_path / "missing.jsonl"
    recorder = JsonLinesRecorder(file_path)

    assert recorder.read_all() == []


def test_recorder_creates_parent_directories(
    tmp_path: Path,
) -> None:
    """Debe crear automáticamente las carpetas necesarias."""
    file_path = tmp_path / "logs" / "uart" / "messages.jsonl"
    recorder = JsonLinesRecorder(file_path)

    message = ParsedMessage(
        protocol="MODBUS",
        fields={"address": 1},
    )

    recorder.record(message)

    assert file_path.exists()
    assert recorder.file_path == file_path