import os
from binance.um_futures import UMFutures
from dotenv import load_dotenv
from bot.logging_config import logger

load_dotenv()

class ClientWrapper:
    def __init__(self):
        # grab keys from env
        key = os.getenv("BINANCE_API_KEY")
        secret = os.getenv("BINANCE_API_SECRET")
        
        if not key or not secret:
            logger.warning("missing API keys in env")
            
        # force testnet URL
        base = "https://testnet.binancefuture.com"
        logger.info(f"connecting to {base}")
        
        self.client = UMFutures(key=key, secret=secret, base_url=base)

    def get(self):
        return self.client
