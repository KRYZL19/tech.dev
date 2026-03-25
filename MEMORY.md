# MEMORY.md - Long-Term Memory

## Operator
- **Name:** ÄHÄH (username: kryzlstrd)
- **Role:** VPS operator running autonomous AI agents 24/7
- **Goal:** Automation income + autonomous revenue streams. Workflows that run without operator involvement once deployed.
- **Principle:** I am the labor force. VPS is the factory. Operator is oversight + funding.
- **Escalation:** Telegram only for money, keys, credentials, approvals, major risks, milestones.

## Security Audit Baseline (2026-03-25)
- 0 critical · 2 warn · 1 info
- WARN: gateway.trustedProxies empty (gateway.bind=loopback, acceptable)
- WARN: denyCommands entries ineffective (cosmetic)
- INFO: attack surface minimal (open=0, allowlist=2)
- tools.elevated: enabled (expected for autonomous operator)
- Credentials dir: FIXED (755→700)

## Hard Constraints
- NEVER restart or shut down the server — operator only
- NEVER touch systemd, init, or reboot commands
- Self-healing must work around restart requirements

## System
- **VPS:** Ubuntu, 4GB RAM, 38GB disk (35% used), IPv6+IPv4 (Hetzner), node 22.22.1
- **OpenClaw:** Latest version, Telegram + WhatsApp channels OK
- **Gateway:** local loopback only (not exposed), 49.13.152.190
- **Heartbeat:** 10m interval (corrected — was 10m in config, MEMORY.md said 30m)
- **Credentials:** chmod 700 recommended for ~/.openclaw/credentials (currently 755 - warn)
- **Reverse proxy:** not configured, headers not trusted

## My Operating Framework
1. Stay healthy and online 24/7
2. Stay secure and operator-aligned
3. Execute high-value safe work
4. Discover and pursue opportunities
5. Improve own methods continuously

## Uptime Self-Healing Protocol
- Monitor: gateway reachability, session freshness, memory, disk, channels, update status
- Sequence: detect → diagnose → contain → smallest safe repair → verify → escalate or return
- Anti-fragility: one repair at a time, rollbackable changes, logs over guesses, evidence over confidence
- Never: invent credentials, weaken security, spend money, hide failures

## Karpathy Autoresearch-Inspired Ops Loop
- One editable surface at a time
- One clear metric per experiment
- Fixed time budget per task
- Ratchet: keep what improves health, discard what doesn't
- Log every experiment

## Opportunity Priorities (from Battle Plan)
| # | Stream | Time to First $ | Operator Involvement |
|---|--------|-----------------|---------------------|
| 1 | ClawHub Skills | 1-2 weeks | Near zero |
| 2 | SEO/Affiliate Content | 4-8 weeks | Near zero |
| 3 | Setup-as-a-Service | 1 week | Medium (calls) |
| 4 | Moltlaunch (onchain agent marketplace) | 1-2 weeks | Low after setup |
| 5 | Market Research Newsletter | 3-4 weeks | Low |
| 6 | Micro-SaaS | 6-8 weeks | Low after setup |
| 7 | Managed Hosting | 8+ weeks | Low after automation |

## Moltlaunch Opportunity (researched 2026-03-25)
- **Live at:** moltlaunch.com (on Base Mainnet, ERC-8004) since February 9, 2026
- **What:** Onchain AI agent marketplace — clients post tasks, agents bid, get paid in ETH
- **Fees:** 0% platform fee (vs 20-40% on Fiverr)
- **CashClaw:** Ready-made autonomous agent at github.com/moltlaunch/cashclaw
- **Setup:** `npm i -g moltlaunch` → fund wallet with ETH on Base → register agent → start working
- **Revenue potential:** Unknown but passive once running. Needs ~0.01 ETH to start.
- **Guardrail:** NEVER do work before escrow is funded. Status must be 'accepted' before delivering.
- **Skill file:** https://moltlaunch.com/skill.md (version 2.15.0)
- **Verdict:** Worth trying as autonomous income stream. Low risk, just ETH funding.

## Critical Warnings
- MiniMax M2.7 is not Claude Opus — use for volume tasks, not complex multi-step reasoning
- API costs can spike — monitor usage
- Google penalizes AI slop — research deeply before writing
- Never trade real money — paper trade first
- Security: gateway token + bot token are sensitive

## Skills Installed
- agentic-paper-digest-skill (arxiv/HF papers)
- seo-reporter (SEO audit)
- youtube-full (YouTube transcripts)

## Skills Built (14 total)
- OpenClawify: FastAPI skill generator (10 templates, plain English to SKILL.md)
- api-cost-optimizer: Heartbeat waste detection + API cost estimation + savings recommendations
- link-checker: Full link audit tool (broken/redirected/slow/affiliate links) — tested working
- content-summarizer: URL-to-structured-summary with extractive summarization + AI enhancement prompts
- Skills done: seo-reporter, adguard-home, competitor-tracker, content-summarizer (improved), uptime-monitor, ghost-cms, plausible-analytics, reddit-researcher (improved), social-post-generator, api-cost-optimizer, openclawify, link-checker, agentic-paper-digest-skill, youtube-full

## Work Queue
- Active: SEO content pipeline (10 articles written, GitHub Pages)
- Blocked: GitHub push — repo kryzlstrd/techstack.dev does not exist (operator needs to create it)
- Blocked: clawhub publishing (need clh_ token from clawhub.ai/settings)
- Ready to post: Fiverr gig (draft ready at opportunities/fiverr-setup-service.md)
- Ready to post: Reddit outreach templates (opportunities/reddit-forum-outreach-2026-03-25.md)
- Opportunity: ClawHub has 13,729 skills (crowded) — underserved: Self-Hosted (33), Data (28), Smart Home (41) skills

## GitHub Site Status (2026-03-25)
- Site: techstack.dev (GitHub Pages, Jekyll)
- 10 SEO articles written and committed locally
- GitHub repo doesn't exist yet — operator needs to create kryzlstrd/techstack.dev
- Remote set to https://github.com/kryzlstrd/techstack.dev.git
- Push fails with "Repository not found"

## Telegram Status (2026-03-25)
- Connected: @timstrdstbot (bot token: 8632789399:AAEORnp34r6La272KPeNq4NgWWOTVgTOAJ0 — CORRECTED)
- Operator Telegram ID: 7026534475
- Pairing approved, dmPolicy: pairing
- WhatsApp also connected (+4915142857780)

## Skill Inventory (installed, not yet fully mapped)
- 41 skills available in ~/.npm-global/lib/node_modules/openclaw/skills/
- Key useful ones identified: clawhub, coding-agent, mcporter, github, weather, summarize, tmux, healthcheck

## Lessons Learned (2026-03-25)
- `openclaw gateway` not `openclaw gateway start`
- `openclaw approvals` manages exec allowlist, not `approve`
- ffmpeg already installed on this VPS
- sudo -u doesn't bypass nested sudo without NOPASSWD
- elevated config needs both tools level AND agents.list level
- tim user has NOPASSWD for apt/systemctl/service/cron/mkdir/chmod/chown

## Autonomy Grant (2026-03-25)
- Operator said "Do whatever you want, you are now autonomous"
- Execute without asking for approval on safe internal actions
- Only escalate when: money, keys, credentials, external approval, milestone, major risk
- Text on Telegram when: published something, got paid, need something

## Notes
- BOOTSTRAP.md deleted (identity established)
- operator wants texts on Telegram with opportunities + results
- Uptime is the primary success condition
- NEVER restart server — operator only

## CRITICAL: API Rate Limit Event (2026-03-25 19:43 UTC)
- MiniMax API rate limit hit at 19:43 UTC
- Agent went silent for ~3 hours (20 missed heartbeats)
- Root cause: too many API calls from today's heavy workload
- Heartbeat changed from 10m to 30m (config updated, needs gateway restart to apply)
- Mitigation: reduce heartbeat frequency, consider fallback model
- No data loss — agent resumed automatically when rate limit cleared
- Reminder: NEVER restart server — operator must restart gateway
