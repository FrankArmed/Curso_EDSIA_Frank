"""Pruebas de integración para las alertas."""

# Frank Asael Méndez García - 15/08/2026

from fastapi.testclient import TestClient


def create_sensor_with_threshold(
    client: TestClient,
    threshold: float = 30.0,
) -> None:
    """Crea un sensor con umbral de alerta."""
    response = client.post(
        "/sensors",
        json={
            "id": "TH-ALERT-01",
            "sensor_type": "temperature",
            "unit": "C",
            "alert_threshold": threshold,
        },
    )

    assert response.status_code == 201


def test_sensor_accepts_alert_threshold(
    client: TestClient,
) -> None:
    """El sensor debe guardar su umbral."""
    response = client.post(
        "/sensors",
        json={
            "id": "TH-01",
            "sensor_type": "temperature",
            "unit": "C",
            "alert_threshold": 30.0,
        },
    )

    assert response.status_code == 201
    assert response.json()["alert_threshold"] == 30.0


def test_normal_reading_does_not_create_alert(
    client: TestClient,
) -> None:
    """Una lectura normal no debe crear alertas."""
    create_sensor_with_threshold(client)

    response = client.post(
        "/sensors/TH-ALERT-01/readings",
        json={
            "value": 25.0,
            "unit": "C",
        },
    )

    assert response.status_code == 201

    alerts = client.get("/alerts")

    assert alerts.status_code == 200
    assert alerts.json() == []


def test_reading_above_threshold_creates_alert(
    client: TestClient,
) -> None:
    """Superar el umbral debe registrar una alerta."""
    create_sensor_with_threshold(client)

    reading = client.post(
        "/sensors/TH-ALERT-01/readings",
        json={
            "value": 35.0,
            "unit": "C",
        },
    )

    assert reading.status_code == 201

    alerts = client.get("/alerts")

    assert alerts.status_code == 200
    assert len(alerts.json()) == 1
    assert alerts.json()[0]["sensor_id"] == "TH-ALERT-01"
    assert alerts.json()[0]["value"] == 35.0
    assert alerts.json()[0]["threshold"] == 30.0


def test_multiple_anomalies_create_multiple_alerts(
    client: TestClient,
) -> None:
    """Cada lectura anómala debe generar su alerta."""
    create_sensor_with_threshold(client)

    client.post(
        "/sensors/TH-ALERT-01/readings",
        json={"value": 35.0, "unit": "C"},
    )
    client.post(
        "/sensors/TH-ALERT-01/readings",
        json={"value": 40.0, "unit": "C"},
    )

    alerts = client.get("/alerts")

    assert alerts.status_code == 200
    assert len(alerts.json()) == 2