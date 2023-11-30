"""add: religion field

Revision ID: 284b19912274
Revises: 0f1bbda43a2b
Create Date: 2023-11-30 00:52:32.940950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '284b19912274'
down_revision = '0f1bbda43a2b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("user") as batch_op:
        batch_op.add_column(
            sa.Column("religion", sa.String(200), nullable=True),
        )


def downgrade() -> None:
    with op.batch_alter_table("user") as batch_op:
        batch_op.drop_column("religion")