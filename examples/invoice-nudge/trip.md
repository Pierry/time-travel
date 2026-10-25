# Trip 2026-10-25-invoice-nudge

One file per plan, at `$TIME_TRAVEL_HOME/trips/<ID>/trip.md` (default `~/.time-travel/trips/`). `<ID>` is the date of departure plus a short slug, `2026-10-25-pricing-relaunch`. Sections are numbered because the gate reads them by number. Do not rename, reorder or delete a section: fill it or write `pending: <what is missing>`.

Field keys stay in English so the gate can read them. Values are written in the language the person used.

## 0. Plan

- Departure: 2026-10-25
- Arrival: 2027-04-25
- Goal: Launch Nudge, a SaaS that chases late invoices for freelancers through Stripe and QuickBooks with AI-written reminders
- Timeline: MVP in 6 weeks, Product Hunt launch in week 8
- Budget: $5,000 of savings; $2,000 ads, $3,000 tools and a part-time designer
- Success looks like: 200 paying customers at $29/month six months after launch, about $5,800 MRR

### Details

1. D1: $29/month, 14-day free trial, no free plan
2. D2: solo founder full time, designer 10 hours a week, no co-founder
3. D3: $2,000 of the $5,000 goes to ads
4. D4: MVP built in 6 weeks, launch on Product Hunt in week 8
5. D5: distribution is Product Hunt, a Twitter account with 1,800 followers and r/freelance
6. D6: integrates with Stripe and QuickBooks
7. D7: AI writes the reminder emails and escalates up to a "final notice"
8. D8: success is 200 paying customers six months after launch

## 1. Autopsy

### Cause 1: The launch spike that never became a pipeline

- Likelihood: 70%
- Killed by: Product Hunt and one Twitter thread produced a single week of signups and nothing after it, because no channel was built that keeps sending freelancers
- Traces to: D5
- Premise: a good launch day turns into steady growth on its own
- First warning sign: signups in week 2 after launch below 20% of launch week

| Month | What happened |
|---|---|
| 1 | Launch day lands #7 on Product Hunt, 410 visits, 61 trials, 9 paid |
| 2 | Traffic falls 85%; the r/freelance post is removed as self promotion |
| 3 | 4 new trials a week, all from the founder replying to tweets by hand |
| 4 | Founder spends 70% of the week on support and code, 0 hours on distribution |
| 5 | 31 paying customers, flat for six weeks |
| 6 | 38 paying, 19% of the goal; savings cover two more months |

### Cause 2: Nobody trusts a robot to email their client about money

- Likelihood: 55%
- Killed by: freelancers connect the account, read the first AI draft, and switch auto-send off because one wrong tone costs them a client worth far more than $29
- Traces to: D7
- Premise: freelancers hate chasing invoices so much they will delegate the relationship
- First warning sign: under 30% of trials leave auto-send on after the first draft

| Month | What happened |
|---|---|
| 1 | 64% of trials open the draft editor and rewrite the email by hand |
| 2 | A user posts a screenshot of a "final notice" sent to a long-time client; 40 replies agree it was rude |
| 3 | Auto-send usage drops to 18%; the product is now a reminder calendar |
| 4 | Churn interviews: "I can set a calendar reminder for free" |
| 5 | Monthly churn reaches 14% |
| 6 | Net revenue retention 72%; growth cannot outrun the leak |

### Cause 3: The trial ends before the first invoice is late

- Likelihood: 45%
- Killed by: a 14-day trial ends before most freelancers have an overdue invoice, so the trial shows an empty dashboard and converts nobody
- Traces to: D1
- Premise: the user sees the value inside the trial window
- First warning sign: under 25% of trials have at least one overdue invoice by day 14

| Month | What happened |
|---|---|
| 1 | 61 trials, 9 conversions, 15%; 70% of trials never had an overdue invoice |
| 2 | Support inbox: "I'll come back when someone pays me late" |
| 3 | Trial to paid falls to 8% |
| 4 | Founder extends trials by hand, which nobody tracks |
| 5 | Every acquisition number looks twice as expensive as it is |
| 6 | The ads budget is spent on trials that expire empty |

### Cause 4: The ads budget dies in two weeks

- Likelihood: 35%
- Killed by: $2,000 at $4 to $6 per click on "invoice software" buys about 400 clicks and 3 customers, a customer acquisition cost near $650 against $29 a month
- Traces to: D3
- Premise: paid ads can fill the gap when organic growth is slow
- First warning sign: cost per trial above $40 in the first $300 spent

| Month | What happened |
|---|---|
| 1 | $300 test: 58 clicks, 4 trials, 0 paid |
| 2 | Founder raises the budget hoping it is a learning phase; $1,200 more, 2 paid |
| 3 | The last $500 goes to retargeting; 1 paid |
| 4 | Ads budget gone; 3 customers bought for $2,000 |
| 5 | No money left to test a second channel |
| 6 | The one paid channel tried is marked "doesn't work" for good |

### Cause 5: QuickBooks review eats the runway

- Likelihood: 30%
- Killed by: the QuickBooks app review and token refresh bugs take weeks the six week MVP did not include, so launch slips and half the market cannot connect
- Traces to: D6
- Premise: both integrations are a weekend each
- First warning sign: QuickBooks production keys not approved by week 4
- Note: Stripe alone covers only freelancers who already invoice through Stripe

| Month | What happened |
|---|---|
| 1 | Stripe works in 5 days; QuickBooks sandbox in 9 |
| 2 | Production review asks for a security questionnaire and a privacy policy rewrite |
| 3 | Launch moves from week 8 to week 12 |
| 4 | Token refresh fails silently; 11 accounts stop syncing without notice |
| 5 | Two refund requests: "it said everything was paid" |
| 6 | QuickBooks users churn at twice the rate of Stripe users |

### Cause 6: One person is the whole company

- Likelihood: 25%
- Killed by: the founder is engineer, support, marketer and accountant at once; with the designer at 10 hours a week, every week goes to whatever is on fire
- Traces to: D2
- Premise: one motivated person can run build, sell and support in parallel
- First warning sign: two weeks in a row with no distribution work shipped

| Month | What happened |
|---|---|
| 1 | Launch week: 41 support emails, answered at 2 am |
| 2 | The designer's hours go to the landing page, not the onboarding that leaks |
| 3 | Content calendar abandoned after 2 posts |
| 4 | Founder stops shipping on Fridays to catch up on support |
| 5 | Burnout; a week off with nobody covering |
| 6 | Churn spikes in the week off because sync errors go unanswered |

### Cause 7: The goal measures the wrong thing at the wrong time

- Likelihood: 15%
- Killed by: "200 customers in six months" has no weekly number underneath it, so the founder learns the plan is dead in month 6 instead of month 2
- Traces to: D8
- Premise: a big final number is enough to steer by
- First warning sign: no weekly metric written down by launch day

| Month | What happened |
|---|---|
| 1 | Dashboard shows signups, not activation or retained paying users |
| 2 | 9 paid feels like a start, nobody does the math that it needs 33 a month |
| 3 | The gap to 200 is now 170; still no alarm |
| 4 | Founder changes the goal to "product market fit" without saying so |
| 5 | The decision to stop or pivot is never on the calendar |
| 6 | The plan is declared dead by the bank balance, not by a decision |

## 2. Verdict

- Most likely: Cause 1, the launch spike that never became a pipeline
- Most dangerous: Cause 2, nobody trusts a robot to email their client about money
- Why they differ: Cause 1 is a distribution problem that a better channel fixes; Cause 2 means the core promise, sending the email for them, is the thing users refuse, and no amount of traffic saves a product people switch off
- Hidden assumption: that freelancers want the chasing automated, when the evidence so far is only that they hate doing it
- Fatal flaw: yes: auto-sending AI emails to the client is both the differentiator and the reason to churn; as written, the plan grows a product whose main feature users disable

## 3. Rebuild

| Change | Closes | Why |
|---|---|---|
| Ship "draft and approve" by default: AI writes, the freelancer taps send, auto-send is opt in after 3 approved drafts | Cause 2 | trust is earned email by email instead of demanded on day one |
| Trial starts when the first invoice goes overdue, not on signup, capped at 30 days | Cause 3 | the trial clock runs while the product is doing its job |
| Launch Stripe only; QuickBooks waits for 30 paying users asking for it | Cause 5, Cause 6 | removes the integration that eats the runway and halves the support surface |
| Two hours a day of distribution blocked on the calendar, measured weekly: one partnership with a freelancer community or invoicing newsletter per month | Cause 1, Cause 6 | builds a channel that keeps sending after launch week |
| Ads limited to a $300 test with a $40 cost per trial ceiling; the remaining $1,700 funds community sponsorships | Cause 4 | a cheap test answers the question before the budget is gone |
| Replace "200 in six months" with a weekly target: 8 new paying customers a week from month 2, with a stop or pivot review on the calendar for week 12 | Cause 7 | the plan is judged every week, not at the funeral |

### Pre-launch checklist

| Confirm | Quit if |
|---|---|
| Show 15 freelancers an AI draft for their own late invoice and ask them to send it | fewer than 5 would send it with no edit |
| Ask 20 target freelancers how many overdue invoices they had last quarter | the median is under 1 |
| Pre-sell: offer 3 months for $60 to the waitlist before writing the product | fewer than 10 people pay |
| Price one community sponsorship and ask for its past click numbers | the cost per click implied is above $3 |

## 4. Adversary

- Who: the product lead of an invoicing tool freelancers already pay for, who adds reminders as a free checkbox
- Attack point: Cause 2 and D6; Nudge lives on top of their data, and they own the relationship with the invoice
- Launch week: they ship "Smart reminders, free on every plan" and email their whole user base the same week Nudge is on Product Hunt
- Blind side: they change their API terms so third party tools cannot send emails on behalf of their users, which kills the integration overnight
- Counter: the rebuilt plan sells the tone, the draft and approve step written for the freelancer, not the reminder itself, and keeps a Stripe only base that no single invoicing tool controls

## 5. Alarms

| Cause | Signal | Threshold | Check week |
|---|---|---|---|
| Cause 1 | new trials in the second week after launch, from analytics | under 20% of launch week trials | Week 10 |
| Cause 2 | share of drafts sent with no edit, from the app database | under 30% of drafts | Week 9 |
| Cause 3 | trials with an overdue invoice by trial day 14 | under 25% of trials | Week 10 |
| Cause 4 | cost per trial after the first $300 of ads | above $40 per trial | Week 9 |
| Cause 5 | QuickBooks production keys approved | not approved by week 4 | Week 4 |
| Cause 6 | hours logged on distribution in the week | under 10 hours, two weeks in a row | Week 11 |
| Cause 7 | new paying customers in the week | under 8 per week, three weeks in a row | Week 14 |
