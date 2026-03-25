#!/usr/bin/env bash
# alert.sh — Send alert to webhook

set -euo pipefail

ALERT_WEBHOOK_URL="${ALERT_WEBHOOK_URL:-}"

if [[ -z "$ALERT_WEBHOOK_URL" ]]; then
  echo "WARNING: ALERT_WEBHOOK_URL not set. Skipping alert: $1"
  exit 0
fi

MESSAGE="${1:-Alert from competitor-tracker}"
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

PAYLOAD=$(cat <<EOF
{
  "text": "$MESSAGE",
  "timestamp": "$TIMESTAMP",
  "source": "competitor-tracker"
}
EOF
)

HTTP_CODE=$(curl -sL -o /dev/null -w "%{http_code}" -X POST \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD" \
  --max-time 10 \
  "$ALERT_WEBHOOK_URL" || echo "000")

if [[ "$HTTP_CODE" =~ ^[23] ]]; then
  echo "[$TIMESTAMP] Alert sent successfully (HTTP $HTTP_CODE)"
else
  echo "[$TIMESTAMP] WARNING: Alert failed with HTTP $HTTP_CODE"
  exit 1
fi
