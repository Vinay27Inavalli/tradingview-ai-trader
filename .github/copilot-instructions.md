# Project instructions

This repository is open-source, local-first crypto research software.

- Keep live exchange execution disabled unless explicitly designed, reviewed, and opt-in.
- Default to paper trading.
- Never commit secrets or API keys.
- Prefer free/open-source dependencies.
- Add tests for strategy, risk, and execution changes.
- Avoid look-ahead bias: signals must use information available at the decision timestamp.
- Include fees/slippage assumptions when evaluating strategies.
- Do not describe backtest performance as guaranteed future returns.
