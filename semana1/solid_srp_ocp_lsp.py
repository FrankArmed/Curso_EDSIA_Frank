"""Ejemplos de SRP, OCP y LSP aplicados al dominio de sensores."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: solid_srp_ocp_lsp.py

from abc import ABC, abstractmethod
from dataclasses import dataclass

ADC_MAX_VALUE = 1023
REFERENCE_VOLTAGE = 5.0


# SRP: PRINCIPIO DE RESPONSABILIDAD ÚNICA


@dataclass(frozen=True)
class SensorReading:
    """Representa una lectura de voltaje producida por un sensor."""

    sensor_id: str
    voltage: float


class BadSensorReport:
    """Ejemplo incorrecto: convierte y formatea en una misma clase."""

    # Para estos ejemplos se utilizaron recursos de Internet y herramientas
    # de inteligencia artificial, debido a que todavía no se comprendían
    # completamente los principios de diseño SOLID.
    #
    # Esta clase viola el principio de responsabilidad única porque mezcla:
    # 1. La conversión de una lectura ADC a voltaje.
    # 2. La generación de un reporte textual.

    def build(self, sensor_id: str, raw_adc: int) -> str:
        """Convierte una lectura ADC y construye un reporte de texto."""
        if not 0 <= raw_adc <= ADC_MAX_VALUE:
            raise ValueError("raw_adc debe estar entre 0 y 1023")

        voltage = raw_adc * REFERENCE_VOLTAGE / ADC_MAX_VALUE
        return f"{sensor_id}: {voltage:.2f} V"


class AdcVoltageConverter:
    """Convierte lecturas ADC en lecturas de voltaje."""

    def convert(self, sensor_id: str, raw_adc: int) -> SensorReading:
        """Convierte un valor ADC válido en voltaje."""
        if not 0 <= raw_adc <= ADC_MAX_VALUE:
            raise ValueError("raw_adc debe estar entre 0 y 1023")

        voltage = raw_adc * REFERENCE_VOLTAGE / ADC_MAX_VALUE

        return SensorReading(
            sensor_id=sensor_id,
            voltage=voltage,
        )


class SensorReportFormatter:
    """Convierte una lectura de sensor en texto legible."""

    def format(self, reading: SensorReading) -> str:
        """Genera el reporte textual de una lectura."""
        return f"{reading.sensor_id}: {reading.voltage:.2f} V"


# OCP: PRINCIPIO ABIERTO/CERRADO


class BadSensorAlarm:
    """Ejemplo incorrecto: contiene condiciones por tipo de sensor."""

    # Esta clase viola OCP porque cada vez que se agrega un nuevo tipo
    # de sensor es necesario modificar el método is_alarm().
    #
    # Por ejemplo, para soportar un sensor de humedad se tendría que
    # agregar otra condición dentro de esta misma clase.

    def is_alarm(self, sensor_type: str, value: float) -> bool:
        """Indica si la lectura activa una alarma."""
        if sensor_type == "temperature":
            return value > 80.0

        if sensor_type == "pressure":
            return value > 120.0

        raise ValueError(
            f"tipo de sensor no compatible: {sensor_type}"
        )


class AlarmRule(ABC):
    """Define el contrato que deben cumplir las reglas de alarma."""

    @abstractmethod
    def is_triggered(self, value: float) -> bool:
        """Indica si una lectura debe activar la alarma."""
        raise NotImplementedError


@dataclass(frozen=True)
class UpperLimitRule(AlarmRule):
    """Activa una alarma cuando se supera un límite superior."""

    limit: float

    def is_triggered(self, value: float) -> bool:
        """Comprueba si el valor supera el límite configurado."""
        return value > self.limit


@dataclass(frozen=True)
class RangeRule(AlarmRule):
    """Activa una alarma cuando el valor sale de un intervalo."""

    minimum: float
    maximum: float

    def __post_init__(self) -> None:
        """Valida que el límite mínimo no supere al máximo."""
        if self.minimum > self.maximum:
            raise ValueError(
                "minimum no puede ser mayor que maximum"
            )

    def is_triggered(self, value: float) -> bool:
        """Comprueba si el valor está fuera del intervalo permitido."""
        return not self.minimum <= value <= self.maximum


class SensorAlarm:
    """Evalúa lecturas utilizando una regla recibida por inyección."""

    # Esta clase cumple OCP porque puede recibir reglas nuevas sin que
    # sea necesario modificar su código interno.

    def __init__(self, rule: AlarmRule) -> None:
        """Inicializa la alarma con la regla que utilizará."""
        self._rule = rule

    def is_alarm(self, value: float) -> bool:
        """Evalúa la lectura utilizando la regla configurada."""
        return self._rule.is_triggered(value)
    


# LSP: PRINCIPIO DE SUSTITUCIÓN DE LISKOV


class BadNormalizedSensor(ABC):
    """Contrato que promete una lectura normalizada entre 0.0 y 1.0."""

    @abstractmethod
    def read_normalized(self) -> float:
        """Devuelve una lectura normalizada."""
        raise NotImplementedError


@dataclass(frozen=True)
class BadValidNormalizedSensor(BadNormalizedSensor):
    """Implementación que sí respeta el intervalo prometido."""

    value: float

    def __post_init__(self) -> None:
        """Valida que el valor esté normalizado."""
        if not 0.0 <= self.value <= 1.0:
            raise ValueError("value debe estar entre 0.0 y 1.0")

    def read_normalized(self) -> float:
        """Devuelve la lectura normalizada."""
        return self.value


@dataclass(frozen=True)
class BadRawAdcSensor(BadNormalizedSensor):
    """Ejemplo incorrecto: devuelve ADC crudo en lugar de normalizado."""

    raw_adc: int

    def __post_init__(self) -> None:
        """Valida que la lectura ADC pertenezca al intervalo permitido."""
        if not 0 <= self.raw_adc <= ADC_MAX_VALUE:
            raise ValueError("raw_adc debe estar entre 0 y 1023")

    def read_normalized(self) -> float:
        """Devuelve incorrectamente el valor ADC sin normalizar."""
        return float(self.raw_adc)


class NormalizedSensor(ABC):
    """Contrato para sensores que siempre entregan valores normalizados."""

    @abstractmethod
    def read_normalized(self) -> float:
        """Devuelve una lectura comprendida entre 0.0 y 1.0."""
        raise NotImplementedError


@dataclass(frozen=True)
class FixedNormalizedSensor(NormalizedSensor):
    """Sensor que contiene directamente una lectura normalizada."""

    value: float

    def __post_init__(self) -> None:
        """Comprueba que la lectura respete el contrato."""
        if not 0.0 <= self.value <= 1.0:
            raise ValueError("value debe estar entre 0.0 y 1.0")

    def read_normalized(self) -> float:
        """Devuelve la lectura normalizada almacenada."""
        return self.value


@dataclass(frozen=True)
class AdcNormalizedSensor(NormalizedSensor):
    """Sensor que convierte una lectura ADC en un valor normalizado."""

    raw_adc: int

    def __post_init__(self) -> None:
        """Valida que la lectura ADC sea correcta."""
        if not 0 <= self.raw_adc <= ADC_MAX_VALUE:
            raise ValueError("raw_adc debe estar entre 0 y 1023")

    def read_normalized(self) -> float:
        """Convierte el valor ADC al intervalo entre 0.0 y 1.0."""
        return self.raw_adc / ADC_MAX_VALUE


def normalized_percentage(sensor: NormalizedSensor) -> float:
    """Convierte la lectura normalizada de cualquier sensor a porcentaje."""
    return sensor.read_normalized() * 100.0