"""Pruebas de integración de la API (test api)."""
# Frank Asael Méndez García - 18/07/2026

from fastapi.testclient import TestClient


def create_sensor(
    client: TestClient,
    sensor_id: str = "TH-01",
    sensor_type: str = "temperature",
    unit: str = "C",
    threshold: float | None = 30,
) -> None:
    response = client.post(
        "/sensors",
        json={
            "id": sensor_id,
            "location": "laboratorio",
            "sensor_type": sensor_type,
            "unit": unit,
            "alert_threshold": threshold,
        },
    )
    assert response.status_code == 201


def create_reading(
    client: TestClient,
    value: float,
    recorded_at: str = "2026-08-19T10:00:00Z",
) -> int:
    response = client.post(
        "/sensors/TH-01/readings",
        json={"value": value, "unit": "C", "recorded_at": recorded_at},
    )
    assert response.status_code == 201
    return int(response.json()["id"])


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_sensor(client: TestClient) -> None:
    create_sensor(client)
    response = client.get("/sensors/TH-01")
    assert response.status_code == 200
    assert response.json()["location"] == "laboratorio"
    assert response.json()["is_active"] is True


def test_duplicate_sensor(client: TestClient) -> None:
    create_sensor(client)
    response = client.post(
        "/sensors",
        json={"id": "TH-01", "sensor_type": "temperature", "unit": "C"},
    )
    assert response.status_code == 409


def test_sensor_pagination(client: TestClient) -> None:
    create_sensor(client, "TH-01")
    create_sensor(client, "TH-02")
    create_sensor(client, "TH-03")
    response = client.get("/sensors", params={"offset": 1, "limit": 1})
    assert response.status_code == 200
    assert response.json()[0]["id"] == "TH-02"


def test_update_sensor(client: TestClient) -> None:
    create_sensor(client)
    response = client.patch(
        "/sensors/TH-01",
        json={"location": "sala 2", "alert_threshold": 35},
    )
    assert response.status_code == 200
    assert response.json()["location"] == "sala 2"
    assert response.json()["alert_threshold"] == 35


def test_delete_sensor_is_soft_delete(client: TestClient) -> None:
    create_sensor(client)
    response = client.delete("/sensors/TH-01")
    assert response.status_code == 204

    # El sensor deja de estar disponible para operaciones normales.
    response = client.get("/sensors/TH-01")
    assert response.status_code == 404


def test_inactive_sensor_rejects_new_reading(client: TestClient) -> None:
    create_sensor(client)
    client.delete("/sensors/TH-01")
    response = client.post(
        "/sensors/TH-01/readings",
        json={"value": 20, "unit": "C"},
    )
    assert response.status_code in {404, 409}


def test_reading_and_warning_alert(client: TestClient) -> None:
    create_sensor(client, threshold=30)
    create_reading(client, 31)

    alerts = client.get("/alerts")
    assert alerts.status_code == 200
    assert alerts.json()[0]["level"] == "WARNING"
    assert alerts.json()[0]["status"] == "open"


def test_critical_alert(client: TestClient) -> None:
    create_sensor(client, threshold=30)
    create_reading(client, 40)
    response = client.get("/alerts", params={"status": "open"})
    assert response.status_code == 200
    assert response.json()[0]["level"] == "CRITICAL"


def test_alert_state_changes(client: TestClient) -> None:
    create_sensor(client, threshold=30)
    create_reading(client, 31)
    alert_id = client.get("/alerts").json()[0]["id"]

    response = client.patch(
        f"/alerts/{alert_id}",
        json={"status": "acknowledged"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "acknowledged"

    response = client.patch(
        f"/alerts/{alert_id}",
        json={"status": "resolved"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "resolved"


def test_invalid_alert_status(client: TestClient) -> None:
    create_sensor(client, threshold=30)
    create_reading(client, 31)
    alert_id = client.get("/alerts").json()[0]["id"]
    response = client.patch(
        f"/alerts/{alert_id}",
        json={"status": "bad"},
    )
    assert response.status_code == 422


def test_reading_physical_validation(client: TestClient) -> None:
    create_sensor(client)
    response = client.post(
        "/sensors/TH-01/readings",
        json={"value": 130, "unit": "C"},
    )
    assert response.status_code == 422


def test_reading_unit_validation(client: TestClient) -> None:
    create_sensor(client)
    response = client.post(
        "/sensors/TH-01/readings",
        json={"value": 20, "unit": "%"},
    )
    assert response.status_code == 422


def test_reading_date_filter(client: TestClient) -> None:
    create_sensor(client, threshold=None)
    create_reading(client, 10, "2026-08-18T10:00:00Z")
    create_reading(client, 20, "2026-08-19T10:00:00Z")
    response = client.get(
        "/sensors/TH-01/readings",
        params={"from": "2026-08-19T00:00:00Z"},
    )
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["value"] == 20


def test_reading_statistics(client: TestClient) -> None:
    create_sensor(client, threshold=None)
    create_reading(client, 10)
    create_reading(client, 20)
    create_reading(client, 30)
    response = client.get("/sensors/TH-01/statistics")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 3
    assert data["minimum"] == 10
    assert data["maximum"] == 30
    assert data["average"] == 20


def test_statistics_empty_sensor(client: TestClient) -> None:
    create_sensor(client, threshold=None)
    response = client.get("/sensors/TH-01/statistics")
    data = response.json()
    assert data["count"] == 0
    assert data["minimum"] is None


def test_unknown_sensor(client: TestClient) -> None:
    response = client.get("/sensors/UNKNOWN")
    assert response.status_code == 404


def test_unknown_alert(client: TestClient) -> None:
    response = client.patch("/alerts/999", json={"status": "resolved"})
    assert response.status_code == 404


def test_metrics_endpoint(client: TestClient) -> None:
    client.get("/health")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "requests_total" in response.json()
