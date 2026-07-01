# binance futures testnet bot

a simple python script to place orders on the binance futures testnet (usdt-m). uses `typer` for the cli and `rich` to make the output look decent.

## features
- supports `MARKET`, `LIMIT`, and `STOP_MARKET` orders
- long/short (BUY/SELL)
- grabs keys from `.env`
- logs all requests to `trading_bot.log` so you can debug the api payloads

## setup

1. install stuff:
```bash
pip install -r requirements.txt
```

2. create a `.env` file in this folder with your testnet keys:
```env
BINANCE_API_KEY=your_testnet_key_here
BINANCE_API_SECRET=your_testnet_secret_here
```
*(make sure to use testnet keys, not your real ones)*

## usage

just run it through python:

**market buy (0.001 btc):**
```bash
python cli.py BTCUSDT BUY MARKET 0.001
```

**limit sell (0.001 btc @ 65000):**
```bash
python cli.py BTCUSDT SELL LIMIT 0.001 --price 65000
```

**stop market sell (trigger @ 60000):**
```bash
python cli.py BTCUSDT SELL STOP_MARKET 0.001 --price 60000
```

## assumptions & notes
- **Testnet Only:** Assumes API interactions are exclusively for the USDT-M Futures Testnet.
- **Keys in Environment:** Assumes credentials (`BINANCE_API_KEY`, `BINANCE_API_SECRET`) are present in a `.env` file in the root directory.
- **USDT-M symbols:** Assumes input symbols exist on the USDT-M futures exchange (e.g., `BTCUSDT`).
- **Logs:** Logs of all requests/responses are output to `trading_bot.log` in the root folder.

