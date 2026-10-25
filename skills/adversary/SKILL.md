---
name: adversary
description: Leg 4 of Time Travel. Writes section 4 of the trip file - plays the person who gains the most if the plan goes wrong (a competitor, a rival, someone who wants the seat), who has seen the plan, and says exactly where they would attack, what they would do in launch week, and the blow the person would never see coming. Use after the rebuild leg of /time-travel:premortem passes the gate.
---

# Adversary

> Now play the person who gains the most if my plan goes wrong. A competitor, a rival, someone who wants my seat. You have seen my plan. Tell me exactly where you would attack, what you would do in my launch week, and the blow I would never see coming.

Fill section 4, playing to win:

- `Who`: the role that profits most from the failure: the incumbent product, the rival team that loses budget if this wins, the vendor that loses the contract. A role, never a real named private person.
- `Attack point`: exactly where, tied to a detail (`D5`) or a cause. The adversary read the plan; they attack what it depends on most.
- `Launch week`: what they do in the week the plan launches, dated against the plan's own timeline.
- `Blind side`: the move the person would never see coming, because it hits something the plan treats as fixed (a partner's API, a price, an approval, a person's loyalty).
- `Counter`: the single change in the rebuilt plan that blunts the attack, or the one that has to be added.

Attack the rebuilt plan, not the original one: the person will execute the rebuild.

## Gate

```bash
python3 "<root>/sensors/trip_lint.py" --artifact <trip.md> --phase adversary
```
