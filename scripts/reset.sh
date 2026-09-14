#!/usr/bin/env bash
# Put your files back to a known state.
#
#   ./scripts/reset.sh                    discard changes you have not saved
#   ./scripts/reset.sh --undo             step back one save of your own
#   ./scripts/reset.sh --starter m01      restore one assignment's starter file
#   ./scripts/reset.sh --baseline         every file back to the starters given
#
# This rewrites files. Anything you have not saved with save.sh is lost.
# Run ./scripts/diff.sh first if you want to see what you would lose.
set -e
cd "$(dirname "$0")/.."

confirm() {
  printf "%s Continue? [y/N] " "$1"
  read -r a
  [ "$a" = y ] || [ "$a" = Y ] || { echo "Cancelled."; exit 0; }
}

case "${1:-}" in
  "")
    confirm "This discards changes you have not saved, back to your last save."
    git checkout -- .
    ;;
  --undo)
    git fetch --quiet origin 2>/dev/null || true
    # Only your own saves can be undone. Commits that came with the course are
    # not yours to step back through.
    saves=$(git rev-list origin/main..HEAD --count 2>/dev/null || echo 0)
    if [ "$saves" -eq 0 ]; then
      echo "You have no saves of your own to undo."
      echo "To discard unsaved changes instead, run: ./scripts/reset.sh"
      exit 0
    fi
    confirm "This steps back one save."
    git reset --hard HEAD~1 >/dev/null
    ;;
  --starter)
    [ -z "${2:-}" ] && { echo "Which assignment? e.g. ./scripts/reset.sh --starter m01"; exit 1; }
    folder="${2%/}"
    [ -d "$folder" ] || { echo "There is no folder called '$folder'."; exit 1; }
    confirm "This replaces everything in $folder with the files you were given."
    git fetch --quiet origin 2>/dev/null || true
    git checkout origin/main -- "$folder"
    echo "Restored $folder."
    exit 0
    ;;
  --baseline)
    confirm "This puts EVERY file back to the starters you were given, across all assignments."
    git fetch --quiet origin 2>/dev/null || true
    git reset --hard origin/main >/dev/null
    ;;
  *)
    echo "Unknown option: $1"
    echo "Try: ./scripts/reset.sh | --undo | --starter <folder> | --baseline"
    exit 1
    ;;
esac

echo "Done."
