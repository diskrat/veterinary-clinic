import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Carrega variáveis do .env
from dotenv import load_dotenv
load_dotenv()

# Adiciona o diretório raiz do projeto no sys.path para importar seus modelos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa seu Base com schema
from models.base import Base  # Base declarative_base() com metadata(schema="veterinaria")

# Esta é a meta info usada por Alembic para autogenerate
target_metadata = Base.metadata

# Configuração do Alembic
config = context.config

# Substituir a url do banco pela variável de ambiente
config.set_main_option('sqlalchemy.url', os.getenv('DATABASE_URL'))

# Interpretar o arquivo de configuração do logging
fileConfig(config.config_file_name)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema="veterinaria"  # Garante que a tabela de versões fique no schema
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table_schema="veterinaria"  # Mesma coisa para a tabela alembic_version
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
