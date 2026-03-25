from fastapi import APIRouter
from models.schemas import OddsConvertRequest, OddsConvertResponse

router = APIRouter(prefix="/api/v1/odds", tags=["odds"])


def decimal_to_fractional(d: float) -> float:
    return round((d - 1), 2)


def decimal_to_american(d: float) -> float:
    if d >= 2.0:
        return round((d - 1) * 100, 2)
    else:
        return round(-100 / (d - 1), 2)


def decimal_to_implied(d: float) -> float:
    return round(1 / d, 6)


def american_to_decimal(a: float) -> float:
    if a >= 0:
        return round(a / 100 + 1, 4)
    else:
        return round(100 / (-a) + 1, 4)


def fractional_to_decimal(f: float) -> float:
    return round(f + 1, 4)


def implied_to_decimal(p: float) -> float:
    return round(1 / p, 4)


@router.post("/convert", response_model=OddsConvertResponse)
async def convert_odds(req: OddsConvertRequest):
    # Convert whichever is provided to all formats
    if req.decimal_odds is not None:
        d = req.decimal_odds
    elif req.fractional_odds is not None:
        d = fractional_to_decimal(req.fractional_odds)
    elif req.american_odds is not None:
        d = american_to_decimal(req.american_odds)
    elif req.implied_probability is not None:
        d = implied_to_decimal(req.implied_probability)
    else:
        d = 2.0

    f = decimal_to_fractional(d)
    a = decimal_to_american(d)
    imp = decimal_to_implied(d)

    return OddsConvertResponse(
        decimal=round(d, 4),
        fractional=round(f, 2),
        american=round(a, 2),
        implied_probability=round(imp, 6)
    )
