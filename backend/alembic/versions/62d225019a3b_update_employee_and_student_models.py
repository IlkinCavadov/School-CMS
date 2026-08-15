"""update employee and student models

Revision ID: 62d225019a3b
Revises: 609789a9d628
Create Date: 2026-08-09 14:05:17.932669

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "62d225019a3b"
down_revision: Union[str, Sequence[str], None] = "609789a9d628"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    employee_type = sa.Enum(
        "TEACHER",
        "PRINCIPAL",
        name="employee_type",
    )

    # Create PostgreSQL enum type first
    employee_type.create(op.get_bind(), checkfirst=True)

    # Add employee_type as nullable because existing employees
    # don't necessarily have a type yet.
    op.add_column(
        "employee",
        sa.Column(
            "employee_type",
            employee_type,
            nullable=True,
        ),
    )

    # Employee number can initially be NULL.
    # It will be generated later by the application.
    op.alter_column(
        "employee",
        "employee_number",
        existing_type=sa.VARCHAR(length=50),
        nullable=True,
    )

    # Hire date only needs a calendar date, not a timestamp.
    op.alter_column(
        "employee",
        "hire_date",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        type_=sa.Date(),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    # Change hire_date back to timestamp
    op.alter_column(
        "employee",
        "hire_date",
        existing_type=sa.Date(),
        type_=postgresql.TIMESTAMP(timezone=True),
        existing_nullable=False,
    )

    # employee_number becomes required again
    op.alter_column(
        "employee",
        "employee_number",
        existing_type=sa.VARCHAR(length=50),
        nullable=False,
    )

    # Remove employee_type column
    op.drop_column(
        "employee",
        "employee_type",
    )

    # Remove PostgreSQL enum type
    employee_type = sa.Enum(
        "TEACHER",
        "PRINCIPAL",
        name="employee_type",
    )

    employee_type.drop(
        op.get_bind(),
        checkfirst=True,
    )