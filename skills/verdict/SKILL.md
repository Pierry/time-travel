---
name: verdict
description: Leg 2 of Time Travel. Writes section 2 of the trip file - of the seven causes, which is the most likely and which is the most dangerous and why they differ, the biggest hidden assumption the person holds without noticing, and whether the plan has a fatal flaw, said with every letter. Use after the autopsy leg of /time-travel:premortem passes the gate.
---

# Verdict

> Of these seven failures, which is the most likely and which is the most dangerous, and why are they different? Then point out the biggest hidden assumption. Be direct. If the plan has a fatal flaw, say it with every letter.

Fill section 2:

- `Most likely`: `Cause n` and its name. It is the cause with the highest likelihood in section 1; the gate refuses a verdict that contradicts the autopsy.
- `Most dangerous`: `Cause m` and its name. The one whose damage is largest or least reversible if it happens, whatever its likelihood.
- `Why they differ`: probability against damage. Why the one that will probably happen is not the one that hurts most. When it is the same cause, start with `same:` and say why the most probable failure is also the worst.
- `Hidden assumption`: the premise underneath several causes at once, the one the person never wrote down because it did not feel like an assumption. Look at the `Premise` lines of the seven causes; the hidden assumption is usually what three of them share.
- `Fatal flaw`: `yes: <the flaw>` when the plan as written cannot succeed, or `no: <why none of the seven is fatal on its own>`. No hedging. "It could be a concern" is not an answer.

## Gate

```bash
python3 "<root>/sensors/trip_lint.py" --artifact <trip.md> --phase verdict
```
