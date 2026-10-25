Arrival is 2027-04-25. The most likely way Nudge dies is a single launch spike with nothing after it. Product Hunt, 1,800 followers and an r/freelance post bring one week of trials in the week before Christmas, and nothing in the plan brings a second week. By April that leaves about 17 paying customers against the target of 200.

**Verdict**
- **Most likely:** Cause 1, one launch spike, then silence (60%). You can recover from it: you lose months but can relaunch.
- **Most dangerous:** Cause 7. An AI-written final notice goes to a freelancer's biggest client over an invoice that was already paid or disputed, and the story gets posted in r/freelance. It's only 20% likely, but it can't be undone: it damages a customer's income and closes the one community channel the plan sells into.
- **Fatal flaw:** yes. The distribution as written can't reach the goal.
  - 200 paying customers at a typical 10–15% trial-to-paid rate means roughly 1,300–2,000 trials.
  - At 2–4% of visitors starting a trial, that means 30,000–100,000 visitors.
  - Your three channels plus $2,000 of ads deliver perhaps 5,000–10,000. These are typical ranges for this kind of launch, not measurements, but the goal is off by a factor of five to ten.

**Hidden assumption:** that late invoices are a monthly pain freelancers will pay $29/month to hand to software that writes to their clients. Four of the seven causes rest on it, and the plan hasn't tested it with a single freelancer. In reality the pain may come once a quarter, and Stripe and QuickBooks already send reminders for free.

**Pre-launch checklist**

| Confirm | Quit if |
|---|---|
| By week 3: interview 20 freelancers about how many invoices went late in the last 90 days | Fewer than 6 of 20 had 2 or more late invoices |
| By week 4: sell a hand-run month of invoice chasing at $29, paid up front | Fewer than 5 people pay |
| By week 4: show each payer the free reminders in their Stripe or QuickBooks next to Nudge | 3 or more of the first 5 say the free one is enough |
| By week 12, before the public launch: count waitlist emails | Fewer than 150 |
| During the hand-run month: count how often payers approve the escalation emails | Fewer than half get approved, or 2 of 5 payers refuse any email to their client |

The rebuild also moves the launch to week 13 (2027-01-17) and cuts the MVP to one integration plus manual entry. It resets the six-month goal to 60 paying customers, holds the ad budget until trial-to-paid has been measured, and requires one-click approval for every step after the friendly reminder. In the rival's playbook, the attack you wouldn't see coming is a funded competitor republishing an expanded version of your free email templates. Because its site already ranks in search, it takes the traffic the rebuilt plan counts on after the launch spike.

**Earliest alarms**
- **Week 4** (Nov 15–21): 3 or more of the first 5 hand-run customers say the free reminder is enough (Cause 4).
- **Week 7** (Dec 6–12): no real overdue invoice from a real account has synced end to end (Cause 2).
- **Week 8** (Dec 13–19): fewer than 75 waitlist emails (Cause 1), or fewer than 1.5 late invoices per hand-run customer over 30 days (Cause 3).

The trip file passed the gate on every leg and once more on the whole file:
`$TIME_TRAVEL_HOME/trips/2026-10-25-nudge-launch/trip.md`

Nothing was sent or added to a calendar. To export the alarms to a calendar file you can import:

```bash
python3 <plugin root>/scripts/alarms_ics.py --artifact "$TIME_TRAVEL_HOME/trips/2026-10-25-nudge-launch/trip.md" --out alarms.ics
```
