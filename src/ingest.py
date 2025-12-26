import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_crypto_data():
    """Fetches live market data from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,cardano,solana",
        "order": "market_cap_desc"
    }
    try:
        logging.info("Fetching data from API...")
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Successfully retrieved {len(data)} records.")
        return data
    except Exception as e:
        logging.error(f"API Error: {e}")
        return None
