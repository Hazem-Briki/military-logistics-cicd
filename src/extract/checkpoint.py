import json
from pathlib import Path


CHECKPOINT_FILE = Path("data/checkpoints/purchase_orders.json")


def read_checkpoint(checkpoint_file=CHECKPOINT_FILE):
    if not checkpoint_file.exists():
        return None

    with checkpoint_file.open("r", encoding="utf-8") as file:
        checkpoint = json.load(file)

    return checkpoint.get("last_updated_at")


def write_checkpoint(last_updated_at, checkpoint_file=CHECKPOINT_FILE):
    checkpoint = {
        "last_updated_at": last_updated_at
    }

    checkpoint_file.parent.mkdir(parents=True, exist_ok=True)

    with checkpoint_file.open("w", encoding="utf-8") as file:
        json.dump(checkpoint, file, indent=4)