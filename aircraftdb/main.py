from flask import Flask
from flask_cors import CORS
from routes.aircraft import aircraft_bp, registry_bp, mfr_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(aircraft_bp)
app.register_blueprint(registry_bp)
app.register_blueprint(mfr_bp)


@app.get("/")
def index():
    return {
        "name": "AIRCRAFTDB",
        "tagline": "N-number lookup before you buy.",
        "hook": "Airworthiness status, useful load, owner history.",
        "version": "1.0.0",
        "endpoints": [
            "GET  /api/v1/aircraft/{n_number}",
            "GET  /api/v1/aircraft/{n_number}/history",
            "POST /api/v1/aircraft/useful-load",
            "GET  /api/v1/registry/expiring?days={n}",
            "GET  /api/v1/manufacturer/{mfr}",
        ],
    }


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
