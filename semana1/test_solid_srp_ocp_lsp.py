"""Pruebas de los principios SRP, OCP y LSP."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_solid_srp_ocp_lsp.py

import pytest

from semana1.solid_srp_ocp_lsp import (
    AdcNormalizedSensor,
    AdcVoltageConverter,
    AlarmRule,
    BadRawAdcSensor,
    BadSensorAlarm,
    BadSensorReport,
    FixedNormalizedSensor,
    NormalizedSensor,
    SensorAlarm,
    SensorReportFormatter,
    normalized_percentage,
) 



# PRUEBAS DE SRP



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



# PRUEBAS DE OCP



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



# PRUEBAS DE LSP


def test_bad_lsp_breaks_normalized_sensor_contract() -> None:
    """El ejemplo incorrecto devuelve un valor fuera del intervalo prometido."""
    sensor = BadRawAdcSensor(512)

    reading = sensor.read_normalized()

    assert reading == 512.0
    assert not 0.0 <= reading <= 1.0


def test_good_lsp_allows_sensor_substitution() -> None:
    """Las implementaciones correctas pueden sustituirse sin romper el cálculo."""
    sensors: list[NormalizedSensor] = [
        FixedNormalizedSensor(0.5),
        AdcNormalizedSensor(512),
    ]

    percentages = [normalized_percentage(sensor) for sensor in sensors]

    assert percentages[0] == pytest.approx(50.0)
    assert percentages[1] == pytest.approx(512 / 1023 * 100.0)