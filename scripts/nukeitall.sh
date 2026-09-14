#!/usr/bin/env bash
#
# Start completely over: remove every copy of the assignments and fetch a fresh
# one. Use this when something is so tangled that a reset is not enough. It
# throws away every file you have written.

# Derived from this clone's own remote, so this script is the same file in
# every course repository.
SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REPO="$(git -C "$SELF" remote get-url origin 2>/dev/null)"
REPO_NAME="$(basename "${REPO%.git}")"
[ -n "$REPO_NAME" ] || { echo "Could not work out which repository this is. Is it a git clone?"; exit 1; }
BASE="$HOME/cloudshell_open/$REPO_NAME"

# Where the terminal was when this was run, before any cd. This removes every
# copy, so the caller's folder is gone afterward and we must point them back.
LAUNCH_DIR="$PWD"

echo "This removes every copy of your assignments, including all the code you"
echo "have written, and fetches brand-new starter files."
echo
echo "If you only want to fix one assignment, cancel and run this instead:"
echo "  ./scripts/reset.sh --starter m01"
echo
printf "Remove everything and start over? [y/N] "
read -r a
[ "$a" = y ] || [ "$a" = Y ] || { echo "Cancelled."; exit 0; }

cd "$HOME/cloudshell_open" 2>/dev/null || cd "$HOME"
rm -rf "$BASE"*
echo "Fetching a fresh copy..."
git clone --quiet "$REPO" "$BASE" || { echo "Could not fetch the assignments. Check your connection and try again."; exit 1; }
echo "Fresh copy ready. If the file list looks empty, refresh it."
echo
cd "$BASE" && bash scripts/start.sh

# The caller's folder was removed with the rest, so their terminal is orphaned.
# A script cannot change its parent shell, so say what to run.
if [ ! -d "$LAUNCH_DIR" ] || [ "$LAUNCH_DIR" != "$BASE" ]; then
  echo
  echo "Your terminal is not in the project folder. Move into it:"
  echo "  cd $BASE"
fi
