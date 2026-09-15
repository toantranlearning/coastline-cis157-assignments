#!/usr/bin/env bash
#
# Setup and tidy-up for the course assignments in Google Cloud Shell.
# It checks what is already done and only does the missing parts, so it is
# safe to run every time you open the project.
#
# Run it as:    source scripts/start.sh
#
# "source" runs it inside your own terminal, which is what lets it move you
# into the project folder when it is done. Run as "bash scripts/start.sh" it
# still works, but a script run that way cannot move the shell that started
# it, so it can only tell you where to cd.

# Sourced or executed? Decides whether we may move the caller's shell, and
# whether a failure should return (sourced) or exit (executed).
_cs_sourced=0
[ "${BASH_SOURCE[0]}" != "$0" ] && _cs_sourced=1

# This script sits in scripts/, so the project root is its parent.
SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# Everything below is derived from the clone's own remote, so this script is
# the same file in every course repository. Nothing here names a course.
REPO_URL="$(git -C "$SELF" remote get-url origin 2>/dev/null)"
REPO_NAME="$(basename "${REPO_URL%.git}")"
if [ -z "$REPO_NAME" ]; then
  echo "Could not work out which repository this is. Is it a git clone?"
  [ "$_cs_sourced" = 1 ] && return 1 || exit 1
fi
# Where the working copy lives (its natural clone path).
BASE="$HOME/cloudshell_open/$REPO_NAME"
# Where the terminal was before any cd.
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
# Opening the setup link again makes another folder named after the repo
# plus a suffix (name-0, name-1, ...), and Cloud Shell opens that new one, so
# it is possible to spend a session typing into a copy you did not mean to use.
# Deleting duplicates blindly can therefore throw away real work; keeping them
# scatters your work across folders, which is worse. So: find the copy that has
# work in it, make that one canonical, and remove the rest.
_cs_dirty=()
for _cs_d in "$BASE"*; do
  [ -d "$_cs_d" ] || continue
  [ -n "$(git -C "$_cs_d" status --porcelain 2>/dev/null)" ] && _cs_dirty+=("$_cs_d")
done

if [ "${#_cs_dirty[@]}" -gt 1 ]; then
  # Work in more than one copy. A script should not guess which to keep, and
  # merging them is not something to do behind your back.
  echo "More than one copy has work in it, so none were removed:"
  for _cs_d in "${_cs_dirty[@]}"; do echo "  $(basename "$_cs_d")"; done
  echo "Move what you want to keep into one folder, delete the others, then run this again."
else
  # The keeper is the copy with work, or the canonical one if no copy has any.
  _cs_keeper="${_cs_dirty[0]:-$BASE}"
  if [ "$_cs_keeper" != "$BASE" ]; then
    rm -rf "$BASE"
    mv "$_cs_keeper" "$BASE"
    echo "Your work was in $(basename "$_cs_keeper"); that copy is now the project folder."
  fi
  for _cs_d in "$BASE"*; do
    [ -d "$_cs_d" ] && [ "$_cs_d" != "$BASE" ] && rm -rf "$_cs_d" && echo "Removed an unused duplicate copy: $(basename "$_cs_d")"
  done
fi

# From here on, work from the project folder. When sourced, this is also what
# moves the caller's terminal there, out of any folder that was just removed.
cd "$BASE" 2>/dev/null || cd "$SELF" 2>/dev/null || cd "$HOME"

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

# Confirm Python is present. It ships with Cloud Shell, so this is a check
# rather than an install.
if command -v python3 >/dev/null 2>&1; then
  echo
  echo "Python $(python3 -V 2>&1 | awk '{print $2}') is ready. Your assignments are in $BASE"
else
  echo "Python 3 was not found, which is unexpected in Cloud Shell. Message your instructor."
  [ "$_cs_sourced" = 1 ] && return 1 || exit 1
fi

echo
if [ "$_cs_sourced" = 1 ]; then
  echo "Your terminal is in the project folder."
elif [ "$LAUNCH_DIR" != "$BASE" ]; then
  # Executed rather than sourced: a script cannot move the shell that ran it.
  echo "Move your terminal into the project folder so the other commands work:"
  echo "  cd $BASE"
  echo "(Next time, run  source scripts/start.sh  and it will move you there itself.)"
fi
echo "Open this week's folder, for example:  cd m01"

# Tidy up the names this script used, since when sourced they would otherwise
# stay in your shell.
unset _cs_sourced _cs_dirty _cs_d _cs_keeper SELF REPO_URL REPO_NAME LAUNCH_DIR
