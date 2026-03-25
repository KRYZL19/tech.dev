"""SAWMILL — Lumber Cut Optimizer API.

Hook: "12 boards, cut list, yield 94%, waste $23. This is the math."
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import routes.cut as cut
import routes.yield_est as yield_route
import routes.board as board
import routes.price as price

app = FastAPI(
    title="SAWMILL",
    description="Lumber Cut Optimizer — maximize yield, minimize waste, get the math right.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(cut.router, prefix="/api/v1")
app.include_router(yield_route.router, prefix="/api/v1")
app.include_router(board.router, prefix="/api/v1")
app.include_router(price.router, prefix="/api/v1")


@app.get("/", tags=["health"])
def root():
    return {
        "name": "SAWMILL",
        "tagline": "12 boards, cut list, yield 94%, waste $23. This is the math.",
        "version": "1.0.0",
    }


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8765, reload=True)
