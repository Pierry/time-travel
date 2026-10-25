# Trip 2026-10-25-invoice-nudge

One file per plan, at `$TIME_TRAVEL_HOME/trips/<ID>/trip.md` (default `~/.time-travel/trips/`). Sections are numbered because the gate reads them by number. Do not rename, reorder or delete a section: fill it or write `pending: <what is missing>`.

Field keys stay in English so the gate can read them. Values are written in the language the person used.

## 0. Plan

The plan exactly as the person gave it, cut into numbered details. Every cause of death in section 1 points back to one of these, or to something the plan left out.

- Departure: 2026-10-25
- Arrival: 2027-04-25
- Goal: Launch Nudge, a SaaS that chases late invoices for freelancers: plugs into Stripe and QuickBooks, writes reminder emails with AI, and escalates politely from "friendly heads-up" to "final notice".
- Timeline: build the MVP in 6 weeks, launch on Product Hunt in week 8.
- Budget: $5,000 of savings. $2,000 for ads, the rest for tools and the designer. Team: founder full time, a part-time designer (10 h/week), no co-founder.
- Success looks like: 200 paying customers six months after launch.

### Details

1. D1: Price is $29/month, single tier.
2. D2: 14-day free trial, no free plan.
3. D3: Integrations with both Stripe and QuickBooks at launch.
4. D4: AI writes the reminder emails, escalating from "friendly heads-up" to "final notice", sent to the freelancer's own clients.
5. D5: Team is the founder full time plus a part-time designer at 10 h/week; no co-founder.
6. D6: Budget is $5,000 of savings: $2,000 for ads, $3,000 for tools and the designer.
7. D7: MVP built in 6 weeks.
8. D8: Product Hunt launch in week 8.
9. D9: Distribution is Product Hunt, the founder's Twitter (1,800 followers) and Reddit r/freelance.
10. D10: Target customer is freelancers.
11. D11: Success is 200 paying customers six months after launch.

## 1. Autopsy

Seven causes of death, most probable first. Each one is traced to a detail above (`D2`) or to something the plan cut (`cut: <what is missing>`). No generic advice.

Calendar used below: week 1 starts 2026-10-26. Week 8 lands on 2026-12-14, the second-to-last full week before Christmas. Month 1 is November 2026, month 6 is April 2027.

### Cause 1: The launch spike was the whole funnel

- Likelihood: 60%
- Killed by: Product Hunt, 1,800 Twitter followers and one Reddit thread produced a single week of trials in mid-December and no repeatable source of new trials after it, while 200 paying customers needed roughly 1,000 to 1,500 trials.
- Traces to: D9, D8
- Premise: "Once it is live on Product Hunt and I tell my followers, word of mouth among freelancers will carry it."
- First warning sign: trials started in week 10 (the week after launch) below 20, against 150+ in launch week.

| Month | What happened |
|---|---|
| 1 | Building. No waitlist, no landing page collecting emails; distribution work postponed to "after the MVP". |
| 2 | Launch on 2026-12-15, a pre-holiday Tuesday. Finished #9 of the day, ~1,400 visits, 140 trials. Tweet thread got 22 retweets. r/freelance post removed within 3 hours under the no-self-promotion rule. |
| 3 | January: 31 new trials all month, mostly from a lingering PH listing. Two founder tweets a week reach the same 1,800 people, most of whom are developers, not invoicing freelancers. |
| 4 | February: 24 new trials. Founder starts cold-posting in Facebook groups and Indie Hackers, one-off bumps of 5 to 8 trials each. |
| 5 | March: 19 new trials. Paying customers at 41. |
| 6 | April 2027: 47 paying customers, trial volume flat at ~5 a week. 200 is out of reach at any conversion rate; plan declared dead. |

### Cause 2: The trial ended before any invoice went late

- Likelihood: 55%
- Killed by: Freelancers on net-30 terms rarely had an overdue invoice inside a 14-day trial, so most trials expired before Nudge sent a single reminder or recovered a single dollar, and they did not pay for a promise.
- Traces to: D2, D10
- Premise: "Fourteen days is the SaaS standard; they will see the value as soon as they connect Stripe."
- First warning sign: under 40% of launch-week trials had a reminder sent by day 14, visible in the database by week 10.

| Month | What happened |
|---|---|
| 1 | Trial length copied from other SaaS; no check of how many overdue invoices a typical freelancer has at a given moment. |
| 2 | 140 launch trials. Median user had 0 overdue invoices at connect time; 1 if they had any. |
| 3 | First cohort expires in early January: 11 of 140 convert (7.9%). Exit survey answer most given: "never got to use it". |
| 4 | Founder extends trial to 30 days for new users; conversion rises, but cash from paying users is pushed a month later. |
| 5 | Trial-to-paid stabilizes at ~10%; with Cause 1's volume that is 2 to 3 new customers a week. |
| 6 | Too few cohorts at 10% to reach 200; the trial design consumed 2 of the 4 post-launch months in waiting. |

### Cause 3: Freelancers would not let an AI email their clients

- Likelihood: 45%
- Killed by: The core action, an AI-written email escalating to "final notice" sent to the freelancer's own client, is exactly what a freelancer living on 3 to 8 client relationships is afraid of, so users connected their accounts but kept automatic sending off and used Nudge as a draft tool worth less than $29.
- Traces to: D4, D10
- Premise: "Chasing invoices is the awkward part; they will be relieved to hand it off."
- First warning sign: in week 9 to 10, fewer than 1 in 3 connected accounts turned on automatic sending.

| Month | What happened |
|---|---|
| 1 | Escalation ladder designed down to "final notice"; no interviews with freelancers about who they would let write to their clients. |
| 2 | Launch comments on PH include "I'd never let a bot send 'final notice' to my best client" with 30 upvotes. |
| 3 | 28% of trial users enable auto-send. One user's client replies angrily to an AI email that mentioned the wrong project; the user tweets it. |
| 4 | Founder adds an "approve every email" mode; most active users switch to it, and Nudge becomes a template generator. |
| 5 | Churn interviews: "I can write a polite reminder myself in 2 minutes." |
| 6 | Value perceived at the level of a free email template; paid base stalls under 50. |

### Cause 4: Two integrations in six weeks, built by one person

- Likelihood: 40%
- Killed by: Stripe plus QuickBooks (OAuth, invoice sync, webhooks for paid status, Intuit app review) plus AI email generation plus sending and deliverability did not fit in 6 weeks for a solo builder, so launch slipped from week 8 into January and the QuickBooks half shipped buggy.
- Traces to: D3, D7, D5
- Premise: "The APIs are well documented; integrations are a week each."
- First warning sign: at end of week 4 (2026-11-22), QuickBooks sync not yet marking invoices as paid reliably.

| Month | What happened |
|---|---|
| 1 | Stripe integration done in 2 weeks. QuickBooks sandbox data differs from real accounts; paid-status sync breaks on partial payments. |
| 2 | Intuit app listing review not submitted in time. Launch held to week 8 with QuickBooks marked "beta"; 2 users get reminders sent on invoices already paid. |
| 3 | January spent on QuickBooks bug fixes and email deliverability (reminders landing in spam from a new sending domain); zero distribution work. |
| 4 | A reminder-on-paid-invoice incident costs a vocal user a client; refund and public complaint. |
| 5 | Founder estimates 60% of build time since launch went to integration maintenance. |
| 6 | Product stable at last, but 4 months of selling time gone. |

### Cause 5: $2,000 of ads bought about ten customers

- Likelihood: 35%
- Killed by: Paid acquisition for a $29/month tool sold to freelancers ran at roughly $150 to $250 per paying customer, so the $2,000 ad budget produced around 10 customers and was gone by February with no channel learned.
- Traces to: D6, D1
- Premise: "$2,000 in ads will fill the funnel while organic catches up."
- First warning sign: after the first $500 of spend (week 10), cost per trial above $15.

| Month | What happened |
|---|---|
| 1 | $0 spent; no tracking plan for ad-to-paid attribution. |
| 2 | $500 on Google Ads for "invoice reminder software"; bids dominated by accounting suites. Cost per trial $19. |
| 3 | $900 on Meta targeting "freelancer"; cheap clicks, trials from people with no invoices. 4 paying customers from ads. |
| 4 | Last $600 spent; total ad-sourced paying customers: 11, at $182 each. |
| 5 | No ad budget left; the $3,000 for tools and designer is half spent. |
| 6 | No money to test a second channel; the plan has no fuel. |

### Cause 6: "My invoicing tool already does that"

- Likelihood: 30%
- Killed by: Stripe Invoicing and QuickBooks Online, the two platforms Nudge plugs into, already send automatic overdue reminders for free, and every prospect who already used them saw Nudge as a $29 duplicate.
- Traces to: cut: no competitor named and no difference stated against the reminders built into Stripe, QuickBooks, FreshBooks or Chaser
- Premise: "Nobody is doing this well for freelancers."
- First warning sign: the reply "Stripe already sends reminders" appearing in launch-week comments or in the first 10 sales conversations.

| Month | What happened |
|---|---|
| 1 | Positioning written as "automatic invoice reminders", the same feature name the integrations carry. |
| 2 | Top PH comment: "QuickBooks has had this for years, what's different?"; founder's answer ("AI tone") gets no traction. |
| 3 | Of churned trials surveyed, 40% say they turned on built-in reminders in their invoicing tool instead. |
| 4 | Founder repositions around "escalation that sounds human"; message does not travel. |
| 5 | Converted users are the minority who did not know the built-in reminders existed. |
| 6 | No defensible reason to pay; growth limited to the unaware. |

### Cause 7: Paying customers left once their invoice was paid

- Likelihood: 25%
- Killed by: Late invoices are episodic for most freelancers, so customers subscribed when one client was late and cancelled after it was paid, running monthly churn at 12% to 15% and making 200 active paying customers a bucket with a hole.
- Traces to: D1, D10, D11
- Premise: "Late payments are a constant pain, so they will stay subscribed."
- First warning sign: in month 3, more than 1 in 10 of December's paying customers cancelled within 45 days.

| Month | What happened |
|---|---|
| 1 | Pricing set at monthly $29 with no annual plan or usage-based option; "200 paying" never defined as active vs ever-paid. |
| 2 | First 11 paying customers. |
| 3 | 3 of them cancel after their overdue invoice clears. |
| 4 | Monthly churn measured at 14%. |
| 5 | Every new month's acquisition is a third eaten by churn. |
| 6 | 47 active paying customers out of 74 ever-paid; even at Cause 1's best case the ceiling is under 100. |

## 2. Verdict

- Most likely: Cause 1, the launch spike was the whole funnel
- Most dangerous: Cause 6, "my invoicing tool already does that"
- Why they differ: Cause 1 is a go-to-market failure; it is probable because one launch plus 1,800 followers cannot produce the 1,000+ trials the goal needs, but it is recoverable with time and a second channel. Cause 6 is a product failure: if the two platforms Nudge plugs into already send reminders for free, no channel, trial length or price fixes it, every dollar spent on distribution buys more people who leave, and it stays invisible until after the 6 weeks of build are spent.
- Hidden assumption: that freelancers have a recurring late-invoice problem painful enough to pay $29 every month for, that is not already solved by their invoicing tool, and that they want a machine to handle it in their name. It sits under the premises of Causes 2, 3, 6 and 7 at once, and the plan does not contain a single conversation with a freelancer to test it before building.
- Fatal flaw: yes: the plan has no acquisition channel sized to the goal. 200 paying customers at a 10% trial-to-paid rate needs about 2,000 trials, plus replacements for churn; one Product Hunt day, 1,800 followers, a subreddit that removes self-promotion and $2,000 of ads add up to roughly 300 to 400. The success date also sits beyond this trip: 200 customers "six months after launch" is week 34, so at the six-month mark the plan is measured at about 4 months of selling, the first of them in the Christmas holidays.

## 3. Rebuild

The plan rewritten with every failure mode resolved. Each change names the causes it closes; every cause from 1 to 7 is closed by at least one change.

Rebuilt timeline: weeks 1 to 3 interviews and landing page (no code), weeks 4 to 9 a Stripe-only MVP, weeks 10 to 11 private beta with the waitlist, public launch in week 12 (2027-01-12), success measured as active paying customers at week 26 and at week 34.

| Change | Closes | Why |
|---|---|---|
| Weeks 1 to 3: interview 20 freelancers who invoice through Stripe or QuickBooks before writing code; ask how many invoices went late in the last 90 days, whether they use the built-in reminders, and whether they would let a tool email a client in their name. | Cause 2, Cause 3, Cause 6, Cause 7 | Tests the hidden assumption for about $0 and 15 hours, before the 6 weeks of build and the $5,000 are committed. |
| Ship Stripe only. QuickBooks waits until 30 paying customers ask for it; MVP scope is Stripe sync, paid-status webhooks, reminder drafting and sending. | Cause 4 | Halves the integration surface, removes the Intuit app review from the critical path, and leaves room to finish inside 6 weeks. |
| Send reminders from the freelancer's own Gmail or Outlook, threaded under the original invoice email, stopping the moment the client replies or pays; "draft and approve" is the default, auto-send is earned after 3 approved emails, and "final notice" is opt-in per client. | Cause 3, Cause 6 | Gives the freelancer control of what reaches their client, and does the two things the reminders built into Stripe and QuickBooks do not: come from the person's own inbox and react to replies. |
| Replace the 14-day trial with "free until Nudge sends its first reminder, then 14 days": the clock starts at the first overdue invoice. | Cause 2 | Every trial gets to see an overdue invoice handled before it is asked to pay. |
| Build the waitlist from week 2 with one repeatable channel: free "late payment email" template pages (search-driven) that capture emails, plus one sponsored post in a freelancer newsletter. Product Hunt becomes a launch-week bonus, not the funnel. | Cause 1 | Creates a source of trials that keeps producing after launch week, measured weekly from week 4. |
| Move the public launch from week 8 (2026-12-15) to week 12 (2027-01-12), after a private beta with the waitlist. | Cause 1, Cause 4 | Avoids the Christmas weeks, buys 4 weeks of build buffer, and launches to an audience already collected. |
| Hold the $2,000 ad budget: spend $300 as a test after launch and only scale while cost per paying customer stays under $90 (about 3 months of revenue). | Cause 5 | One test with a stop rule instead of one blind attempt that empties the budget. |
| Add an annual plan at $240/year and a "pause" option at $5/month instead of cancel; define success as 200 active paying customers, not ever-paid. | Cause 7 | Captures customers whose need is episodic and stops counting customers who already left. |

### Pre-launch checklist

Three to five things to confirm before executing anything, each with the result that means quit for good.

| Confirm | Quit if |
|---|---|
| 20 interviews with freelancers invoicing through Stripe or QuickBooks: count those with at least one invoice more than 14 days late in the last 90 days. | fewer than 8 of 20 had a late invoice in the last 90 days |
| In the same 20 interviews: how many use the reminders built into their invoicing tool, and how many would let Nudge email a client from their own inbox after approving the first drafts. | fewer than 5 of 20 would let a tool send in their name, or 6 or more of the built-in users say those reminders are enough and none names a gap |
| Pre-sale: on the landing page, offer a founding annual plan at $190 to the waitlist, charged now. | fewer than 10 pre-paid customers by week 6 from a waitlist of at least 200 |
| Channel test: the template pages and one newsletter sponsorship, measured on waitlist signups. | under 150 waitlist signups by week 6, or cost per signup above $10 on paid placements |
| Personal runway: months the founder can live without income, outside the $5,000 budget. | under 9 months of living costs covered; do not go full time, build it on evenings until the interviews and pre-sale pass |

## 4. Adversary

The person who gains the most if the plan goes wrong, playing to win.

- Who: the product lead for invoicing at the payment platform Nudge plugs into, whose free built-in reminders are the thing Nudge asks freelancers to pay $29 to replace.
- Attack point: D3 and Cause 6. Nudge's rebuilt difference is "reminders from your own inbox that react to replies"; the platform owns the invoice, the payment link and the paid status Nudge depends on, so it only has to close the visible gap to make Nudge a duplicate again.
- Launch week: in week 12 (2027-01-12), the platform's changelog and in-dashboard banner announce "smart reminders": AI-adjusted tone, an escalation schedule and auto-stop on payment, free, on by default for every account. Nudge's launch-day comments fill with links to it.
- Blind side: the rebuilt plan treats the Stripe connection as fixed. Platform terms for third-party apps that email a merchant's customers can tighten, or an app listing can be held in review, and the paid-status webhook Nudge needs is the same one the platform's own feature uses; one policy change on contacting end customers or on app approval stops Nudge on the day it has the most users waiting.
- Counter: the send-from-your-own-inbox design in the rebuild. It keeps the email history in the freelancer's Gmail or Outlook, not on the platform, so Nudge can read paid status from a second source (bank feed or a manual "mark paid") and survive losing the Stripe connection; build that fallback before launch, not after.

## 5. Alarms

One measurable alarm per cause. A threshold carries a number; a check week is a week number or a date. Week 1 starts 2026-10-26.

| Cause | Signal | Threshold | Check week |
|---|---|---|---|
| Cause 1 | waitlist signups from the template pages and newsletter, in the email tool, excluding friends and Twitter | under 150 total | Week 6 |
| Cause 2 | share of beta and trial accounts that had at least 1 reminder sent within 14 days of connecting, from the database | under 40% | Week 14 |
| Cause 3 | interviewees who say they would let a tool email a client in their name after approving drafts, from the interview notes | under 5 of 20 | Week 3 |
| Cause 4 | Stripe sync tested on 20 real invoices including partial payments and refunds: invoices marked paid correctly | fewer than 20 of 20 | Week 8 |
| Cause 5 | cost per paying customer from the $300 ad test, ad spend divided by paying customers attributed | above $90 | Week 16 |
| Cause 6 | interviewees using built-in Stripe or QuickBooks reminders who say those are enough and name no gap, from the interview notes | 6 or more | Week 3 |
| Cause 7 | paying customers who cancel within 45 days of their first payment, from Stripe billing | above 10% | Week 20 |
