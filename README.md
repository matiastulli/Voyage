# Voyage

To use Alembic, do::

    -> use to migrate changes in backend
    pip install alembic
    alembic init migrations
    alembic revision --autogenerate -m "First Migration"
    alembic upgrade head