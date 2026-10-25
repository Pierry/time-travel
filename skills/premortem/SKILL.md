---
name: premortem
description: The one entry point of Time Travel. Takes a plan (pasted text, a file path, or the plan discussed in the conversation), travels six months ahead to the day it failed, and writes the trip file in five legs (autopsy, verdict, rebuild, adversary, alarm) with a deterministic gate between them. Use for "/time-travel:premortem", "premortem this plan", "pre-mortem", "what kills this plan", "faz o pré-mortem do meu plano", "onde esse plano vai morrer".
argument-hint: "<plan text | path/to/plan.md>"
---

# Premortem

The single command a person types. Everything else in Time Travel is a leg this skill runs in order.

```
/time-travel:premortem launch my SaaS in 8 weeks with $5k and 200 customers in 6 months
/time-travel:premortem docs/plans/q1-migration.md
```

## 1. Resolve the plan

From `$ARGUMENTS` and the conversation:

| Given | Plan |
|---|---|
| a path to a file | read it whole |
| pasted text | that text |
| nothing, but a plan was discussed above | that plan; quote the parts you are using |
| nothing at all | ask for the plan: what, by when, with what budget, and what success looks like |

A plan with no goal, or a one liner, gets at most three questions in one message (timeline, budget, success). What stays unanswered is written as `not given`.

## 2. Leg 0, the plan

Read `<root>/agents/time-travel.md` once and follow it. `<root>` is `${CLAUDE_PLUGIN_ROOT}` under Claude Code; elsewhere it is the folder two levels above this file.

Resolve the trips folder in the shell, never by assuming the default, because the person may have set `TIME_TRAVEL_HOME`:

```bash
echo "${TIME_TRAVEL_HOME:-$HOME/.time-travel}/trips"
```

Copy `<root>/templates/trip.md` to `<that folder>/<YYYY-MM-DD>-<slug>/trip.md`. Fill section 0:

- Departure is today. Arrival is the same day six months later.
- Goal, Timeline, Budget and Success looks like in the person's words, `not given` where they gave nothing.
- Details: every concrete thing the plan commits to (a date, a number, an owner, a channel, a dependency, a price) as `n. Dn: ...`. Eight to twelve is usual; three is the floor. These are what the causes trace back to, so a detail you skip here is a cause you cannot cite later.

Gate it:

```bash
python3 "<root>/sensors/trip_lint.py" --artifact <trip.md> --phase plan
```

## 3. Run the legs

In order, each one gated before the next: `time-travel:autopsy`, `time-travel:verdict`, `time-travel:rebuild`, `time-travel:adversary`, `time-travel:alarm`. Then run the gate once more with `--phase all`.

Run them here, in the main conversation, so the person can interrupt between legs.

## 4. Close

End with the closing of `agents/time-travel.md`. Nothing is sent, scheduled or published; the calendar export is a command the person runs.
