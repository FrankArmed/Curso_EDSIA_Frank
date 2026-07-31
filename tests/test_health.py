"""Pruebas del endpoint de salud."""  ##estaba malito el pobre codigo :c

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_health.py

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    """El endpoint debe confirmar que la API funciona."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}