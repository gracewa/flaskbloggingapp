"""empty message

Revision ID: 0b36910b3ab3
Revises: e39ad8e8cd22
Create Date: 2020-10-06 07:14:41.267812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b36910b3ab3'
down_revision = 'e39ad8e8cd22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogpost', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogpost', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogpost', type_='foreignkey')
    op.drop_column('blogpost', 'user_id')
    # ### end Alembic commands ###
