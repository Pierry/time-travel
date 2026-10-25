#!/usr/bin/env bash
# PostToolUse hook: every write of a trip.md runs the gate on the legs written
# so far. A blocker comes back to the model as exit 2, with the findings on
# stderr, so the next leg does not start over a broken one.
#
# Any other file, or a trip with nothing filled yet, passes untouched.
# TIME_TRAVEL_GATE=off turns the hook off.
set -uo pipefail

[ "${TIME_TRAVEL_GATE:-on}" = "off" ] && exit 0

root="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
path="$(python3 -c 'import json,sys
try:
    print((json.load(sys.stdin).get("tool_input") or {}).get("file_path") or "")
except Exception:
    print("")' 2>/dev/null)"

case "$path" in
  */trip.md|trip.md) ;;
  */docs/premortem/*.md) ;;
  *) exit 0 ;;
esac
[ -f "$path" ] || exit 0
grep -q '^## 0\. Plan' "$path" || exit 0

if ! out="$(python3 "$root/sensors/trip_lint.py" --artifact "$path" --phase auto 2>&1)"; then
  printf 'time-travel gate refused %s\n%s\n' "$path" "$out" >&2
  exit 2
fi
exit 0
