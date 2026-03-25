from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.simulate import router as simulate_router
from routes.odds import router as odds_router
from routes.kelly import router as kelly_router
from games.blackjack import calculate_blackjack_odds
from games.roulette import calculate_roulette_odds
from models.schemas import BlackjackOddsResponse, RouletteOddsResponse

app = FastAPI(
    title="BETTORDB",
    version="1.0.0",
    description="Casino Probability Engine — The math proves the martingale always loses. Now prove it to your users."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simulate_router)
app.include_router(odds_router)
app.include_router(kelly_router)


@app.get("/api/v1/health")
async def health():
    return {"status": "ok", "service": "BETTORDB", "tagline": "The math proves the martingale always loses."}


@app.get("/api/v1/game/blackjack/odds", response_model=BlackjackOddsResponse)
async def blackjack_odds(decks: int = 6):
    result = calculate_blackjack_odds(decks)
    return BlackjackOddsResponse(**result)


@app.get("/api/v1/game/roulette/odds", response_model=RouletteOddsResponse)
async def roulette_odds(variant: str = "european"):
    result = calculate_roulette_odds(variant)
    return RouletteOddsResponse(**result)
