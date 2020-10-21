"""empty message

Revision ID: 9664d7f6af50
Revises: 
Create Date: 2020-10-21 14:52:39.572571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9664d7f6af50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column(
        'status', sa.SmallInteger(), server_default='0'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entry', 'status')
    # ### end Alembic commands ###
