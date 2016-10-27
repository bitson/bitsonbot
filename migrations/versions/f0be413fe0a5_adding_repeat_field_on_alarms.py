"""Adding repeat field on alarms

Revision ID: f0be413fe0a5
Revises: 5881f65eb492
Create Date: 2016-10-27 00:01:15.995728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0be413fe0a5'
down_revision = '5881f65eb492'
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alarms', 'enable')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alarms', sa.Column('enable', sa.BOOLEAN(), autoincrement=False, nullable=True))
    ### end Alembic commands ###
