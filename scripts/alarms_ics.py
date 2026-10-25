#!/usr/bin/env python3
"""
Turn the alarms of a trip into calendar events.

Reads section 5 of a trip file and writes one all day event per alarm, on the
last day of its check week counted from the departure date (week 1 ends six
days after departure), or on the date the alarm names. Each event carries the
signal and the threshold, and a reminder at 09:00 that day.

Standard library only. Writes a file; never touches a calendar.

    python3 scripts/alarms_ics.py --artifact trip.md --out alarms.ics
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "sensors"))

import trip_lint as t  # noqa: E402


def check_day(departure: date, when: str) -> date | None:
    week = t.WEEK.search(when)
    if week:
        return departure + timedelta(days=7 * int(week.group(1)) - 1)
    return t.iso(when)


def alarms(text: str) -> list[dict]:
    secs = t.sections(text)
    departure = t.iso(t.field(secs.get("0", ""), "Departure"))
    if departure is None:
        raise ValueError("section 0 has no Departure date; run the gate first")
    names = {n: name for n, name, _ in t.causes(text)}
    out = []
    for row in t.table_rows(secs.get("5", "")):
        if len(row) < 4:
            continue
        refs = t.cause_refs(row[0])
        day = check_day(departure, row[3])
        if len(refs) != 1 or day is None:
            continue
        n = next(iter(refs))
        out.append({"cause": n, "name": names.get(n, ""), "signal": row[1], "threshold": row[2], "when": row[3], "day": day})
    return out


def escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def fold(line: str) -> str:
    """RFC 5545: lines longer than 75 octets continue on the next line after a space."""
    raw = line.encode("utf-8")
    if len(raw) <= 75:
        return line
    parts, chunk = [], b""
    for ch in line:
        b = ch.encode("utf-8")
        if len(chunk) + len(b) > (75 if not parts else 74):
            parts.append(chunk.decode("utf-8"))
            chunk = b""
        chunk += b
    parts.append(chunk.decode("utf-8"))
    return "\r\n ".join(parts)


def ics(text: str, trip_id: str, now: datetime | None = None) -> str:
    stamp = (now or datetime.now(timezone.utc)).strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//time-travel//premortem alarms//EN",
        "CALSCALE:GREGORIAN",
        f"X-WR-CALNAME:{escape('Premortem alarms: ' + trip_id)}",
    ]
    for a in alarms(text):
        uid = hashlib.sha1(f"{trip_id}:{a['cause']}:{a['signal']}".encode()).hexdigest()[:16]
        summary = f"Alarm, cause {a['cause']}: {a['name']}" if a["name"] else f"Alarm, cause {a['cause']}"
        description = f"Signal: {a['signal']}\nRings at: {a['threshold']}\nCheck: {a['when']}\nTrip: {trip_id}"
        lines += [
            "BEGIN:VEVENT",
            f"UID:{uid}@time-travel",
            f"DTSTAMP:{stamp}",
            f"DTSTART;VALUE=DATE:{a['day']:%Y%m%d}",
            f"DTEND;VALUE=DATE:{a['day'] + timedelta(days=1):%Y%m%d}",
            f"SUMMARY:{escape(summary)}",
            f"DESCRIPTION:{escape(description)}",
            "BEGIN:VALARM",
            "ACTION:DISPLAY",
            "TRIGGER:PT9H",
            f"DESCRIPTION:{escape(summary)}",
            "END:VALARM",
            "END:VEVENT",
        ]
    lines.append("END:VCALENDAR")
    return "\r\n".join(fold(line) for line in lines) + "\r\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Export the alarms of a trip to an .ics calendar file.")
    ap.add_argument("--artifact", required=True, help="path to trip.md")
    ap.add_argument("--out", default="-", help="output .ics path, or - for stdout (default)")
    args = ap.parse_args(argv)
    path = Path(args.artifact)
    if not path.exists():
        print(f"alarms_ics: artifact not found: {path}", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8")
    try:
        body = ics(text, path.parent.name if path.name == "trip.md" else path.stem)
    except ValueError as e:
        print(f"alarms_ics: {e}", file=sys.stderr)
        return 1
    if args.out == "-":
        sys.stdout.write(body)
    else:
        Path(args.out).write_text(body, encoding="utf-8", newline="")
        print(f"alarms_ics: {body.count('BEGIN:VEVENT')} alarms written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
