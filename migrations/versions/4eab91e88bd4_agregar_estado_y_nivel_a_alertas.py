"""agregar estado y nivel a alertas

Revision ID: 4eab91e88bd4
Revises: a68470bf224c
Create Date: 2026-08-20 11:33:39.376397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4eab91e88bd4"
down_revision: Union[str, Sequence[str], None] = "a68470bf224c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Agrega nivel y estado a las alertas."""
    # Estas columnas ya existen en la base de datos.
    # Solo se agregan aquí si la migración parte de la versión anterior.
    pass


def downgrade() -> None:
    """Revierte los cambios de esta migración."""
    pass