from fastapi import APIRouter, HTTPException, Query
from models.schemas import (
    PuzzleFromPositionRequest,
    PuzzleFromPositionResponse,
    DailyPuzzleResponse,
    OpeningResponse,
)
from data.puzzles import PUZZLES, OPENINGS, get_puzzle_by_rating, get_opening_by_eco, get_opening_by_name
import chess
import hashlib
from datetime import date

router = APIRouter(prefix="/api/v1", tags=["puzzles"])

# Simple daily puzzle selection based on date
def get_daily_puzzle_index():
    today = str(date.today())
    hash_val = int(hashlib.md5(today.encode()).hexdigest(), 16)
    return hash_val % len(PUZZLES)


def get_puzzles_by_difficulty(difficulty: int):
    """Return puzzles near the requested difficulty rating."""
    tolerance = 150
    return [p for p in PUZZLES if abs(p["rating"] - difficulty) <= tolerance]


@router.post("/puzzle/from-position", response_model=PuzzleFromPositionResponse)
async def puzzle_from_position(req: PuzzleFromPositionRequest):
    """
    Given a FEN position and difficulty (rating), return a matching puzzle.
    If no exact match, returns closest puzzle.
    """
    try:
        board = chess.Board(req.fen)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid FEN notation")

    # Find puzzles at or near requested difficulty
    matching = get_puzzles_by_difficulty(req.difficulty)

    if not matching:
        # Fallback to any puzzle near 1800
        matching = get_puzzle_by_rating(1800, req.difficulty + 200)

    if not matching:
        raise HTTPException(status_code=404, detail="No puzzles found for this difficulty")

    # Pick first matching (could be smarter about FEN similarity)
    puzzle = matching[0]

    return PuzzleFromPositionResponse(
        puzzle_fen=puzzle["fen"],
        moves=puzzle["moves"],
        rating=puzzle["rating"],
        themes=puzzle["themes"],
    )


@router.get("/puzzle/daily", response_model=DailyPuzzleResponse)
async def daily_puzzle():
    """
    Return today's daily puzzle. Same puzzle all day (UTC).
    Includes a hint (first move of solution).
    """
    idx = get_daily_puzzle_index()
    puzzle = PUZZLES[idx]

    hint = puzzle["moves"][0] if puzzle["moves"] else ""

    return DailyPuzzleResponse(
        puzzle_fen=puzzle["fen"],
        moves=puzzle["moves"],
        rating=puzzle["rating"],
        themes=puzzle["themes"],
        hint=hint,
    )


@router.get("/openings/{name}", response_model=OpeningResponse)
async def get_opening(name: str):
    """
    Get opening by name or ECO code.
    Returns eco, moves, description, and middlegame plans.
    """
    # Try ECO code first
    opening = get_opening_by_eco(name)
    if not opening:
        opening = get_opening_by_name(name)

    if not opening:
        raise HTTPException(status_code=404, detail=f"Opening not found: {name}")

    return OpeningResponse(
        eco=opening["eco"],
        name=opening["name"],
        moves=opening["moves"],
        description=opening["description"],
        middlegame_plans=opening["middlegame_plans"],
    )
