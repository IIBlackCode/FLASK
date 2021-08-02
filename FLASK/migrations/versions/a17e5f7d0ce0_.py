"""empty message

Revision ID: a17e5f7d0ce0
Revises: 
Create Date: 2021-08-02 17:47:00.011722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a17e5f7d0ce0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('member_email', sa.String(length=50), nullable=True),
    sa.Column('member_password', sa.String(length=200), nullable=False),
    sa.Column('member_favorite', sa.String(length=120), nullable=True),
    sa.Column('member_tier', sa.String(length=10), nullable=True),
    sa.Column('member_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('member_id'),
    sa.UniqueConstraint('member_email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member')
    # ### end Alembic commands ###
