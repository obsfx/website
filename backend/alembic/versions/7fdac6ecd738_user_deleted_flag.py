"""User deleted flag

Revision ID: 7fdac6ecd738
Revises: 7f294d530215
Create Date: 2022-02-22 13:56:43.801551

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "7fdac6ecd738"
down_revision = "7f294d530215"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("flathubuser", sa.Column("deleted", sa.Boolean(), nullable=True))
    op.execute("UPDATE flathubuser SET deleted=false")
    op.alter_column("flathubuser", "deleted", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("flathubuser", "deleted")
    # ### end Alembic commands ###