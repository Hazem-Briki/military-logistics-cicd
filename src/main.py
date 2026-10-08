import logging
from datetime import datetime
from pathlib import Path

from src.config.logging import configure_logging
from src.extract.checkpoint import read_checkpoint, write_checkpoint
from src.extract.postgresql import extract_purchase_orders
from src.load.gcs import upload_file_to_gcs
from src.load.jsonl import write_dataframe_to_jsonl


configure_logging()

logger = logging.getLogger(__name__)


BUCKET_NAME = "military-logistics-dev-raw"


def main():
    logger.info("Starting purchase order ETL.")

    # 1. Extract
    purchase_orders = extract_purchase_orders()

    if purchase_orders.empty:
        logger.info("No new purchase orders found. ETL finished.")
        return

    logger.info(
        "Extracted %s purchase orders.",
        len(purchase_orders),
    )

    # 2. Prepare file paths
    ingestion_datetime = datetime.now()
    ingestion_date = ingestion_datetime.strftime("%Y-%m-%d")
    timestamp = ingestion_datetime.strftime("%Y%m%d_%H%M%S")

    local_file_path = Path(
        f"data/raw/postgres/purchase_orders/"
        f"ingestion_date={ingestion_date}/"
        f"purchase_orders_{timestamp}.jsonl"
    )

    gcs_file_path = (
        f"postgres/purchase_orders/"
        f"ingestion_date={ingestion_date}/"
        f"purchase_orders_{timestamp}.jsonl"
    )

    # 3. Write JSONL
    write_dataframe_to_jsonl(
        purchase_orders,
        local_file_path,
    )

    # 4. Upload to GCS
    upload_file_to_gcs(
        local_file_path,
        BUCKET_NAME,
        gcs_file_path,
    )

    # 5. Update checkpoint ONLY after successful upload
    latest_updated_at = purchase_orders["updated_at"].max()

    write_checkpoint(str(latest_updated_at))

    logger.info(
        "Checkpoint updated to: %s",
        latest_updated_at,
    )

    logger.info("Purchase order ETL finished successfully.")


if __name__ == "__main__":
    main()