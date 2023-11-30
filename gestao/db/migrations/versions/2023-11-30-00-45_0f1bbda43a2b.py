"""add: religion field

Revision ID: 0f1bbda43a2b
Revises: d304dbbb6ffe
Create Date: 2023-11-30 00:45:51.838752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f1bbda43a2b'
down_revision = 'd304dbbb6ffe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("user") as batch_op:
        batch_op.add_column(
            sa.Column("religion", sa.String(200), nullable=True),
        )


def downgrade() -> None:
    pass
