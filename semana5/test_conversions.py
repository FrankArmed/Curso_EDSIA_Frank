"""Pruebas para las conversiones de la Semana 5."""

# Frank Asael Méndez García - 14/08/2026

from semana5.conversions import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_celsius_cero() -> None:
    """0 °C debe equivaler a 32 °F."""
    assert celsius_to_fahrenheit(0) == 32.0


def test_celsius_cien() -> None:
    """100 °C debe equivaler a 212 °F."""
    assert celsius_to_fahrenheit(100) == 212.0


def test_celsius_negativo() -> None:
    """-40 °C tiene el mismo valor en Fahrenheit."""
    assert celsius_to_fahrenheit(-40) == -40.0


def test_fahrenheit_cero() -> None:
    """32 °F debe equivaler a 0 °C."""
    assert fahrenheit_to_celsius(32) == 0.0


def test_fahrenheit_cien() -> None:
    """212 °F debe equivaler a 100 °C."""
    assert fahrenheit_to_celsius(212) == 100.0


def test_fahrenheit_negativo() -> None:
    """-40 °F tiene el mismo valor en Celsius."""
    assert fahrenheit_to_celsius(-40) == -40.0