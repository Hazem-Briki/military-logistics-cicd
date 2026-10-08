import logging

from src.config.logging import configure_logging
from src.extract.postgresql import extract_purchase_orders


configure_logging()

logger = logging.getLogger(__name__)


logger.info("Starting purchase order extraction.")

purchase_orders = extract_purchase_orders()

logger.info(
    "Purchase order extraction finished. Rows: %s",
    len(purchase_orders),
)

print(purchase_orders)
print()
print(f"Number of rows: {len(purchase_orders)}")