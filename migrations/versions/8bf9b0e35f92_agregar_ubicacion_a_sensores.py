"""agregar ubicacion a sensores

Revision ID: 8bf9b0e35f92
Revises: e1e2e1303a6c
Create Date: 2026-08-20 11:03:25.887995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bf9b0e35f92'
down_revision: Union[str, Sequence[str], None] = 'e1e2e1303a6c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Agrega la ubicación de los sensores."""
    op.add_column(
        "sensors",
        sa.Column("location", sa.String(length=100), nullable=True),
    )


def downgrade() -> None:
    """Elimina la ubicación de los sensores."""
    op.drop_column("sensors", "location")