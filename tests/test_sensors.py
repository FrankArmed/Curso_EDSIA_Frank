"""Pruebas de integración para los sensores."""

# Frank Asael Méndez García - 01/08/2026

from fastapi.testclient import TestClient


def create_sensor(
    client: TestClient,
    sensor_id: str,
    sensor_type: str = "temperature",
    unit: str = "C",
) -> None:
    """Crea un sensor para las pruebas."""
    response = client.post(
        "/sensors",
        json={
            "id": sensor_id,
            "sensor_type": sensor_type,
            "unit": unit,
        },
    )

    assert response.status_code == 201


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
    assert response.json() == {
        "id": "TH-01",
        "sensor_type": "temperature",
        "unit": "C",
        "alert_threshold": None,
    }


def test_list_sensors_with_pagination(
    client: TestClient,
) -> None:
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


def test_get_sensor(client: TestClient) -> None:  ##Segmento del codigo hecho con ayuda de la IA.
    """Debe obtener un sensor por su ID."""
    create_sensor(client, "TH-01")

    response = client.get("/sensors/TH-01")

    assert response.status_code == 200
    assert response.json()["id"] == "TH-01"


def test_get_unknown_sensor(client: TestClient) -> None:
    """Debe devolver 404 si el sensor no existe."""
    response = client.get("/sensors/UNKNOWN")

    assert response.status_code == 404


def test_reject_duplicate_sensor(client: TestClient) -> None:
    """Debe devolver 409 si el sensor está repetido."""
    create_sensor(client, "TH-01")

    response = client.post(
        "/sensors",
        json={
            "id": "TH-01",
            "sensor_type": "temperature",
            "unit": "C",
        },
    )

    assert response.status_code == 409


def test_reject_wrong_sensor_unit(
    client: TestClient,
) -> None:
    """Debe rechazar una unidad incompatible."""
    response = client.post(
        "/sensors",
        json={
            "id": "HU-01",
            "sensor_type": "humidity",
            "unit": "C",
        },
    )

    assert response.status_code == 422


def test_update_sensor(client: TestClient) -> None:
    """Debe actualizar parcialmente un sensor."""
    create_sensor(client, "TH-01")

    response = client.patch(
        "/sensors/TH-01",
        json={
            "sensor_type": "humidity",
            "unit": "%",
        },
    )

    assert response.status_code == 200
    assert response.json()["sensor_type"] == "humidity"
    assert response.json()["unit"] == "%"


def test_delete_sensor(client: TestClient) -> None:
    """Debe eliminar un sensor."""
    create_sensor(client, "TH-01")

    response = client.delete("/sensors/TH-01")

    assert response.status_code == 204
    assert response.content == b""

    get_response = client.get("/sensors/TH-01")
    assert get_response.status_code == 404


def test_reject_invalid_limit(client: TestClient) -> None:
    """Debe rechazar un limit menor que uno."""
    response = client.get(
        "/sensors",
        params={"limit": 0},
    )

    assert response.status_code == 422