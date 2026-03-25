"""
Simulation endpoints: slots and betting systems.
"""
from fastapi import APIRouter, HTTPException
from models.schemas import (
    SlotsSimRequest, SlotsSimResponse,
    BettingSystemRequest, BettingSystemResponse,
)
from games.slots import simulate_slots
from games.martingale import simulate_betting_system

router = APIRouter(prefix="/api/v1/simulate", tags=["simulation"])


@router.post("/slots", response_model=SlotsSimResponse)
async def simulate_slot_machine(req: SlotsSimRequest):
    """
    Simulate slot machine spins with weighted reel analysis.
    Returns house edge, RTP, expected loss, and confidence intervals.
    """
    if len(req.symbol_weights) < 2:
        raise HTTPException(status_code=400, detail="At least 2 symbols required")

    result = simulate_slots(
        spins=req.spins,
        paylines=req.paylines,
        symbol_weights=req.symbol_weights,
        reels=req.reels,
        symbol_values=req.symbol_values,
        bet_per_line=req.bet_per_line,
    )
    return result


@router.post("/betting-system", response_model=BettingSystemResponse)
async def simulate_betting(req: BettingSystemRequest):
    """
    Simulate betting systems (Martingale, Fibonacci, D'Alembert, Flat).
    Monte Carlo simulation of 10,000 sequences.
    """
    if req.win_probability <= 0 or req.win_probability >= 1:
        raise HTTPException(status_code=400, detail="win_probability must be between 0 and 1")

    result = simulate_betting_system(
        system=req.system,
        base_bet=req.base_bet,
        target_wins=req.target_wins,
        max_bets=req.max_bets,
        bankroll=req.bankroll,
        win_probability=req.win_probability,
        payout=req.payout,
        n_simulations=10_000,
    )
    return result
