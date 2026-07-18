"""Ejemplos de SRP, OCP y LSP aplicados al dominio de sensores."""

from dataclasses import dataclass

ADC_MAX_VALUE = 1023
REFERENCE_VOLTAGE = 5.0


@dataclass(frozen=True)
class SensorReading:
    """Representa una lectura de voltaje producida por un sensor."""

    sensor_id: str
    voltage: float


class BadSensorReport:
    """Ejemplo incorrecto: convierte y formatea en una misma clase."""
    ##NOTA: para estos ejemplos se utilizaron recursos de Internet como recursos de Inteligencia Artificial dado que aun no habia comprendido completamente los principios de diseño SOLID.
    ##NOTA: para este ejemplo se considera que la clase tiene una responsabilidad única, pero en realidad está violando el principio de responsabilidad única (SRP) al mezclar la conversión de ADC a voltaje y la generación de un reporte textual.
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
        return SensorReading(sensor_id=sensor_id, voltage=voltage)


class SensorReportFormatter:
    """Convierte una lectura de sensor en texto legible."""

    def format(self, reading: SensorReading) -> str:
        """Genera el reporte textual de una lectura."""
        return f"{reading.sensor_id}: {reading.voltage:.2f} V"