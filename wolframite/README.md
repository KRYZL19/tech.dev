# WOLFRAMITE — Chess Puzzle API

> **"Chess puzzles rated 1800+ from any FEN position. Not an app. An API."**

A lightweight FastAPI-powered chess puzzle and analysis API. Evaluate positions, fetch puzzles, get daily challenges, explore openings, and annotate games.

---

## Endpoints

### POST `/api/v1/puzzle/from-position`
Get a chess puzzle from any FEN position at your target difficulty.

```json
// Request
{
  "fen": "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4",
  "difficulty": 1900
}

// Response
{
  "puzzle_fen": "...",
  "moves": ["h5f7"],
  "rating": 1800,
  "themes": ["short", "mate", "scholars_mate"]
}
```

### GET `/api/v1/puzzle/daily`
Today's daily puzzle with a hint. Same puzzle all day (UTC).

```json
{
  "puzzle_fen": "...",
  "moves": ["f3g5", "d8g5", "c4f7"],
  "rating": 1950,
  "themes": ["sacrifice", "fork"],
  "hint": "f3g5"
}
```

### POST `/api/v1/eval/position`
Evaluate a position: centipawn score, best move (UCI), and classification.

```json
// Request
{
  "fen": "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4"
}

// Response
{
  "eval_score_centipawns": 127,
  "best_move_uci": "f3g5",
  "classification": "advantage"
}
```

### GET `/api/v1/openings/{name}`
Get opening info by name or ECO code.

```json
// GET /api/v1/openings/A45
{
  "eco": "A45",
  "name": "Trompowsky Attack",
  "moves": ["d4", "Nf6", "Bg5"],
  "description": "White immediately attacks theNf6 knight...",
  "middlegame_plans": "Exchange on f6 and play e2-e4..."
}
```

### POST `/api/v1/game/annotate`
Annotate a PGN game and get blunders, mistakes, and inaccuracies.

```json
// Request body: pgn=1.e4 e5 2.Nf3 Nc6 ...
{
  "pgn": "1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4+ ..."
}

// Response
{
  "blunders": [...],
  "mistakes": [...],
  "inaccuracies": [...]
}
```

---

## Pricing

| Tier | Rate | Limits |
|------|------|--------|
| **Free** | $0 | 50 requests/day |
| **Dev** | $14/mo | 1,000 requests/day |
| **Pro** | $39/mo | 10,000 requests/day |

Pass `X-Plan: dev` or `X-Plan: pro` header to use your tier.

---

## Bundle

- **50 puzzles** — FEN + solution moves + rating (1800-2100) + themes
- **20 openings** — ECO codes A00-E00 with descriptions and middlegame plans
- **Material + pawn structure evaluation** — centipawn scoring without Stockfish dependency

---

## Setup

```bash
cd wolframite
pip install -r requirements.txt
python main.py
# or
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

API docs at: `http://localhost:8000/docs`

---

## Stack

- **FastAPI** — async web framework
- **python-chess** — FEN/PGN parsing, move generation, board evaluation
- **Pydantic** — request/response validation
- **uvicorn** — ASGI server
