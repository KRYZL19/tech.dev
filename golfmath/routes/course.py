# routes/course.py
from fastapi import APIRouter, HTTPException
from models.schemas import (
    CourseResponse, HoleData,
    ScorecardRequest, ScorecardResponse, ScorecardStats
)
from data.course_data import get_course, COURSES

router = APIRouter(prefix="/api/v1", tags=["course"])


@router.get("/course/{course_name}", response_model=CourseResponse)
def get_course_info(course_name: str):
    """Get course data: par, rating, slope, hole-by-hole breakdown."""
    # Normalize: lowercase, replace spaces with hyphens
    course_id = course_name.lower().replace(" ", "-")

    # Try exact match first
    course = get_course(course_id)

    # Try partial match
    if not course:
        for cid, cdata in COURSES.items():
            if course_name.lower() in cdata["name"].lower() or course_name.lower() in cid:
                course = cdata
                break

    if not course:
        available = ", ".join(COURSES.keys())
        raise HTTPException(
            status_code=404,
            detail=f"Course '{course_name}' not found. Available: {available}"
        )

    return CourseResponse(
        course_id=course["course_id"],
        name=course["name"],
        location=course["location"],
        par=course["par"],
        rating=course["rating"],
        slope=course["slope"],
        holes=[HoleData(**h) for h in course["holes"]]
    )


@router.post("/round/scorecard", response_model=ScorecardResponse)
def submit_scorecard(req: ScorecardRequest):
    """Analyze a scorecard: score vs par, stats breakdown, Course Replay estimate."""
    course = get_course(req.course_id)
    if not course:
        raise HTTPException(status_code=404, detail=f"Course '{req.course_id}' not found")

    if len(req.strokes_per_hole) != 18 or len(req.putts_per_hole) != 18:
        raise HTTPException(status_code=400, detail="Must provide 18 holes of data")

    course_par = course["par"]
    total_strokes = sum(req.strokes_per_hole)
    total_putts = sum(req.putts_per_hole)
    score_vs_par = total_strokes - course_par

    fairways = sum(req.fairways_hit)
    gir_count = sum(req.gir)

    if score_vs_par > 0:
        score_breakdown = f"+{score_vs_par}"
    elif score_vs_par < 0:
        score_breakdown = str(score_vs_par)
    else:
        score_breakdown = "E"

    # Score vs par by hole
    hole_by_hole = []
    running_total = 0
    for i, h in enumerate(course["holes"]):
        diff = req.strokes_per_hole[i] - h["par"]
        running_total += diff
        prefix = "+" if running_total > 0 else "" if running_total < 0 else "E"
        hole_by_hole.append(f"H{i+1}: {req.strokes_per_hole[i]} ({prefix}{running_total})")

    # GIR putts
    avg_putts_gir = None
    if gir_count > 0:
        gir_putts = [req.putts_per_hole[i] for i in range(18) if req.gir[i]]
        if gir_putts:
            avg_putts_gir = round(sum(gir_putts) / len(gir_putts), 1)

    # Course Replay estimate: fictional "stress score" based on bogey+ rate
    bogey_plus = 0
    for i, strokes in enumerate(req.strokes_per_hole):
        h_par = course["holes"][i]["par"]
        if strokes >= h_par + 2:
            bogey_plus += 1

    bogey_rate = bogey_plus / 18
    if bogey_rate < 0.1:
        replay = "🔥 Would definitely replay — elite round"
    elif bogey_rate < 0.25:
        replay = "👍 Solid round, worth a replay"
    elif bogey_rate < 0.4:
        replay = "😐 Mixed bag, maybe worth another look"
    else:
        replay = "💀 Hard pass on the replay"

    stats = ScorecardStats(
        total_strokes=total_strokes,
        total_putts=total_putts,
        fairways_hit=fairways,
        gir=gir_count,
        gir_percentage=round(gir_count / 18 * 100, 1),
        avg_putts_per_gir=avg_putts_gir
    )

    return ScorecardResponse(
        course_id=req.course_id,
        course_name=course["name"],
        score_vs_par=score_vs_par,
        score_breakdown=score_breakdown,
        stats=stats,
        course_replay_estimate=replay
    )
