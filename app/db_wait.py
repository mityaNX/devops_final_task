import time
import psycopg2
from psycopg2 import OperationalError
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def wait_for_db(retries=10, delay=3):
    for i in range(retries):
        try:
            conn = psycopg2.connect(DATABASE_URL)
            conn.close()
            print("PostgreSQL is ready")
            return
        except OperationalError:
            print(f"Waiting for PostgreSQL... ({i+1}/{retries})")
            time.sleep(delay)

    raise RuntimeError("PostgreSQL is not available")
