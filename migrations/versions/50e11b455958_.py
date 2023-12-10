"""empty message

Revision ID: 50e11b455958
Revises: ca84a0db4d3c
Create Date: 2023-10-18 15:02:51.539894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50e11b455958'
down_revision = 'ca84a0db4d3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('public_id', sa.String(length=256), server_default='<function Test.<lambda> at 0x7f2c4b2f2160>', nullable=True))
        batch_op.add_column(sa.Column('entity_type', sa.String(length=256), server_default='GEN', nullable=True))
        batch_op.create_unique_constraint(None, ['public_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('entity_type')
        batch_op.drop_column('public_id')

    # ### end Alembic commands ###