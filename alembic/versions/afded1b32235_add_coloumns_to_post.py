"""add coloumns to post

Revision ID: afded1b32235
Revises: 93949ab0b582
Create Date: 2025-08-04 20:12:02.894525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afded1b32235'
down_revision: Union[str, Sequence[str], None] = '93949ab0b582'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('sqlachemyposts',
                  sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False))
    op.add_column('sqlachemyposts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable=False))

    pass


def downgrade() -> None:
    op.drop_column('sqlachemyposts', 'published')
    op.drop_column('sqlachemyposts', 'created_at')
    pass
