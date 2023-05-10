"""add foreign key in lectures table

Revision ID: 3f71a28d9893
Revises: 31152dd66549
Create Date: 2023-05-03 20:58:08.986228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f71a28d9893'
down_revision = '31152dd66549'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.execute("""
    #     alter table lectures add foreign key (user_id) references users (id)
    # """)
    pass

def downgrade() -> None:
    pass
