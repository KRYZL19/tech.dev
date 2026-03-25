#!/usr/bin/env bash
# track.sh — Check tracked URLs for changes

set -euo pipefail

STATE_DIR="${STATE_DIR:-$(dirname "$0")/../state}"
TRACKED_URLS="${TRACKED_URLS:-}"
ALERT_WEBHOOK_URL="${ALERT_WEBHOOK_URL:-}"
CHECK_INTERVAL="${CHECK_INTERVAL:-3600}"

mkdir -p "$STATE_DIR"

if [[ -z "$TRACKED_URLS" ]]; then
  echo "ERROR: TRACKED_URLS is not set. Set it as a comma-separated list of URLs."
  exit 1
fi

IFS=',' read -ra URLS <<< "$TRACKED_URLS"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CHANGES=0

for URL in "${URLS[@]}"; do
  URL=$(echo "$URL" | tr -d ' ')
  [[ -z "$URL" ]] && continue

  # Create a safe filename from URL
  SAFE_NAME=$(echo "$URL" | sha256sum | cut -c1-16)
  HASH_FILE="$STATE_DIR/${SAFE_NAME}.hash"
  BODY_FILE="$STATE_DIR/${SAFE_NAME}.body"

  # Fetch content
  CONTENT=$(curl -sL --max-time 30 -A "competitor-tracker/1.0" "$URL" || true)

  if [[ -z "$CONTENT" ]]; then
    echo "[$TIMESTAMP] WARNING: Failed to fetch $URL"
    continue
  fi

  # Compute hash of content
  CURRENT_HASH=$(echo "$CONTENT" | sha256sum | cut -c1-64)

  # Check for changes
  if [[ -f "$HASH_FILE" ]]; then
    OLD_HASH=$(cat "$HASH_FILE")
    if [[ "$CURRENT_HASH" != "$OLD_HASH" ]]; then
      CHANGES=$((CHANGES + 1))
      echo "[$TIMESTAMP] CHANGE DETECTED"
      echo "URL: $URL"
      echo "Old hash: $OLD_HASH"
      echo "New hash: $CURRENT_HASH"
      echo ""

      # Save old content for diff
      if [[ -f "$BODY_FILE" ]]; then
        cp "$BODY_FILE" "$STATE_DIR/${SAFE_NAME}.body.old"
      fi

      # Send alert if webhook is configured
      if [[ -n "$ALERT_WEBHOOK_URL" ]]; then
        "$(dirname "$0")/alert.sh" "Competition alert: $URL changed"
      fi
    fi
  else
    echo "[$TIMESTAMP] NEW URL TRACKED: $URL"
  fi

  # Store current state
  echo "$CURRENT_HASH" > "$HASH_FILE"
  echo "$CONTENT" > "$BODY_FILE"
done

if [[ $CHANGES -eq 0 ]]; then
  echo "[$TIMESTAMP] No changes detected. Monitored ${#URLS[@]} URLs."
fi
