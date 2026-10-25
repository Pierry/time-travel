Arrival is 2027-04-25. By then Nudge has about 47 paying customers. Product Hunt, 1,800 Twitter followers and one Reddit post brought a single week of trials in mid-December, and nothing brought more after that. Reaching 200 customers would have taken roughly 1,000 to 1,500 trials. All six legs passed the gate (`--phase all` returned ok).

**Verdict**
- **Most likely: Cause 1 (60%).** The launch spike was the only source of customers. This is a sales and distribution failure, and time plus a second channel can fix it.
- **Most dangerous: Cause 6, "my invoicing tool already does that."** Stripe and QuickBooks, the two tools Nudge connects to, already send overdue reminders for free. If freelancers see Nudge as a $29 copy of that, no channel, trial length or price saves it. You would also only find out after the 6 weeks of building were spent.
- **Fatal flaw: yes.** No channel in the plan can bring in enough customers for the goal. At a 10% trial-to-paid rate, 200 customers needs about 2,000 trials. Your channels add up to roughly 300 to 400. The target date also falls outside this trip: "six months after launch" is week 34. At the six-month mark you will have had about 4 months of selling, and the first of those is the Christmas holidays.

**Hidden assumption:** freelancers have a late-invoice problem every month, painful enough to pay $29 for, that their invoicing tool doesn't already solve. You're also assuming they want software to email their clients in their name. Causes 2, 3, 6 and 7 all depend on this. The plan doesn't include a single conversation with a freelancer before building starts.

**Pre-launch checklist**

| Confirm | Quit if |
|---|---|
| 20 interviews: how many had an invoice more than 14 days late in the last 90 days | fewer than 8 of 20 |
| Same interviews: who would let Nudge send from their own inbox, and whether the built-in reminders are enough | fewer than 5 of 20 would let it send, or 6 or more built-in users say those reminders are enough and name no gap |
| Pre-sale: a $190 founding annual plan, charged up front to the waitlist | fewer than 10 paid by week 6, from a waitlist of at least 200 |
| Channel test: free template pages plus one newsletter sponsorship | under 150 waitlist signups by week 6, or more than $10 per signup on paid placements |
| Personal runway outside the $5,000 | under 9 months covered; don't go full time |

**Three earliest alarms**
- **Week 3, Cause 3:** fewer than 5 of 20 interviewees would let a tool email their clients.
- **Week 3, Cause 6:** 6 or more people who use the built-in reminders say those are enough.
- **Week 6, Cause 1:** fewer than 150 waitlist signups from the template pages and newsletter.

The trip file, with the full rebuilt plan and the adversary section, is at `/tmp/nudge/.time-travel/trips/2026-10-25-invoice-nudge/trip.md`. The rebuild drops QuickBooks at launch, sends reminders from your own inbox, starts the trial at the first overdue invoice and moves launch to 2027-01-12. The adversary is the invoicing platform's own product lead. It announces free AI reminders the same week you launch and controls the Stripe connection Nudge depends on.

Nothing was sent or scheduled. To put the alarms in your calendar, run this and import the file:

```
python3 /Users/pierryborges/Development/time-travel/scripts/alarms_ics.py --artifact /tmp/nudge/.time-travel/trips/2026-10-25-invoice-nudge/trip.md --out alarms.ics
```