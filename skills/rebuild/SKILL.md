---
name: rebuild
description: Leg 3 of Time Travel. Writes section 3 of the trip file - the plan rewritten with every failure mode resolved, showing what changed and why, and a pre-launch checklist of 3 to 5 things to confirm before executing anything, each with the result that means quit for good. Use after the verdict leg of /time-travel:premortem passes the gate.
---

# Rebuild

> Rewrite my plan with each of these failure modes resolved. Show what changed and why. Then give me a pre-launch checklist with 3 to 5 things I need to confirm before executing anything, and tell me which result in each one would mean I should give up for good.

Fill section 3.

## The change table

| Change | Closes | Why |
|---|---|---|

- `Change`: what is different in the plan, concrete enough to execute: the new number, the new order, the dropped feature, the added person.
- `Closes`: the causes it resolves, as `Cause 1, Cause 4`. Every cause from 1 to 7 is closed by at least one change; the gate counts.
- `Why`: the mechanism by which the change stops that death.

Start with the fatal flaw if the verdict found one. Prefer changes that close several causes. A change that only adds effort ("work harder on marketing") closes nothing.

## Pre-launch checklist

| Confirm | Quit if |
|---|---|

Three to five items. Each one is a cheap test the person can run before spending the budget, aimed at the hidden assumption and the most dangerous cause first. `Quit if` is a measured result ("fewer than 5 of 15 would pay"), never a feeling. This is the part of the trip that saves the most money; write it so it gets done.

## Gate

```bash
python3 "<root>/sensors/trip_lint.py" --artifact <trip.md> --phase rebuild
```
