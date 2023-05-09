"""drop lectures table

Revision ID: 3942df77c862
Revises: 3f71a28d9893
Create Date: 2023-05-03 21:18:58.837584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3942df77c862'
down_revision = '3f71a28d9893'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("lectures")


def downgrade() -> None:
    pass
