"""rename column user.mother_date to user.mother_name and add column user.password

Revision ID: e8a3e8746d3e
Revises: 0084e7dffc7c
Create Date: 2023-11-02 16:33:58.855003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8a3e8746d3e'
down_revision = '0084e7dffc7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("user", "mother_date", new_column_name="mother_name", type_=sa.String(length=200))
    with op.batch_alter_table("user") as batch_op:
        batch_op.add_column(
            sa.Column("password", sa.String(200), nullable=True),
        )

def downgrade() -> None:
    op.alter_column("user", "mother_name", new_column_name="mother_date", type_=sa.String(length=200))
    with op.batch_alter_table("user") as batch_op:
        batch_op.drop_column("password")
