"""Pruebas de los principios ISP y DIP."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_solid_isp_dip.py

import pytest

from semana1.solid_isp_dip import (
    BadPassiveTemperatureSensor,
    BadTemperatureMonitor,
    MemoryAlertSender,
    ReadableSensor,
    SmartTemperatureSensor,
    TemperatureMonitor,
    TemperatureProbe,
)


# PRUEBAS DE ISP


def test_bad_isp_forces_unsupported_operations() -> None:
    """La interfaz grande obliga a implementar métodos incompatibles."""
    sensor = BadPassiveTemperatureSensor(24.5)

    assert sensor.read() == pytest.approx(24.5)

    with pytest.raises(NotImplementedError, match="calibración"):
        sensor.calibrate(1.0)

    with pytest.raises(NotImplementedError, match="transmitir"):
        sensor.transmit()


def test_good_isp_uses_only_required_interfaces() -> None:
    """Cada sensor implementa únicamente las capacidades necesarias."""
    probe: ReadableSensor = TemperatureProbe(24.5)
    smart_sensor = SmartTemperatureSensor(25.0)

    smart_sensor.calibrate(-0.5)

    assert probe.read() == pytest.approx(24.5)
    assert smart_sensor.read() == pytest.approx(24.5)
    assert smart_sensor.transmit() == "24.50 C"


# PRUEBAS DE DIP, Apartado realizado con ayuda de IA, ya que no se encontraba en el archivo original.


def test_bad_dip_depends_on_concrete_alert_service() -> None:
    """El ejemplo incorrecto crea directamente un servicio concreto."""
    monitor = BadTemperatureMonitor(threshold=80.0)

    assert not monitor.evaluate(70.0)
    assert monitor.evaluate(81.0)
    assert monitor.sender.messages == [
        "ALERTA: temperatura 81.00 C"
    ]


def test_good_dip_accepts_injected_alert_service() -> None:
    """El monitor correcto recibe su dependencia externamente."""
    sender = MemoryAlertSender()
    monitor = TemperatureMonitor(
        threshold=80.0,
        sender=sender,
    )

    assert not monitor.evaluate(70.0)
    assert sender.messages == []

    assert monitor.evaluate(85.0)
    assert sender.messages == [
        "ALERTA: temperatura 85.00 C"
    ]