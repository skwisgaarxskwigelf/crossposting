"""empty message

Revision ID: 55a43fabbb4b
Revises: 
Create Date: 2019-04-26 22:37:53.199053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55a43fabbb4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('header', sa.String(), nullable=True),
    sa.Column('post', sa.Text(), nullable=True),
    sa.Column('img_path', sa.String(), nullable=True),
    sa.Column('img_date', sa.DateTime(), nullable=True),
    sa.Column('post_date', sa.DateTime(), nullable=True),
    sa.Column('sent', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('channels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('channels')
    op.drop_table('posts')
    # ### end Alembic commands ###
