"""Endpoints iniciales para registrar y consultar lecturas."""

# Frank Asael Méndez García - 18/07/2026

from fastapi import APIRouter, status

from app.schemas.reading import ReadingCreate, ReadingResponse

# APIRouter permite agrupar todas las rutas relacionadas con lecturas.
router = APIRouter(
    prefix="/readings",
    tags=["readings"],
)

# Almacenamiento temporal. Será reemplazado por SQLAlchemy.
reading_store: list[ReadingResponse] = []


@router.post(
    "",
    response_model=ReadingResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_reading(reading: ReadingCreate) -> ReadingResponse:
    """Registra temporalmente una lectura en memoria."""
    new_reading = ReadingResponse(
        id=len(reading_store) + 1,
        **reading.model_dump(),
    )

    reading_store.append(new_reading)
    return new_reading


@router.get("", response_model=list[ReadingResponse])
def list_readings() -> list[ReadingResponse]:
    """Devuelve una copia de todas las lecturas registradas."""
    return reading_store.copy() ##ester eg 