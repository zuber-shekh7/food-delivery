"""empty message

Revision ID: ac9edba5af65
Revises: dd1d80a94194
Create Date: 2020-04-25 17:10:34.610795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac9edba5af65'
down_revision = 'dd1d80a94194'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('owner', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('mobile', sa.String(), nullable=False),
    sa.Column('license', sa.String(), nullable=False),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant')
    # ### end Alembic commands ###