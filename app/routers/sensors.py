"""Endpoints relacionados con los sensores."""

# Frank Asael Méndez García - 31/07/2026

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Sensor
from app.repositories.sensor_repository import SensorRepository
from app.schemas.sensor import SensorCreate, SensorResponse
from app.services.sensor_service import (
    InvalidSensorUnitError,
    SensorAlreadyExistsError,
    SensorService,
)

# Agrupa los endpoints de sensores.
router = APIRouter(
    prefix="/sensors",
    tags=["sensors"],
)


@router.post(
    "",
    response_model=SensorResponse,
    status_code=status.HTTP_201_CREATED,
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
        # Devuelve 409 cuando el sensor ya existe.
        raise HTTPException(
            status_code=409,
            detail=str(error),
        ) from error

    except InvalidSensorUnitError as error:
        # Devuelve 400 cuando la unidad es incorrecta.
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@router.get("", response_model=list[SensorResponse])
def list_sensors(
    session: Session = Depends(get_db),
) -> list[Sensor]:
    """Devuelve todos los sensores."""
    repository = SensorRepository(session)
    service = SensorService(repository)

    return service.list_sensors()