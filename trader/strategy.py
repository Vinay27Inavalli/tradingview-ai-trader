import pandas as pd

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["ema_fast"] = out["close"].ewm(span=20, adjust=False).mean()
    out["ema_slow"] = out["close"].ewm(span=50, adjust=False).mean()
    delta = out["close"].diff()
    gain = delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean()
    rs = gain / loss.replace(0, float("nan"))
    out["rsi"] = 100 - (100 / (1 + rs))
    return out

def add_signals(df: pd.DataFrame) -> pd.DataFrame:
    out = add_indicators(df)
    cross_up = (out["ema_fast"] > out["ema_slow"]) & (out["ema_fast"].shift(1) <= out["ema_slow"].shift(1))
    cross_down = (out["ema_fast"] < out["ema_slow"]) & (out["ema_fast"].shift(1) >= out["ema_slow"].shift(1))
    out["buy"] = cross_up & out["rsi"].between(45, 70)
    out["sell"] = cross_down | (out["rsi"] > 75)
    return out
