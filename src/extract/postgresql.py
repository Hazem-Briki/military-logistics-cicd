import logging

import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.database.connection import create_database_engine
from src.extract.checkpoint import read_checkpoint, write_checkpoint


logger = logging.getLogger(__name__)


def extract_purchase_orders():
    last_updated_at = read_checkpoint()

    if last_updated_at:
        query = text(
            """
            SELECT
                purchase_order_id,
                supplier_id,
                order_date,
                expected_delivery_date,
                status,
                currency,
                total_amount,
                created_at,
                updated_at
            FROM purchase_orders
            WHERE updated_at > :last_updated_at
            ORDER BY updated_at
            """
        )

        query_parameters = {
            "last_updated_at": last_updated_at
        }

        logger.info(
            "Starting incremental extraction from checkpoint: %s",
            last_updated_at,
        )

    else:
        query = text(
            """
            SELECT
                purchase_order_id,
                supplier_id,
                order_date,
                expected_delivery_date,
                status,
                currency,
                total_amount,
                created_at,
                updated_at
            FROM purchase_orders
            ORDER BY updated_at
            """
        )

        query_parameters = {}

        logger.info(
            "No checkpoint found. Starting initial extraction."
        )

    engine = create_database_engine()

    try:
        purchase_orders = pd.read_sql(
            query,
            engine,
            params=query_parameters,
        )

        row_count = len(purchase_orders)

        logger.info(
            "Extracted %s purchase orders from PostgreSQL.",
            row_count,
        )

        if row_count == 0:
            logger.info("No new or updated purchase orders found.")
            return purchase_orders

        latest_updated_at = purchase_orders["updated_at"].max()

        write_checkpoint(str(latest_updated_at))

        logger.info(
            "Checkpoint updated to: %s",
            latest_updated_at,
        )

        return purchase_orders

    except SQLAlchemyError:
        logger.exception(
            "Failed to extract purchase orders from PostgreSQL."
        )
        raise

    finally:
        engine.dispose()