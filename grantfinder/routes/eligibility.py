from flask import Blueprint, request, jsonify
from data.grant_index import check_eligibility

eligibility_bp = Blueprint("eligibility", __name__)

@eligibility_bp.route("/eligibility/check", methods=["POST"])
def eligibility_check():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body required"}), 400
    
    org_type = data.get("organization_type")
    annual_revenue = data.get("annual_revenue")
    employees = data.get("employees")
    sector = data.get("sector", [])
    
    if not org_type:
        return jsonify({"error": "organization_type is required"}), 400
    
    eligible_grants = check_eligibility(org_type, annual_revenue, employees, sector)
    
    return jsonify({
        "organization_type": org_type,
        "sectors": sector,
        "total_eligible": len(eligible_grants),
        "eligible_grants": eligible_grants
    })
