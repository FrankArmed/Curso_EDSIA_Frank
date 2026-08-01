"""Endpoints relacionados con las lecturas."""

# Frank Asael Méndez García - 31/07/2026

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Reading
from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.schemas.reading import ReadingCreate, ReadingResponse
from app.services.reading_service import (
    InvalidDateRangeError,
    InvalidReadingError,
    ReadingNotFoundError,
    ReadingService,
    SensorNotFoundError,
)

# Agrupa las rutas de lecturas.
router = APIRouter(
    prefix="/readings",
    tags=["readings"],
)


def create_service(session: Session) -> ReadingService:
    """Crea el servicio de lecturas."""
    reading_repository = ReadingRepository(session)
    sensor_repository = SensorRepository(session)

    return ReadingService(
        reading_repository,
        sensor_repository,
    )


@router.post(
    "",
    response_model=ReadingResponse,
    status_code=201,
)
def create_reading(
    data: ReadingCreate,
    session: Session = Depends(get_db),
) -> Reading:
    """Crea una lectura nueva."""
    service = create_service(session)

    try:
        return service.create_reading(data)

    except SensorNotFoundError as error:
        # El sensor indicado no existe.
        raise HTTPException(
            status_code=404,
            detail=str(error),
        ) from error

    except InvalidReadingError as error:
        # La unidad o el valor no son válidos.
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@router.get(
    "",
    response_model=list[ReadingResponse],
)
def list_readings(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    session: Session = Depends(get_db),
) -> list[Reading]:
    """Devuelve lecturas paginadas y filtradas."""
    service = create_service(session)

    try:
        return service.list_readings(
            offset,
            limit,
            start_date,
            end_date,
        )

    except InvalidDateRangeError as error:
        # La fecha inicial es posterior a la final.
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@router.get(
    "/{reading_id}",
    response_model=ReadingResponse,
)
def get_reading(
    reading_id: int,
    session: Session = Depends(get_db),
) -> Reading:
    """Devuelve una lectura por su ID."""
    service = create_service(session)

    try:
        return service.get_reading(reading_id)

    except ReadingNotFoundError as error:
        # La lectura solicitada no existe.
        raise HTTPException(
            status_code=404,
            detail=str(error),
        ) from error ##Easter egg 