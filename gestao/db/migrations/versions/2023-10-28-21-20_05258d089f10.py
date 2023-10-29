"""add user workstation and nickname

Revision ID: 05258d089f10
Revises: 532e4deb3c37
Create Date: 2023-10-28 21:20:43.696192

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "05258d089f10"
down_revision = "532e4deb3c37"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("user") as batch_op:
        batch_op.add_column(
            sa.Column("workstation", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("nickname", sa.String(200), nullable=True),
        )


def downgrade():
    with op.batch_alter_table("user") as batch_op:
        batch_op.drop_column("workstation")
        batch_op.drop_column("nickname")
