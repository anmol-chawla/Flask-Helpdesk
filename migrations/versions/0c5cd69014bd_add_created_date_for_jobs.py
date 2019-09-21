"""Add created date for jobs

Revision ID: 0c5cd69014bd
Revises: c702fce408b4
Create Date: 2019-09-21 15:56:37.972523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c5cd69014bd'
down_revision = 'c702fce408b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'created_at')
    # ### end Alembic commands ###