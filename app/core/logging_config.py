"""Configuración mínima de logs estructurados."""
# Frank Asael Méndez García - 18/07/2026

import json
import logging
import os
import sys


class JsonFormatter(logging.Formatter):
    """Convierte cada evento de log a una línea JSON."""

    def format(self, record: logging.LogRecord) -> str:
        data = {
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if hasattr(record, "event"):
            data["event"] = record.event
        return json.dumps(data, ensure_ascii=False)


def configure_logging() -> None:
    """Configura el logger principal desde el entorno."""
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level)
