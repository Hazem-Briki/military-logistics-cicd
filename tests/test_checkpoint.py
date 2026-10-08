from pathlib import Path

from src.extract.checkpoint import read_checkpoint, write_checkpoint


def test_checkpoint(tmp_path):
    checkpoint_file = Path(tmp_path) / "purchase_orders.json"

    write_checkpoint(
        "2026-09-16 14:52:46",
        checkpoint_file,
    )

    checkpoint = read_checkpoint(checkpoint_file)

    assert checkpoint == "2026-09-16 14:52:46"