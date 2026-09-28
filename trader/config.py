import os
from dotenv import load_dotenv

load_dotenv()
EXCHANGE = os.getenv("EXCHANGE", "kraken")
SYMBOL = os.getenv("SYMBOL", "BTC/USDT")
TIMEFRAME = os.getenv("TIMEFRAME", "1h")
CANDLE_LIMIT = int(os.getenv("CANDLE_LIMIT", "1000"))
STARTING_CASH = float(os.getenv("STARTING_CASH", "10000"))
FEE_RATE = float(os.getenv("FEE_RATE", "0.001"))
RISK_PER_TRADE = float(os.getenv("RISK_PER_TRADE", "0.01"))
STOP_LOSS_PCT = float(os.getenv("STOP_LOSS_PCT", "0.02"))
