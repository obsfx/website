"""user_verified_app

Revision ID: 253ab628caf8
Revises: 18bbc5ea44de
Create Date: 2022-03-08 04:48:12.590882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '253ab628caf8'
down_revision = '18bbc5ea44de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userverifiedapp',
    sa.Column('app_id', sa.String(), nullable=False),
    sa.Column('account', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['account'], ['flathubuser.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('app_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userverifiedapp')
    # ### end Alembic commands ###