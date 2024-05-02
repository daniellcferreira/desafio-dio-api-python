from alembic import op
import sqlalchemy as sa

revision = 'c006e8463ed4'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:

    op.create_table('categorias',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('centros_treinamento',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('endereco', sa.String(length=60), nullable=False),
    sa.Column('proprietario', sa.String(length=30), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('atletas',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.Column('peso', sa.Float(), nullable=False),
    sa.Column('altura', sa.Float(), nullable=False),
    sa.Column('sexo', sa.String(length=1), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.Column('centro_treinamento_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categoria.pk_id'],),
    sa.ForeignKeyConstraint(['centro_treinamento_id'], ['centros_treinamento.pk_id'],),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('nome')
    )

    def downgrade() -> None:
        op.drop_table('atletas')
        op.drop_table('centros_treinamento')
        op.drop_table('categorias')