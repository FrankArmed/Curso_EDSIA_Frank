"""Reglas puras del dominio de telemetría."""

# Frank Asael Méndez García - 18/08/2026

import math


TEMPERATURE_RANGE = (-40.0, 125.0)
HUMIDITY_RANGE = (0.0, 100.0)


def validate_reading(
    sensor_type: str,
    sensor_unit: str,
    value: float,
    unit: str,
) -> None:
    """Valida unidad y rango físico de una lectura."""

    if not math.isfinite(value):
        raise ValueError("El valor debe ser finito")

    if unit != sensor_unit:
        raise ValueError(f"La unidad debe ser {sensor_unit}")

    if sensor_type == "temperature":
        minimum, maximum = TEMPERATURE_RANGE
    elif sensor_type == "humidity":
        minimum, maximum = HUMIDITY_RANGE
    else:
        raise ValueError("Tipo de sensor no soportado")

    if value < minimum or value > maximum:
        raise ValueError(
            f"El valor debe estar entre {minimum:g} y {maximum:g}"
        )


def alert_level(value: float, threshold: float) -> str | None:
    """Clasifica una lectura según el umbral configurado."""

    if value <= threshold:
        return None

    if value > threshold * 1.20:
        return "CRITICAL"

    return "WARNING"