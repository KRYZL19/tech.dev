# routes/handicap.py
from fastapi import APIRouter
from models.schemas import HandicapCalculateRequest, HandicapCalculateResponse, RoundDifferential
import math

router = APIRouter(prefix="/api/v1/handicap", tags=["handicap"])


def calc_differential(score: int, course_rating: float, slope_rating: int) -> float:
    """USGA Course Differential: (Score - Course Rating) × 113 / Slope Rating"""
    return (score - course_rating) * 113 / slope_rating


@router.post("/calculate", response_model=HandicapCalculateResponse)
def calculate_handicap(req: HandicapCalculateRequest):
    """
    Calculate handicap index from recent scores.
    Uses USGA formula with best-8-of-20 differential averaging.
    """
    n = len(req.scores)
    if n == 0:
        return HandicapCalculateResponse(
            handicap_index=0.0,
            differentials=[],
            best_8_differential=0.0,
            rounds_used=0
        )

    diffs = []
    for i in range(n):
        d = calc_differential(req.scores[i], req.course_ratings[i], req.slope_ratings[i])
        diffs.append(RoundDifferential(
            round=i + 1,
            score=req.scores[i],
            course_rating=req.course_ratings[i],
            slope_rating=req.slope_ratings[i],
            differential=round(d, 2)
        ))

    # Use all available differentials (min 3 for provisional)
    diffs_sorted = sorted(diffs, key=lambda x: x.differential)

    # Table for handicap calculation (number of rounds → number to use)
    if n == 1:
        used = 1
    elif n == 2:
        used = 2
    elif n == 3:
        used = 3
    elif n == 4:
        used = 4
    elif n == 5:
        used = 5
    elif n == 6:
        used = 6
    elif n == 7:
        used = 8
    elif n == 8:
        used = 8
    elif n == 9:
        used = 9
    elif n == 10:
        used = 10
    elif n == 11:
        used = 11
    elif n == 12:
        used = 12
    elif n == 13:
        used = 13
    elif n == 14:
        used = 14
    elif n == 15:
        used = 15
    elif n == 16:
        used = 16
    elif n == 17:
        used = 17
    else:  # 18+
        used = 20

    used_diffs = diffs_sorted[:min(used, n)]
    avg_diff = sum(d.differential for d in used_diffs) / len(used_diffs)

    # Handicap index = average × 0.96 (USGA constant)
    handicap_index = round(avg_diff * 0.96, 1)
    # Cap at 54.0
    handicap_index = min(handicap_index, 54.0)

    best_8_avg = 0.0
    if n >= 8:
        best_8 = diffs_sorted[:8]
        best_8_avg = round(sum(d.differential for d in best_8) / 8 * 0.96, 1)

    return HandicapCalculateResponse(
        handicap_index=handicap_index,
        differentials=diffs,
        best_8_differential=best_8_avg,
        rounds_used=n
    )
