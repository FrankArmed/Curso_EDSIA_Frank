"""Endpoints relacionados con los sensores."""

# Frank Asael Méndez García - 01/08/2026

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    Response,
)
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Sensor
from app.repositories.sensor_repository import SensorRepository
from app.schemas.sensor import (
    SensorCreate,
    SensorResponse,
    SensorUpdate,
)
from app.services.sensor_service import (
    InvalidSensorUnitError,
    SensorAlreadyExistsError,
    SensorNotFoundError,
    SensorService,
)

# Agrupa todos los endpoints relacionados con sensores.
router = APIRouter(
    prefix="/sensors",
    tags=["sensors"],
)


def get_sensor_service(
    session: Session = Depends(get_db),
) -> SensorService:
    """Crea el servicio que utilizarán los endpoints de sensores."""
    repository = SensorRepository(session)
    return SensorService(repository)


@router.post(
    "",
    response_model=SensorResponse,
    status_code=201,
)
def create_sensor(
    data: SensorCreate,
    service: SensorService = Depends(get_sensor_service),
) -> Sensor:
    """Crea un sensor nuevo."""
    try:
        return service.create_sensor(data)
    except SensorAlreadyExistsError as error:
        raise HTTPException(409, str(error)) from error
    except InvalidSensorUnitError as error:
        raise HTTPException(422, str(error)) from error


@router.get("", response_model=list[SensorResponse])
def list_sensors(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    service: SensorService = Depends(get_sensor_service),
) -> list[Sensor]:
    """Devuelve una lista paginada de sensores."""
    return service.list_sensors(offset, limit)


@router.get(
    "/{sensor_id}",
    response_model=SensorResponse,
)
def get_sensor(
    sensor_id: str,
    service: SensorService = Depends(get_sensor_service),
) -> Sensor:
    """Consulta un sensor mediante su identificador."""
    try:
        return service.get_sensor(sensor_id)
    except SensorNotFoundError as error:
        raise HTTPException(404, str(error)) from error


@router.patch(
    "/{sensor_id}",
    response_model=SensorResponse,
)
def update_sensor(
    sensor_id: str,
    data: SensorUpdate,
    service: SensorService = Depends(get_sensor_service),
) -> Sensor:
    """Actualiza parcialmente los datos de un sensor."""
    try:
        return service.update_sensor(sensor_id, data)
    except SensorNotFoundError as error:
        raise HTTPException(404, str(error)) from error
    except InvalidSensorUnitError as error:
        raise HTTPException(422, str(error)) from error


@router.delete(
    "/{sensor_id}",
    status_code=204,
    response_class=Response,
)
def delete_sensor(
    sensor_id: str,
    service: SensorService = Depends(get_sensor_service),
) -> Response:
    """Elimina un sensor mediante su identificador."""
    try:
        service.delete_sensor(sensor_id)
        return Response(status_code=204)
    except SensorNotFoundError as error:
        raise HTTPException(404, str(error)) from error