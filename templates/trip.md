# Trip <ID>

One file per plan, at `$TIME_TRAVEL_HOME/trips/<ID>/trip.md` (default `~/.time-travel/trips/`). `<ID>` is the date of departure plus a short slug, `2026-10-25-pricing-relaunch`. Sections are numbered because the gate reads them by number. Do not rename, reorder or delete a section: fill it or write `pending: <what is missing>`.

Field keys stay in English so the gate can read them. Values are written in the language the person used.

## 0. Plan

The plan exactly as the person gave it, cut into numbered details. Every cause of death in section 1 points back to one of these, or to something the plan left out.

- Departure: <YYYY-MM-DD, today>
- Arrival: <YYYY-MM-DD, six months later, the day the plan is declared dead>
- Goal: <what the plan wants, in the person's words>
- Timeline: <the schedule as given, or `not given`>
- Budget: <money, people, hours, or `not given`>
- Success looks like: <the outcome the person would call a win, with a number when they gave one>

### Details

1. D1: <one concrete detail from the plan: a date, an owner, a channel, a number, a dependency>
2. D2: <...>
3. D3: <...>

## 1. Autopsy

Seven causes of death, most probable first. Each one is traced to a detail above (`D2`) or to something the plan cut (`cut: <what is missing>`). No generic advice.

### Cause 1: <short name of what killed the plan>

- Likelihood: <percent, the highest of the seven>
- Killed by: <the mechanism, one sentence>
- Traces to: <D1 | cut: what the plan never mentioned>
- Premise: <the belief of the person that let this happen>
- First warning sign: <what they would have seen first, and when>

| Month | What happened |
|---|---|
| 1 | <...> |
| 2 | <...> |
| 3 | <...> |
| 4 | <...> |
| 5 | <...> |
| 6 | <...> |

### Cause 2: <...>

(repeat the block above until Cause 7, likelihood never rising)

## 2. Verdict

- Most likely: <Cause n, and its name>
- Most dangerous: <Cause m, and its name>
- Why they differ: <probability against damage, why the one that will probably happen is not the one that hurts most; when n equals m, start with `same:` and say why>
- Hidden assumption: <the biggest premise the person holds without noticing>
- Fatal flaw: <yes: the flaw, said plainly | no: why none of the seven is fatal on its own>

## 3. Rebuild

The plan rewritten with every failure mode resolved. Each change names the causes it closes; every cause from 1 to 7 is closed by at least one change.

| Change | Closes | Why |
|---|---|---|
| <what changes in the plan> | <Cause 1, Cause 4> | <why this closes them> |

### Pre-launch checklist

Three to five things to confirm before executing anything, each with the result that means quit for good.

| Confirm | Quit if |
|---|---|
| <what to confirm, and how> | <the measured result that kills the plan> |

## 4. Adversary

The person who gains the most if the plan goes wrong, playing to win.

- Who: <a competitor, a rival, someone who wants the seat; a role, never a real named person>
- Attack point: <exactly where they hit, tied to a detail or a cause>
- Launch week: <what they do the week the plan launches>
- Blind side: <the blow the person would never see coming>
- Counter: <the one move in the rebuilt plan that blunts it>

## 5. Alarms

One measurable alarm per cause. A threshold carries a number; a check week is a week number or a date.

| Cause | Signal | Threshold | Check week |
|---|---|---|---|
| <Cause 1> | <what to measure and where> | <the number that means it is starting> | <Week 4 or YYYY-MM-DD> |
