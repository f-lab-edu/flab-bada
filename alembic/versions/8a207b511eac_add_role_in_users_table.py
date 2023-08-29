"""add role in users table

Revision ID: 8a207b511eac
Revises: 36104b3b9a54
Create Date: 2023-05-03 19:34:58.683989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8a207b511eac"
down_revision = "36104b3b9a54"
branch_labels = None
depends_on = None


def upgrade() -> None:
    "일반 유저 상세 정보 테이블 추가"
    op.create_table(
        "user_details",
        sa.Column("seq", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("name", sa.VARCHAR(30)),
        sa.Column("phone", sa.VARCHAR(30)),
        sa.Column("nick_name", sa.VARCHAR(30)),
        sa.Column("create_date", sa.TIMESTAMP, server_default=sa.sql.func.now()),
        sa.Column("update_date", sa.TIMESTAMP, server_default=sa.sql.func.now()),
    )


def downgrade() -> None:
    pass
