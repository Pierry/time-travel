---
name: autopsy
description: Leg 1 of Time Travel. Writes section 1 of the trip file, the autopsy of a plan that failed six months from now - the seven most probable causes of death in order, each with what killed it, how it happened month by month, the premise of the person that let it happen, and the first warning sign. Every cause traces to a plan detail or to something the plan cut. Use after leg 0 of /time-travel:premortem, or alone on a trip file whose section 0 passes the gate.
---

# Autopsy

> We are six months ahead and this plan failed completely. Write the autopsy.

Fill section 1 of the trip with seven `### Cause n: <name>` blocks, Cause 1 the most probable.

For each cause:

- `Likelihood`: your honest estimate in percent. Never higher than the cause above it. They do not sum to 100.
- `Killed by`: the mechanism in one sentence. What happened, not what was missing.
- `Traces to`: the detail from section 0 that made it possible (`D3`), or `cut: <what the plan never mentioned>`. Most causes should trace to a detail the person gave; an autopsy built only on cuts is generic advice, and the gate warns.
- `Premise`: the belief of the person that let it happen, in their voice.
- `First warning sign`: the earliest thing they would have seen, with a number and a moment.
- The month table, 1 to 6: what happened each month. A number when one fits. Month 6 is the death.

## Where the seven come from

Walk the plan detail by detail and ask what kills it: the channel that dries up, the number that was a guess, the person who is a single point of failure, the dependency on someone else's approval, the budget that buys one attempt, the success metric nobody measures weekly. Then ask what the plan never says: who the competitor is, what happens when the first customer says no, who covers when the owner is out.

Rank by likelihood, not by drama. The cause that is boring and probable goes above the one that is spectacular and rare; the verdict leg is where danger gets its own say.

No generic advice: "poor execution", "market conditions", "lack of focus" are not causes. If a cause would fit any plan, it is not finished.

## Gate

```bash
python3 "<root>/sensors/trip_lint.py" --artifact <trip.md> --phase autopsy
```
