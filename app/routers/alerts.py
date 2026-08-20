"""Endpoints para consultar y actualizar alertas."""

# Frank Asael Méndez García - 20/08/2026

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Alert
from app.repositories.alert_repository import AlertRepository
from app.schemas.alert import AlertResponse, AlertUpdate
from app.services.alert_service import AlertService
from app.services.notification import ConsoleNotificationStrategy


router = APIRouter(
    prefix="/alerts",
    tags=["alerts"],
)


def get_alert_service(
    session: Session = Depends(get_db),
) -> AlertService:
    """Crea el servicio de alertas."""
    repository = AlertRepository(session)
    notifier = ConsoleNotificationStrategy()

    return AlertService(repository, notifier)


@router.get("", response_model=list[AlertResponse])
def list_alerts(
    status: str | None = Query(default=None),
    session: Session = Depends(get_db),
) -> list[Alert]:
    """Devuelve las alertas registradas."""
    repository = AlertRepository(session)

    if status is None:
        return repository.list_all(0, 100)

    alerts = repository.list_all(0, 100)
    return [alert for alert in alerts if alert.status == status]


@router.patch(
    "/{alert_id}",
    response_model=AlertResponse,
)
def update_alert(
    alert_id: int,
    data: AlertUpdate,
    session: Session = Depends(get_db),
) -> Alert:
    """Actualiza el estado de una alerta."""
    alert = session.get(Alert, alert_id)

    if alert is None:
        raise HTTPException(
            status_code=404,
            detail="Alerta no encontrada",
        )

    alert.status = data.status
    session.commit()
    session.refresh(alert)

    return alert