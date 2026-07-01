from bot.client import ClientWrapper
from bot.logging_config import logger
from binance.error import ClientError

def execute_trade(symbol: str, side: str, type: str, qty: float, price: float = None):
    client = ClientWrapper().get()

    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": type.upper(),
        "quantity": qty,
    }

    # limits need a price
    if params["type"] == "LIMIT":
        if not price:
            raise ValueError("need a price for LIMIT")
        params["price"] = price
        params["timeInForce"] = "GTC" # good till cancel

    # stops also need a price trigger
    if params["type"] == "STOP_MARKET":
        if not price:
             raise ValueError("need a stop price for STOP_MARKET")
        params["stopPrice"] = price

    logger.info(f"Placing {params['type']} {params['side']} order: {qty} {params['symbol']}")
    logger.debug(f"Request parameters: {params}")

    try:
        res = client.new_order(**params)
        logger.info(f"Order placed successfully. ID: {res.get('orderId')}")
        logger.debug(f"API response: {res}")
        return res
    except ClientError as e:
        logger.error(f"Binance API error: {e.error_message} (status_code={e.status_code})")
        raise ValueError(e.error_message)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise e
