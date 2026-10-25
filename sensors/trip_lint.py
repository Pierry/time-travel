#!/usr/bin/env python3
"""
The gate between the five legs of a trip.

Reads one trip file (`templates/trip.md` filled in) and refuses the next leg
while the current one is missing evidence: seven causes, each traced to the
plan and walked month by month; a verdict that names two causes; a rebuild that
closes all seven; an adversary with a launch week; one measurable alarm per
cause. Reassurance anywhere in the file is refused, because the person asked
never to be reassured.

Standard library only. Exit 0 releases the leg, exit 1 lists what to fix.

    python3 sensors/trip_lint.py --artifact trip.md --phase all
    python3 sensors/trip_lint.py --artifact trip.md --phase auto

Artifact contract: numbered level-2 sections, `## <n>. <Name>`. The number is
the stable key; the name is prose and may change without breaking the gate.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

CAUSES = 7
MONTHS = 6
CHECKLIST = (3, 5)

PHASES = ["plan", "autopsy", "verdict", "rebuild", "adversary", "alarm"]
SECTION_OF = {name: str(i) for i, name in enumerate(PHASES)}

PLACEHOLDER = re.compile(r"<[^<>\n]{1,240}>")
SECTION = re.compile(r"^##\s+(\d+)\.\s*(.*)$", re.MULTILINE)
CAUSE_HEADING = re.compile(r"^###[ \t]+Cause[ \t]+(\d+)[ \t]*:[ \t]*(.*)$", re.MULTILINE | re.IGNORECASE)
CAUSE_REF = re.compile(r"\bcause\s+(\d+)\b", re.IGNORECASE)
DETAIL = re.compile(r"^\s*\d+\.\s+D(\d+)\s*:\s*(.+)$", re.MULTILINE)
DETAIL_REF = re.compile(r"\bD(\d+)\b")
ISO_DATE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
WEEK = re.compile(r"\b(?:week|semana|wk)\s*(\d{1,2})\b", re.IGNORECASE)
PERCENT = re.compile(r"(\d{1,3}(?:[.,]\d+)?)\s*%")

# The person asked never to be reassured. These are the phrases a model reaches
# for when it softens a post-mortem. English and Brazilian Portuguese, because
# those are the languages the trips are written in so far.
REASSURANCE = [
    r"don'?t worry",
    r"no need to worry",
    r"you'?ll be fine",
    r"you will be fine",
    r"it'?ll be fine",
    r"great plan",
    r"solid plan",
    r"strong plan",
    r"good luck",
    r"rest assured",
    r"não se preocupe",
    r"nao se preocupe",
    r"fique tranquil[oa]",
    r"vai dar (tudo )?certo",
    r"(ótimo|otimo|excelente|bom) plano",
    r"boa sorte",
]
REASSURANCE_RE = re.compile(r"\b(" + "|".join(REASSURANCE) + r")\b", re.IGNORECASE)


class Finding:
    """One gate finding. Hard blocks the leg, soft only warns."""

    def __init__(self, section: str, message: str, severity: str = "hard"):
        self.section = section
        self.message = message
        self.severity = severity

    def __str__(self) -> str:
        mark = "FAIL" if self.severity == "hard" else "warn"
        return f"[{mark}] section {self.section}: {self.message}"


# Parsing


def sections(text: str) -> dict[str, str]:
    """Return {section_number: body}. Body excludes the heading itself."""
    marks = list(SECTION.finditer(text))
    out: dict[str, str] = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        out[m.group(1)] = text[m.end():end].strip("\n")
    return out


def field(body: str, key: str) -> str | None:
    """
    Read `- Key: value`, tolerant to case.

    Horizontal whitespace only around the colon: `\\s*` would match a newline,
    so an empty field would capture the next line and look filled.
    """
    pattern = re.compile(
        r"^[-*][ \t]*" + re.escape(key) + r"[ \t]*:[ \t]*(.*)$",
        re.MULTILINE | re.IGNORECASE,
    )
    m = pattern.search(body)
    return m.group(1).strip() if m else None


def table_rows(body: str) -> list[list[str]]:
    """Data rows of the first markdown table in body, without header or separator."""
    rows: list[list[str]] = []
    started = False
    for raw in body.splitlines():
        s = raw.strip()
        if not (s.startswith("|") and s.endswith("|")):
            if started:
                break
            continue
        started = True
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:] if len(rows) > 1 else []


def block_under(text: str, title_prefix: str) -> str | None:
    """Body under the first level-3 heading whose title starts with the prefix."""
    marks = list(re.finditer(r"^###\s+(.+)$", text, re.MULTILINE))
    for i, m in enumerate(marks):
        if m.group(1).strip().lower().startswith(title_prefix.lower()):
            end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
            return text[m.end():end]
    return None


def before_subsections(body: str) -> str:
    m = re.search(r"^###\s", body, re.MULTILINE)
    return body[: m.start()] if m else body


def empty(value: str | None) -> bool:
    """Missing, blank, a template placeholder, or a dangling ellipsis."""
    if value is None:
        return True
    v = value.strip()
    if not v or v in {"...", "-", "n/a", "N/A"}:
        return True
    return bool(PLACEHOLDER.search(v))


def pending(value: str | None) -> bool:
    return bool(value) and value.strip().lower().startswith("pending")


def iso(value: str | None) -> date | None:
    if not value:
        return None
    m = ISO_DATE.search(value)
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def cause_refs(value: str) -> set[int]:
    return {int(n) for n in CAUSE_REF.findall(value)}


def need(body: str, key: str, section: str, out: list[Finding]) -> str:
    value = field(body, key)
    if value is None:
        out.append(Finding(section, f"field `{key}` is missing"))
        return ""
    if pending(value):
        out.append(Finding(section, f"`{key}` is still pending: {value}"))
        return ""
    if empty(value):
        out.append(Finding(section, f"`{key}` is empty or still the template placeholder"))
        return ""
    return value


def details(text: str) -> dict[int, str]:
    body = sections(text).get("0", "")
    return {int(n): d.strip() for n, d in DETAIL.findall(body) if not empty(d)}


def causes(text: str) -> list[tuple[int, str, str]]:
    """[(number, name, body)] for every `### Cause n:` block in section 1."""
    body = sections(text).get("1", "")
    marks = list(CAUSE_HEADING.finditer(body))
    out = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        out.append((int(m.group(1)), m.group(2).strip(), body[m.end():end]))
    return out


def likelihood(value: str) -> float | None:
    m = PERCENT.search(value or "")
    return float(m.group(1).replace(",", ".")) if m else None


# Legs


def check_plan(text: str, out: list[Finding]) -> None:
    body = sections(text).get("0")
    if body is None:
        out.append(Finding("0", "section missing from the trip"))
        return
    dep = iso(need(body, "Departure", "0", out))
    arr = iso(need(body, "Arrival", "0", out))
    if field(body, "Departure") and not empty(field(body, "Departure")) and dep is None:
        out.append(Finding("0", "`Departure` is not a YYYY-MM-DD date"))
    if field(body, "Arrival") and not empty(field(body, "Arrival")) and arr is None:
        out.append(Finding("0", "`Arrival` is not a YYYY-MM-DD date"))
    if dep and arr:
        days = (arr - dep).days
        if not 170 <= days <= 200:
            out.append(Finding("0", f"the trip goes {days} days forward; the autopsy is written six months ahead (170 to 200 days)"))
    for key in ("Goal", "Timeline", "Budget", "Success looks like"):
        need(body, key, "0", out)
    found = details(text)
    if len(found) < 3:
        out.append(Finding("0", f"{len(found)} plan details listed as `n. Dn: ...`; at least 3, so the causes have something to trace to"))
    elif sorted(found) != list(range(1, len(found) + 1)):
        out.append(Finding("0", f"details are numbered {sorted(found)}; number them D1 to D{len(found)} with no gap"))


def check_autopsy(text: str, out: list[Finding]) -> None:
    if "1" not in sections(text):
        out.append(Finding("1", "section missing from the trip"))
        return
    found = causes(text)
    numbers = [n for n, _, _ in found]
    if numbers != list(range(1, CAUSES + 1)):
        out.append(Finding("1", f"causes numbered {numbers}; the autopsy has exactly {CAUSES}, Cause 1 to Cause {CAUSES} in order"))
    known = details(text)
    traced = 0
    previous: float | None = None
    for n, name, body in found:
        where = f"1, cause {n}"
        if empty(name):
            out.append(Finding(where, "the cause has no name in its heading"))
        raw = need(body, "Likelihood", where, out)
        value = likelihood(raw)
        if raw and value is None:
            out.append(Finding(where, f"`Likelihood` carries no percent: {raw}"))
        if value is not None:
            if not 0 < value <= 100:
                out.append(Finding(where, f"likelihood {value}% is outside 1 to 100"))
            if previous is not None and value > previous:
                out.append(Finding(where, f"likelihood {value}% is above the cause before it ({previous}%); most probable first"))
            previous = value
        for key in ("Killed by", "Premise", "First warning sign"):
            need(body, key, where, out)
        trace = need(body, "Traces to", where, out)
        if trace:
            refs = {int(r) for r in DETAIL_REF.findall(trace)}
            cut = trace.lower().startswith("cut:") and len(trace) > len("cut:") + 5
            missing = sorted(r for r in refs if r not in known)
            if missing:
                out.append(Finding(where, f"`Traces to` points at D{missing[0]}, which section 0 does not list"))
            elif refs:
                traced += 1
            elif not cut:
                out.append(Finding(where, "`Traces to` names no plan detail (D1) and no `cut: <what the plan left out>`"))
        months = {}
        for row in table_rows(body):
            if row and row[0].isdigit():
                months[int(row[0])] = row[1] if len(row) > 1 else ""
        if sorted(months) != list(range(1, MONTHS + 1)):
            out.append(Finding(where, f"the timeline covers months {sorted(months)}; it walks month 1 to {MONTHS}"))
        else:
            blank = [m for m, v in months.items() if empty(v) or pending(v)]
            if blank:
                out.append(Finding(where, f"month {blank[0]} of the timeline is empty"))
    if found and traced < 3:
        out.append(Finding("1", f"only {traced} causes trace to a detail the person gave; the rest are cuts. An autopsy of what was not said is generic advice", "soft"))


def check_verdict(text: str, out: list[Finding]) -> None:
    body = sections(text).get("2")
    if body is None:
        out.append(Finding("2", "section missing from the trip"))
        return
    found = {n: body_ for n, _, body_ in causes(text)}
    likely = need(body, "Most likely", "2", out)
    danger = need(body, "Most dangerous", "2", out)
    a = cause_refs(likely)
    b = cause_refs(danger)
    for key, refs, raw in (("Most likely", a, likely), ("Most dangerous", b, danger)):
        if raw and len(refs) != 1:
            out.append(Finding("2", f"`{key}` names {len(refs)} causes; it names exactly one, as `Cause n`"))
        elif raw and next(iter(refs)) not in found:
            out.append(Finding("2", f"`{key}` points at a cause the autopsy does not have"))
    if len(a) == 1 and next(iter(a)) in found:
        odds = {n: likelihood(field(b_, "Likelihood") or "") for n, b_ in found.items()}
        top = max((v for v in odds.values() if v is not None), default=None)
        chosen = odds.get(next(iter(a)))
        if top is not None and chosen is not None and chosen < top:
            out.append(Finding("2", f"`Most likely` is a {chosen}% cause while another sits at {top}%; the verdict contradicts the autopsy"))
    why = need(body, "Why they differ", "2", out)
    if why and a and a == b and not why.lower().startswith("same:"):
        out.append(Finding("2", "the same cause is most likely and most dangerous; `Why they differ` starts with `same:` and says why"))
    need(body, "Hidden assumption", "2", out)
    flaw = need(body, "Fatal flaw", "2", out)
    if flaw and not re.match(r"^(yes|no|sim|não|nao)\s*:\s*\S", flaw, re.IGNORECASE):
        out.append(Finding("2", "`Fatal flaw` starts with `yes:` and the flaw, or `no:` and why; said with every letter"))


def check_rebuild(text: str, out: list[Finding]) -> None:
    body = sections(text).get("3")
    if body is None:
        out.append(Finding("3", "section missing from the trip"))
        return
    changes = table_rows(before_subsections(body))
    if not changes:
        out.append(Finding("3", "the rebuilt plan has no change table"))
    closed: set[int] = set()
    for i, row in enumerate(changes, 1):
        if len(row) < 3 or any(empty(c) or pending(c) for c in row[:3]):
            out.append(Finding("3", f"change {i} has an empty cell; each change says what, which causes and why"))
            continue
        refs = cause_refs(row[1])
        if not refs:
            out.append(Finding("3", f"change {i} closes no cause; write `Cause n` in the Closes column"))
        closed |= refs
    if changes:
        open_ = [n for n in range(1, CAUSES + 1) if n not in closed]
        if open_:
            out.append(Finding("3", f"cause {open_[0]} is not closed by any change; {len(open_)} of {CAUSES} still open"))
    block = block_under(body, "Pre-launch checklist")
    if block is None:
        out.append(Finding("3", "`### Pre-launch checklist` is missing"))
        return
    rows = table_rows(block)
    lo, hi = CHECKLIST
    if not lo <= len(rows) <= hi:
        out.append(Finding("3", f"the checklist has {len(rows)} items; {lo} to {hi}, so it gets confirmed instead of skimmed"))
    for i, row in enumerate(rows, 1):
        if len(row) < 2 or any(empty(c) or pending(c) for c in row[:2]):
            out.append(Finding("3", f"checklist item {i} has no `Quit if`; every check says which result means give up for good"))


def check_adversary(text: str, out: list[Finding]) -> None:
    body = sections(text).get("4")
    if body is None:
        out.append(Finding("4", "section missing from the trip"))
        return
    for key in ("Who", "Attack point", "Launch week", "Blind side", "Counter"):
        need(body, key, "4", out)


def check_alarm(text: str, out: list[Finding]) -> None:
    body = sections(text).get("5")
    if body is None:
        out.append(Finding("5", "section missing from the trip"))
        return
    plan = sections(text).get("0", "")
    dep, arr = iso(field(plan, "Departure")), iso(field(plan, "Arrival"))
    rows = table_rows(body)
    seen: dict[int, int] = {}
    for i, row in enumerate(rows, 1):
        if len(row) < 4 or any(empty(c) or pending(c) for c in row[:4]):
            out.append(Finding("5", f"alarm {i} has an empty cell; cause, signal, threshold and check week"))
            continue
        refs = cause_refs(row[0])
        if len(refs) != 1:
            out.append(Finding("5", f"alarm {i} names {len(refs)} causes in its first column; one alarm per cause"))
            continue
        n = next(iter(refs))
        seen[n] = seen.get(n, 0) + 1
        if not re.search(r"\d", row[2]):
            out.append(Finding("5", f"the alarm for cause {n} has no number in its threshold; an alarm that cannot be measured never rings"))
        week = WEEK.search(row[3])
        when = iso(row[3])
        if week:
            if not 1 <= int(week.group(1)) <= 26:
                out.append(Finding("5", f"the alarm for cause {n} is checked in week {week.group(1)}; inside the six months, weeks 1 to 26"))
        elif when:
            if dep and arr and not dep <= when <= arr:
                out.append(Finding("5", f"the alarm for cause {n} is checked on {when}, outside the trip ({dep} to {arr})"))
        else:
            out.append(Finding("5", f"the alarm for cause {n} has no exact check week (`Week 4`) or date"))
    missing = [n for n in range(1, CAUSES + 1) if n not in seen]
    if missing:
        out.append(Finding("5", f"cause {missing[0]} has no alarm; {len(missing)} of {CAUSES} unwatched"))
    doubled = [n for n, c in seen.items() if c > 1]
    if doubled:
        out.append(Finding("5", f"cause {doubled[0]} has {seen[doubled[0]]} alarms; one each, the sharpest", "soft"))


def check_tone(text: str, out: list[Finding]) -> None:
    """Never reassure. Checked on every leg, over every filled section."""
    first = SECTION.search(text)
    body = text[first.start():] if first else text
    for m in REASSURANCE_RE.finditer(body):
        line = body.count("\n", 0, m.start()) + 1
        out.append(Finding("*", f"reassurance in the trip: \"{m.group(0)}\" (line {line} of the sections); the person asked never to be reassured"))


CHECKS = {
    "plan": check_plan,
    "autopsy": check_autopsy,
    "verdict": check_verdict,
    "rebuild": check_rebuild,
    "adversary": check_adversary,
    "alarm": check_alarm,
}


def reached(text: str) -> str | None:
    """The last leg with any filled field or table cell, so a hook gates only what was written so far."""
    secs = sections(text)
    last = None
    for name in PHASES:
        body = secs.get(SECTION_OF[name], "")
        values = [m.group(1) for m in re.finditer(r"^[-*][ \t]*[\w ]+:[ \t]*(.+)$", body, re.MULTILINE)]
        for table in re.split(r"\n(?!\s*\|)", body):
            for row in table_rows(table):
                values.extend(row[1:])
        if any(not empty(v) and not pending(v) for v in values):
            last = name
    return last


def run(text: str, phase: str) -> list[Finding]:
    if phase == "auto":
        phase = reached(text)
        if phase is None:
            return []
    upto = PHASES if phase == "all" else PHASES[: PHASES.index(phase) + 1]
    out: list[Finding] = []
    for name in upto:
        CHECKS[name](text, out)
    check_tone(text, out)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Gate one leg of a time-travel trip, and every leg before it.")
    ap.add_argument("--artifact", required=True, help="path to trip.md")
    ap.add_argument("--phase", default="all", choices=PHASES + ["all", "auto"], help="the leg to gate (default: all)")
    args = ap.parse_args(argv)
    path = Path(args.artifact)
    if not path.exists():
        print(f"trip_lint: artifact not found: {path}", file=sys.stderr)
        return 1
    findings = run(path.read_text(encoding="utf-8"), args.phase)
    for f in findings:
        print(f"trip_lint: {f}")
    hard = [f for f in findings if f.severity == "hard"]
    if hard:
        print(f"trip_lint: {len(hard)} blocker(s), fix the trip and run again")
        return 1
    print("trip_lint: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
