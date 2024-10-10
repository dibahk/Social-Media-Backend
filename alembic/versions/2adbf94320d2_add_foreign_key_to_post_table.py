"""add foreign key to post table

Revision ID: 2adbf94320d2
Revises: 896f10a6197b
Create Date: 2024-10-10 18:32:00.756399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2adbf94320d2'
down_revision: Union[str, None] = 'f9953b6b6bb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable= False))
    op.create_foreign_key('posts_users_fk', source_table= "posts", referent_table= "users", 
                          local_cols= ['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
