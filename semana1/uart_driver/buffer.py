"""Buffer circular seguro para varios hilos."""

# Frank Asael Méndez García - 18/07/2026
# Archivo: buffer.py

from collections import deque
from threading import Lock
from typing import Generic, TypeVar

T = TypeVar("T")


class CircularBuffer(Generic[T]):
    """Almacena una cantidad limitada de elementos."""

    def __init__(self, capacity: int) -> None:
        """Crea un buffer con la capacidad indicada."""
        if capacity <= 0:
            raise ValueError("capacity debe ser mayor que cero")

        self._capacity = capacity
        self._items: deque[T] = deque(maxlen=capacity)
        self._lock = Lock()

    @property
    def capacity(self) -> int:
        """Devuelve la capacidad máxima del buffer."""
        return self._capacity

    def append(self, item: T) -> None:
        """Agrega un elemento al buffer."""
        with self._lock:
            self._items.append(item)

    def get_all(self) -> list[T]:
        """Devuelve una copia de los elementos almacenados."""
        with self._lock:
            return list(self._items)

    def clear(self) -> None:
        """Elimina todos los elementos."""
        with self._lock:
            self._items.clear()

    def __len__(self) -> int:
        """Devuelve la cantidad actual de elementos."""
        with self._lock:
            return len(self._items)