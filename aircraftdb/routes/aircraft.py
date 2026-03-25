from flask import Blueprint, jsonify, request
from datetime import date
from data.aircraft_index import get_aircraft_by_n_number, get_aircraft_by_manufacturer
from models.schemas import (
    AircraftResponse,
    AircraftHistoryResponse,
    OwnerRecord,
    UsefulLoadResponse,
    ManufacturerResponse,
    AircraftBase,
)

aircraft_bp = Blueprint("aircraft", __name__, url_prefix="/api/v1/aircraft")
registry_bp = Blueprint("registry", __name__, url_prefix="/api/v1/registry")
mfr_bp = Blueprint("manufacturer", __name__, url_prefix="/api/v1/manufacturer")


@aircraft_bp.route("/<n_number>", methods=["GET"])
def get_aircraft(n_number: str):
    ac = get_aircraft_by_n_number(n_number)
    if not ac:
        return jsonify({"error": "Aircraft not found", "n_number": n_number}), 404

    return jsonify({
        "n_number": ac["n_number"],
        "serial_number": ac["serial_number"],
        "year": ac["year"],
        "make": ac["make"],
        "model": ac["model"],
        "engine_make": ac["engine_make"],
        "engine_model": ac["engine_model"],
        "engine_hp": ac["engine_hp"],
        "number_of_seats": ac["number_of_seats"],
        "number_of_engines": ac["number_of_engines"],
        "empty_weight": ac["empty_weight"],
        "gross_weight": ac["gross_weight"],
        "certificate": ac["certificate"],
        "status": ac["status"],
        "type_engine": ac["type_engine"],
        "category": ac["category"],
        "owner_name": ac["owner_name"],
        "owner_city": ac["owner_city"],
        "owner_state": ac["owner_state"],
        "registration_expires": ac["registration_expires"],
    })


@aircraft_bp.route("/<n_number>/history", methods=["GET"])
def get_history(n_number: str):
    ac = get_aircraft_by_n_number(n_number)
    if not ac:
        return jsonify({"error": "Aircraft not found", "n_number": n_number}), 404

    current_owner = {
        "owner_name": ac["owner_name"],
        "owner_city": ac["owner_city"],
        "owner_state": ac["owner_state"],
        "registration_issued": ac["registration_issued"],
        "registration_expires": ac["registration_expires"],
        "cancellation_date": None,
    }

    return jsonify({
        "n_number": ac["n_number"],
        "current_owner": current_owner,
        "owner_history": ac.get("owner_history", []),
    })


@aircraft_bp.route("/useful-load", methods=["POST"])
def calc_useful_load():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body required"}), 400

    n_number = data.get("n_number", "")
    pilot_weight = float(data.get("pilot_weight", 0))
    passengers = float(data.get("passengers", 0))
    baggage = float(data.get("baggage", 0))
    fuel_gallons = float(data.get("fuel_gallons", 0))

    ac = get_aircraft_by_n_number(n_number)
    if not ac:
        return jsonify({"error": "Aircraft not found", "n_number": n_number}), 404

    empty = ac["empty_weight"]
    gross = ac["gross_weight"]
    max_useful = gross - empty
    fuel_weight = fuel_gallons * 6.0
    payload_used = pilot_weight + passengers + baggage
    payload_remaining = max_useful - payload_used - fuel_weight
    useful_available = max(0.0, payload_remaining)
    within = payload_used + fuel_weight <= max_useful

    return jsonify({
        "n_number": ac["n_number"],
        "empty_weight": empty,
        "gross_weight": gross,
        "max_useful_load": max_useful,
        "fuel_weight": fuel_weight,
        "payload_used": payload_used,
        "payload_remaining": round(payload_remaining, 2),
        "useful_load_available": round(useful_available, 2),
        "within_limits": within,
    })


@registry_bp.route("/expiring", methods=["GET"])
def get_expiring():
    from data.aircraft_index import get_expiring as _get_expiring
    days = request.args.get("days", 90, type=int)
    results = _get_expiring(days)
    return jsonify({
        "count": len(results),
        "days": days,
        "aircraft": [
            {
                "n_number": ac["n_number"],
                "owner_name": ac["owner_name"],
                "owner_city": ac["owner_city"],
                "owner_state": ac["owner_state"],
                "expires": ac["registration_expires"],
                "days_remaining": ac["days_to_expire"],
                "make": ac["make"],
                "model": ac["model"],
            }
            for ac in sorted(results, key=lambda x: x["days_to_expire"])
        ],
    })


@mfr_bp.route("/<mfr>", methods=["GET"])
def get_by_manufacturer(mfr: str):
    results = get_aircraft_by_manufacturer(mfr)
    aircraft_list = [
        {
            "n_number": ac["n_number"],
            "serial_number": ac["serial_number"],
            "year": ac["year"],
            "make": ac["make"],
            "model": ac["model"],
            "engine_hp": ac["engine_hp"],
            "number_of_seats": ac["number_of_seats"],
        }
        for ac in results
    ]
    return jsonify({
        "manufacturer": mfr.upper(),
        "aircraft": aircraft_list,
        "total_count": len(aircraft_list),
    })
