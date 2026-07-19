"""Pruebas para el buffer circular."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: test_buffer.py

from threading import Thread

import pytest

from semana1.uart_driver.buffer import CircularBuffer


def test_buffer_stores_items() -> None:
    """Debe almacenar los elementos agregados."""
    buffer = CircularBuffer[int](3)

    buffer.append(10)
    buffer.append(20)

    assert buffer.get_all() == [10, 20]
    assert len(buffer) == 2


def test_buffer_discards_oldest_item() -> None:
    """Debe eliminar el elemento más antiguo cuando se llena."""
    buffer = CircularBuffer[int](3)

    for value in [1, 2, 3, 4]:
        buffer.append(value)

    assert buffer.get_all() == [2, 3, 4]


def test_buffer_rejects_invalid_capacity() -> None:
    """Debe rechazar capacidades menores o iguales a cero."""
    with pytest.raises(ValueError, match="mayor que cero"):
        CircularBuffer[int](0)


def test_buffer_can_be_cleared() -> None:
    """Debe permitir eliminar todos sus elementos."""
    buffer = CircularBuffer[str](3)

    buffer.append("A")
    buffer.append("B")
    buffer.clear()

    assert buffer.get_all() == []
    assert len(buffer) == 0


def test_buffer_supports_multiple_threads() -> None:
    """Debe aceptar datos desde diferentes hilos."""
    buffer = CircularBuffer[int](200)

    def add_values(start: int) -> None:
        for value in range(start, start + 100):
            buffer.append(value)

    first_thread = Thread(target=add_values, args=(0,))
    second_thread = Thread(target=add_values, args=(100,))

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()

    values = buffer.get_all()

    assert len(values) == 200
    assert set(values) == set(range(200))