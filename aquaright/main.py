from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import chemistry, cycling

app = FastAPI(
    title="AQUARIGHT API",
    description="## Aquarium Water Chemistry Manager\n\n**The Nitrogen Cycle Explained:**\n\nThe nitrogen cycle is the biological process that converts toxic ammonia (from fish waste) into less harmful substances. **It takes 2-6 weeks to establish.**\n\n1. **Ammonia Spike** (Days 1-14): Fish waste produces ammonia. This is NORMAL and signals that beneficial bacteria are beginning to colonize your filter.\n\n2. **Nitrite Spike** (Days 7-21): Ammonia-oxidizing bacteria convert ammonia to nitrite. Nitrite is still toxic - this is the most dangerous phase for fish.\n\n3. **Nitrate Rise** (Days 14-42): Nitrite-oxidizing bacteria establish and convert nitrite to nitrate. Both ammonia and nitrite should be near zero.\n\n4. **Cycled Tank**: Your filter can now instantly process ammonia and nitrite. Only relatively harmless nitrate remains.\n\n---\n\n### Pricing Tiers\n| Tier | Calls/Day | Price |\n|------|-----------|-------|\n| Free | 100 | $0 |\n| Dev | Unlimited | $9/mo |\n| Pro | Unlimited + Priority | $29/mo |\n\n### The Beginner Problem\nMost beginners give up on day 3 because they don't understand why their ammonia keeps spiking. **This is supposed to happen.** The spike means your tank is becoming a healthy ecosystem. Stay patient, don't add fish, and trust the process.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chemistry.router)
app.include_router(cycling.router)

@app.get("/", tags=["health"])
async def root():
    return {
        "service": "AQUARIGHT API",
        "version": "1.0.0",
        "status": "operational",
        "tagline": "The Nitrogen Cycle takes 2-6 weeks. Stay patient. Trust the process."
    }

@app.get("/health", tags=["health"])
async def health():
    return {"status": "healthy"}
