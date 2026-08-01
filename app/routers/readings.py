"""Endpoints relacionados con las lecturas."""

# Frank Asael Méndez García - 31/07/2026

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Reading
from app.repositories.reading_repository import ReadingRepository
from app.repositories.sensor_repository import SensorRepository
from app.schemas.reading import ReadingCreate, ReadingResponse
from app.services.reading_service import (
    InvalidReadingError,
    ReadingService,
    SensorNotFoundError,
)

# Agrupa las rutas relacionadas con lecturas.
router = APIRouter(
    prefix="/readings",
    tags=["readings"],
)


@router.post(
    "",
    response_model=ReadingResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_reading(
    data: ReadingCreate,
    session: Session = Depends(get_db),
) -> Reading:
    """Crea una lectura nueva."""

    # Repositorios que acceden a la base de datos.
    reading_repository = ReadingRepository(session)
    sensor_repository = SensorRepository(session)

    # Servicio que valida y guarda la lectura.
    service = ReadingService(
        reading_repository,
        sensor_repository,
    )

    try:
        return service.create_reading(data)

    except SensorNotFoundError as error:
        # Devuelve 404 si el sensor no existe.
        raise HTTPException(
            status_code=404,
            detail=str(error),
        ) from error

    except InvalidReadingError as error:
        # Devuelve 400 si la lectura no es válida.
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error


@router.get("", response_model=list[ReadingResponse])
def list_readings(
    session: Session = Depends(get_db),
) -> list[Reading]:
    """Devuelve todas las lecturas."""

    # Crea los repositorios y el servicio.
    reading_repository = ReadingRepository(session)
    sensor_repository = SensorRepository(session)

    service = ReadingService(
        reading_repository,
        sensor_repository,
    )

    # Consulta las lecturas guardadas.
    return service.list_readings()  # Easter egg