"""create users table

Revision ID: d43197b3c81c
Revises: 
Create Date: 2023-04-27 22:37:46.617182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd43197b3c81c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("users")

    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("email", sa.VARCHAR(30)),
        sa.Column("password", sa.VARCHAR(100)),
        sa.Column("use_yn", sa.CHAR(1), server_default="Y"),
        sa.Column("role", sa.VARCHAR(10), server_default="user"),
        sa.Column("create_date", sa.TIMESTAMP, server_default=sa.sql.func.now()),
        sa.Column("update_date", sa.TIMESTAMP, server_default=sa.sql.func.now()),
    )


def downgrade() -> None:
    op.drop_table("users")
