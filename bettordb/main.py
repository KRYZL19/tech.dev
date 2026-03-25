"""
BETTORDB API — Casino Probability & Simulation Engine
FastAPI backend for gambling probability data.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from routes.simulate import router as simulate_router
from routes.odds import router as odds_router
from routes.kelly import router as kelly_router
from models.schemas import BlackjackOddsResponse, RouletteOddsResponse
from games.blackjack import get_blackjack_odds
from games.roulette import get_roulette_odds
from games.baccarat import get_baccarat_odds


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("BETTORDB API starting up...")
    yield
    # Shutdown
    print("BETTORDB API shutting down...")


app = FastAPI(
    title="BETTORDB API",
    description="Casino Probability & Simulation Engine — for game developers and betting system researchers",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(simulate_router)
app.include_router(odds_router)
app.include_router(kelly_router)


@app.get("/api/v1/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "BETTORDB API",
        "version": "1.0.0",
    }


@app.get("/api/v1/game/blackjack/odds", response_model=BlackjackOddsResponse)
async def blackjack_odds(decks: int = 6, dealer_stands_on: int = 17):
    """
    Get blackjack odds for given deck count and dealer rule.
    """
    if decks < 1 or decks > 20:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Decks must be 1-20")
    if dealer_stands_on < 1 or dealer_stands_on > 21:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="dealer_stands_on must be 1-21")

    return get_blackjack_odds(decks=decks, dealer_stands_on=dealer_stands_on)


@app.get("/api/v1/game/roulette/odds", response_model=RouletteOddsResponse)
async def roulette_odds(variant: str = "european"):
    """
    Get roulette odds for American or European variant.
    """
    if variant.lower() not in ("american", "european"):
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="variant must be 'american' or 'european'")

    return get_roulette_odds(variant=variant.lower())


@app.get("/api/v1/game/baccarat/odds")
async def baccarat_odds(decks: int = 8):
    """Get baccarat odds for given number of decks."""
    if decks < 1 or decks > 20:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Decks must be 1-20")
    return get_baccarat_odds(decks=decks)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
