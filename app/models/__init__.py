"""Modelos de base de datos utilizados por SensorHub."""

# Frank Asael Méndez García - 18/07/2026, actualización 15/08/2026
# Archivo: __init__.py

from app.models.alert import Alert
from app.models.reading import Reading
from app.models.sensor import Sensor

__all__ = ["Alert", "Reading", "Sensor"]