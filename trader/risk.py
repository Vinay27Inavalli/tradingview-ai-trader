def position_size(cash: float, price: float, risk_fraction: float, stop_pct: float) -> float:
    if cash <= 0 or price <= 0 or stop_pct <= 0:
        return 0.0
    risk_budget = cash * risk_fraction
    qty_by_risk = risk_budget / (price * stop_pct)
    return min(qty_by_risk, cash / price)
