"""Configuración validada para dispositivos UART."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: config.py

from dataclasses import dataclass
from typing import Final

SUPPORTED_BAUDRATES: Final[frozenset[int]] = frozenset(
    {
        1200,
        2400,
        4800,
        9600,
        19200,
        38400,
        57600,
        115200,
        230400,
        460800,
        921600,
    }
)


@dataclass(frozen=True, slots=True)
class UartConfig:
    """Configuración inmutable para una comunicación UART."""

    port: str
    baudrate: int = 9600
    timeout: float = 1.0

    def __post_init__(self) -> None:
        """Valida y normaliza los parámetros de configuración."""
        normalized_port = self.port.strip()

        if not normalized_port:
            raise ValueError("port no puede estar vacío")

        if self.baudrate not in SUPPORTED_BAUDRATES:
            supported = ", ".join(
                str(value) for value in sorted(SUPPORTED_BAUDRATES)
            )
            raise ValueError(
                f"baudrate no compatible: {self.baudrate}. "
                f"Valores permitidos: {supported}"
            )

        if self.timeout < 0:
            raise ValueError("timeout no puede ser negativo")

        object.__setattr__(self, "port", normalized_port)