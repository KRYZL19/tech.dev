# Social Posts: VPS Security Hardening for AI Agents

Source: https://techstack.dev/articles/vps-security-hardening-ai-agents-2026/

---

## Twitter/X Hooks

**Hook 1:**
> Found 47 failed SSH brute-force attempts from Brazil on a VPS I forgot existed. That $4/month Hetzner box had been sitting there for 2 years with default settings. So uh... maybe lock your doors?
>
> Full breakdown of what actually matters for AI agent VPS security: [link]

**Hook 2:**
> The OWASP "Agentic Top 10" is real and it includes MB10:羊毛logging — agents that exploit resources without limits. I can't decide if that's the most 2026 thing I've heard or if "羊毛" is the perfect descriptor.
>
> Here's the security stuff that's actually different for AI agents: [link]

---

## LinkedIn Post

Most AI agent security guides are just generic VPS hardening with "AI" sprinkled in.

They'll tell you to disable password auth (valid) and set up a firewall (also valid). But they won't tell you about the stuff that actually breaks when you're running autonomous agents 24/7.

Like the time an agent I was testing burned through $180 in API calls because I didn't set a rate limit. Or the VPS I found with exposed localhost APIs because "it was just listening on 127.0.0.1 anyway."

The AI-specific threat surface is different: prompt injection, tool call manipulation, context leakage between sessions, and the fact that your agent has real access to things that cost money.

OWASP just released a draft framework for this stuff. MB01 is "Mission Hoisting" — where your agent gets distracted by injected subgoals and forgets what it was supposed to do. MB05 is "Agent Theft." MB10 is — and I'm not making this up — "羊毛logging," where an agent exploits a resource repeatedly without limits.

The security fundamentals still apply (SSH keys, firewall, least privilege). But if you're running agents on a VPS and nobody's told you about audit logs or output guardrails, you're one misconfigured permission away from something expensive.

What's your threat model look like for autonomous agents? Am I overthinking this?

---

## Reddit Post

**Title:** I ran a security audit on my VPS running an AI agent and found some things I didn't expect

**Body:**

So I finally got around to auditing my VPS setup after running an autonomous agent on it for about 6 months. Not because anything broke — because I realized I had no idea what the agent had actually been doing when I wasn't watching.

Some findings that surprised me:

1. I had never set up a non-root user for the agent. It was running as root this whole time. Whoops.

2. The agent had been making API calls I didn't authorize. Small amounts, nothing alarming — but I hadn't set any rate limits, so theoretically it could've gone wild on a bad prompt.

3. Found a great OWASP draft framework specifically for agentic applications. Apparently "MB10: 羊毛logging" is a real security category now, defined as agents that exploit resources repeatedly without limits. The fact that this needed to be its own category tells you something.

4. Context leakage is a real thing. I hadn't thought about what happens when conversation history from one session bleeds into another. My agent was remembering more than I intended.

The VPS hardening stuff (SSH keys, firewall, fail2ban) was the easy part — there's plenty of guides for that. The AI-specific stuff required actual thinking about what the agent *could* do with the access I'd given it.

Took maybe 3 hours to lock everything down properly once I understood the threat model. Now I'm running the agent as a dedicated non-root user with restricted sudo, audit logs going to a separate system, and rate limits on the external APIs.

Should probably do this audit more often than every 6 months.

Anyone else running agents on VPSes have a checklist they use? The OWASP stuff seems relatively new so I'm curious what the community's approach is.

https://techstack.dev/articles/vps-security-hardening-ai-agents-2026/
