"""add foreign key to post table

Revision ID: 93949ab0b582
Revises: 901715512507
Create Date: 2025-08-04 20:04:37.789420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93949ab0b582'
down_revision: Union[str, Sequence[str], None] = '901715512507'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('sqlachemyposts',
                  sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_posts_users', source_table='sqlachemyposts',
                          referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('fk_posts_users', table_name='sqlachemyposts')
    op.drop_column('sqlachemyposts', 'owner_id')
    pass
