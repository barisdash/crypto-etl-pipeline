import os
import logging
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_connection():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        return None

def create_price_table():
    """Creates the crypto_prices table if it does not exist."""
    query = """
    CREATE TABLE IF NOT EXISTS crypto_prices (
        id SERIAL PRIMARY KEY,
        coin_id VARCHAR(50),
        symbol VARCHAR(10),
        current_price DECIMAL,
        market_cap BIGINT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            logging.info("Database schema verified (Table exists or was created).")
            cur.close()
            conn.close()
        except Exception as e:
            logging.error(f"Error creating table: {e}")