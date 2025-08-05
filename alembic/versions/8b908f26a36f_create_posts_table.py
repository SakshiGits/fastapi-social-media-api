"""create posts table

Revision ID: 8b908f26a36f
Revises: 
Create Date: 2025-08-04 19:38:58.466217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b908f26a36f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('sqlachemyposts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),
                    )
    pass


def downgrade() -> None:
    op.drop_table('sqlachemyposts')
    pass
