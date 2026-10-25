#!/usr/bin/env python3
"""
The repository checks itself.

A leg with no skill, a skill with a broken frontmatter, three manifests that
disagree on the version, a release with no changelog entry, a badge that lies
about the version or the test count, a dash in prose: each one fails here
before it reaches main.

    python3 sensors/repo_lint.py
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "sensors"))

import trip_lint as t  # noqa: E402

MANIFESTS = [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".codex-plugin/plugin.json"]
SKILLS = ["premortem", "autopsy", "verdict", "rebuild", "adversary", "alarm"]
PROSE = ["README.md", "AGENTS.md", "CHANGELOG.md", "agents", "skills", "templates", "examples"]
DASHES = re.compile("[–—]")
TEST_FILES = ["sensors/test_sensors.py", "scripts/test_alarms_ics.py"]


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def count_tests() -> int:
    total = 0
    for rel in TEST_FILES:
        suite = unittest.defaultTestLoader.discover(str(ROOT / Path(rel).parent), pattern=Path(rel).name)
        total += suite.countTestCases()
    return total


def version() -> str:
    return json.loads((ROOT / ".claude-plugin/plugin.json").read_text())["version"]


def check() -> list[str]:
    errors: list[str] = []

    # Every leg of the gate has a skill, and every skill is well formed.
    for name in SKILLS:
        path = ROOT / "skills" / name / "SKILL.md"
        if not path.exists():
            errors.append(f"skills/{name}/SKILL.md is missing")
            continue
        fm = frontmatter(path)
        if fm.get("name") != name:
            errors.append(f"skills/{name}/SKILL.md frontmatter name is {fm.get('name')!r}, expected {name!r}")
        if len(fm.get("description", "")) < 40:
            errors.append(f"skills/{name}/SKILL.md has no real description; it is what makes the skill trigger")
    legs = {p for p in t.PHASES if p != "plan"}
    for leg in legs:
        if leg not in SKILLS:
            errors.append(f"gate leg {leg!r} has no skill")
    agent = (ROOT / "agents/time-travel.md").read_text(encoding="utf-8")
    for name in SKILLS:
        if f"time-travel:{name}" not in agent:
            errors.append(f"agents/time-travel.md never names the skill time-travel:{name}")

    # The template carries every section the gate reads.
    template = (ROOT / "templates/trip.md").read_text(encoding="utf-8")
    numbers = set(t.sections(template))
    for i in range(len(t.PHASES)):
        if str(i) not in numbers:
            errors.append(f"templates/trip.md has no section {i}")

    # One version, everywhere it is declared.
    v = version()
    for rel in MANIFESTS:
        data = json.loads((ROOT / rel).read_text())
        if data.get("version") != v:
            errors.append(f"{rel} declares version {data.get('version')}, plugin.json declares {v}")
    if f"## [{v}]" not in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"):
        errors.append(f"CHANGELOG.md has no `## [{v}]` entry")

    # The README does not lie.
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"badge/release-v([\d.]+)-", readme)
    if not m or m.group(1) != v:
        errors.append(f"README release badge says {m.group(1) if m else 'nothing'}, the version is {v}")
    m = re.search(r"badge/tests-(\d+)-", readme)
    n = count_tests()
    if not m or int(m.group(1)) != n:
        errors.append(f"README tests badge says {m.group(1) if m else 'nothing'}, there are {n} tests")

    # Nothing left from the scaffold.
    for rel in MANIFESTS + [".agents/plugins/marketplace.json", "README.md", "install.sh"]:
        if "__OWNER__" in (ROOT / rel).read_text(encoding="utf-8"):
            errors.append(f"{rel} still has the __OWNER__ placeholder")

    # Hooks parse and point at files that exist.
    hooks = json.loads((ROOT / "hooks/hooks.json").read_text())
    for group in hooks.get("hooks", {}).values():
        for entry in group:
            for h in entry.get("hooks", []):
                for script in re.findall(r"hooks/[\w.-]+\.sh", h.get("command", "")):
                    if not (ROOT / script).exists():
                        errors.append(f"hooks.json runs {script}, which does not exist")

    # The example the README shows passes the gate it advertises.
    example = (ROOT / "examples/invoice-nudge/trip.md").read_text(encoding="utf-8")
    hard = [f for f in t.run(example, "all") if f.severity == "hard"]
    if hard:
        errors.append(f"examples/invoice-nudge/trip.md fails its own gate: {hard[0]}")

    # House style: no en or em dash in prose.
    for rel in PROSE:
        base = ROOT / rel
        files = [base] if base.is_file() else sorted(base.rglob("*.md"))
        for f in files:
            for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                if DASHES.search(line):
                    errors.append(f"{f.relative_to(ROOT)}:{i} has an en or em dash; use a comma, a colon or two sentences")

    return errors


def main() -> int:
    errors = check()
    for e in errors:
        print(f"repo_lint: [FAIL] {e}")
    if errors:
        print(f"repo_lint: {len(errors)} problem(s)")
        return 1
    print(f"repo_lint: ok (version {version()}, {count_tests()} tests)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
