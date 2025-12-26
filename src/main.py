import logging
from ingest import fetch_crypto_data
from database import get_connection, create_price_table

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_to_database(data):
    """
    Takes a list of dictionaries (coin data) and inserts them into the database.
    Includes error handling and connection management.
    """
    if not data:
        logging.warning("No data received from API. Skipping database load.")
        return

    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            insert_query = """
                INSERT INTO crypto_prices (coin_id, symbol, current_price, market_cap) 
                VALUES (%s, %s, %s, %s)
            """
            
            for coin in data:
                cur.execute(insert_query, (
                    coin['id'], 
                    coin['symbol'], 
                    coin['current_price'], 
                    coin['market_cap']
                ))
            
            conn.commit() 
            logging.info(f"Successfully loaded {len(data)} records to the database.")
            
            cur.close()
            conn.close()
        except Exception as e:
            logging.error(f"Error occurred while loading data: {e}")

if __name__ == "__main__":
    logging.info("--- Starting ETL Pipeline ---")
    
    create_price_table()
    raw_data = fetch_crypto_data()
    load_to_database(raw_data)
    
    logging.info("--- ETL Process Finished Successfully ---")