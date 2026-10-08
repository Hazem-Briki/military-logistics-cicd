import logging
from pathlib import Path

from google.cloud import storage


logger = logging.getLogger(__name__)


def upload_file_to_gcs(
    local_file_path,
    bucket_name,
    destination_blob_name,
):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(local_file_path)

        logger.info(
            "File uploaded to GCS: gs://%s/%s",
            bucket_name,
            destination_blob_name,
        )

    except Exception:
        logger.exception(
            "Failed to upload file to GCS: %s",
            local_file_path,
        )
        raise