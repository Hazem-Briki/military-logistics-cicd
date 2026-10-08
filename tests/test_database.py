from src.database.connection import get_database_url


def test_database_url():
    database_url = get_database_url()

    assert database_url.startswith("postgresql+psycopg://")
    assert "@localhost:5432/" in database_url
    assert database_url.endswith("/military_supply")