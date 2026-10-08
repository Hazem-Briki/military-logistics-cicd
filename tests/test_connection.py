from src.database.connection import (
    check_database_connection,
    create_database_engine,
)


engine = create_database_engine()

if check_database_connection(engine):
    print("PostgreSQL connection successful.")
else:
    print("PostgreSQL connection failed.")