import ccxt
import pandas as pd
from . import config

def fetch_ohlcv():
    exchange_cls = getattr(ccxt, config.EXCHANGE)
    exchange = exchange_cls({"enableRateLimit": True})
    rows = exchange.fetch_ohlcv(config.SYMBOL, config.TIMEFRAME, limit=config.CANDLE_LIMIT)
    df = pd.DataFrame(rows, columns=["timestamp","open","high","low","close","volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
    return df
