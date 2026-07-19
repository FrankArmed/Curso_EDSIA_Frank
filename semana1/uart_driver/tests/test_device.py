"""Pruebas sencillas para UartDevice."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_device.py

import pytest

from semana1.uart_driver.config import UartConfig
from semana1.uart_driver.device import UartDevice
from semana1.uart_driver.parsers import (
    ModbusParser,
    NMEAParser,
)

##Esta parte del codigo fue reestructurada y corregida con ayuda de la IA, para mejorar la claridad y la funcionalidad de las pruebas unitarias.
def test_device_keeps_config_and_parser() -> None:
    """Debe conservar la configuración y el parser recibidos."""
    config = UartConfig(
        port="COM3",
        baudrate=9600,
    )
    parser = ModbusParser()

    device = UartDevice(config, parser)

    assert device.config is config
    assert device.parser is parser


def test_device_processes_modbus_message() -> None:
    """Debe procesar un mensaje mediante ModbusParser."""
    device = UartDevice(
        config=UartConfig(port="COM3"),
        parser=ModbusParser(),
    )

    message = device.receive(
        bytes.fromhex("01 03 00 00 00 02")
    )

    assert message.protocol == "MODBUS"
    assert message.fields["address"] == 1
    assert message.fields["function_code"] == 3


def test_device_processes_nmea_message() -> None:
    """Debe procesar una sentencia mediante NMEAParser."""
    device = UartDevice(
        config=UartConfig(port="COM4"),
        parser=NMEAParser(),
    )

    message = device.receive(
        b"$GPGLL,4916.45,N,12311.12,W"
    )

    assert message.protocol == "NMEA"
    assert message.fields["talker"] == "GP"
    assert message.fields["sentence_type"] == "GLL"


def test_device_propagates_parser_errors() -> None:
    """Debe comunicar los errores producidos por el parser."""
    device = UartDevice(
        config=UartConfig(port="COM4"),
        parser=NMEAParser(),
    )

    with pytest.raises(ValueError, match="comenzar con"):
        device.receive(b"GPGLL,4916.45,N")