from flask import Flask, jsonify
from flask_cors import CORS
from routes.search import search_bp
from routes.eligibility import eligibility_bp
from data.grant_index import get_grant_by_id, get_grants_by_agency, get_summary

app = Flask(__name__)
CORS(app)

app.register_blueprint(search_bp, url_prefix="/api/v1")
app.register_blueprint(eligibility_bp, url_prefix="/api/v1")

@app.route("/api/v1/grant/<grant_id>", methods=["GET"])
def get_grant(grant_id):
    grant = get_grant_by_id(grant_id)
    if not grant:
        return jsonify({"error": "Grant not found"}), 404
    return jsonify(grant)

@app.route("/api/v1/agency/<agency_name>/grants", methods=["GET"])
def agency_grants(agency_name):
    grants = get_grants_by_agency(agency_name)
    return jsonify({
        "agency": agency_name.upper(),
        "total_grants": len(grants),
        "grants": [{
            "grant_id": g["grant_id"],
            "title": g["title"],
            "award_amount_min": g["award_amount_min"],
            "award_amount_max": g["award_amount_max"],
            "application_deadline": g["application_deadline"],
            "sector": g["sector"]
        } for g in grants]
    })

@app.route("/api/v1/summary", methods=["GET"])
def summary():
    return jsonify(get_summary())

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
