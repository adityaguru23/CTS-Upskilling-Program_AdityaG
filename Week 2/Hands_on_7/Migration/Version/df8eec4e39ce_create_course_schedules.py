"""Create course schedules table

Revision ID: df8eec4e39ce
Revises: cdd976c80b93
Created On: 2026-06-28 21:18:03.981709
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# Alembic revision details
revision: str = "df8eec4e39ce"
down_revision: Union[str, Sequence[str], None] = "cdd976c80b93"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Apply migration."""

    op.create_table(
        "course_schedules",
        sa.Column("schedule_id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("course_id", sa.Integer(), sa.ForeignKey("courses.course_id")),
        sa.Column("day_of_week", sa.String(20)),
        sa.Column("start_time", sa.String(10)),
        sa.Column("end_time", sa.String(10))
    )


def downgrade() -> None:
    """Rollback migration."""

    op.drop_table("course_schedules")