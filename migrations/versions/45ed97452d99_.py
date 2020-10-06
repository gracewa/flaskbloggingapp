"""empty message

Revision ID: 45ed97452d99
Revises: 0b36910b3ab3
Create Date: 2020-10-06 09:48:41.050713

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '45ed97452d99'
down_revision = '0b36910b3ab3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('subtitle', sa.String(length=50), nullable=True),
    sa.Column('author', sa.String(length=20), nullable=True),
    sa.Column('date_posted', sa.Time(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_title', sa.String(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('posted', sa.Time(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('blogpost')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogpost',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('subtitle', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('author', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('date_posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='blogpost_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blogpost_pkey')
    )
    op.drop_table('comments')
    op.drop_table('blogs')
    # ### end Alembic commands ###
