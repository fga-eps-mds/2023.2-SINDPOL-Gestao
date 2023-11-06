"""add dependent cof gender and pensioner

Revision ID: 0084e7dffc7c
Revises: 05258d089f10
Create Date: 2023-10-28 21:23:57.809923

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0084e7dffc7c"
down_revision = "05258d089f10"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("dependent") as batch_op:
        batch_op.add_column(
            sa.Column("cpf", sa.String(200), nullable=True, unique=True),
        )
        batch_op.add_column(
            sa.Column("gender", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("phone", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("pensioner", sa.Boolean(), default=False),
        )


def downgrade():
    with op.batch_alter_table("dependent") as batch_op:
        batch_op.drop_column("cpf")
        batch_op.drop_column("gender")
        batch_op.drop_column("phone")
        batch_op.drop_column("pensioner")
