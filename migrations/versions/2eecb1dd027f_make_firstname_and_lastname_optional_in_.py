"""Make firstname and lastname optional in user

Revision ID: 2eecb1dd027f
Revises: dca2317ac876
Create Date: 2019-01-20 13:50:36.120541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eecb1dd027f'
down_revision = 'dca2317ac876'
branch_labels = None
depends_on = None


def upgrade():
  op.alter_column('user', 'first_name', nullable=True)
  op.alter_column('user', 'last_name', nullable=True)


def downgrade():
  op.alter_column('user', 'first_name', nullable=False)
  op.alter_column('user', 'last_name', nullable=False)
