"""Acceso a las alertas almacenadas."""

# Frank Asael Méndez García - 15/08/2026

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Alert


class AlertRepository:
    """Realiza operaciones sobre alertas."""

    def __init__(self, session: Session) -> None:
        """Guarda la sesión de base de datos."""
        self.session = session

    def create(self, alert: Alert) -> Alert:
        """Guarda una alerta."""
        self.session.add(alert)
        self.session.commit()
        self.session.refresh(alert)
        return alert

    def list_all(
        self,
        offset: int,
        limit: int,
    ) -> list[Alert]:
        """Devuelve las alertas almacenadas."""
        statement = (
            select(Alert)
            .order_by(Alert.id)
            .offset(offset)
            .limit(limit)
        )

        return list(self.session.scalars(statement))