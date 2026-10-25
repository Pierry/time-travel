# Time Travel, the premortem agent

Instructions for any coding agent running Time Travel or working in this repository. Claude Code reads `agents/time-travel.md` and the `skills/` folder through the plugin. Codex reads the same `skills/` folder through `.codex-plugin/plugin.json`, and this file. Anything else reads this file.

Everything that enforces the method is plain Python with no SDK and no network. The agent layer only decides who reads which file.

# What it does

Takes a plan and writes, as if from six months ahead, the autopsy of its failure: seven causes traced to the plan, a verdict, the plan rebuilt, the rival's attack, and one measurable alarm per cause. Artifact: `$TIME_TRAVEL_HOME/trips/<YYYY-MM-DD>-<slug>/trip.md`, default `~/.time-travel`, copied from `templates/trip.md`.

# Method

Six sections on one file, filled in order, gated after each.

0. Plan: the plan cut into numbered details D1..Dn, departure today, arrival six months later. `skills/premortem/SKILL.md`
1. Autopsy: seven causes, most probable first, each traced to a detail or a cut, each walked month 1 to 6. `skills/autopsy/SKILL.md`
2. Verdict: most likely, most dangerous, why they differ, the hidden assumption, the fatal flaw. `skills/verdict/SKILL.md`
3. Rebuild: every cause closed by a change; 3 to 5 checks with the result that means quit. `skills/rebuild/SKILL.md`
4. Adversary: who gains from the failure, where they attack, launch week, blind side, counter. `skills/adversary/SKILL.md`
5. Alarms: one per cause, a signal, a threshold with a number, a check week. `skills/alarm/SKILL.md`

Full persona, limits and the closing reply: `agents/time-travel.md`.

# The gate

```bash
python3 sensors/trip_lint.py --artifact <trip.md> --phase <plan|autopsy|verdict|rebuild|adversary|alarm|all>
```

Exit 1 means fix the trip before the next leg. Codex has no write hook: run the gate yourself after each leg. Two repairs at most, then stop and say what is stuck.

# The rules that matter most

- Every cause traces to a plan detail (`D3`) or to `cut: <what the plan left out>`. No generic advice
- Likelihoods in percent, most probable first, never rising
- Never reassure. The gate refuses "don't worry", "great plan", "good luck" and their Portuguese twins
- Say the fatal flaw with every letter: `yes: <flaw>` or `no: <why>`
- The adversary is a role, never a real named person
- Analyse, never execute: no messages, events or purchases unless asked for that exact action

# Working on this repository

```bash
python3 sensors/repo_lint.py          # structure, versions, badges, house style
python3 sensors/test_sensors.py       # every gate rule both ways
python3 scripts/test_alarms_ics.py    # the calendar export
```

Standard library only. A false positive destroys trust in a gate, so every rule has a case that must pass as well as one that must be caught.

Changing behaviour: bump `version` in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and `.codex-plugin/plugin.json`, and add the entry to `CHANGELOG.md`. CI refuses a PR that changes the plugin without a new version, and the merge to `main` tags and releases it.

Every file is in English. No en or em dashes in prose (`repo_lint` refuses them), no emoji, numbers with their source.
