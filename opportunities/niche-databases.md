# Niche Database APIs — Legal Public Data
*Built: 2026-03-25*

---

## The Moat
Scraping + structuring public data = a database that would take months to build manually. The database IS the product. Other people can't recreate it quickly.

**Key rules:**
- Data must be public domain or public sector (government data = legal)
- No personal data, no scraping private sites
- No PII, no scraping behind auth walls
- Use official APIs and public datasets where possible
- Attribution where required by source

---

## Database APIs to Build

### 1. PATENTLOOK — US Patent Database Lookup
**Data source:** USPTO Bulk Data (public), Google Patents API
**Hook:** "Search 50 years of US patents by technical claim, not just keyword."
**What:** Full-text claim search, inventor lookup, assignee history, filing status, examiner data
**Revenue:** $29-99/month — researchers, inventors, lawyers

### 2. VESSELFIND — Boat & Ship Registration Database
**Data source:** USCG Vessel Documentation Portal (public), state DMV boat registration
**Hook:** "That boat has three owners and a lien against it. One API call tells you before you buy."
**What:** USCG documentation lookup, vessel specifications, owner history, encumbrance check, state registration cross-reference
**Revenue:** $19-59/month — boat dealers, brokers, insurance, buyers

### 3. FCCLOOKUP — FCC Licensee & Equipment Database
**Data source:** FCC Universal Licensing System (ULS) public data, Equipment Authorization database
**Hook:** "Ham radio license in 10 seconds. Amateur band allocation chart. Equipment certification lookup."
**What:** Callsign lookup, license class, FRN search, equipment type acceptance (TCB), interference lookup
**Revenue:** $9-29/month — ham radio operators, equipment installers, hobbyists

### 4. AIRCRAFTDB — FAA Aircraft Registry
**Data source:** FAA Civil Aviation Registry (public download)
**Hook:** "N-number lookup before you buy. Lien check, airworthiness status, useful load calculation."
**What:** N-number search, owner history, accident/incident cross-reference, airworthiness status, useful load computation
**Revenue:** $19-49/month — aircraft buyers, brokers, mechanics, insurance

### 5. COURTCLERK — Federal Court Docket Aggregator
**Data source:** PACER (public after 90 days), CourtListener/RECAP API
**Hook:** "Search every federal court case by attorney name, without PACER's UI."
**What:** Docket search, attorney appearance history, case outcome by judge, filing pattern analysis
**Revenue:** $49-199/month — attorneys, journalists, investigators, compliance

### 6. HOMICIDEWATCH — US Criminal Court Case Database
**Data source:** State court public records, CourtListener
**Hook:** "Search criminal cases by charge, county, and outcome. Where your local DA actually prosecutes."
**What:** Case outcomes by charge type, county-level conviction rates, sentencing patterns by judge
**Revenue:** $29-99/month — journalists, researchers, defense attorneys, policy advocates

### 7. BUILDINGCODE — US Building Code Cross-Reference
**Data source:** ICC public code data, state building code adoptions
**Hook:** "What version of the IBC does your city use? What did they adopt and when?"
**What:** State-by-state code adoption history, local amendment tracking, code version by address, ADA requirements by building type
**Revenue:** $29-79/month — architects, contractors, building officials, permit expeditors

### 8. USDAsoil — USDA SSURGO Soil Survey Database
**Data source:** USDA Web Soil Survey (public), SSURGO shapefile downloads
**Hook:** "Enter an address. Get soil type, percolation rate, shrink-swell potential, bearing capacity. For free."
**What:** Soil type by address/coordinates, agricultural capability class, engineering properties, runoff potential
**Revenue:** $19-59/month — builders, engineers, farmers, real estate developers

### 9. CLINICALTRL — Clinical Trial Results Database
**Data source:** ClinicalTrials.gov API (free, NIH)
**Hook:** "Find all trials for drug X that completed in phase 3 with positive results. In one query."
**What:** Trial search by drug, phase, outcome, sponsor, location, result status, enrollment
**Revenue:** $49-149/month — pharma researchers, investors, journalists, medical writers

### 10. STORMTRACK — Historical Hurricane & Storm Database
**Data source:** NOAA Atlantic Hurricane Database (HURDAT2 — public), NHC track data
**Hook:** "What's the hurricane history for this coastal address? 1950-2025."
**What:** Historical storm tracks by location, return period analysis, wind/swath analysis, NOAA storm data
**Revenue:** $29-79/month — insurance agents, real estate developers, coastal property buyers, emergency managers

### 11. SECFILER — SEC Filing Alert Database
**Data source:** SEC EDGAR full-text search API (free)
**Hook:** "Alert me when any company in sector X files a Form 4 within 24 hours."
**What:** Real-time SEC filing search, insider trading alerts, 8-K event detection, sector/industry filing frequency
**Revenue:** $49-149/month — investors, compliance officers, financial journalists

### 12. CRIMINALINK — National Sex Offender Registry Aggregator
**Data source:** State DOJ public registries (scrape-able with attribution), Dru Sjodin National Registry
**Hook:** "Multi-state sex offender search by address radius. One query, all states."
**Note:** Requires clear terms of service compliance, not for commercial resale of personal data. Better for: anonymized analytics only.

### 13. GRANTFINDER — US Government Grant Opportunities
**Data source:** Grants.gov public API, SAM.gov
**Hook:** "Tell me every open grant for 'rural broadband' in the next 60 days. Filter by eligibility."
**What:** Grant search by keyword/eligibility/agency/deadline, historical award data, eligibility checker
**Revenue:** $29-79/month — nonprofits, local governments, small businesses, consultants

### 14. NEIGHBORHOODDB — Demographics & Real Estate Comp Database
**Data source:** Census Bureau API, Zillow public data, Redfin public data
**Hook:** "Average days on market, price per sqft trend, median rent — by neighborhood, updated monthly."
**What:** Neighborhood comps, demographic trends, school ratings, crime stats, investment metrics
**Revenue:** $29-99/month — real estate investors, property managers, developers

### 15. SUNGLASSES — FAA Sunglasses/Glare Report Database
**Data source:** ASRS NASA Aviation Safety Reporting System (public)
**Hook:** "Pilot reported a laser incident at this airport 12 times last year."
**What:** NASA ASRS incident reports by airport/location/aircraft type, laser illuminations, wildlife strikes, operational incidents
**Revenue:** $19-49/month — pilots, airports, aviation safety researchers

---

## Implementation Priority

| # | Database | Data Source | Legal Risk | Revenue Potential |
|---|---------|-------------|-----------|------------------|
| 1 | STORMTRACK | NOAA (public) | None | $29-79/mo |
| 2 | PATENTLOOK | USPTO (public) | None | $29-99/mo |
| 3 | FCCLOOKUP | FCC ULS (public) | None | $9-29/mo |
| 4 | USDAsoil | USDA (public) | None | $19-59/mo |
| 5 | AIRCRAFTDB | FAA (public) | None | $19-49/mo |
| 6 | VESSELFIND | USCG (public) | Low | $19-59/mo |
| 7 | COURTCLERK | PACER (public) | None | $49-199/mo |
| 8 | SECFILER | SEC EDGAR (free API) | None | $49-149/mo |
| 9 | CLINICALTRL | NIH (free API) | None | $49-149/mo |
| 10 | GRANTFINDER | Grants.gov (public) | None | $29-79/mo |
| 11 | BUILDINGCODE | ICC (public) | None | $29-79/mo |
| 12 | HOMICIDEWATCH | CourtListener (public) | Low | $29-99/mo |
| 13 | NEIGHBORHOODDB | Census (public) | None | $29-99/mo |
| 14 | SUNGLASSES | NASA ASRS (public) | None | $19-49/mo |

---

## Technical Approach

**Build once, sell forever:**
- Scrape/import once → PostgreSQL database
- REST API on top → Stripe billing → monthly subscription
- Update schedule: monthly for static data, daily for court/SEC data
- Deploy: Railway PostgreSQL + FastAPI

**The business model:**
- One-time data license OR monthly subscription
- API access is the product
- Niche verticals pay more for clean, structured data they can't get elsewhere

**Revenue target:** $500-5,000/month per database at scale.
