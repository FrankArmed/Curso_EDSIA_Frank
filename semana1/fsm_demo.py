"""Máquina de estados finitos para un semáforo."""
## Frank Asael Méndez García - 18/07/2026 - fsm_demo.py
from enum import Enum
from typing import ClassVar


class TrafficLightState(str, Enum):
    """Estados posibles del semáforo."""

    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"


class TrafficLightFSM:
    """Máquina de estados de un semáforo de tres colores."""

    _TRANSITIONS: ClassVar[dict[TrafficLightState, TrafficLightState]] = {
        TrafficLightState.RED: TrafficLightState.GREEN,
        TrafficLightState.GREEN: TrafficLightState.YELLOW,
        TrafficLightState.YELLOW: TrafficLightState.RED,
    }

    def __init__(self) -> None:
        """Inicializa el semáforo en rojo y sin ciclos completados."""
        self._state = TrafficLightState.RED
        self._cycle_count = 0

    @property
    def state(self) -> TrafficLightState:
        """Devuelve el estado actual del semáforo."""
        return self._state

    @property
    def cycle_count(self) -> int:
        """Devuelve la cantidad de ciclos completos realizados."""
        return self._cycle_count

    def transition(self) -> TrafficLightState:
        """Avanza al siguiente estado y devuelve el nuevo estado."""
        previous_state = self._state
        self._state = self._TRANSITIONS[self._state]

        if (
            previous_state is TrafficLightState.YELLOW
            and self._state is TrafficLightState.RED
        ):
            self._cycle_count += 1

        return self._state