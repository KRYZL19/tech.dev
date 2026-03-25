# Selling Machine — Build Plan
*Built: 2026-03-25 — Status: EXECUTING*

---

## The Machine

```
Content (Reddit/YouTube/Human posts)
       ↓
Landing Page (converts visitors to email)
       ↓
API/SaaS (converts emails to paid users)
       ↓
Stripe billing (monthly recurring revenue)
```

Every piece of content should feed at least one of:
- Traffic to landing page
- Email list growth
- Direct signups

---

## API Build Priority

### NOW: GRIDOPT — Energy Tariff API
**Why first:** Home Assistant subreddit has 1.2M members. Every post about energy/OLED tariffs gets thousands of upvotes. The integration is the viral loop.

**What it does:**
- TOU tariff lookup by utility company
- Optimal appliance scheduling
- Solar self-consumption optimizer
- Demand charge minimizer

**Revenue model:** Freemium → $9-49/month

**Build time:** 40-60 hours

**Traffic strategy:**
- Post in r/homeassistant, r/solar, r/teslamotors
- "I built an API to automatically run my dishwasher at 2am when electricity is cheapest"
- YouTube: "How to cut your electricity bill with time-of-use tariffs"

### NEXT: BETTORDB — Gambling Probability API
**Why second:** Gambling niche pays premium. Casino game developers pay $200-500/month without blinking.

**What it does:**
- Casino simulation engine (millions of iterations)
- House edge calculator
- Betting system analyzer (martingale, fibonacci — exposes expected loss)
- Odds converter
- Kelly criterion calculator

**Revenue model:** Usage-based, $49-199/month

**Traffic strategy:**
- Post in r/gamedev, r/poker, r/blackjack
- "I ran 10 million simulations of the martingale betting system. Here's why it always loses."
- YouTube: "The math behind casino games — why the house always wins"

### AFTER: ARCHISPEAK — Architectural Data API
**Why third:** Architects are underserved online, pay premium, stickiness is very high.

**What it does:**
- Zoning compliance lookup
- FAR calculator
- Building code cross-reference
- Permit checklist generator

**Revenue model:** $29-99/month developer tier

---

## SaaS Frontend

Build a single landing page that showcases all APIs:
- `gridopt.dev` — "APIs for developers who charge for optimization"
- Or: `nicheapi.io` — one brand, multiple vertical APIs

Each API gets:
- Landing page with live demo (free tier call)
- Stripe subscription
- Documentation (openapi spec)
- Status page

**Stack:** Next.js + Vercel + Stripe. Fast to build, cheap to run.

---

## Traffic Channels

### Reddit (highest conversion)
Post in small communities first (build karma):
- r/homeassistant — GRIDOPT
- r/gamedev — BETTORDB
- r/architecture — ARCHISPEAK
- r/Entrepreneur — general "I built X" story

Format: "I analyzed [topic] and found [unexpected result]" — never promotional

### YouTube
Short-form: "The math behind [X]" — explains why the casino always wins, how TOU tariffs work

Long-form: "I built an API that [does X]. Here's how it works."

Upload schedule: 1 video per API, 1 video per skill

### Twitter/X
Human-first posts from the human-content-writer skill.
1 hot take per piece of content. No threads.

---

## Skills (Passive Income)

Publish more to ClawHub:
1. uptime-monitor (renamed to avoid conflict)
2. healthcheck-pro (enhanced version of existing healthcheck)
3. reddit-researcher (already improved)
4. Self-built: seo-content-pipeline, content-repurposer (already done)

---

## Execution Order

| Week | Build | Traffic |
|------|-------|---------|
| Week 1 | GRIDOPT API + landing page | 3 Reddit posts, 1 YouTube video |
| Week 2 | BETTORDB API + landing page | 3 Reddit posts, 1 YouTube video |
| Week 3 | ARCHISPEAK API + landing page | 3 Reddit posts |
| Week 4 | SaaS bundle + Stripe integration | Launch post in r/SideProject |

**Revenue target by week 4:** $500-2,000/mo combined
**Revenue target by week 8:** $2,000-8,000/mo combined
