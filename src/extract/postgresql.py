import logging

import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.database.connection import create_database_engine


logger = logging.getLogger(__name__)


def extract_purchase_orders():
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
        """
    )

    engine = create_database_engine()

    try:
        purchase_orders = pd.read_sql(query, engine)

        logger.info(
            "Extracted %s purchase orders from PostgreSQL.",
            len(purchase_orders),
        )

        return purchase_orders

    except SQLAlchemyError:
        logger.exception("Failed to extract purchase orders from PostgreSQL.")
        raise

    finally:
        engine.dispose()