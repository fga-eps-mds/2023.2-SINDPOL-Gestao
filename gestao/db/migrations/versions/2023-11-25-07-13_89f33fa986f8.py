"""rename column 'mother_date' to 'mother_name' and add columns 'password and 'religion'

Revision ID: 89f33fa986f8
Revises: 0084e7dffc7c
Create Date: 2023-11-25 07:13:16.617587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89f33fa986f8'
down_revision = '0084e7dffc7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("user") as batch_op:
        batch_op.alter_column('mother_date', new_column_name='mother_name', existing_type=sa.String(length=200))
        batch_op.add_column(
            sa.Column("password", sa.String(200), nullable=True),
        )
        batch_op.add_column(
            sa.Column("religion", sa.String(200), nullable=True),
        )


def downgrade() -> None:
    with op.batch_alter_table("user") as batch_op:
        batch_op.alter_column('mother_name', new_column_name='mother_date', existing_type=sa.String(length=200))
        batch_op.drop_column("password")
        batch_op.drop_column("religion")
