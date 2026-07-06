"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Created On: ${create_date}
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

${imports if imports else ""}

# Alembic Revision Information
revision: str = ${repr(up_revision)}
down_revision: Union[str, Sequence[str], None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Apply database changes."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Revert database changes."""
    ${downgrades if downgrades else "pass"}