"""create letures table

Revision ID: 36104b3b9a54
Revises: d43197b3c81c
Create Date: 2023-04-28 15:31:09.974093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36104b3b9a54'
down_revision = 'd43197b3c81c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "lectures",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("name", sa.VARCHAR(20)),
        sa.Column("doc", sa.TEXT),
        sa.Column("create_date", sa.TIMESTAMP, server_default=sa.sql.func.now()),
        sa.Column("update_date", sa.TIMESTAMP, server_default=sa.sql.func.now())
    )


def downgrade() -> None:
    op.drop_table("lectures")
