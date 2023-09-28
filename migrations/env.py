import os
from dotenv import load_dotenv

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from app.libs import database
from app.utils.base import metadata
from alembic import context


load_dotenv()
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Set up the database connection
engine = database.engine

# Your model's MetaData object (Base) should be used for 'autogenerate' support.
target_metadata = metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    with engine.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata,
            compare_type=True,  # Add this option to enable type comparison during migrations
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
