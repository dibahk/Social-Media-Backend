"""add content column to post table

Revision ID: ad368b0b7094
Revises: db0f4925e310
Create Date: 2024-10-10 18:07:15.934231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad368b0b7094'
down_revision: Union[str, None] = 'db0f4925e310'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column("posts", 'content')
    pass
