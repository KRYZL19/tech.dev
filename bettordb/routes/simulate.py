from fastapi import APIRouter
from models.schemas import SlotsSimulateRequest, SlotsSimulateResponse, BettingSystemRequest, BettingSystemResponse
from games.slots import simulate_slots
from games.martingale import simulate_betting_system

router = APIRouter(prefix="/api/v1/simulate", tags=["simulate"])


@router.post("/slots", response_model=SlotsSimulateResponse)
async def simulate_slots_endpoint(req: SlotsSimulateRequest):
    result = simulate_slots(
        spins=req.spins,
        paylines=req.paylines,
        symbol_weights=req.symbol_weights,
        reels=req.reels,
        bet_per_line=req.bet_per_line
    )
    return SlotsSimulateResponse(**result)


@router.post("/betting-system", response_model=BettingSystemResponse)
async def simulate_betting_system_endpoint(req: BettingSystemRequest):
    result = simulate_betting_system(
        system=req.system,
        base_bet=req.base_bet,
        target_wins=req.target_wins,
        max_bets=req.max_bets,
        bankroll=req.bankroll,
        win_probability=req.win_probability,
        n_simulations=10000
    )
    return BettingSystemResponse(**result)
