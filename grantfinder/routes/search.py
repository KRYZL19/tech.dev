from flask import Blueprint, request, jsonify
from data.grant_index import search_grants

search_bp = Blueprint("search", __name__)

@search_bp.route("/search", methods=["GET"])
def search():
    q = request.args.get("q")
    agency = request.args.get("agency")
    deadline_within_days = request.args.get("deadline_within_days", type=int)
    limit = request.args.get("limit", type=int)
    
    if not q:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    results = search_grants(
        keyword=q,
        agency=agency,
        deadline_within_days=deadline_within_days,
        limit=limit
    )
    
    summaries = [{
        "grant_id": g["grant_id"],
        "title": g["title"],
        "agency": g["agency"],
        "award_amount_min": g["award_amount_min"],
        "award_amount_max": g["award_amount_max"],
        "application_deadline": g["application_deadline"],
        "sector": g["sector"]
    } for g in results]
    
    return jsonify({
        "query": q,
        "total_results": len(summaries),
        "grants": summaries
    })
