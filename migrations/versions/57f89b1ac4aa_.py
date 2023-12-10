"""empty message

Revision ID: 57f89b1ac4aa
Revises: 43b997313676
Create Date: 2023-10-18 16:11:29.931835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57f89b1ac4aa'
down_revision = '43b997313676'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('another_id', sa.String(length=256), server_default=sa.text("lower('536a3f13-590b-4eee-9b69-40670a6b5461')"), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_column('another_id')

    # ### end Alembic commands ###