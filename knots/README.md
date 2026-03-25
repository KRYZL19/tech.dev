# KNOTDB — Nautical Knot Reference API

**50 knots with load ratings. Bowline vs cleat vs rolling hitch — know the difference before you need it.**

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

API runs at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

## Endpoints

### List All Knots
```
GET /api/v1/knots
```
Returns all 50 knots with name, category, difficulty (1-5), strength %, and use cases.

### Knot Details
```
GET /api/v1/knot/{name}
```
Full details including:
- `how_to_tie_steps[]` — Step-by-step instructions
- `breaking_strength_lbs` — Breaking strength in pounds
- `proper_use` — When to use this knot
- `when_not_to_use` — Limitations and dangers
- `related_knots[]` — Similar alternatives

### Filter by Category
```
GET /api/v1/knots/category/{category}
```
Categories: `bending`, `binding`, `loop`, `stopper`, `slip`, `hitch`

### Search by Use Case
```
GET /api/v1/knots/search?use_case={query}
```
Find knots for: anchoring, mooring, towing, rescue, fishing, climbing

### Compare Knots Under Load
```
POST /api/v1/load/compare
{
  "knot1_name": "Bowline",
  "knot2_name": "Clove Hitch",
  "load_lbs": 500
}
```
Returns safety factors, failure modes, and recommendations.

### Load Capacity
```
GET /api/v1/load/calculate/{knot_name}
```
Returns breaking strength, safe working load, and strength percentage.

## Example Usage

```bash
# List all knots
curl http://localhost:8000/api/v1/knots

# Get Bowline details
curl http://localhost:8000/api/v1/knot/Bowline

# Compare Bowline vs Clove Hitch at 500lb load
curl -X POST http://localhost:8000/api/v1/load/compare \
  -H "Content-Type: application/json" \
  -d '{"knot1_name":"Bowline","knot2_name":"Clove Hitch","load_lbs":500}'

# Find knots for mooring
curl "http://localhost:8000/api/v1/knots/search?use_case=mooring"
```

## Included Knots (50 total)

**Loops:** Bowline, Double Bowline, Eye Splice, Figure Eight Loop, Flemish Loop, Lariat, Osman, Perfect, Simple Simon, Skene, Sling, Student, Surrey

**Bends:** Sheet Bend, Trucker's Hitch, Carrick Bend, Counterpart, Diagonal Bend, Fisherman's Knot, Blood Knot, Ring Bend, Anchor Bend, Ashley Bend, Zeppelin Bend, Magnusson, Jesuit's Bend, Water, Ring Bend Alt

**Hitches:** Clove Hitch, Rolling Hitch, Taut-Line Hitch, Anchor Bend, Munter Hitch, Prusik, Blackwall Hitch, Cat's Paw, Highwayman's Hitch, Midshipman's, Tarbuck, Timber, Killick, Palm, Slippery

**Binding:** Constrictor, Strangle, Grain Bind, Packer's Bend, Seize, Barrel Hitch, Needle Yarn

**Stoppers:** Figure Eight, Overhand, Stevedore, Pile

## Pricing

| Tier | Price | Requests/Day |
|------|-------|---------------|
| Free | $0 | 100 |
| Dev | $9/mo | 10,000 |
| Pro | $29/mo | Unlimited |

Rate limits applied via `X-RateLimit-*` headers.

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run server with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Run tests (when added)
pytest
```

## License

MIT License
