"""Pruebas para la máquina de estados del semáforo."""
## Frank Asael Méndez García - 18/07/2026 - test_fsm.py
from semana1.fsm_demo import TrafficLightFSM, TrafficLightState


def test_initial_state_is_red() -> None:
    """La máquina debe iniciar en rojo y con cero ciclos."""
    fsm = TrafficLightFSM()

    assert fsm.state is TrafficLightState.RED
    assert fsm.cycle_count == 0


def test_transition_from_red_to_green() -> None:
    """La primera transición debe cambiar de rojo a verde."""
    fsm = TrafficLightFSM()

    new_state = fsm.transition()

    assert new_state is TrafficLightState.GREEN
    assert fsm.state is TrafficLightState.GREEN


def test_complete_cycle_returns_to_red() -> None:
    """Tres transiciones deben completar un ciclo y volver a rojo."""
    fsm = TrafficLightFSM()

    fsm.transition()  # RED -> GREEN
    fsm.transition()  # GREEN -> YELLOW
    fsm.transition()  # YELLOW -> RED

    assert fsm.state is TrafficLightState.RED


def test_cycle_count_increments() -> None:
    """El contador debe aumentar por cada ciclo completo."""
    fsm = TrafficLightFSM()

    for _ in range(6):
        fsm.transition()

    assert fsm.state is TrafficLightState.RED
    assert fsm.cycle_count == 2