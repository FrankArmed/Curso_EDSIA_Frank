"""Pruebas para la configuración UART."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_config.py

from dataclasses import FrozenInstanceError

import pytest

from semana1.uart_driver.config import UartConfig


def test_config_accepts_valid_values() -> None:
    """Debe aceptar y conservar una configuración UART válida."""
    config = UartConfig(
        port="COM3",
        baudrate=115200,
        timeout=0.5,
    )

    assert config.port == "COM3"
    assert config.baudrate == 115200
    assert config.timeout == pytest.approx(0.5)


def test_config_normalizes_port_name() -> None:
    """Debe eliminar espacios externos del nombre del puerto."""
    config = UartConfig(port="  COM4  ")

    assert config.port == "COM4"


def test_config_rejects_empty_port() -> None:
    """Debe rechazar nombres de puerto vacíos."""
    with pytest.raises(ValueError, match="port"):
        UartConfig(port="   ")


def test_config_rejects_unsupported_baudrate() -> None:
    """Debe rechazar velocidades UART no compatibles."""
    with pytest.raises(ValueError, match="baudrate"):
        UartConfig(
            port="COM3",
            baudrate=12345,
        )


def test_config_rejects_negative_timeout() -> None:
    """Debe rechazar tiempos de espera negativos."""
    with pytest.raises(ValueError, match="timeout"):
        UartConfig(
            port="COM3",
            timeout=-0.5,
        )


def test_config_is_immutable() -> None:
    """No debe permitir cambios después de su creación."""
    config = UartConfig(port="COM3")

    with pytest.raises(FrozenInstanceError):
        setattr(config, "baudrate", 115200)