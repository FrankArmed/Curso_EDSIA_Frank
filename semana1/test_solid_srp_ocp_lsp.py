"""Pruebas de los principios SRP, OCP y LSP."""
## Frank Asael Méndez García - 18/07/2026 - test_solid_srp_ocp_lsp.py 
import pytest

from semana1.solid_srp_ocp_lsp import (
    AdcVoltageConverter,
    BadSensorReport,
    SensorReportFormatter,
)


def test_bad_srp_builds_sensor_report() -> None:
    """El ejemplo incorrecto convierte y formatea en una sola clase."""
    report_builder = BadSensorReport()

    report = report_builder.build("S1", 1023)

    assert report == "S1: 5.00 V"


def test_good_srp_separates_conversion_and_formatting() -> None:
    """El ejemplo correcto separa conversión y presentación.""" ##Parte hecha con IA.
    converter = AdcVoltageConverter()
    formatter = SensorReportFormatter()

    reading = converter.convert("S1", 512)
    report = formatter.format(reading)

    assert reading.sensor_id == "S1"
    assert reading.voltage == pytest.approx(512 * 5.0 / 1023)
    assert report == "S1: 2.50 V"