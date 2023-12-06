"""Fix: Refactoring user fields

Revision ID: 02379f0ee4ac
Revises: 89f33fa986f8
Create Date: 2023-12-01 21:33:24.578159

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "02379f0ee4ac"
down_revision = "89f33fa986f8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("dependent")
    op.drop_table("user")

    op.create_table(
        "user",
        sa.Column("id", sa.String(length=200), primary_key=True, nullable=False),
        sa.Column("fullName", sa.String(length=200), nullable=False),
        sa.Column("warName", sa.String(length=200), nullable=True),
        sa.Column("registration", sa.String(length=200), unique=True, nullable=False),
        sa.Column("birthDate", sa.Date(), nullable=False),
        sa.Column("rg", sa.String(length=200), unique=True, nullable=False),
        sa.Column("cpf", sa.String(length=200), unique=True, nullable=False),
        sa.Column("placeOfBirth", sa.String(length=200), nullable=False),
        sa.Column("ufNatural", sa.String(length=200), nullable=False),
        sa.Column("civilState", sa.String(length=200), nullable=False),
        sa.Column("cep", sa.String(length=200), nullable=False),
        sa.Column("address", sa.String(length=200), nullable=False),
        sa.Column("number", sa.String(length=200), nullable=False),
        sa.Column("neighborhood", sa.String(length=200), nullable=False),
        sa.Column("city", sa.String(length=200), nullable=False),
        sa.Column("complement", sa.String(length=200), nullable=False),
        sa.Column("uf", sa.String(length=200), nullable=False),
        sa.Column("email", sa.String(length=200), unique=True, nullable=False),
        sa.Column("cellphone", sa.String(length=200), nullable=False),
        sa.Column("phone", sa.String(length=200), nullable=False),
        sa.Column("gender", sa.String(length=200), nullable=False),
        sa.Column("motherName", sa.String(length=200), nullable=False),
        sa.Column("fatherName", sa.String(length=200), nullable=False),
        sa.Column("scolarity", sa.String(length=200), nullable=False),
        sa.Column("religion", sa.String(length=200), nullable=False),
        sa.Column("bloodType", sa.String(length=200), nullable=False),
        sa.Column("actualWorkSituation", sa.String(length=200), nullable=False),
        sa.Column("admissionDate", sa.Date(), nullable=False),
        sa.Column("jobRole", sa.String(length=200), nullable=False),
        sa.Column("bodyOfLaw", sa.String(length=200), nullable=False),
        sa.Column("lotation", sa.String(length=200), nullable=False),
        sa.Column("workPost", sa.String(length=200), nullable=False),
        sa.Column("systemRole", sa.String(length=200), nullable=False),
        sa.Column("password", sa.String(length=200), nullable=False),
        sa.Column("status", sa.String(length=200), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        schema="public",
    )

    op.create_table(
        "dependent",
        sa.Column("id", sa.String(length=200), primary_key=True, nullable=False),
        sa.Column(
            "user_id",
            sa.String(length=200),
            sa.ForeignKey("user.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("relationship", sa.String(length=200), nullable=False),
        sa.Column("cpf", sa.String(200), nullable=True, unique=True),
        sa.Column("gender", sa.String(200), nullable=True),
        sa.Column("phone", sa.String(200), nullable=True),
        sa.Column("pensioner", sa.Boolean(), default=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        schema="public",
    )


def downgrade() -> None:
    op.drop_table("dependent")
    op.drop_table("user")

    op.create_table(
        "user",
        sa.Column("id", sa.String(length=200), primary_key=True, nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("address", sa.String(length=200), nullable=True),
        sa.Column("neighborhood", sa.String(length=200), nullable=False),
        sa.Column("city", sa.String(length=200), nullable=False),
        sa.Column("state", sa.String(length=200), nullable=False),
        sa.Column("zipcode", sa.String(length=200), nullable=False),
        sa.Column("cpf", sa.String(length=200), unique=True, nullable=False),
        sa.Column("rg", sa.String(length=200), unique=True, nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("place_of_birth", sa.String(length=200), nullable=False),
        sa.Column("blood_type", sa.String(length=200), nullable=False),
        sa.Column("gender", sa.String(length=200), nullable=False),
        sa.Column("father_name", sa.String(length=200), nullable=False),
        sa.Column("mother_name", sa.String(length=200), nullable=False),
        sa.Column("position", sa.String(length=200), nullable=False),
        sa.Column("admission_date", sa.Date(), nullable=False),
        sa.Column("situation", sa.String(length=200), nullable=False),
        sa.Column("phone", sa.String(length=200), nullable=False),
        sa.Column("email", sa.String(length=200), unique=True, nullable=False),
        sa.Column("marital_status", sa.String(length=200), nullable=False),
        sa.Column("education", sa.String(length=200), nullable=False),
        sa.Column("registration", sa.String(length=200), unique=True, nullable=False),
        sa.Column("role", sa.String(length=200), nullable=False),
        sa.Column("category", sa.String(length=200), nullable=False),
        sa.Column("pattern", sa.String(length=200), nullable=False),
        sa.Column("status", sa.String(length=200), nullable=False),
        sa.Column("workstation", sa.String(length=200), nullable=False),
        sa.Column("nickname", sa.String(length=200), nullable=False),
        sa.Column("password", sa.String(length=200), nullable=False),
        sa.Column("religion", sa.String(length=200), nullable=False),
        sa.Column("dispatcher", sa.String(length=200), nullable=False),
        sa.Column("dispatched_date", sa.Date(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        schema="public",
    )

    op.create_table(
        "dependent",
        sa.Column("id", sa.String(length=200), primary_key=True, nullable=False),
        sa.Column(
            "user_id",
            sa.String(length=200),
            sa.ForeignKey("user.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("relationship", sa.String(length=200), nullable=False),
        sa.Column("cpf", sa.String(200), nullable=True, unique=True),
        sa.Column("gender", sa.String(200), nullable=True),
        sa.Column("phone", sa.String(200), nullable=True),
        sa.Column("pensioner", sa.Boolean(), default=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        schema="public",
    )
