import logging

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from src.config.settings import (
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_NAME,
    DATABASE_USER,
    DATABASE_PASSWORD,
)


logger = logging.getLogger(__name__)


def get_database_url():
    return (
        f"postgresql+psycopg://"
        f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
        f"{DATABASE_HOST}:{DATABASE_PORT}/"
        f"{DATABASE_NAME}"
    )


def create_database_engine():
    try:
        database_url = get_database_url()

        engine = create_engine(
            database_url,
            pool_pre_ping=True,
        )

        logger.info("PostgreSQL database engine created successfully.")

        return engine

    except SQLAlchemyError:
        logger.exception("Failed to create PostgreSQL database engine.")
        raise


def check_database_connection(engine):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        logger.info("PostgreSQL connection successful.")
        return True

    except SQLAlchemyError:
        logger.exception("PostgreSQL connection failed.")
        return False