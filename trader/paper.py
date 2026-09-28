import csv
from pathlib import Path
from .data import fetch_ohlcv
from .strategy import add_signals
from . import config

JOURNAL = Path("data/paper_signals.csv")

def run():
    df = add_signals(fetch_ohlcv())
    r = df.iloc[-2]  # last fully closed candle
    action = "BUY" if bool(r["buy"]) else "SELL" if bool(r["sell"]) else "HOLD"
    print(f'{r["timestamp"]} {config.SYMBOL} {config.TIMEFRAME} close={r["close"]:.2f} signal={action}')
    JOURNAL.parent.mkdir(exist_ok=True)
    new = not JOURNAL.exists()
    with JOURNAL.open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new: w.writerow(["timestamp","symbol","timeframe","close","signal"])
        w.writerow([r["timestamp"], config.SYMBOL, config.TIMEFRAME, r["close"], action])
    print(f"Paper signal saved to {JOURNAL}. No live order was sent.")

if __name__ == "__main__":
    run()
