"""Version 0.1.0

Revision ID: baa78950306e
Revises: 
Create Date: 2021-10-14 20:28:53.875007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baa78950306e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_location_rank'), 'location', ['rank'], unique=False)
    op.create_unique_constraint(None, 'location', ['sid'])
    op.add_column('sensor', sa.Column('last_bat_chg', sa.DateTime(), nullable=True))
    op.add_column('sensor', sa.Column('nbr_bat_chg', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sensor', 'nbr_bat_chg')
    op.drop_column('sensor', 'last_bat_chg')
    op.drop_constraint(None, 'location', type_='unique')
    op.drop_index(op.f('ix_location_rank'), table_name='location')
    # ### end Alembic commands ###
