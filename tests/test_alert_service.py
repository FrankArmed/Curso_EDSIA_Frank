"""Pruebas para la detección de anomalías y alertas."""

# Frank Asael Méndez García - 15/08/2026

from app.models import Reading, Sensor
from app.services.alert_service import AlertService


class FakeAlertRepository:
    """Guarda alertas en memoria para las pruebas."""

    def __init__(self) -> None:
        self.alerts: list[object] = []

    def create(self, alert: object) -> object:
        """Guarda una alerta sin utilizar base de datos."""
        self.alerts.append(alert)
        return alert


class FakeNotificationStrategy:
    """Registra si una alerta fue notificada."""

    def __init__(self) -> None:
        self.was_notified = False

    def notify(self, alert: object) -> None:
        """Marca que recibió una alerta."""
        self.was_notified = True


def create_sensor(
    threshold: float | None = 30.0,
) -> Sensor:
    """Crea un sensor sencillo para las pruebas."""
    return Sensor(
        id="TH-01",
        sensor_type="temperature",
        unit="C",
        alert_threshold=threshold,
    )


def create_reading(value: float) -> Reading:
    """Crea una lectura sencilla."""
    reading = Reading(
        sensor_id="TH-01",
        value=value,
        unit="C",
    )
    reading.id = 1
    return reading


def test_no_alert_without_threshold() -> None:
    """Sin umbral no debe generarse una alerta."""
    repository = FakeAlertRepository()
    notifier = FakeNotificationStrategy()
    service = AlertService(repository, notifier)

    result = service.evaluate(
        create_sensor(None),
        create_reading(40.0),
    )

    assert result is None
    assert repository.alerts == []


def test_no_alert_below_threshold() -> None:
    """Una lectura debajo del umbral es normal."""
    repository = FakeAlertRepository()
    notifier = FakeNotificationStrategy()
    service = AlertService(repository, notifier)

    result = service.evaluate(
        create_sensor(30.0),
        create_reading(25.0),
    )

    assert result is None
    assert repository.alerts == []


def test_no_alert_equal_to_threshold() -> None:
    """Igualar el umbral todavía se considera normal."""
    repository = FakeAlertRepository()
    notifier = FakeNotificationStrategy()
    service = AlertService(repository, notifier)

    result = service.evaluate(
        create_sensor(30.0),
        create_reading(30.0),
    )

    assert result is None


def test_alert_above_threshold() -> None:
    """Superar el umbral debe crear una alerta."""
    repository = FakeAlertRepository()
    notifier = FakeNotificationStrategy()
    service = AlertService(repository, notifier)

    result = service.evaluate(
        create_sensor(30.0),
        create_reading(35.0),
    )

    assert result is not None
    assert len(repository.alerts) == 1


def test_alert_notifies_strategy() -> None:
    """Una anomalía debe utilizar la estrategia configurada."""
    repository = FakeAlertRepository()
    notifier = FakeNotificationStrategy()
    service = AlertService(repository, notifier)

    service.evaluate(
        create_sensor(30.0),
        create_reading(35.0),
    )

    assert notifier.was_notified is True