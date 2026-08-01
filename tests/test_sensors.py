"""Pruebas de los endpoints de sensores."""

# Frank Asael Méndez García - 31/07/2026

from fastapi.testclient import TestClient


def create_sensor(
    client: TestClient,
    sensor_id: str,
) -> None:
    """Crea un sensor para las pruebas."""
    client.post(
        "/sensors",
        json={
            "id": sensor_id,
            "sensor_type": "temperature",
            "unit": "C",
        },
    )


def test_create_sensor(client: TestClient) -> None:
    """Debe crear un sensor."""
    response = client.post(
        "/sensors",
        json={
            "id": "TH-01",
            "sensor_type": "temperature",
            "unit": "C",
        },
    )

    assert response.status_code == 201
    assert response.json()["id"] == "TH-01"


def test_get_sensor(client: TestClient) -> None:
    """Debe consultar un sensor por ID."""
    create_sensor(client, "TH-01")

    response = client.get("/sensors/TH-01")

    assert response.status_code == 200
    assert response.json()["id"] == "TH-01"


def test_get_unknown_sensor(client: TestClient) -> None:
    """Debe devolver 404 si el sensor no existe."""
    response = client.get("/sensors/UNKNOWN")

    assert response.status_code == 404


def test_sensor_pagination(client: TestClient) -> None:
    """Debe aplicar offset y limit."""
    create_sensor(client, "TH-01")
    create_sensor(client, "TH-02")
    create_sensor(client, "TH-03")

    response = client.get(
        "/sensors",
        params={
            "offset": 1,
            "limit": 1,
        },
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["id"] == "TH-02"


def test_reject_invalid_limit(client: TestClient) -> None:
    """Debe rechazar un límite menor que uno."""
    response = client.get(
        "/sensors",
        params={"limit": 0},
    )

    assert response.status_code == 422