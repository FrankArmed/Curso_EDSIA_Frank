"""Métricas simples en memoria para SensorHub."""
# Frank Asael Méndez García - 18/07/2026


class Metrics:
    """Guarda contadores básicos del proceso."""

    def __init__(self) -> None:
        self.requests = 0
        self.errors = 0
        self.alerts = 0

    def record_request(self) -> None:
        self.requests += 1

    def record_error(self) -> None:
        self.errors += 1

    def record_alert(self) -> None:
        self.alerts += 1

    def snapshot(self) -> dict[str, int]:
        return {
            "requests_total": self.requests,
            "errors_total": self.errors,
            "alerts_total": self.alerts,
        }


metrics = Metrics()
