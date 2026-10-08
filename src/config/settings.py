import os

from dotenv import load_dotenv


load_dotenv()


DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")


def validate_settings():
    required_settings = {
        "DATABASE_HOST": DATABASE_HOST,
        "DATABASE_NAME": DATABASE_NAME,
        "DATABASE_USER": DATABASE_USER,
        "DATABASE_PASSWORD": DATABASE_PASSWORD,
    }

    missing_settings = [
        name
        for name, value in required_settings.items()
        if not value
    ]

    if missing_settings:
        raise ValueError(
            f"Missing required settings: {', '.join(missing_settings)}"
        )