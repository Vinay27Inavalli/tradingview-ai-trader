# tradingview-ai-trader

Open-source, local-first crypto strategy research and paper-trading system.

## V1
- Free public OHLCV data via CCXT
- EMA + RSI reference strategy
- Backtesting with fees
- Risk-based position sizing
- Local paper trading
- CSV trade journal
- No paid TradingView dependency
- No exchange API keys required

> Research/education software. Paper trading is the default. Backtests do not guarantee future results.

## Quick start

```powershell
git clone https://github.com/Vinay27Inavalli/tradingview-ai-trader.git
cd tradingview-ai-trader
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m trader.backtest
python -m trader.paper
```

Default market: BTC/USDT, 1h candles.

TradingView and GitHub Copilot are optional; the core project requires neither.
