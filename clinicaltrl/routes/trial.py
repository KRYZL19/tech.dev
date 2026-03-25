from fastapi import APIRouter, HTTPException
from models.schemas import Trial
from data.trial_index import TRIAL_INDEX

router = APIRouter(prefix="/api/v1", tags=["trial"])

@router.get("/trial/{nct_id}", response_model=Trial)
def get_trial(nct_id: str):
    trial = TRIAL_INDEX.get(nct_id.upper())
    if not trial:
        trial = TRIAL_INDEX.get(nct_id)
    if not trial:
        raise HTTPException(status_code=404, detail="Trial not found")
    return trial
