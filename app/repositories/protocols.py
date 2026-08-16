"""Contratos utilizados por los servicios."""

# Frank Asael Méndez García - 01/08/2026

from datetime import datetime
from typing import Protocol

from app.models import Alert, Reading, Sensor


class SensorRepositoryProtocol(Protocol):
    """Operaciones necesarias para sensores."""

    def create(self, sensor: Sensor) -> Sensor: ...

    def get_by_id(self, sensor_id: str) -> Sensor | None: ...

    def list_all(self, offset: int, limit: int) -> list[Sensor]: ...

    def save(self, sensor: Sensor) -> Sensor: ...

    def delete(self, sensor: Sensor) -> None: ...


class ReadingRepositoryProtocol(Protocol): ##No guarda datos ni ejecuta consultas. Solo define los métodos disponibles. 
    """Operaciones necesarias para lecturas."""

    def create(self, reading: Reading) -> Reading: ...

    def get_by_id(self, reading_id: int) -> Reading | None: ...

    def list_for_sensor(
        self,
        sensor_id: str,
        offset: int,
        limit: int,
        from_date: datetime | None,
        to_date: datetime | None,
    ) -> list[Reading]: ...

    def save(self, reading: Reading) -> Reading: ...

    def delete(self, reading: Reading) -> None: ...


class AlertRepositoryProtocol(Protocol):
    """Operaciones necesarias para alertas."""

    def create(self, alert: Alert) -> Alert: ...