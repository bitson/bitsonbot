"""change data type to chat_id and hour fields on alarm

Revision ID: 623f55fb03d3
Revises: f0be413fe0a5
Create Date: 2016-10-27 00:22:27.485465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '623f55fb03d3'
down_revision = 'f0be413fe0a5'
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alarms', sa.Column('enable', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alarms', 'enable')
    ### end Alembic commands ###
