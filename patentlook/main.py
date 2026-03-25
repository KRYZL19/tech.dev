from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PATENTLOOK", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

PATENTS = [
    {"patent_num": "US10123456B2", "title": "Neural network training with dynamic learning rate scheduling", "assignee": "OpenAI", "filed": "2021-03-15", "granted": "2023-09-12", "inventors": ["Sam Altman", "Ilya Sutskever"], "cpc": "G06N3/08", "abstract": "A method for training neural networks using adaptive learning rates based on gradient variance."},
    {"patent_num": "US9876543A1", "title": "Lattice-based cryptographic key encapsulation mechanism", "assignee": "Cloudflare", "filed": "2020-07-22", "granted": "2022-02-08", "inventors": ["Matthew Prince"], "cpc": "H04L9/30", "abstract": "A method for quantum-resistant key exchange using CRYSTALS-Kyber."},
    {"patent_num": "US11234567C1", "title": "Autonomous vehicle path planning using reinforcement learning", "assignee": "Waymo", "filed": "2019-11-30", "granted": "2021-06-15", "inventors": ["Dmitri Dolgov"], "cpc": "B60W60/00", "abstract": "A system for real-time path planning in autonomous vehicles using model-free RL."},
    {"patent_num": "US9981234D1", "title": "Attention mechanism with linear complexity for long sequences", "assignee": "Carnegie Mellon", "filed": "2022-01-10", "granted": None, "inventors": ["Taco Cohen"], "cpc": "G06N3/02", "abstract": "A linear attention mechanism achieving O(n) complexity for sequence modeling."},
]

@app.get("/")
def read_root(): return {"patentlook": "patent search API", "endpoints": ["/patent/{num}", "/search"]}
@app.get("/health")
def health(): return {"status": "ok", "version": "1.0.0"}
@app.get("/api/v1/patent/{patent_num}")
def patent(patent_num: str):
    for p in PATENTS:
        if p["patent_num"] == patent_num: return p
    return {"error": "patent not found", "available": [p["patent_num"] for p in PATENTS]}
@app.get("/api/v1/search")
def search(q: str = None, cpc: str = None, assignee: str = None):
    r = PATENTS
    if q: r = [p for p in r if q.lower() in p["title"].lower() or q.lower() in p.get("abstract","").lower()]
    if cpc: r = [p for p in r if p["cpc"].startswith(cpc)]
    if assignee: r = [p for p in r if assignee.lower() in p["assignee"].lower()]
    return {"count": len(r), "patents": r}
