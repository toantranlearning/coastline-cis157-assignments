#!/usr/bin/env bash
# Show everything you have written since the starters you were given.
# Run this before you reset, so you can see what you would be throwing away.
cd "$(dirname "$0")/.."
git fetch --quiet origin 2>/dev/null || true
git --no-pager diff origin/main
