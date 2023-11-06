"""dependent table

Revision ID: 532e4deb3c37
Revises: 071cefd86342
Create Date: 2023-10-22 02:46:30.124158

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "532e4deb3c37"
down_revision = "071cefd86342"
branch_labels = None
depends_on = None


def upgrade() -> None:
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
