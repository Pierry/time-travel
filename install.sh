#!/usr/bin/env bash
# time-travel installer, for Claude Code and Codex.
#
#   gh api repos/Pierry/time-travel/contents/install.sh -H "Accept: application/vnd.github.raw" | bash
#
# The repository is private, so a plain curl of raw.githubusercontent.com
# returns 404. gh carries the login, and `gh auth setup-git` lets both CLIs
# clone the marketplace over https.
#
# The repository is its own marketplace for both hosts, so nothing is cloned by
# hand and no path is hardcoded.
#
#   TARGET=claude|codex|both  where to install (default: every CLI found on PATH)
#   SCOPE=user|project|local  Claude Code scope (default: user)
#   REPO=owner/name           install from a fork
set -uo pipefail

REPO="${REPO:-Pierry/time-travel}"
SCOPE="${SCOPE:-user}"
TARGET="${TARGET:-auto}"
NAME=time-travel

say() { printf '%s\n' "$*"; }
die() { printf 'install: %s\n' "$*" >&2; exit 1; }

command -v python3 >/dev/null 2>&1 \
  || die "python3 is not on PATH; the gate and the calendar export need Python 3.10+"
command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1 \
  || die "gh is not logged in. The repository is private: run 'gh auth login' and 'gh auth setup-git' first."

case "$SCOPE" in user|project|local) ;; *) die "SCOPE must be user, project or local; got '$SCOPE'" ;; esac

has() { command -v "$1" >/dev/null 2>&1; }
want_claude=no; want_codex=no
case "$TARGET" in
  auto)   has claude && want_claude=yes; has codex && want_codex=yes ;;
  claude) want_claude=yes ;;
  codex)  want_codex=yes ;;
  both)   want_claude=yes; want_codex=yes ;;
  *) die "TARGET must be claude, codex or both; got '$TARGET'" ;;
esac
[ "$want_claude$want_codex" = "nono" ] \
  && die "neither claude nor codex is on PATH. Install Claude Code (https://claude.com/claude-code) or Codex (https://developers.openai.com/codex) first."

if [ "$want_claude" = yes ]; then
  has claude || die "TARGET includes claude, but the claude CLI is not on PATH"
  say "time-travel: Claude Code, adding marketplace $REPO"
  claude plugin marketplace add "$REPO" >/dev/null 2>&1 \
    || claude plugin marketplace update "$NAME" >/dev/null 2>&1 \
    || die "could not add the Claude Code marketplace. Run 'gh auth setup-git' and try again."
  say "time-travel: Claude Code, installing plugin (scope: $SCOPE)"
  claude plugin install "$NAME@$NAME" --scope "$SCOPE" >/dev/null \
    || die "the Claude Code install failed. Run it by hand to see why: claude plugin install $NAME@$NAME --scope $SCOPE"
fi

if [ "$want_codex" = yes ]; then
  has codex || die "TARGET includes codex, but the codex CLI is not on PATH"
  say "time-travel: Codex, adding marketplace $REPO"
  codex plugin marketplace add "$REPO" >/dev/null 2>&1 \
    || codex plugin marketplace upgrade "$NAME" >/dev/null 2>&1 \
    || die "could not add the Codex marketplace. Run 'gh auth setup-git' and try again."
  say "time-travel: Codex, installing plugin"
  codex plugin add "$NAME@$NAME" >/dev/null \
    || die "the Codex install failed. Run it by hand to see why: codex plugin add $NAME@$NAME"
fi

mkdir -p "${TIME_TRAVEL_HOME:-$HOME/.time-travel}/trips"

say ""
say "time-travel installed. It loads on the next session."
say ""
[ "$want_claude" = yes ] && say "  Claude Code > /time-travel:premortem <your plan, or a path to it>"
[ "$want_codex" = yes ]  && say "  Codex       > \$premortem <your plan, or a path to it>"
say ""
say "Trips are written to ${TIME_TRAVEL_HOME:-$HOME/.time-travel}/trips."
