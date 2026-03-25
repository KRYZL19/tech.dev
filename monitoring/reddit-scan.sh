#!/bin/bash
# Reddit monitoring script - scans for OpenClaw/selfhosted opportunities
# Runs via cron every hour

SEARCH_TERM="openclaw|selfhosted|AI agent|automation"
SUBREDDITS="r/openclaw,r/selfhosted,r/Entrepreneur,r/SideProject"
OUTPUT="/home/tim/.openclaw/workspace/monitoring/reddit-findings.md"

echo "# Reddit Opportunity Scan - $(date)" > "$OUTPUT"
echo "" >> "$OUTPUT"

# Simple check using web search for recent posts
curl -s --max-time 10 "https://www.reddit.com/r/openclaw/search.rss?q=help+OR+setup+OR+request&sort=new&limit=5" 2>/dev/null | grep -oP '(?<=<title>)[^<]+' | head -10 >> "$OUTPUT" || echo "Could not fetch Reddit" >> "$OUTPUT"

echo "Scan complete: $OUTPUT"
