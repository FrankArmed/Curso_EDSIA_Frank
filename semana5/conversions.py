"""Conversiones sencillas utilizadas en los ejercicios de la Semana 5."""

# Frank Asael Méndez García - 14/08/2026


def celsius_to_fahrenheit(c: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    fahrenheit = (c * 9 / 5) + 32
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(f: float) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    celsius = (f - 32) * 5 / 9
    return round(celsius, 2)