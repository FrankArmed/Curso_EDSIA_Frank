"""Repositorios en memoria para probar los servicios."""

# Frank Asael Méndez García - 01/08/2026

from datetime import datetime

from app.models import Reading, Sensor


class FakeSensorRepository:
    """Guarda sensores en memoria."""

    def __init__(self) -> None:
        self.sensors: dict[str, Sensor] = {}

    def create(self, sensor: Sensor) -> Sensor:
        """Guarda un sensor."""
        self.sensors[sensor.id] = sensor
        return sensor

    def get_by_id(self, sensor_id: str) -> Sensor | None:
        """Busca un sensor."""
        return self.sensors.get(sensor_id)

    def list_all(
        self,
        offset: int,
        limit: int,
    ) -> list[Sensor]:
        """Devuelve sensores paginados."""
        sensors = sorted(
            self.sensors.values(),
            key=lambda sensor: sensor.id,
        )

        return sensors[offset : offset + limit]

    def save(self, sensor: Sensor) -> Sensor:
        """Guarda cambios."""
        self.sensors[sensor.id] = sensor
        return sensor

    def delete(self, sensor: Sensor) -> None:
        """Elimina un sensor."""
        del self.sensors[sensor.id]


class FakeReadingRepository:  ##Apartado hecho con ayuda de la IA. Se ha modificado para que cumpla con el protocolo.
    """Guarda lecturas en memoria."""

    def __init__(self) -> None:
        self.readings: dict[int, Reading] = {}
        self.next_id = 1

    def create(self, reading: Reading) -> Reading:
        """Guarda una lectura."""
        reading.id = self.next_id
        self.readings[reading.id] = reading
        self.next_id += 1

        return reading

    def get_by_id(self, reading_id: int) -> Reading | None:
        """Busca una lectura."""
        return self.readings.get(reading_id)

    def list_for_sensor(
        self,
        sensor_id: str,
        offset: int,
        limit: int,
        from_date: datetime | None,
        to_date: datetime | None,
    ) -> list[Reading]:
        """Filtra lecturas de un sensor."""
        readings = [
            reading
            for reading in self.readings.values()
            if reading.sensor_id == sensor_id
        ]

        if from_date is not None:
            readings = [
                reading
                for reading in readings
                if reading.recorded_at >= from_date
            ]

        if to_date is not None:
            readings = [
                reading
                for reading in readings
                if reading.recorded_at <= to_date
            ]

        readings.sort(key=lambda reading: reading.id)

        return readings[offset : offset + limit]

    def save(self, reading: Reading) -> Reading:
        """Guarda cambios."""
        self.readings[reading.id] = reading
        return reading

    def delete(self, reading: Reading) -> None:
        """Elimina una lectura."""
        del self.readings[reading.id]