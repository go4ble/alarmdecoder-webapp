"""Added enable to notifications.

Revision ID: fdc8fd4be3c0
Revises: 279107daa1ff
Create Date: 2016-02-18 15:17:03.795749

"""

# revision identifiers, used by Alembic.
revision = 'fdc8fd4be3c0'
down_revision = '279107daa1ff'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notifications', sa.Column('enabled', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notifications', 'enabled')
    ### end Alembic commands ###
