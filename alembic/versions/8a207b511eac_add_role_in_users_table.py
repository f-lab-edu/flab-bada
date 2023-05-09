"""add role in users table

Revision ID: 8a207b511eac
Revises: 36104b3b9a54
Create Date: 2023-05-03 19:34:58.683989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a207b511eac'
down_revision = '36104b3b9a54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.execute("""
    #     alter table users
    #     add role varchar(20) after `use_yn`
    # """)
    pass

def downgrade() -> None:
    pass
