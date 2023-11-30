"""Fix: Refactoring user fields

Revision ID: d304dbbb6ffe
Revises: 0084e7dffc7c
Create Date: 2023-11-29 23:43:01.708622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd304dbbb6ffe'
down_revision = '0084e7dffc7c'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("user") as batch_op:
        batch_op.add_column(
            sa.Column("fullName", sa.String(200)),
        )
        batch_op.add_column(
            sa.Column("warName", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("birthDate", sa.Date()),
        )
        batch_op.add_column(
            sa.Column("placeOfBirth", sa.String(200)),
        )
        batch_op.add_column(
            sa.Column("ufNatural", sa.String(100)),
        )
        batch_op.add_column(
            sa.Column("civilState", sa.String(100), nullable=True),
        )
        batch_op.add_column(
            sa.Column("cep", sa.String(100), nullable=True),
        )
        batch_op.add_column(
            sa.Column("number", sa.String(100), nullable=True),
        )
        batch_op.add_column(
            sa.Column("complement", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("uf", sa.String(100)),
        )
        batch_op.add_column(
            sa.Column("cellphone", sa.String(200)),
        )
        batch_op.add_column(
            sa.Column("motherName", sa.String(200)),
        )
        batch_op.add_column(
            sa.Column("fatherName", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("scolarity", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("bloodType", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("actualWorkSituation", sa.String(200)),
        )
        batch_op.add_column(
            sa.Column("admissionDate", sa.Date()),
        )
        batch_op.add_column(
            sa.Column("jobRole", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("bodyOfLaw", sa.String(200)),
        )
        batch_op.add_column(
            sa.Column("lotation", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("workPost", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("systemRole", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("password", sa.String(200), nullable=True),
        )


def downgrade():
    with op.batch_alter_table("user") as batch_op:
        batch_op.drop_column("name")
        batch_op.drop_column("nickname")
        batch_op.drop_column("birth_date")
        batch_op.drop_column("place_of_birth")
        batch_op.drop_column("marital_status")
        batch_op.drop_column("zipcode")
        batch_op.drop_column("state")
        batch_op.drop_column("mother_date")
        batch_op.drop_column("mother_name")
        batch_op.drop_column("father_name")
        batch_op.drop_column("education")
        batch_op.drop_column("blood_type")
        batch_op.drop_column("situation")
        batch_op.drop_column("role")
        batch_op.drop_column("workstation")
        batch_op.drop_column("dispatcher")
        batch_op.drop_column("dispatched_date")
        batch_op.drop_column("position")
        batch_op.drop_column("occupancy")
        batch_op.drop_column("admission_date")
        batch_op.drop_column("category")
        batch_op.drop_column("pattern")