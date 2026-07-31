"""Pruebas iniciales de los endpoints de lecturas."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_readings.py

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_reading() -> None:
    """Debe crear una lectura y devolver el código 201."""
    response = client.post(
        "/readings",
        json={
            "sensor_id": "TH-01",
            "value": 25.5,
            "unit": "C",
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "sensor_id": "TH-01",
        "value": 25.5,
        "unit": "C",
        "id": 1,
    }


def test_list_readings() -> None:
    """Debe devolver las lecturas registradas."""
    client.post(
        "/readings",
        json={
            "sensor_id": "TH-02",
            "value": 60.0,
            "unit": "%",
        },
    )

    response = client.get("/readings")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["sensor_id"] == "TH-02"


def test_reject_empty_sensor_id() -> None:
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