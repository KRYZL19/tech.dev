from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import math

app = FastAPI(title="GOLFMATH", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

def calc_handicap(scores: list[int], course_par: int = 72) -> dict:
    """USGA handicap index calculation from 20 most recent scores."""
    if len(scores) < 3:
        return {"error": "need at least 3 rounds", "have": len(scores)}
    # Differential = (Adjusted Gross Score - Course Rating) × 113 / Slope Rating
    # Use fixed slope=113 for simplicity (USGA average)
    differentials = [(max(score, course_par - 10) - course_par) * 113 / 113 for score in scores[-20:]]
    differentials.sort()
    used = differentials[:min(3 if len(differentials) < 5 else 5 if len(differentials) < 9 else 8, len(differentials))]
    avg_diff = sum(used) / len(used)
    handicap = avg_diff * 0.96  # .96 is the "bonus for excellence"
    return {
        "rounds_used": len(used),
        "differentials_used": [round(d, 1) for d in used],
        "handicap_index": round(handicap, 1),
        "course_handicap": round(handicap * 1.0, 0),  # at scratch level
        "interpretation": f"scratch player or +{handicap:.0f}" if handicap <= 0 else f"{handicap:.0f}-handicap",
    }

@app.get("/")
def read_root():
    return {"golfmath": "golf handicap API", "endpoints": ["/handicap", "/course-handicap"]}

@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/api/v1/handicap")
def handicap(scores: str, course_par: int = 72):
    """scores as comma-separated ints, e.g. 82,78,88,76,90"""
    try:
        score_list = [int(s.strip()) for s in scores.split(",")]
    except:
        return {"error": "invalid scores format"}
    return calc_handicap(score_list, course_par)
