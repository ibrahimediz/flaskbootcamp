"""empty message

Revision ID: 8289f77226e5
Revises: 
Create Date: 2022-01-23 09:47:31.936452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8289f77226e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kullanici',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kullanici_adi', sa.String(length=64), nullable=True),
    sa.Column('eposta', sa.String(length=120), nullable=True),
    sa.Column('sifre_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_kullanici_eposta'), 'kullanici', ['eposta'], unique=True)
    op.create_index(op.f('ix_kullanici_kullanici_adi'), 'kullanici', ['kullanici_adi'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_kullanici_kullanici_adi'), table_name='kullanici')
    op.drop_index(op.f('ix_kullanici_eposta'), table_name='kullanici')
    op.drop_table('kullanici')
    # ### end Alembic commands ###
