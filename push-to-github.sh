#!/bin/bash
set -e
cd /tmp/tech.dev.clone

echo "=== Files in clone ==="
ls -la

echo "=== Adding files ==="
touch .nojekyll
cp /home/tim/.openclaw/workspace/site/.nojekyll .
cp /home/tim/.openclaw/workspace/site/index.html .
cp -r /home/tim/.openclaw/workspace/site/articles/* articles/
cp /home/tim/.openclaw/workspace/site/style.css .

echo "=== Git add and commit ==="
git add -A
git commit -m "Update site - $(date)"

echo "=== Git log ==="
git log --oneline -3

echo "=== Pushing force ==="
git push -f origin main

echo "=== Done ==="
