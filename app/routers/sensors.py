"""Endpoints relacionados con los sensores."""

# Frank Asael Méndez García - 31/07/2026

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Sensor
from app.repositories.sensor_repository import SensorRepository
from app.schemas.sensor import SensorCreate, SensorResponse
from app.services.sensor_service import (
    InvalidSensorUnitError,
    SensorAlreadyExistsError,
    SensorNotFoundError,
    SensorService,
)

# Agrupa las rutas de sensores.
router = APIRouter(
    prefix="/sensors",
    tags=["sensors"],
)


@router.post(
    "",
    response_model=SensorResponse,
    status_code=201,
)
def create_sensor(
    data: SensorCreate,
    session: Session = Depends(get_db),
) -> Sensor:
    """Crea un sensor nuevo."""
    repository = SensorRepository(session)
    service = SensorService(repository)

    try:
        return service.create_sensor(data)

    except SensorAlreadyExistsError as error:
        # El sensor ya está registrado.
        raise HTTPException(
            status_code=409,
            detail=str(error),
        ) from error

    except InvalidSensorUnitError as error:
        # La unidad no coincide con el tipo.
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@router.get(
    "",
    response_model=list[SensorResponse],
)
def list_sensors(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    session: Session = Depends(get_db),
) -> list[Sensor]:
    """Devuelve sensores paginados."""
    repository = SensorRepository(session)
    service = SensorService(repository)

    return service.list_sensors(offset, limit)


@router.get(
    "/{sensor_id}",
    response_model=SensorResponse,
)
def get_sensor(
    sensor_id: str,
    session: Session = Depends(get_db),
) -> Sensor:
    """Devuelve un sensor por su ID."""
    repository = SensorRepository(session)
    service = SensorService(repository)

    try:
        return service.get_sensor(sensor_id)

    except SensorNotFoundError as error:
        # El sensor solicitado no existe.
        raise HTTPException(
            status_code=404,
            detail=str(error),
        ) from error ##Easter egg 