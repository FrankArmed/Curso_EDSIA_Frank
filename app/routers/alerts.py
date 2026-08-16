"""Endpoints para consultar alertas."""

# Frank Asael Méndez García - 15/08/2026

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Alert
from app.repositories.alert_repository import AlertRepository
from app.schemas.alert import AlertResponse
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


@router.get(
    "",
    response_model=list[AlertResponse],
)
def list_alerts(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    service: AlertService = Depends(get_alert_service),
) -> list[Alert]:
    """Devuelve las alertas registradas."""
    return service.list_alerts(offset, limit)