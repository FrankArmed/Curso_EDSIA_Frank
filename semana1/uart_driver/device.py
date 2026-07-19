"""Dispositivo UART que utiliza configuración y parser por inyección."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: device.py

from semana1.uart_driver.config import UartConfig
from semana1.uart_driver.parsers import MessageParser, ParsedMessage


class UartDevice:
    """Representa un dispositivo UART configurable."""

    def __init__(
        self,
        config: UartConfig,
        parser: MessageParser,
    ) -> None:
        """Recibe la configuración y el parser que utilizará."""
        self._config = config
        self._parser = parser

    @property
    def config(self) -> UartConfig:
        """Devuelve la configuración UART del dispositivo."""
        return self._config

    @property
    def parser(self) -> MessageParser:
        """Devuelve el parser utilizado por el dispositivo."""
        return self._parser

    def receive(self, payload: bytes) -> ParsedMessage:
        """Procesa los bytes recibidos utilizando el parser."""
        return self._parser.parse(payload)