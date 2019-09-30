"""empty message

Revision ID: 4476623b5ebd
Revises: None
Create Date: 2019-09-30 11:41:31.390837

"""

# revision identifiers, used by Alembic.
revision = '4476623b5ebd'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loguser1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jmeno', sa.String(), nullable=False),
    sa.Column('prijmeni', sa.String(), nullable=False),
    sa.Column('pohlavi', sa.Boolean(name='zena'), nullable=True),
    sa.Column('datum_insertu', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_loguser1'),
    sqlite_autoincrement=True
    )
    op.create_index('ix_loguser1_prijmeni', 'loguser1', ['prijmeni'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activate_token', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('verified', sa.Boolean(name='verified'), nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_users')
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.create_table('maso',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('typ', sa.Integer(), nullable=False),
    sa.Column('cast', sa.Integer(), nullable=False),
    sa.Column('cena', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_maso'),
    sqlite_autoincrement=True
    )
    op.create_index('ix_maso_cast', 'maso', ['cast'], unique=False)
    op.create_table('parent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prijmeni', sa.String(), nullable=False),
    sa.Column('pohlavi', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_parent'),
    sqlite_autoincrement=True
    )
    op.create_index('ix_parent_prijmeni', 'parent', ['prijmeni'], unique=False)
    op.create_table('loguser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Petr', sa.String(), nullable=False),
    sa.Column('Grussmann', sa.String(), nullable=False),
    sa.Column('pohlavi', sa.Boolean(name='zena'), nullable=True),
    sa.Column('datum_insertu', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_loguser'),
    sqlite_autoincrement=True
    )
    op.create_index('ix_loguser_Grussmann', 'loguser', ['Grussmann'], unique=False)
    op.create_table('user_password_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('used', sa.Boolean(name='used'), nullable=True),
    sa.Column('expiration_dt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_user_password_tokens_user_id_users'),
    sa.PrimaryKeyConstraint('id', name='pk_user_password_tokens')
    )
    op.create_index('ix_user_password_tokens_value', 'user_password_tokens', ['value'], unique=False)
    op.create_table('child',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('jmeno', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent.id'], name='fk_child_parent_id_parent'),
    sa.PrimaryKeyConstraint('id', name='pk_child')
    )
    op.create_index('ix_child_jmeno', 'child', ['jmeno'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_child_jmeno', table_name='child')
    op.drop_table('child')
    op.drop_index('ix_user_password_tokens_value', table_name='user_password_tokens')
    op.drop_table('user_password_tokens')
    op.drop_index('ix_loguser_Grussmann', table_name='loguser')
    op.drop_table('loguser')
    op.drop_index('ix_parent_prijmeni', table_name='parent')
    op.drop_table('parent')
    op.drop_index('ix_maso_cast', table_name='maso')
    op.drop_table('maso')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_loguser1_prijmeni', table_name='loguser1')
    op.drop_table('loguser1')
    ### end Alembic commands ###
