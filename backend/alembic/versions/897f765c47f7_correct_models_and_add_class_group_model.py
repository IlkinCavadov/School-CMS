"""refactor school class model

Revision ID: 8c4f7b1d92aa
Revises: e6ddddb726f5
Create Date: 2026-08-15 20:10:00.000000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "8c4f7b1d92aa"
down_revision: Union[str, Sequence[str], None] = "e6ddddb726f5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ---------------------------------------------------------
    # 1. Create class_group
    # ---------------------------------------------------------

    op.create_table(
        "class_group",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column(
            "name",
            sa.String(length=50),
            nullable=False,
        ),
        sa.UniqueConstraint(
            "name",
            name="uq_class_group_name",
        ),
    )

    # ---------------------------------------------------------
    # 2. Create groups from existing school_class names
    #
    # Existing examples:
    #   8A -> A
    #   8B -> B
    #   9A -> A
    #   9B -> B
    # ---------------------------------------------------------

    op.execute(
        """
        INSERT INTO class_group (name)
        SELECT DISTINCT
            regexp_replace(name, '^[0-9]+', '')
        FROM school_class
        WHERE name IS NOT NULL
        """
    )

    # ---------------------------------------------------------
    # 3. Add new columns to school_class
    # ---------------------------------------------------------

    op.add_column(
        "school_class",
        sa.Column(
            "class_group_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.add_column(
        "school_class",
        sa.Column(
            "grade",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.add_column(
        "school_class",
        sa.Column(
            "school_year",
            sa.String(length=9),
            nullable=True,
        ),
    )

    # ---------------------------------------------------------
    # 4. Populate new columns from existing data
    # ---------------------------------------------------------

    op.execute(
        """
        UPDATE school_class sc
        SET
            class_group_id = cg.id,
            grade = substring(sc.name from '^[0-9]+')::INTEGER,
            school_year =
                sc.start_year::TEXT
                || '/'
                || right(sc.end_year::TEXT, 2)
        FROM class_group cg
        WHERE cg.name = regexp_replace(sc.name, '^[0-9]+', '')
        """
    )

    # ---------------------------------------------------------
    # 5. Make new columns required
    # ---------------------------------------------------------

    op.alter_column(
        "school_class",
        "class_group_id",
        nullable=False,
    )

    op.alter_column(
        "school_class",
        "grade",
        nullable=False,
    )

    op.alter_column(
        "school_class",
        "school_year",
        nullable=False,
    )

    # ---------------------------------------------------------
    # 6. Add foreign key
    # ---------------------------------------------------------

    op.create_foreign_key(
        "fk_school_class_class_group",
        "school_class",
        "class_group",
        ["class_group_id"],
        ["id"],
    )

    # ---------------------------------------------------------
    # 7. Remove old representation
    # ---------------------------------------------------------

    op.drop_column("school_class", "name")
    op.drop_column("school_class", "start_year")
    op.drop_column("school_class", "end_year")


def downgrade() -> None:
    # ---------------------------------------------------------
    # 1. Restore old columns
    # ---------------------------------------------------------

    op.add_column(
        "school_class",
        sa.Column(
            "name",
            sa.String(length=100),
            nullable=True,
        ),
    )

    op.add_column(
        "school_class",
        sa.Column(
            "start_year",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.add_column(
        "school_class",
        sa.Column(
            "end_year",
            sa.Integer(),
            nullable=True,
        ),
    )

    # ---------------------------------------------------------
    # 2. Reconstruct old values
    #
    # grade 8 + group A -> 8A
    # 2025/26 -> 2025, 2026
    # ---------------------------------------------------------

    op.execute(
        """
        UPDATE school_class sc
        SET
            name = sc.grade::TEXT || cg.name,
            start_year = split_part(sc.school_year, '/', 1)::INTEGER,
            end_year =
                split_part(sc.school_year, '/', 1)::INTEGER + 1
        FROM class_group cg
        WHERE cg.id = sc.class_group_id
        """
    )

    # ---------------------------------------------------------
    # 3. Make old columns required again
    # ---------------------------------------------------------

    op.alter_column(
        "school_class",
        "name",
        nullable=False,
    )

    op.alter_column(
        "school_class",
        "start_year",
        nullable=False,
    )

    op.alter_column(
        "school_class",
        "end_year",
        nullable=False,
    )

    # ---------------------------------------------------------
    # 4. Remove FK and new columns
    # ---------------------------------------------------------

    op.drop_constraint(
        "fk_school_class_class_group",
        "school_class",
        type_="foreignkey",
    )

    op.drop_column("school_class", "school_year")
    op.drop_column("school_class", "grade")
    op.drop_column("school_class", "class_group_id")

    # ---------------------------------------------------------
    # 5. Remove class_group
    # ---------------------------------------------------------

    op.drop_table("class_group")