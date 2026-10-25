# Changelog

Format [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versions [SemVer](https://semver.org/). The version lives in `.claude-plugin/plugin.json`; every merge to `main` that carries a new version is tagged and released from the entry below.

## [Unreleased]

## [0.1.1] - 2026-10-25

- Python 3.10 is the supported minimum. GitHub's Ubuntu 26.04 runners no longer ship 3.9, so 3.9 could not be tested; CI now runs on 3.10 and 3.14 without fail fast.

## [0.1.0] - 2026-10-25

First trip.

- `/time-travel:premortem <plan>`: one entry point that runs the five legs on one trip file, `~/.time-travel/trips/<date>-<slug>/trip.md`.
- Five legs, one skill each: autopsy (seven causes, traced and walked month by month), verdict (most likely against most dangerous, hidden assumption, fatal flaw), rebuild (every cause closed, a 3 to 5 item checklist with quit conditions), adversary (attack point, launch week, blind side, counter), alarm (one measurable alarm per cause with the week to check).
- `sensors/trip_lint.py`: the deterministic gate between legs, standard library only. Refuses untraced causes, skipped months, a verdict that contradicts the likelihoods, open causes, alarms with no number or no week, and reassurance in English or Portuguese.
- `scripts/alarms_ics.py`: exports the alarms to an `.ics` file, one all day event per alarm with a 09:00 reminder.
- Claude Code plugin with a PostToolUse hook that gates every write of a trip file; Codex plugin sharing the same skills; `AGENTS.md` for any other agent.
- CI on every push and PR (repository lint, 79 tests, the example trip through the gate, planted breaks the gate must refuse); release and tag on every merge to `main` that bumps the version, with a moving major tag.
