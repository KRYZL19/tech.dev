"""
Odds conversion endpoints.
Converts between decimal, fractional, American, and implied probability formats.
"""
from fastapi import APIRouter
from models.schemas import OddsConvertRequest, OddsConvertResponse

router = APIRouter(prefix="/api/v1/odds", tags=["odds"])


@router.post("/convert", response_model=OddsConvertResponse)
async def convert_odds(req: OddsConvertRequest):
    """
    Convert odds between decimal, fractional, American (moneyline), and implied probability.

    Formats:
    - decimal: e.g. 2.50 (return on 1 unit stake)
    - fractional: e.g. "3/2" (profit/stake)
    - american: e.g. +150 or -200 (moneyline)
    - implied: e.g. 0.40 or 40.0 (probability as decimal or percent)
    """
    # First convert to decimal
    decimal = _to_decimal(req.value, req.from_format)

    # Then convert to all formats
    fractional = _decimal_to_fractional(decimal)
    american = _decimal_to_american(decimal)
    implied = 1 / decimal if decimal > 0 else 0

    return OddsConvertResponse(
        decimal=round(decimal, 4),
        fractional=fractional,
        american=american,
        implied_percent=round(implied * 100, 4),
    )


def _to_decimal(value: float, fmt: str) -> float:
    """Convert any format to decimal."""
    if fmt == "decimal":
        return value
    elif fmt == "fractional":
        # value is string like "3/2" or float like 1.5
        if isinstance(value, str) and "/" in value:
            num, den = value.split("/")
            return float(num) / float(den) + 1
        return float(value) + 1
    elif fmt == "american":
        if value > 0:
            return value / 100 + 1
        else:
            return 100 / abs(value) + 1
    elif fmt == "implied":
        if value > 1:
            # Already a percentage (e.g. 40 = 40%)
            value = value / 100
        return 1 / value if value > 0 else 0
    return value


def _decimal_to_fractional(decimal: float) -> str:
    """Convert decimal to fractional string."""
    if decimal <= 1:
        return "0/1"

    # Find best rational approximation with denominator up to 100
    profit = decimal - 1
    for d in range(1, 101):
        n = round(profit * d)
        if abs(n / d - profit) < 0.01:
            return f"{n}/{d}"

    # Fallback: use decimal representation
    return f"{round(profit, 2)}/1"


def _decimal_to_american(decimal: float) -> int:
    """Convert decimal to American (moneyline) odds."""
    if decimal == 1:
        return 0
    if decimal >= 2:
        # Positive odds: (decimal - 1) * 100
        return int(round((decimal - 1) * 100))
    else:
        # Negative odds: -100 / (decimal - 1)
        return int(round(-100 / (decimal - 1)))
