"""Ejemplos de ISP y DIP aplicados al dominio de sensores."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: solid_isp_dip.py

from abc import ABC, abstractmethod
from dataclasses import dataclass, field



# ISP: PRINCIPIO DE SEGREGACIÓN DE INTERFACES



class BadSensorDevice(ABC):
    """Interfaz incorrecta que obliga a implementar demasiadas operaciones."""

    @abstractmethod
    def read(self) -> float:
        """Obtiene una lectura del sensor."""
        raise NotImplementedError

    @abstractmethod
    def calibrate(self, offset: float) -> None:
        """Calibra el sensor utilizando un desplazamiento."""
        raise NotImplementedError

    @abstractmethod
    def transmit(self) -> str:
        """Transmite la lectura del sensor."""
        raise NotImplementedError


@dataclass(frozen=True)
class BadPassiveTemperatureSensor(BadSensorDevice):
    """Sensor pasivo obligado a implementar operaciones incompatibles."""

    value: float

    def read(self) -> float:
        """Devuelve la lectura disponible."""
        return self.value

    def calibrate(self, offset: float) -> None:
        """Rechaza la calibración porque el sensor no la permite."""
        raise NotImplementedError(
            "el sensor pasivo no admite calibración"
        )

    def transmit(self) -> str:
        """Rechaza la transmisión porque no posee comunicación."""
        raise NotImplementedError(
            "el sensor pasivo no puede transmitir"
        )


class ReadableSensor(ABC):
    """Interfaz para sensores que pueden proporcionar lecturas."""

    @abstractmethod
    def read(self) -> float:
        """Obtiene una lectura del sensor."""
        raise NotImplementedError


class CalibratableSensor(ABC):
    """Interfaz para sensores que permiten calibración."""

    @abstractmethod
    def calibrate(self, offset: float) -> None:
        """Configura el desplazamiento de calibración."""
        raise NotImplementedError


class TransmittableSensor(ABC):
    """Interfaz para sensores que pueden transmitir información."""

    @abstractmethod
    def transmit(self) -> str:
        """Genera un mensaje con la lectura del sensor."""
        raise NotImplementedError


@dataclass(frozen=True)
class TemperatureProbe(ReadableSensor):
    """Sensor sencillo que solamente permite obtener una lectura."""

    value: float

    def read(self) -> float:
        """Devuelve la temperatura medida."""
        return self.value


@dataclass
class SmartTemperatureSensor(
    ReadableSensor,
    CalibratableSensor,
    TransmittableSensor,
):
    """Sensor inteligente que implementa las tres interfaces."""

    value: float
    offset: float = 0.0

    def read(self) -> float:
        """Devuelve la lectura considerando la calibración."""
        return self.value + self.offset

    def calibrate(self, offset: float) -> None:
        """Actualiza el desplazamiento de calibración."""
        self.offset = offset

    def transmit(self) -> str:
        """Genera un mensaje con la temperatura actual."""
        return f"{self.read():.2f} C"



# DIP: PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS



@dataclass
class BadEmailAlertSender:
    """Servicio concreto utilizado directamente por el ejemplo incorrecto."""

    messages: list[str] = field(default_factory=list)

    def send(self, message: str) -> None:
        """Registra el mensaje que sería enviado por correo."""
        self.messages.append(message)


class BadTemperatureMonitor:
    """Ejemplo incorrecto acoplado a un servicio concreto."""

    def __init__(self, threshold: float) -> None:
        """Crea internamente el servicio concreto de alertas."""
        self._threshold = threshold
        self._sender = BadEmailAlertSender()

    @property
    def sender(self) -> BadEmailAlertSender:
        """Devuelve el servicio concreto usado por el monitor."""
        return self._sender

    def evaluate(self, temperature: float) -> bool:
        """Envía una alerta cuando se supera el límite."""
        if temperature <= self._threshold:
            return False

        message = f"ALERTA: temperatura {temperature:.2f} C"
        self._sender.send(message)
        return True


class AlertSender(ABC):
    """Abstracción para cualquier sistema de envío de alertas."""

    @abstractmethod
    def send(self, message: str) -> None:
        """Envía o registra un mensaje de alerta."""
        raise NotImplementedError


@dataclass
class MemoryAlertSender(AlertSender):
    """Implementación que almacena las alertas en memoria.""" ##Para esta parte, se realizo con ayuda de IA.

    messages: list[str] = field(default_factory=list)

    def send(self, message: str) -> None:
        """Almacena el mensaje recibido."""
        self.messages.append(message)


class TemperatureMonitor:
    """Monitor que depende de la abstracción AlertSender."""

    def __init__(
        self,
        threshold: float,
        sender: AlertSender,
    ) -> None:
        """Recibe el sistema de alertas mediante inyección."""
        self._threshold = threshold
        self._sender = sender

    def evaluate(self, temperature: float) -> bool:
        """Evalúa la temperatura y utiliza el servicio inyectado."""
        if temperature <= self._threshold:
            return False

        message = f"ALERTA: temperatura {temperature:.2f} C"
        self._sender.send(message)
        return True