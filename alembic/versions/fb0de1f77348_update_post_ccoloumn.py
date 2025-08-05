"""update post ccoloumn

Revision ID: fb0de1f77348
Revises: 8b908f26a36f
Create Date: 2025-08-04 19:52:52.875187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb0de1f77348'
down_revision: Union[str, Sequence[str], None] = '8b908f26a36f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('sqlachemyposts',
                  sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('sqlachemyposts', 'content')
    pass
