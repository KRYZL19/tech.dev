---
name: competitor-tracker
description: Monitor competitor websites for pricing, feature, and content changes. Track page changes via HTTP headers + content diffing, alert on new blog posts and pricing updates. Useful for competitive intelligence, market monitoring, and staying ahead of competitor moves.
metadata:
  {
    "openclaw":
      {
        "requires": { "bins": ["curl"] },
        "install": [],
      },
  }
---

# Competitor Tracker

Monitor competitor websites for changes in pricing, features, blog posts, and content.

## Setup

```bash
# Set environment variables
export TRACKED_URLS="https://competitor1.com,https://competitor1.com/blog,https://competitor2.com/pricing"
export CHECK_INTERVAL="3600"  # seconds between checks
export ALERT_WEBHOOK_URL="https://your-webhook-endpoint.com/alert"
export STATE_DIR="/home/tim/.openclaw/workspace/skills/competitor-tracker/state"
```

## Scripts

### track.sh — Check for Changes

```bash
./scripts/track.sh
```

Fetches each URL in `TRACKED_URLS`, computes a hash of the content, and compares against stored hashes. Outputs changes detected.

### alert.sh — Send Alert

```bash
./scripts/alert.sh "Competition alert: Competitor1 pricing page changed"
```

Sends an alert to `ALERT_WEBHOOK_URL` via POST with JSON payload.

### diff.sh — Show What Changed

```bash
./scripts/diff.sh https://competitor1.com/pricing
```

Shows the diff between the last known content and current content for a URL.

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `TRACKED_URLS` | Yes | — | Comma-separated list of URLs to monitor |
| `CHECK_INTERVAL` | No | `3600` | Seconds between automated checks |
| `ALERT_WEBHOOK_URL` | No | — | Webhook URL for alerts (POST with `{"text": "...", "url": "...", "timestamp": "..."}`) |
| `STATE_DIR` | No | `./state` | Directory to store hash snapshots |

## Usage Example

```bash
# Initial setup
mkdir -p state
export TRACKED_URLS="https://acme.com,https://acme.com/blog,https://acme.com/pricing"
export ALERT_WEBHOOK_URL="https://hooks.example.com/alert"

# Check for changes
./scripts/track.sh

# See what changed
./scripts/diff.sh https://acme.com/pricing

# Set up a cron job (every hour)
# 0 * * * * cd /home/tim/.openclaw/workspace/skills/competitor-tracker && ./scripts/track.sh >> /var/log/competitor-tracker.log 2>&1
```

## Output Format

When changes are detected:
```
[2024-01-15T10:30:00Z] CHANGE DETECTED
URL: https://competitor.com/pricing
Type: content (hash mismatch)
Old hash: a1b2c3...
New hash: d4e5f6...

Run ./scripts/diff.sh https://competitor.com/pricing to see the diff
```

## Tips

- Start with blog RSS feeds (often at `/feed` or `/rss`) for easy change detection
- Store your `STATE_DIR` outside the skill folder to preserve state across updates
- Combine with `cron` for fully automated monitoring
- Use descriptive aliases for URLs in `TRACKED_URLS` by maintaining a separate config file
