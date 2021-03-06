"""clue table

Revision ID: ef260033ad0e
Revises: 424e9e0e37e3
Create Date: 2020-08-31 10:35:12.498286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef260033ad0e'
down_revision = '424e9e0e37e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('needer', sa.Integer(), nullable=True),
    sa.Column('holder', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['holder'], ['puzzle.id'], ),
    sa.ForeignKeyConstraint(['needer'], ['puzzle.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clue')
    # ### end Alembic commands ###
