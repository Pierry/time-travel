# How this example was recorded

A real, unedited run of the plugin, not a hand-written sample.

| | |
|---|---|
| Date | 2026-10-25 |
| Command | `claude -p --setting-sources project --plugin-dir <repo> --output-format stream-json "/time-travel:premortem plan.md"` |
| Input | [`plan.md`](plan.md), nothing else |
| Model | `claude-opus-5-5` |
| Wall time | 205 s |
| Cost | $0.81 |
| Turns | 18 |
| Gate calls | 6, one per leg plus `--phase all` at the end; 6 of 6 returned `trip_lint: ok` on the first try, no repair round |
| Plugin version | 0.1.1 |

`--setting-sources project` keeps the recorder's personal settings out of the run, so the output is what a fresh install produces.

## Files

| File | What it is |
|---|---|
| [`plan.md`](plan.md) | the plan, exactly as given |
| [`reply.md`](reply.md) | the reply printed in the conversation |
| [`trip.md`](trip.md) | the trip file the agent wrote, all six sections |
| [`alarms.ics`](alarms.ics) | the 7 alarms exported with `scripts/alarms_ics.py`, ready to import |

## What was changed after the run

Two local paths in `reply.md`: the scratch folder the run wrote to was removed, and the absolute path of the calendar export command became `<plugin root>`. Nothing else was touched.

## Reproduce it

```bash
claude plugin install time-travel@time-travel
cd examples/invoice-nudge
claude -p "/time-travel:premortem plan.md"
```

Model output varies between runs. The structure does not, because the gate refuses any trip without it.
