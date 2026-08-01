"""Pruebas de los endpoints de lecturas."""

# Frank Asael Méndez García - 31/07/2026

from fastapi.testclient import TestClient


def create_temperature_sensor(client: TestClient) -> None:
    """Crea un sensor para las pruebas."""
    client.post(
        "/sensors",
        json={
            "id": "TH-01",
            "sensor_type": "temperature",
            "unit": "C",
        },
    )


def create_humidity_sensor(client: TestClient) -> None:
    """Crea un sensor de humedad."""
    client.post(
        "/sensors",
        json={
            "id": "HU-01",
            "sensor_type": "humidity",
            "unit": "%",
        },
    )


def test_create_reading(client: TestClient) -> None:
    """Debe crear una lectura válida."""
    create_temperature_sensor(client)

    response = client.post(
        "/readings",
        json={
            "sensor_id": "TH-01",
            "value": 25.5,
            "unit": "C",
        },
    )

    assert response.status_code == 201
    assert response.json()["sensor_id"] == "TH-01"
    assert response.json()["value"] == 25.5
    assert response.json()["unit"] == "C"


def test_list_readings(client: TestClient) -> None:
    """Debe devolver las lecturas guardadas."""
    create_humidity_sensor(client)

    client.post(
        "/readings",
        json={
            "sensor_id": "HU-01",
            "value": 60.0,
            "unit": "%",
        },
    )

    response = client.get("/readings")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["sensor_id"] == "HU-01"
    assert response.json()[0]["value"] == 60.0


def test_reject_unknown_sensor(client: TestClient) -> None:
    """Debe devolver 404 si el sensor no existe."""
    response = client.post(
        "/readings",
        json={
            "sensor_id": "UNKNOWN",
            "value": 25.5,
            "unit": "C",
        },
    )

    assert response.status_code == 404


def test_reject_empty_sensor_id(client: TestClient) -> None:
    """Debe rechazar un identificador vacío."""
    response = client.post(
        "/readings",
        json={
            "sensor_id": "",
            "value": 25.5,
            "unit": "C",
        },
    )

    assert response.status_code == 422