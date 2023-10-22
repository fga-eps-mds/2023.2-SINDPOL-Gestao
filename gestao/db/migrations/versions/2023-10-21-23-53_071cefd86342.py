"""user table

Revision ID: 071cefd86342
Revises:
Create Date: 2023-10-21 23:53:52.242776

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "071cefd86342"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.String(length=200), primary_key=True, nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("address", sa.String(length=200), nullable=False),
        sa.Column("neighborhood", sa.String(length=200), nullable=False),
        sa.Column("city", sa.String(length=100), nullable=False),
        sa.Column("state", sa.String(length=100), nullable=False),
        sa.Column("zipcode", sa.String(length=100), nullable=False),
        sa.Column("cpf", sa.String(length=200), unique=True, nullable=False),
        sa.Column("rg", sa.String(length=200), unique=True, nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("place_of_birth", sa.String(length=200), nullable=False),
        sa.Column("blood_type", sa.String(length=200), nullable=False),
        sa.Column("gender", sa.String(length=200), nullable=False),
        sa.Column("father_name", sa.String(length=200), nullable=False),
        sa.Column("mother_date", sa.String(length=200), nullable=False),
        sa.Column("position", sa.String(length=200), nullable=False),
        sa.Column("occupancy", sa.String(length=200), nullable=False),
        sa.Column("admission_date", sa.Date(), nullable=False),
        sa.Column("situation", sa.String(length=200), nullable=False),
        sa.Column("phone", sa.String(length=200), nullable=False),
        sa.Column("email", sa.String(length=200), nullable=False),
        sa.Column("marital_status", sa.String(length=200), nullable=False),
        sa.Column("education", sa.String(length=200), nullable=False),
        sa.Column("registration", sa.String(length=200), unique=True, nullable=False),
        sa.Column("role", sa.String(length=200), nullable=False),
        sa.Column("category", sa.String(length=200), nullable=False),
        sa.Column("pattern", sa.String(length=200), nullable=False),
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


def downgrade() -> None:
    op.drop_table("user")
