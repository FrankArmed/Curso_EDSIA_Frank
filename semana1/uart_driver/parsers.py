"""Parsers sencillos para mensajes Modbus, NMEA y CAN."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: parsers.py

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeAlias

ParsedValue: TypeAlias = int | str | list[int] | list[str]


@dataclass(frozen=True)
class ParsedMessage:
    """Representa un mensaje interpretado."""

    protocol: str
    fields: dict[str, ParsedValue]


class MessageParser(ABC):
    """Clase base para los parsers de mensajes."""

    @abstractmethod
    def parse(self, payload: bytes) -> ParsedMessage:
        """Convierte bytes en un mensaje interpretado."""
        raise NotImplementedError


class ModbusParser(MessageParser):
    """Parser didáctico para mensajes Modbus."""

    def parse(self, payload: bytes) -> ParsedMessage:
        """Separa dirección, función y datos del mensaje."""
        if len(payload) < 2:
            raise ValueError("el mensaje Modbus necesita al menos 2 bytes")

        address = payload[0]
        function_code = payload[1]
        data = list(payload[2:])

        if address > 247:
            raise ValueError("la dirección Modbus debe estar entre 0 y 247")

        return ParsedMessage(
            protocol="MODBUS",
            fields={
                "address": address,
                "function_code": function_code,
                "data": data,
            },
        )


class NMEAParser(MessageParser):
    """Parser didáctico para sentencias NMEA."""

    def parse(self, payload: bytes) -> ParsedMessage:
        """Separa el encabezado y los datos de una sentencia NMEA."""
        try:
            text = payload.decode("ascii").strip()
        except UnicodeDecodeError as error:
            raise ValueError(
                "el mensaje NMEA debe estar escrito en ASCII"
            ) from error

        if not text.startswith("$"):
            raise ValueError("la sentencia NMEA debe comenzar con '$'")

        content = text[1:]
        body = content.split("*", maxsplit=1)[0]
        parts = body.split(",")

        header = parts[0]

        if len(header) < 5:
            raise ValueError("el encabezado NMEA no es válido")

        return ParsedMessage(
            protocol="NMEA",
            fields={
                "talker": header[:2],
                "sentence_type": header[2:],
                "data": parts[1:],
            },
        )

##Para esta parte del codigo me ayudo la IA.
class CANParser(MessageParser):
    """Parser para tramas CAN representadas como texto hexadecimal."""

    def parse(self, payload: bytes) -> ParsedMessage:
        """Interpreta una trama con formato IDENTIFICADOR#DATOS."""
        try:
            text = payload.decode("ascii").strip().upper()
        except UnicodeDecodeError as error:
            raise ValueError(
                "la trama CAN debe estar escrita en ASCII"
            ) from error

        if text.count("#") != 1:
            raise ValueError(
                "la trama CAN debe usar el formato IDENTIFICADOR#DATOS"
            )

        identifier_text, data_text = text.split("#", maxsplit=1)

        try:
            identifier = int(identifier_text, 16)
            data = bytes.fromhex(data_text)
        except ValueError as error:
            raise ValueError(
                "el identificador y los datos CAN deben ser hexadecimales"
            ) from error

        if identifier > 0x1FFFFFFF:
            raise ValueError(
                "el identificador CAN supera el máximo de 29 bits"
            )

        if len(data) > 8:
            raise ValueError(
                "una trama CAN clásica admite como máximo 8 bytes"
            )

        return ParsedMessage(
            protocol="CAN",
            fields={
                "identifier": identifier,
                "data": list(data),
                "dlc": len(data),
            },
        )