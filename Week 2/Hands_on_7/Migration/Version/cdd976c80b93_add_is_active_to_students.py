"""Add active status column to students

Revision ID: cdd976c80b93
Revises: a4d271ff8e8c
Created On: 2026-06-28 21:15:37.151766
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# Alembic revision information
revision: str = "cdd976c80b93"
down_revision: Union[str, Sequence[str], None] = "a4d271ff8e8c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Apply migration."""

    op.add_column(
        "students",
        sa.Column("is_active", sa.Boolean(), nullable=True)
    )


def downgrade() -> None:
    """Rollback migration."""

    op.drop_column(
        "students",
        "is_active"
    )