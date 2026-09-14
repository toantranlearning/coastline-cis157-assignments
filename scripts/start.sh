#!/usr/bin/env bash
#
# Setup and tidy-up for the CIS C157 assignments in Google Cloud Shell.
# It checks what is already done and only does the missing parts, so it is
# safe to run every time you open the project.

# This script sits in scripts/, so the project root is its parent.
SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# Everything below is derived from the clone's own remote, so this script is
# the same file in every course repository. Nothing here names a course.
REPO_URL="$(git -C "$SELF" remote get-url origin 2>/dev/null)"
REPO_NAME="$(basename "${REPO_URL%.git}")"
[ -n "$REPO_NAME" ] || { echo "Could not work out which repository this is. Is it a git clone?"; exit 1; }
# Where the working copy lives (its natural clone path).
BASE="$HOME/cloudshell_open/$REPO_NAME"
# Where the terminal was before any cd, so we can tell at the end whether it
# is still sitting somewhere sensible.
LAUNCH_DIR="$PWD"

cd "$HOME/cloudshell_open" 2>/dev/null || cd "$HOME"

# A canonical folder emptied out (a "start over" that deleted the files but
# left the folder behind) must not win over a fresh clone.
if [ -d "$BASE" ] && [ ! -f "$BASE/scripts/start.sh" ]; then
  rm -rf "$BASE"
fi

# If there is no canonical copy yet but we launched from a suffixed one,
# promote it to the canonical name.
if [ ! -d "$BASE" ] && [ -d "$SELF" ] && [ "$SELF" != "$BASE" ]; then
  mv "$SELF" "$BASE"
fi

# Keep exactly ONE copy, and make it the one with your work in it.
#
# Clicking the launch link again makes another folder named after the repo
# plus a suffix (name-0, name-1, ...), and Cloud Shell opens that new one, so
# it is possible to spend a session typing into a copy you did not mean to use.
# Deleting duplicates blindly can therefore throw away real work; keeping them
# scatters your work across folders, which is worse. So: find the copy that has
# work in it, make that one canonical, and remove the rest.
dirty=""
for d in "$BASE"*; do
  [ -d "$d" ] || continue
  [ -n "$(git -C "$d" status --porcelain 2>/dev/null)" ] && dirty="$dirty $d"
done

set -- $dirty
if [ "$#" -gt 1 ]; then
  # Work in more than one copy. A script should not guess which to keep, and
  # merging them is not something to do behind your back.
  echo "More than one copy has work in it, so none were removed:"
  for d in "$@"; do echo "  $(basename "$d")"; done
  echo "Move what you want to keep into one folder, delete the others, then run this again."
else
  # The keeper is the copy with work, or the canonical one if no copy has any.
  keeper="${1:-$BASE}"
  if [ "$keeper" != "$BASE" ]; then
    rm -rf "$BASE"
    mv "$keeper" "$BASE"
    echo "Your work was in $(basename "$keeper"); that copy is now the project folder."
  fi
  for d in "$BASE"*; do
    [ -d "$d" ] && [ "$d" != "$BASE" ] && rm -rf "$d" && echo "Removed an unused duplicate copy: $(basename "$d")"
  done
fi

cd "$BASE" 2>/dev/null || cd "$SELF"

# Turn the editor's Gemini Code Assist off by default so its panel does not
# open and it does not suggest code as you type. You write every line you
# submit in this course. Written to the editor's settings, keeping anything
# already there and never overriding a choice you make later. Takes effect on
# the next load.
python3 - <<'PYEOF' 2>/dev/null || true
import json, os
paths = [os.path.expanduser("~/.codeoss/data/Machine/settings.json"),
         os.path.expanduser("~/.codeoss/data/User/settings.json")]
keys = ("geminicodeassist.enable",
        "cloudcode.geminiCodeAssist.enable",
        "cloudcode.enableGeminiCodeAssist",
        "geminicodeassist.inlineSuggestions.enableAuto",
        "cloudcode.geminiCodeAssist.inlineSuggestions.enableAuto")
for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    try:
        d = json.load(open(p)); d = d if isinstance(d, dict) else {}
    except Exception:
        d = {}
    for k in keys:
        d.setdefault(k, False)
    json.dump(d, open(p, "w"), indent=2)
PYEOF

# Gemini leaves a history folder in your home directory that the editor shows
# as its own repository in the Source Control panel. Gemini is off, so clear it.
rm -rf ~/.gemini/history 2>/dev/null || true

# Confirm Python is present. It ships with Cloud Shell, so this is a check
# rather than an install.
if command -v python3 >/dev/null 2>&1; then
  echo
  echo "Python $(python3 -V 2>&1 | awk '{print $2}') is ready. Your assignments are in $BASE"
else
  echo "Python 3 was not found, which is unexpected in Cloud Shell. Message your instructor."
  exit 1
fi

# A script cannot move its parent shell, so say what to run.
if [ "$LAUNCH_DIR" != "$BASE" ]; then
  echo
  echo "Move your terminal into the project folder so the other commands work:"
  echo "  cd $BASE"
fi

echo
echo "Then open this week's folder, for example:  cd m01"
