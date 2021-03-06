"""empty message

Revision ID: 5eb72a27f75d
Revises: d03b3664b087
Create Date: 2020-10-08 10:14:50.291396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5eb72a27f75d'
down_revision = 'd03b3664b087'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('date_modified', sa.DateTime(), nullable=True))
    op.add_column('blogs', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.drop_constraint('blogs_user_id_fkey', 'blogs', type_='foreignkey')
    op.create_foreign_key(None, 'blogs', 'users', ['owner_id'], ['id'])
    op.drop_column('blogs', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.create_foreign_key('blogs_user_id_fkey', 'blogs', 'users', ['user_id'], ['id'])
    op.drop_column('blogs', 'owner_id')
    op.drop_column('blogs', 'date_modified')
    # ### end Alembic commands ###
