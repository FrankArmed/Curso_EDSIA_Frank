"""Pruebas de los principios SRP, OCP y LSP."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_solid_srp_ocp_lsp.py

import pytest

from semana1.solid_srp_ocp_lsp import (
    AdcVoltageConverter,
    AlarmRule,
    BadSensorAlarm,
    BadSensorReport,
    SensorAlarm,
    SensorReportFormatter,
)


# ============================================================
# PRUEBAS DE SRP
# ============================================================


def test_bad_srp_builds_sensor_report() -> None:
    """El ejemplo incorrecto convierte y formatea en una sola clase."""
    report_builder = BadSensorReport()

    report = report_builder.build("S1", 1023)

    assert report == "S1: 5.00 V"


def test_good_srp_separates_conversion_and_formatting() -> None:
    """El ejemplo correcto separa conversión y presentación."""
    converter = AdcVoltageConverter()
    formatter = SensorReportFormatter()

    reading = converter.convert("S1", 512)
    report = formatter.format(reading)

    assert reading.sensor_id == "S1"
    assert reading.voltage == pytest.approx(512 * 5.0 / 1023)
    assert report == "S1: 2.50 V"


# ============================================================
# PRUEBAS DE OCP
# ============================================================


def test_bad_ocp_rejects_unknown_sensor_types() -> None:
    """El ejemplo incorrecto solo acepta tipos definidos internamente."""
    alarm = BadSensorAlarm()

    assert alarm.is_alarm("temperature", 81.0)
    assert not alarm.is_alarm("pressure", 100.0)

    with pytest.raises(ValueError, match="humidity"):
        alarm.is_alarm("humidity", 80.0)


class HumidityAlarmRule(AlarmRule):
    """Regla nueva agregada sin modificar la clase SensorAlarm."""

    def is_triggered(self, value: float) -> bool:
        """Activa la alarma fuera del intervalo permitido."""
        return not 30.0 <= value <= 70.0


def test_good_ocp_accepts_new_rules_without_modification() -> None:
    """SensorAlarm debe aceptar reglas nuevas mediante inyección."""
    alarm = SensorAlarm(HumidityAlarmRule())

    assert not alarm.is_alarm(50.0)
    assert alarm.is_alarm(20.0)
    assert alarm.is_alarm(80.0)