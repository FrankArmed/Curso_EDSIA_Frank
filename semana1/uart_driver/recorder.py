"""Registro de mensajes en formato JSON Lines."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: recorder.py

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from semana1.uart_driver.parsers import ParsedMessage

##Apartado realizado con ayuda de IA.
class JsonLinesRecorder:
    """Guarda mensajes interpretados en un archivo JSON Lines."""

    def __init__(self, file_path: str | Path) -> None:
        """Recibe la ruta del archivo donde se guardarán los mensajes."""
        self._file_path = Path(file_path)

    @property
    def file_path(self) -> Path:
        """Devuelve la ruta del archivo de registros."""
        return self._file_path

    def record(self, message: ParsedMessage) -> None:
        """Agrega un mensaje como una nueva línea JSON."""
        self._file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "protocol": message.protocol,
            "fields": message.fields,
        }

        with self._file_path.open(
            mode="a",
            encoding="utf-8",
        ) as file:
            file.write(
                json.dumps(entry, ensure_ascii=False) + "\n"
            )

    def read_all(self) -> list[dict[str, Any]]:
        """Lee y devuelve todos los registros guardados."""
        if not self._file_path.exists():
            return []

        records: list[dict[str, Any]] = []

        with self._file_path.open(
            mode="r",
            encoding="utf-8",
        ) as file:
            for line in file:
                if line.strip():
                    records.append(json.loads(line))

        return records