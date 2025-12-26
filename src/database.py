import psycopg2
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="crypto_vault",
            user="user",
            password="password",
            port="5432"
        )
        return conn
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        return None

def create_price_table():
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
            logging.info("Table schema verified.")
            cur.close()
            conn.close()
        except Exception as e:
            logging.error(f"Table creation error: {e}")
