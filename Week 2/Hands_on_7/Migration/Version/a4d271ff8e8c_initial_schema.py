"""Initial database schema

Revision ID: a4d271ff8e8c
Revises: None
Created On: 2026-06-28 21:06:51.994332
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# Alembic revision details
revision: str = "a4d271ff8e8c"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Apply migration."""
    # Migration statements will be added here.
    pass


def downgrade() -> None:
    """Rollback migration."""
    # Reverse migration statements will be added here.
    pass