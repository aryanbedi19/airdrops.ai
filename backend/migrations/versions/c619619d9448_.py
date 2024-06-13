"""empty message

Revision ID: c619619d9448
Revises: 
Create Date: 2024-06-12 21:44:20.295981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c619619d9448'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('airdrop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('claim_url', sa.String(length=256), nullable=True),
    sa.Column('logo_url', sa.String(length=256), nullable=True),
    sa.Column('network', sa.String(length=64), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('percentage', sa.Float(), nullable=True),
    sa.Column('sentiment_score', sa.Float(), nullable=True),
    sa.Column('risk_score', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('wallet_address', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('subscription_end_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('wallet_address')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('airdrop')
    # ### end Alembic commands ###