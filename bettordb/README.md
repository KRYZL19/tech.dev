# BETTORDB — Casino Probability Engine API

> *"The math proves the martingale always loses. Now prove it to your users."*

A FastAPI-based casino probability engine. Calculate house edges, simulate betting systems, convert odds formats, and run the Kelly Criterion.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API runs at `http://localhost:8000`. Docs at `http://localhost:8000/docs`.

## Endpoints

### 🎰 Slot Machine Simulation
```
POST /api/v1/simulate/slots
```
Simulate slot spins with weighted symbols.

**Request:**
```json
{
  "spins": 1000,
  "paylines": 1,
  "symbol_weights": {"cherry": 10, "lemon": 8, "orange": 6, "plum": 4, "7": 1},
  "reels": 5,
  "bet_per_line": 1.0
}
```

**Response:**
```json
{
  "house_edge": 0.049,
  "rtp": 0.951,
  "expected_loss": 49.0
}
```

---

### 🎲 Betting System Simulation
```
POST /api/v1/simulate/betting-system
```
Simulate martingale, fibonacci, dalembert, or flat betting over 10,000 sequences. **The martingale will destroy you.**

**Request:**
```json
{
  "system": "martingale",
  "base_bet": 10,
  "target_wins": 5,
  "max_bets": 100,
  "bankroll": 1000,
  "win_probability": 0.475
}
```

**Response:**
```json
{
  "system": "martingale",
  "prob_reaching_target": 0.96,
  "prob_ruin": 0.04,
  "expected_value": -25.3,
  "median_ending_bankroll": 1020.0,
  "worst_case": 0.0,
  "n_simulations": 10000
}
```

> **The martingale trap:** ~96% reach their target but the ~4% who blow up lose everything. Expected value stays negative. The house always wins.

---

### 🔄 Odds Conversion
```
POST /api/v1/odds/convert
```
Convert between decimal, fractional, American, and implied probability.

**Request (any one field):**
```json
{
  "decimal_odds": 2.5
}
```

**Response:**
```json
{
  "decimal": 2.5,
  "fractional": 1.5,
  "american": 150.0,
  "implied_probability": 0.4
}
```

---

### 📊 Kelly Criterion
```
POST /api/v1/kelly/criterion
```
Calculate optimal bet size using the Kelly Criterion.

**Request:**
```json
{
  "bankroll": 10000,
  "odds_decimal": 3.0,
  "probability_win": 0.4
}
```

**Response:**
```json
{
  "kelly_fraction": 0.233333,
  "suggested_bet": 2333.33,
  "is_kelly_positive": true
}
```

---

### 🃏 Blackjack Odds
```
GET /api/v1/game/blackjack/odds?decks=6
```
Returns house edge, blackjack probability, and dealer bust probability.

---

### 🎡 Roulette Odds
```
GET /api/v1/game/roulette/odds?variant=european
```
Returns house edge and pocket count. Supports `european` (37 pockets) or `american` (38 pockets).

---

### 💚 Health
```
GET /api/v1/health
```

## Deployment

### Render
```bash
render.yaml  # Auto-deploys on render.com
```

### Railway
```bash
railway.toml  # Auto-deploys on railway.app
```

## Files

```
bettordb/
├── main.py              # FastAPI app + game endpoints
├── requirements.txt
├── routes/
│   ├── simulate.py      # Slots + betting system simulation
│   ├── odds.py          # Odds format conversion
│   └── kelly.py         # Kelly Criterion
├── games/
│   ├── slots.py         # Slot machine simulator
│   ├── blackjack.py     # Blackjack odds calculator
│   ├── roulette.py      # Roulette odds calculator
│   ├── baccarat.py      # Baccarat odds
│   └── martingale.py    # Betting system simulator (the proof)
├── models/
│   └── schemas.py       # Pydantic request/response models
├── render.yaml
├── railway.toml
└── README.md
```

## The Martingale Proof

Run this to see why martingale fails:

```bash
curl -X POST http://localhost:8000/api/v1/simulate/betting-system \
  -H "Content-Type: application/json" \
  -d '{
    "system": "martingale",
    "base_bet": 10,
    "target_wins": 5,
    "max_bets": 100,
    "bankroll": 1000,
    "win_probability": 0.475
  }'
```

**What you'll find:** ~96% of sequences hit the target. But that 4% ruin rate — combined with the fact that the losers lose EVERYTHING — makes expected value deeply negative. The median looks fine. The worst case is $0. The house edge compounds. No infinite bankroll exists.

Play long enough, and the martingale will take everything.

---

*Built for anyone who thinks they've found a "system."*
