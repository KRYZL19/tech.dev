# BETTORDB API — Casino Probability & Simulation Engine

**For educational and game development use only.**

A FastAPI-powered backend that provides gambling probability data, odds conversion, and Monte Carlo betting system simulations. Built for casino game developers and betting system researchers.

---

## What It Does

BETTORDB provides real-time probability calculations and Monte Carlo simulations for popular casino games and betting systems:

- **Slot Machine Simulation** — Weighted reel analysis with configurable symbols, paylines, and reels. Returns house edge, RTP, expected loss, and 95% confidence intervals.
- **Betting System Simulator** — Monte Carlo analysis (10,000 sequences) for Martingale, Fibonacci, D'Alembert, and Flat betting. Returns probability of reaching target, ruin probability, expected value, and worst-case scenarios.
- **Odds Converter** — Convert between decimal, fractional, American (moneyline), and implied probability formats.
- **Kelly Criterion Calculator** — Optimal bet sizing based on bankroll, odds, and win probability.
- **Blackjack Odds** — House edge for basic strategy and card counting, natural blackjack probability, dealer bust probability.
- **Roulette Odds** — House edge and pocket probabilities for American (38 pockets) and European (37 pockets) variants.
- **Baccarat Odds** — Player, Banker, and Tie probabilities with house edge.

---

## Who It's For

- **Casino game developers** building slot machines, table games, or betting interfaces
- **Betting system researchers** analyzing Martingale, Fibonacci, and other betting strategies
- **Quantitative analysts** working on gambling probability models
- **Game jam / side project developers** needing quick odds calculations

---

## Quick Start

```bash
cd bettordb
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

API docs at `http://localhost:8000/docs`

---

## API Endpoints

### Health Check

```bash
curl http://localhost:8000/api/v1/health
```

### Slot Machine Simulation

```bash
curl -X POST http://localhost:8000/api/v1/simulate/slots \
  -H "Content-Type: application/json" \
  -d '{
    "spins": 1000000,
    "paylines": 5,
    "symbol_weights": [10, 5, 3, 2, 1],
    "reels": 5,
    "bet_per_line": 0.25
  }'
```

### Betting System Simulation (Martingale)

```bash
curl -X POST http://localhost:8000/api/v1/simulate/betting-system \
  -H "Content-Type: application/json" \
  -d '{
    "system": "martingale",
    "base_bet": 10,
    "target_wins": 5,
    "max_bets": 100,
    "bankroll": 1000,
    "win_probability": 0.4768,
    "payout": 2.0
  }'
```

### Odds Conversion

```bash
curl -X POST http://localhost:8000/api/v1/odds/convert \
  -H "Content-Type: application/json" \
  -d '{
    "value": 2.5,
    "from_format": "decimal",
    "to_format": "american"
  }'
```

### Kelly Criterion

```bash
curl -X POST http://localhost:8000/api/v1/kelly/criterion \
  -H "Content-Type: application/json" \
  -d '{
    "bankroll": 1000,
    "odds_decimal": 2.1,
    "probability_win": 0.52
  }'
```

### Blackjack Odds

```bash
curl "http://localhost:8000/api/v1/game/blackjack/odds?decks=6&dealer_stands_on=17"
```

### Roulette Odds

```bash
curl "http://localhost:8000/api/v1/game/roulette/odds?variant=european"
```

---

## Pricing

| Plan | Simulations/Month | Rate Limits | Support |
|------|-------------------|-------------|---------|
| **Free** | 1,000 sims | 100 req/min | Community |
| **Dev** ($49/mo) | 100,000 sims | 1,000 req/min | Email |
| **Pro** ($199/mo) | Unlimited | 10,000 req/min | Priority |

Contact for enterprise licensing and white-label deployments.

---

## Deploy

### Railway

```bash
railway init
railway up
railway domain
```

Or use `railway.toml`:

```toml
[build]
builder = "nixpacks"
nixpacksPlan = "{ language = "python" }"

[deploy]
healthcheckPath = "/api/v1/health"
port = 8000
```

### Render

```bash
render deploy
```

Or use `render.yaml`:

```yaml
services:
  - type: web
    name: bettordb
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    healthCheckPath: /api/v1/health
```

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Tech Stack

- **FastAPI** — Async web framework
- **Pydantic v2** — Data validation
- **NumPy** — Fast Monte Carlo simulations
- **Uvicorn** — ASGI server

---

## Disclaimer

**For educational and game development use only.** This software is provided for simulating casino probabilities and analyzing betting systems. It is not intended for actual gambling. Betting systems do not overcome the house edge — past performance does not guarantee future results. Use responsibly.
