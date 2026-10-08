import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)


def write_dataframe_to_jsonl(dataframe, output_file_path):
    try:
        output_file_path = Path(output_file_path)

        output_file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        dataframe.to_json(
            output_file_path,
            orient="records",
            lines=True,
            date_format="iso",
        )

        logger.info(
            "JSONL file created: %s",
            output_file_path,
        )

        return output_file_path

    except Exception:
        logger.exception(
            "Failed to write DataFrame to JSONL: %s",
            output_file_path,
        )
        raise