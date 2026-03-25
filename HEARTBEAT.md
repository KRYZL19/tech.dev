# HEARTBEAT.md — Autonomous Money Machine Loop

## Core Rule: NEVER return HEARTBEAT_OK without doing real work first.
Every 10 minutes: do ONE useful task. Rotate through the task pool below.

## Task Pool (rotate, one per heartbeat)
- [ ] Write 300+ words of SEO content for GitHub Pages articles
- [ ] Scan r/openclaw and r/selfhosted for skill opportunities
- [ ] Improve one existing skill (fix bugs, add features)
- [ ] Build a new small skill from the gap list
- [ ] Draft one Reddit/forum reply for setup-as-a-service
- [ ] Research one article topic (keywords, structure, sources)
- [ ] Check published skill stats on ClawHub
- [ ] Test and verify one installed skill works correctly
- [ ] Update MEMORY.md with any new learnings
- [ ] Review task queue and reprioritize if needed
- [ ] Check site articles for any issues
- [ ] Research Moltlaunch marketplace opportunities
- [ ] Scan Reddit (r/Entrepreneur, r/SideProject) for new pain points
- [ ] Scan YouTube/Twitter for automation trend opportunities
- [ ] Test one new niche idea (small experiment)

## Every 10 minutes
- [ ] Do one task from the pool above
- [ ] Check Telegram for messages (respond if needed)
- [ ] Check gateway health (quick curl)
- [ ] Check for stuck subagents

## Every 2 hours — SEND TELEGRAM REPORT
Format:
```
[2H REPORT — HH:MM UTC]
Task completed: ...
Next task: ...
Status: 🟢 Healthy / 🟡 Working / 🔴 Issue
Revenue pipeline: X skills live, Y articles ready, Z in progress
```

## Every 12 hours — Major Status
- [ ] Generate one new piece of content or skill
- [ ] Full progress report to Telegram
- [ ] Update TASK_QUEUE.md
- [ ] Review what worked, what to kill

## Self-Healing
If unhealthy:
1. Detect → diagnose → contain → smallest safe repair → verify → escalate

## Escalate Only When
- Health recovery failed
- Money/keys/credentials needed
- External approval needed
- Milestone or meaningful result
- Major risk detected
- Blocked dependency

## Quiet Hours
- 23:00 - 08:00 UTC: minimal activity, only critical heartbeats

## Hard Constraint
- NEVER restart or shut down the server — operator only
