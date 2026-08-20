"""Pruebas unitarias del dominio puro."""
# Frank Asael Méndez García - 18/08/2026

import pytest

from app.domain.telemetry import alert_level, validate_reading


def test_validate_temperature() -> None:
    validate_reading("temperature", "C", 25, "C")


def test_validate_humidity() -> None:
    validate_reading("humidity", "%", 50, "%")


def test_reject_wrong_unit() -> None:
    with pytest.raises(ValueError):
        validate_reading("temperature", "C", 25, "%")


def test_reject_temperature_outside_range() -> None:
    with pytest.raises(ValueError):
        validate_reading("temperature", "C", 130, "C")


def test_reject_humidity_outside_range() -> None:
    with pytest.raises(ValueError):
        validate_reading("humidity", "%", 101, "%")


def test_warning_level() -> None:
    assert alert_level(31, 30) == "WARNING"


def test_critical_level() -> None:
    assert alert_level(37, 30) == "CRITICAL"


def test_no_alert_below_threshold() -> None:
    assert alert_level(25, 30) is None


def test_reject_unknown_sensor_type() -> None:
    with pytest.raises(ValueError):
        validate_reading("pressure", "bar", 2, "bar")


def test_nan_is_invalid() -> None:
    with pytest.raises(ValueError):
        validate_reading("temperature", "C", float("nan"), "C")


def test_infinite_value_is_invalid() -> None:
    with pytest.raises(ValueError):
        validate_reading("temperature", "C", float("inf"), "C")


def test_value_at_threshold_has_no_alert() -> None:
    assert alert_level(30, 30) is None


def test_warning_alert() -> None:
    assert alert_level(35, 30) == "WARNING"


def test_critical_alert() -> None:
    assert alert_level(37, 30) == "CRITICAL"