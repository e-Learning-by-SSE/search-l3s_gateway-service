"""empty message

Revision ID: b5116cd47fa1
Revises: 033acb10cf86
Create Date: 2023-10-25 15:04:52.005568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5116cd47fa1'
down_revision = '033acb10cf86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('task_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('task_id_full', sa.String(length=255), nullable=True))
        batch_op.drop_constraint('Task_task_id_int_key', type_='unique')
        batch_op.drop_constraint('Task_task_id_str_key', type_='unique')
        batch_op.create_unique_constraint(None, ['task_id_full'])
        batch_op.create_unique_constraint(None, ['task_id'])
        batch_op.drop_column('task_id_str')
        batch_op.drop_column('task_id_int')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('task_id_int', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('task_id_str', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('Task_task_id_str_key', ['task_id_str'])
        batch_op.create_unique_constraint('Task_task_id_int_key', ['task_id_int'])
        batch_op.drop_column('task_id_full')
        batch_op.drop_column('task_id')

    # ### end Alembic commands ###