# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import handicap, course, weather

app = FastAPI(
    title="GOLFMATH API",
    description="Your handicap index doesn't account for wind. The USGA formula is 30 years old. Here's something that actually adjusts for conditions.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(handicap.router)
app.include_router(course.router)
app.include_router(weather.router)


@app.get("/")
def root():
    return {
        "name": "GOLFMATH API",
        "tagline": "Your handicap index doesn't account for wind. The USGA formula is 30 years old. Here's something that actually adjusts for conditions.",
        "version": "1.0.0",
        "pricing": {
            "free": "50 calls/day",
            "dev": "$14/month",
            "pro": "$39/month"
        },
        "docs": "/docs",
        "endpoints": [
            "POST /api/v1/handicap/calculate",
            "GET /api/v1/course/{course_name}",
            "POST /api/v1/round/scorecard",
            "POST /api/v1/weather/adjust"
        ],
        "courses": [
            "augusta-national",
            "pebble-beach",
            "st-andrews",
            "torrey-pines",
            "bethpage-black",
            "whistling-straits",
            "kiawah-island",
            "pinehurst-no2"
        ]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
