"""agregar estado activo a sensores

Revision ID: a68470bf224c
Revises: 8bf9b0e35f92
Create Date: 2026-08-20 11:13:20.288714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a68470bf224c'
down_revision: Union[str, Sequence[str], None] = '8bf9b0e35f92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Agrega el estado activo de los sensores."""
    op.add_column(
        "sensors",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=True,
            server_default=sa.true(),
        ),
    )

def downgrade() -> None:
    """Elimina el estado activo de los sensores."""
    op.drop_column("sensors", "is_active")