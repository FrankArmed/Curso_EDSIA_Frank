"""Pruebas de la dependencia de base de datos."""

# Frank Asael Méndez García - 01/08/2026

from pytest import MonkeyPatch

import app.db as db


class FakeSession:
    """Sesión sencilla para comprobar el cierre."""

    def __init__(self) -> None:
        self.closed = False

    def close(self) -> None:
        """Marca la sesión como cerrada."""
        self.closed = True


def test_get_db_closes_session(
    monkeypatch: MonkeyPatch,
) -> None:
    """Debe entregar y cerrar la sesión."""
    fake_session = FakeSession()

    # Sustituye temporalmente SessionLocal.
    monkeypatch.setattr(
        db,
        "SessionLocal",
        lambda: fake_session,
    )

    database = db.get_db()

    session = next(database)
    database.close()

    assert session is fake_session
    assert fake_session.closed is True