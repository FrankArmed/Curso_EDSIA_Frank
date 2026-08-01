"""Pruebas de los endpoints de lecturas."""

# Frank Asael Méndez García - 31/07/2026

from fastapi.testclient import TestClient


def create_temperature_sensor(client: TestClient) -> None:
    """Crea un sensor de temperatura."""
    client.post(
        "/sensors",
        json={
            "id": "TH-01",
            "sensor_type": "temperature",
            "unit": "C",
        },
    )


def create_reading(
    client: TestClient,
    value: float,
    recorded_at: str,
) -> None:
    """Crea una lectura para las pruebas."""
    client.post(
        "/readings",
        json={
            "sensor_id": "TH-01",
            "value": value,
            "unit": "C",
            "recorded_at": recorded_at,
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
            "recorded_at": "2026-07-30T10:00:00",
        },
    )

    assert response.status_code == 201
    assert response.json()["sensor_id"] == "TH-01"
    assert response.json()["value"] == 25.5


def test_get_reading(client: TestClient) -> None:
    """Debe consultar una lectura por ID."""
    create_temperature_sensor(client)
    create_reading(client, 25.0, "2026-07-30T10:00:00")

    response = client.get("/readings/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_unknown_reading(client: TestClient) -> None:
    """Debe devolver 404 si la lectura no existe."""
    response = client.get("/readings/999")

    assert response.status_code == 404


def test_reading_pagination(client: TestClient) -> None:
    """Debe aplicar offset y limit."""
    create_temperature_sensor(client)

    create_reading(client, 10.0, "2026-07-30T10:00:00")
    create_reading(client, 20.0, "2026-07-30T11:00:00")
    create_reading(client, 30.0, "2026-07-30T12:00:00")

    response = client.get(
        "/readings",
        params={
            "offset": 1,
            "limit": 1,
        },
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["value"] == 20.0


def test_filter_readings_by_date(client: TestClient) -> None:
    """Debe filtrar lecturas por fecha."""
    create_temperature_sensor(client)

    create_reading(client, 10.0, "2026-07-29T10:00:00")
    create_reading(client, 20.0, "2026-07-30T10:00:00")
    create_reading(client, 30.0, "2026-07-31T10:00:00")

    response = client.get(
        "/readings",
        params={
            "start_date": "2026-07-30T00:00:00",
            "end_date": "2026-07-30T23:59:59",
        },
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["value"] == 20.0


def test_reject_inverted_date_range(
    client: TestClient,
) -> None:
    """Debe rechazar un rango de fechas invertido."""
    response = client.get(
        "/readings",
        params={
            "start_date": "2026-07-31T00:00:00",
            "end_date": "2026-07-30T00:00:00",
        },
    )

    assert response.status_code == 400


def test_reject_unknown_sensor(client: TestClient) -> None:
    """Debe rechazar una lectura sin sensor."""
    response = client.post(
        "/readings",
        json={
            "sensor_id": "UNKNOWN",
            "value": 25.5,
            "unit": "C",
        },
    )

    assert response.status_code == 404


def test_reject_out_of_range_temperature(
    client: TestClient,
) -> None:
    """Debe rechazar una temperatura fuera del rango."""
    create_temperature_sensor(client)

    response = client.post(
        "/readings",
        json={
            "sensor_id": "TH-01",
            "value": 150,
            "unit": "C",
        },
    )

    assert response.status_code == 400


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