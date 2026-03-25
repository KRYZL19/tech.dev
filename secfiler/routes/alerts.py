from fastapi import APIRouter, HTTPException
from models.schemas import AlertCreateRequest, AlertResponse
import uuid
from datetime import datetime, timezone

router = APIRouter(prefix="/api/v1/alerts", tags=["alerts"])

# In-memory store for demo; swap for DB in production
_alerts: dict[str, AlertCreateRequest] = {}


@router.post("/create", response_model=AlertResponse)
def create_alert(req: AlertCreateRequest):
    alert_id = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()

    # Store for later matching
    _alerts[alert_id] = req

    return AlertResponse(
        alert_id=alert_id,
        keywords=req.keywords,
        form_types=req.form_types,
        sector=req.sector,
        description=req.description or f"Alert for {', '.join(req.keywords) if req.keywords else 'all filings'}",
        created_at=now,
    )


@router.get("/check/{alert_id}")
def check_alert(alert_id: str):
    """Check which current filings match a given alert criteria."""
    if alert_id not in _alerts:
        raise HTTPException(status_code=404, detail="Alert not found")
    req = _alerts[alert_id]

    from data.filing_index import FILINGS

    matches = []
    for f in FILINGS:
        # Match form types
        if req.form_types and f.form_type not in req.form_types:
            continue
        # Match sector
        if req.sector and f.sector != req.sector:
            continue
        # Match keywords
        if req.keywords:
            text = f"{f.description} {f.company_name} {f.ticker}".lower()
            if not any(kw.lower() in text for kw in req.keywords):
                continue
        matches.append(f)

    return {
        "alert_id": alert_id,
        "match_count": len(matches),
        "matches": matches,
    }
