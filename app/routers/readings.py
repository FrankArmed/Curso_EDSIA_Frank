"""Endpoints relacionados con las lecturas."""

# Frank Asael Méndez García - 01/08/2026

from datetime import datetime

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    Response,
)
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Reading
from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.repositories.alert_repository import AlertRepository
from app.services.alert_service import AlertService
from app.services.notification import ConsoleNotificationStrategy
from app.schemas.reading import (
    ReadingCreate,
    ReadingResponse,
    ReadingUpdate,
)
from app.services.reading_service import (
    InvalidDateRangeError,
    InvalidReadingError,
    ReadingNotFoundError,
    ReadingService,
    SensorNotFoundError,
)

router = APIRouter(tags=["readings"])


def create_service(session: Session) -> ReadingService:
    """Crea el servicio de lecturas."""
    reading_repository = ReadingRepository(session)
    sensor_repository = SensorRepository(session)

    return ReadingService(
        reading_repository,
        sensor_repository,
    )

def create_alert_service(
    session: Session,
) -> AlertService:
    """Crea el servicio encargado de las alertas."""
    repository = AlertRepository(session)
    notifier = ConsoleNotificationStrategy()

    return AlertService(repository, notifier)

@router.post(
    "/sensors/{sensor_id}/readings",
    response_model=ReadingResponse,
    status_code=201,
)
def create_reading(
    sensor_id: str,
    data: ReadingCreate,
    session: Session = Depends(get_db),
) -> Reading:
    """Crea una lectura."""
    service = create_service(session)

    try:
        reading = service.create_reading(sensor_id, data)

        sensor = service.get_sensor(sensor_id)

        alert_service = create_alert_service(session)
        alert_service.evaluate(sensor, reading)

        return reading
    except SensorNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    except InvalidReadingError as error:
        raise HTTPException(422, str(error)) from error


@router.get(
    "/sensors/{sensor_id}/readings",
    response_model=list[ReadingResponse],
)
def list_readings(
    sensor_id: str,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    from_date: datetime | None = Query(
        default=None,
        alias="from",
    ),
    to_date: datetime | None = Query(
        default=None,
        alias="to",
    ),
    session: Session = Depends(get_db),
) -> list[Reading]:
    """Lista lecturas de un sensor."""
    service = create_service(session)

    try:
        return service.list_for_sensor(
            sensor_id,
            offset,
            limit,
            from_date,
            to_date,
        )
    except SensorNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    except InvalidDateRangeError as error:
        raise HTTPException(400, str(error)) from error


@router.get(  ##Apartado realizado con ayuda de la IA. Se agregó la función get_reading para consultar una lectura por su ID.
    "/readings/{reading_id}",
    response_model=ReadingResponse,
)
def get_reading(
    reading_id: int,
    session: Session = Depends(get_db),
) -> Reading:
    """Consulta una lectura."""
    service = create_service(session)

    try:
        return service.get_reading(reading_id)
    except ReadingNotFoundError as error:
        raise HTTPException(404, str(error)) from error


@router.patch(
    "/readings/{reading_id}",
    response_model=ReadingResponse,
)
def update_reading(
    reading_id: int,
    data: ReadingUpdate,
    session: Session = Depends(get_db),
) -> Reading:
    """Actualiza una lectura."""
    service = create_service(session)

    try:
        return service.update_reading(reading_id, data)
    except ReadingNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    except SensorNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    except InvalidReadingError as error:
        raise HTTPException(422, str(error)) from error


@router.delete(
    "/readings/{reading_id}",
    status_code=204,
    response_class=Response,
)
def delete_reading(
    reading_id: int,
    session: Session = Depends(get_db),
) -> Response:
    """Elimina una lectura."""
    service = create_service(session)

    try:
        service.delete_reading(reading_id)
        return Response(status_code=204)
    except ReadingNotFoundError as error:
        raise HTTPException(404, str(error)) from error ##Easter egg 