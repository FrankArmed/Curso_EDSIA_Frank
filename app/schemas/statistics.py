"""Esquema para estadísticas de lecturas."""
# Frank Asael Méndez García - 18/07/2026

from pydantic import BaseModel


class ReadingStatistics(BaseModel):
    """Resume las lecturas de un sensor en un periodo."""

    sensor_id: str
    count: int
    minimum: float | None
    maximum: float | None
    average: float | None
