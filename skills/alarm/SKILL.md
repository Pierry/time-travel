---
name: alarm
description: Leg 5 of Time Travel. Writes section 5 of the trip file - for each of the seven failure modes, one measurable signal that shows it is starting to happen and the exact week to check it. Concrete alarms with a number, never a feeling. Exports to an .ics calendar on request. Use after the adversary leg of /time-travel:premortem passes the gate.
---

# Alarm

> For each failure mode, give me a measurable signal that shows it is starting to happen and the exact week I should check. I want concrete alarms, ones I can measure.

Fill section 5, one row per cause:

| Cause | Signal | Threshold | Check week |
|---|---|---|---|

- `Cause`: `Cause n`, one alarm each, all seven.
- `Signal`: what to measure and where it lives (the analytics dashboard, the bank statement, the CRM, the weekly hours log). Something the person can open and read in five minutes.
- `Threshold`: the number that means the cause has started. It carries a digit; "low engagement" is not a threshold.
- `Check week`: `Week n` counted from departure (1 to 26), or a date inside the trip. Pick the earliest week the signal can be read, which is usually well before the month the autopsy says the damage shows.

Start from each cause's `First warning sign` in section 1; the alarm is that sign made measurable and put on a calendar.

## Gate

```bash
python3 "<root>/sensors/trip_lint.py" --artifact <trip.md> --phase alarm
python3 "<root>/sensors/trip_lint.py" --artifact <trip.md> --phase all
```

## Calendar

Offer the export; do not run it into the person's calendar yourself:

```bash
python3 "<root>/scripts/alarms_ics.py" --artifact <trip.md> --out alarms.ics
```

Each alarm becomes an all day event on its check week, with the signal and the threshold in the description. The person imports the file.
