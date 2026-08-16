"""Pruebas de integración para las lecturas."""

# Frank Asael Méndez García - 01/08/2026

from fastapi.testclient import TestClient


def create_sensor(
    client: TestClient,
    sensor_id: str = "TH-01",
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


def create_reading(
    client: TestClient,
    sensor_id: str,
    value: float,
    recorded_at: str,
    unit: str = "C",
) -> int:
    """Crea una lectura y devuelve su ID."""
    response = client.post(
        f"/sensors/{sensor_id}/readings",
        json={
            "value": value,
            "unit": unit,
            "recorded_at": recorded_at,
        },
    )

    assert response.status_code == 201

    return int(response.json()["id"])


def test_create_reading(client: TestClient) -> None:
    """Debe crear una lectura para un sensor."""
    create_sensor(client)

    response = client.post(
        "/sensors/TH-01/readings",
        json={
            "value": 25.5,
            "unit": "C",
            "recorded_at": "2026-07-30T10:00:00",
        },
    )

    assert response.status_code == 201
    assert response.json()["sensor_id"] == "TH-01"
    assert response.json()["value"] == 25.5
    assert response.json()["unit"] == "C"


def test_list_readings_with_pagination(
    client: TestClient,
) -> None:
    """Debe paginar las lecturas del sensor."""
    create_sensor(client)

    create_reading(
        client,
        "TH-01",
        10.0,
        "2026-07-30T10:00:00",
    )
    create_reading(
        client,
        "TH-01",
        20.0,
        "2026-07-30T11:00:00",
    )
    create_reading(
        client,
        "TH-01",
        30.0,
        "2026-07-30T12:00:00",
    )

    response = client.get(
        "/sensors/TH-01/readings",
        params={
            "offset": 1,
            "limit": 1,
        },
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["value"] == 20.0


def test_list_only_requested_sensor_readings(   ##Segmento del codigo hecho con ayuda de la IA. 
    client: TestClient,
) -> None:
    """Debe mostrar solo las lecturas del sensor indicado."""
    create_sensor(client, "TH-01")
    create_sensor(
        client,
        "HU-01",
        sensor_type="humidity",
        unit="%",
    )

    create_reading(
        client,
        "TH-01",
        25.0,
        "2026-07-30T10:00:00",
    )
    create_reading(
        client,
        "HU-01",
        60.0,
        "2026-07-30T11:00:00",
        unit="%",
    )

    response = client.get("/sensors/TH-01/readings")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["sensor_id"] == "TH-01"


def test_filter_readings_by_date(
    client: TestClient,
) -> None:
    """Debe filtrar con from y to."""
    create_sensor(client)

    create_reading(
        client,
        "TH-01",
        10.0,
        "2026-07-29T10:00:00",
    )
    create_reading(
        client,
        "TH-01",
        20.0,
        "2026-07-30T10:00:00",
    )
    create_reading(
        client,
        "TH-01",
        30.0,
        "2026-07-31T10:00:00",
    )

    response = client.get(
        "/sensors/TH-01/readings",
        params={
            "from": "2026-07-30T00:00:00",
            "to": "2026-07-30T23:59:59",
        },
    )

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["value"] == 20.0


def test_reject_inverted_date_range(
    client: TestClient,
) -> None:
    """Debe rechazar un rango invertido."""
    create_sensor(client)

    response = client.get(
        "/sensors/TH-01/readings",
        params={
            "from": "2026-07-31T00:00:00",
            "to": "2026-07-30T00:00:00",
        },
    )

    assert response.status_code == 400


def test_get_reading(client: TestClient) -> None:
    """Debe obtener una lectura por su ID."""
    create_sensor(client)

    reading_id = create_reading(
        client,
        "TH-01",
        25.0,
        "2026-07-30T10:00:00",
    )

    response = client.get(f"/readings/{reading_id}")

    assert response.status_code == 200
    assert response.json()["id"] == reading_id


def test_get_unknown_reading(client: TestClient) -> None:
    """Debe devolver 404 si la lectura no existe."""
    response = client.get("/readings/999")

    assert response.status_code == 404


def test_update_reading(client: TestClient) -> None:
    """Debe actualizar parcialmente una lectura."""
    create_sensor(client)

    reading_id = create_reading(
        client,
        "TH-01",
        25.0,
        "2026-07-30T10:00:00",
    )

    response = client.patch(
        f"/readings/{reading_id}",
        json={"value": 30.0},
    )

    assert response.status_code == 200
    assert response.json()["value"] == 30.0
    assert response.json()["unit"] == "C"


def test_delete_reading(client: TestClient) -> None:
    """Debe eliminar una lectura."""
    create_sensor(client)

    reading_id = create_reading(
        client,
        "TH-01",
        25.0,
        "2026-07-30T10:00:00",
    )

    response = client.delete(f"/readings/{reading_id}")

    assert response.status_code == 204
    assert response.content == b""

    get_response = client.get(f"/readings/{reading_id}")
    assert get_response.status_code == 404


def test_reject_reading_for_unknown_sensor(
    client: TestClient,
) -> None:
    """Debe devolver 404 si el sensor no existe."""
    response = client.post(
        "/sensors/UNKNOWN/readings",
        json={
            "value": 25.0,
            "unit": "C",
        },
    )

    assert response.status_code == 404


def test_reject_out_of_range_temperature(
    client: TestClient,
) -> None:
    """Debe rechazar una temperatura fuera del rango."""
    create_sensor(client)

    response = client.post(
        "/sensors/TH-01/readings",
        json={
            "value": 150.0,
            "unit": "C",
        },
    )

    assert response.status_code == 422


def test_reject_out_of_range_humidity(
    client: TestClient,
) -> None:
    """Debe rechazar una humedad fuera del rango."""
    create_sensor(
        client,
        "HU-01",
        sensor_type="humidity",
        unit="%",
    )

    response = client.post(
        "/sensors/HU-01/readings",
        json={
            "value": 150.0,
            "unit": "%",
        },
    )

    assert response.status_code == 422


def test_reject_unknown_unit(client: TestClient) -> None:
    """Debe rechazar una unidad desconocida."""
    create_sensor(client)

    response = client.post(
        "/sensors/TH-01/readings",
        json={
            "value": 25.0,
            "unit": "kelvins",
        },
    )

    assert response.status_code == 422


##Apartado extra.
def test_reject_future_date_on_create(
    client: TestClient,
) -> None:
    """Debe rechazar una lectura con fecha futura."""
    create_sensor(client)

    response = client.post(
        "/sensors/TH-01/readings",
        json={
            "value": 25.0,
            "unit": "C",
            "recorded_at": "2100-01-01T10:00:00",
        },
    )

    assert response.status_code == 422


def test_reject_future_date_on_update(
    client: TestClient,
) -> None:
    """Debe rechazar una fecha futura al actualizar."""
    create_sensor(client)

    reading_id = create_reading(
        client,
        "TH-01",
        25.0,
        "2026-07-30T10:00:00",
    )

    response = client.patch(
        f"/readings/{reading_id}",
        json={
            "recorded_at": "2100-01-01T10:00:00",
        },
    )

    assert response.status_code == 422


def test_reject_negative_offset(
    client: TestClient,
) -> None:
    """Debe rechazar un offset negativo."""
    response = client.get(
        "/sensors/TH-01/readings",
        params={"offset": -1},
    )

    assert response.status_code == 422


def test_reject_zero_limit(
    client: TestClient,
) -> None:
    """Debe rechazar un limit igual a cero."""
    response = client.get(
        "/sensors/TH-01/readings",
        params={"limit": 0},
    )

    assert response.status_code == 422


def test_reject_limit_above_maximum(
    client: TestClient,
) -> None:
    """Debe rechazar un limit mayor a cien."""
    response = client.get(
        "/sensors/TH-01/readings",
        params={"limit": 101},
    )

    assert response.status_code == 422