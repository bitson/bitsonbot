"""change data type to chat_id and hour fields on alarm

Revision ID: 7c84c190c820
Revises: 5635e1857fbe
Create Date: 2016-10-27 00:23:47.314361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c84c190c820'
down_revision = '5635e1857fbe'
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alarms', sa.Column('chat_id', sa.String(length=100), nullable=True))
    op.add_column('alarms', sa.Column('hour', sa.String(length=100), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alarms', 'hour')
    op.drop_column('alarms', 'chat_id')
    ### end Alembic commands ###
