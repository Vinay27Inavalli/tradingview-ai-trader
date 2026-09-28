from .data import fetch_ohlcv
from .strategy import add_signals
from .risk import position_size
from . import config

def run():
    df = add_signals(fetch_ohlcv())
    cash, qty, entry = config.STARTING_CASH, 0.0, 0.0
    trades = []
    for _, r in df.iterrows():
        price = float(r["close"])
        if qty == 0 and bool(r["buy"]):
            qty = position_size(cash, price, config.RISK_PER_TRADE, config.STOP_LOSS_PCT)
            if qty:
                cost = qty * price
                fee = cost * config.FEE_RATE
                if cost + fee > cash:
                    qty = cash / (price * (1 + config.FEE_RATE))
                    cost, fee = qty * price, qty * price * config.FEE_RATE
                cash -= cost + fee
                entry = price
                trades.append(("BUY", r["timestamp"], price, qty))
        elif qty > 0:
            stopped = price <= entry * (1 - config.STOP_LOSS_PCT)
            if bool(r["sell"]) or stopped:
                proceeds = qty * price
                cash += proceeds - proceeds * config.FEE_RATE
                trades.append(("SELL", r["timestamp"], price, qty))
                qty, entry = 0.0, 0.0
    last = float(df.iloc[-1]["close"])
    equity = cash + qty * last
    print(f"Start: {config.STARTING_CASH:,.2f} USDT")
    print(f"End equity: {equity:,.2f} USDT")
    print(f"Return: {(equity/config.STARTING_CASH-1)*100:.2f}%")
    print(f"Trade events: {len(trades)}")

if __name__ == "__main__":
    run()
