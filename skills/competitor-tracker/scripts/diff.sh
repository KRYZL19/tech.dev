#!/usr/bin/env bash
# diff.sh — Show diff between last known content and current for a URL

set -euo pipefail

STATE_DIR="${STATE_DIR:-$(dirname "$0")/../state}"
URL="${1:-}"

if [[ -z "$URL" ]]; then
  echo "Usage: $0 <url>"
  echo "Shows the diff between cached content and current content for a tracked URL."
  exit 1
fi

SAFE_NAME=$(echo "$URL" | sha256sum | cut -c1-16)
BODY_FILE="$STATE_DIR/${SAFE_NAME}.body"
BODY_OLD_FILE="$STATE_DIR/${SAFE_NAME}.body.old"

if [[ ! -f "$BODY_FILE" ]]; then
  echo "No cached content found for $URL"
  echo "Run track.sh first to establish a baseline."
  exit 1
fi

if [[ ! -f "$BODY_OLD_FILE" ]]; then
  echo "No previous content found for $URL"
  echo "This URL was just added to tracking."
  echo ""
  echo "Current content (first 100 lines):"
  head -100 "$BODY_FILE"
  exit 0
fi

echo "Diff for: $URL"
echo "=========================================="
diff -u --color=always "$BODY_OLD_FILE" "$BODY_FILE" || true
echo "=========================================="
echo ""
echo "Use ./scripts/track.sh to update the baseline after reviewing."
