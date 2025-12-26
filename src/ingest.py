import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

def fetch_crypto_data():
    """Fetches live market data from CoinGecko API."""
    url = os.getenv("COINGECKO_API_URL")
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,cardano,solana",
        "order": "market_cap_desc"
    }
    
    try:
        logging.info("Requesting data from CoinGecko API...")
        response = requests.get(url, params=params)
        response.raise_for_status() 
        
        data = response.json()
        logging.info(f"Successfully retrieved {len(data)} coin records.")
        return data
    except Exception as e:
        logging.error(f"API Ingestion Error: {e}")
        return None