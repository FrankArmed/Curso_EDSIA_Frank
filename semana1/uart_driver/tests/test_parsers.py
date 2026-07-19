"""Pruebas sencillas para los parsers Modbus, NMEA y CAN."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_parsers.py

import pytest

from semana1.uart_driver.parsers import (
    CANParser,
    ModbusParser,
    NMEAParser,
)


# PRUEBAS DE MODBUS


def test_modbus_parser_reads_valid_message() -> None:
    """Debe separar dirección, función y datos."""
    parser = ModbusParser()
    message = parser.parse(
        bytes.fromhex("01 03 00 00 00 02")
    )

    assert message.protocol == "MODBUS"
    assert message.fields["address"] == 1
    assert message.fields["function_code"] == 3
    assert message.fields["data"] == [0, 0, 0, 2]


def test_modbus_parser_rejects_short_message() -> None:
    """Debe rechazar mensajes con menos de dos bytes."""
    parser = ModbusParser()

    with pytest.raises(ValueError, match="al menos 2 bytes"):
        parser.parse(b"\x01")


def test_modbus_parser_rejects_invalid_address() -> None:
    """Debe rechazar direcciones mayores que 247."""
    parser = ModbusParser()

    with pytest.raises(ValueError, match="dirección Modbus"):
        parser.parse(bytes([248, 3, 0, 1]))


# PRUEBAS DE NMEA
## En este apartado del codigo me ayudo la IA a hacer las pruebas de NMEA, ya que no sabia como hacerlas. Ademas, me ayudo a hacer las pruebas de CAN, ya que no sabia como hacerlas.

def test_nmea_parser_reads_valid_sentence() -> None:
    """Debe separar el emisor, el tipo y los datos."""
    parser = NMEAParser()
    message = parser.parse(
        b"$GPGLL,4916.45,N,12311.12,W"
    )

    assert message.protocol == "NMEA"
    assert message.fields["talker"] == "GP"
    assert message.fields["sentence_type"] == "GLL"
    assert message.fields["data"] == [
        "4916.45",
        "N",
        "12311.12",
        "W",
    ]


def test_nmea_parser_requires_start_symbol() -> None:
    """Debe exigir que la sentencia comience con el símbolo dólar."""
    parser = NMEAParser()

    with pytest.raises(ValueError, match="comenzar con"):
        parser.parse(b"GPGLL,4916.45,N")


def test_nmea_parser_rejects_non_ascii_message() -> None:
    """Debe rechazar mensajes que no estén escritos en ASCII."""
    parser = NMEAParser()

    with pytest.raises(ValueError, match="ASCII"):
        parser.parse(b"\xff\xfe")


# PRUEBAS DE CAN


def test_can_parser_reads_valid_frame() -> None:
    """Debe separar el identificador y los datos CAN."""
    parser = CANParser()
    message = parser.parse(b"123#11223344")

    assert message.protocol == "CAN"
    assert message.fields["identifier"] == 0x123
    assert message.fields["data"] == [
        0x11,
        0x22,
        0x33,
        0x44,
    ]
    assert message.fields["dlc"] == 4


def test_can_parser_requires_separator() -> None:
    """Debe exigir el separador numeral entre ID y datos."""
    parser = CANParser()

    with pytest.raises(ValueError, match="IDENTIFICADOR#DATOS"):
        parser.parse(b"12311223344")


def test_can_parser_rejects_more_than_eight_bytes() -> None:
    """Debe rechazar más de ocho bytes de datos."""
    parser = CANParser()

    with pytest.raises(ValueError, match="máximo 8 bytes"):
        parser.parse(b"123#010203040506070809")