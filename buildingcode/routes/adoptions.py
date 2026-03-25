from fastapi import APIRouter, HTTPException
from models.schemas import AdoptionResponse, StateCodeResponse
from data.code_adoptions import CODE_ADOPTIONS, STATE_CODES

router = APIRouter(prefix="/api/v1", tags=["adoptions"])


@router.get("/adoption/{state}/{city}", response_model=AdoptionResponse)
def get_adoption(state: str, city: str):
    """Get code adoption info for a specific city."""
    state_upper = state.upper()
    city_title = city.title()

    if state_upper not in CODE_ADOPTIONS:
        raise HTTPException(status_code=404, detail=f"State '{state}' not in database. States covered: {list(CODE_ADOPTIONS.keys())}")

    if city_title not in CODE_ADOPTIONS[state_upper]:
        available = list(CODE_ADOPTIONS[state_upper].keys())
        raise HTTPException(status_code=404, detail=f"City '{city}' not found in {state_upper}. Available cities: {available}")

    data = CODE_ADOPTIONS[state_upper][city_title]
    return AdoptionResponse(
        city=city_title,
        state=state_upper,
        ibc_version=data["ibc_version"],
        irc_version=data["irc_version"],
        nec_version=data["nec_version"],
        effective_date=data["effective_date"],
        amendments=data["amendments"],
        local_amendments=data["local_amendments"],
    )


@router.get("/state/{state}/codes", response_model=StateCodeResponse)
def get_state_codes(state: str):
    """Get the codes adopted by a state."""
    state_upper = state.upper()

    if state_upper not in STATE_CODES:
        raise HTTPException(status_code=404, detail=f"State '{state}' not found.")

    data = STATE_CODES[state_upper]
    city_count = len(CODE_ADOPTIONS.get(state_upper, {}))
    return StateCodeResponse(
        state=state_upper,
        codes_adopted=data["code"],
        adoption_date=data["adopted"],
        cities_covered=city_count,
    )
