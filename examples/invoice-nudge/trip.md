# Trip 2026-10-25-nudge-launch

One file per plan, at `$TIME_TRAVEL_HOME/trips/2026-10-25-nudge-launch/trip.md`. Sections are numbered because the gate reads them by number. Do not rename, reorder or delete a section: fill it or write `pending: what is missing`.

## 0. Plan

Source: `plan.md`, read whole.

- Departure: 2026-10-25
- Arrival: 2027-04-25
- Goal: launch Nudge, a SaaS that chases late invoices for freelancers. It plugs into Stripe and QuickBooks, writes reminder emails with AI, and escalates politely from "friendly heads-up" to "final notice".
- Timeline: build the MVP in 6 weeks, launch on Product Hunt in week 8.
- Budget: $5,000 of savings. $2,000 for ads, the rest for tools and the designer. Me full time, a part-time designer (10 h/week), no co-founder.
- Success looks like: 200 paying customers six months after launch.

### Details

1. D1: The product sends reminder emails to the freelancer's own clients, written by AI, escalating from "friendly heads-up" to "final notice".
2. D2: Integrations with Stripe and QuickBooks are part of the product, both in the 6-week MVP.
3. D3: Price is $29/month, with a 14-day free trial and no free plan.
4. D4: Team is one founder full time and a part-time designer at 10 h/week; no co-founder, no second engineer.
5. D5: Budget is $5,000 of personal savings, the only money in the plan.
6. D6: $2,000 of the budget goes to ads; the remaining $3,000 covers tools and the designer.
7. D7: The MVP is built in 6 weeks (by about 2026-12-06).
8. D8: Launch is on Product Hunt in week 8 (about 2026-12-20, the week before Christmas).
9. D9: Distribution is three channels: Product Hunt, the founder's Twitter (1,800 followers) and Reddit r/freelance.
10. D10: Success is 200 paying customers six months after launch, which is about $5,800 MRR at $29.
11. D11: The trip arrives on 2027-04-25, about 18 weeks after launch, so the plan needs well over half of the 200 by then to still be on track.

## 1. Autopsy

The months run from departure: month 1 is November 2026, month 6 is April 2027. Estimates of traffic and conversion are typical ranges for a $29 B2B tool launched from a small audience, not measured numbers; the alarms in section 5 replace them with real ones.

### Cause 1: One launch spike, then silence

- Likelihood: 60%
- Killed by: Product Hunt, 1,800 Twitter followers and an r/freelance post produced a single week of traffic in the week before Christmas, and nothing in the plan generated a second week.
- Traces to: D8, D9, D11
- Premise: "If the product is good, a Product Hunt launch and my followers will get the first wave, and word of mouth does the rest."
- First warning sign: in launch week, under 1,500 site visitors and under 40 trial signups; the r/freelance post removed within hours as self-promotion.

| Month | What happened |
|---|---|
| 1 | Building. No waitlist, no landing page collecting emails, no posts about the build; the Twitter account posts twice about "something coming". |
| 2 | Launch on 2026-12-20, the week before Christmas. Product Hunt gives about 1,100 visitors and 35 trials; Twitter drives 200 clicks; the r/freelance post is removed by the moderators. |
| 3 | January. Daily signups fall from 8 to under 1 by mid-month. 6 of the 35 trials convert. No channel was planned for week 2 onward. |
| 4 | February. Founder tries a second Product Hunt angle, cold DMs and a Hacker News post; 14 new trials in the month, 3 paid. 11 paying customers. |
| 5 | March. Organic search is zero because no content was ever written. 15 paying customers, about $435 MRR. |
| 6 | April 2027. 17 paying customers against the 200 the plan needs, with no channel left to turn up. The plan is declared dead. |

### Cause 2: Two integrations ate the six weeks

- Likelihood: 50%
- Killed by: Stripe and QuickBooks each needed OAuth, invoice sync, webhook handling, overdue detection and edge cases (partial payments, credit notes, currencies), and QuickBooks needed production-key approval from Intuit, so one founder shipped neither well in 6 weeks.
- Traces to: D2, D4, D7
- Premise: "Stripe and QuickBooks both have good APIs; wiring them up is a couple of weeks each."
- First warning sign: at the end of week 3, no real overdue invoice from a real Stripe account has been pulled into Nudge yet.

| Month | What happened |
|---|---|
| 1 | Stripe sync works on test data in week 3; real accounts surface partial payments and invoices marked paid outside Stripe. QuickBooks sandbox only. |
| 2 | Week 6 passes with QuickBooks unfinished. The founder launches on 2026-12-20 anyway with QuickBooks "coming soon", which was half of the pitch. |
| 3 | Two trial users receive a reminder sent to their client for an invoice already paid by bank transfer; both cancel. Founder spends January on sync bugs instead of selling. |
| 4 | QuickBooks production access arrives in February after the app review; the launch moment is gone and only 4 users connect it. |
| 5 | Support for sync errors takes 15 hours a week; no new channel work happens. |
| 6 | Product works for the first time in April, for 14 paying customers. The plan is dead with a finished product. |

### Cause 3: Late invoices are episodic, the subscription is monthly

- Likelihood: 45%
- Killed by: a freelancer has one or two late invoices a quarter, so they subscribed to chase one invoice and cancelled the month it was paid, and the paying base never grew past churn.
- Traces to: D3, D1, D10
- Premise: "Late invoices are a constant pain for freelancers; once Nudge saves them one invoice they will keep paying forever."
- First warning sign: in the first cohort, more than a third of payers cancel within 30 days of their chased invoice being marked paid.

| Month | What happened |
|---|---|
| 1 | No interviews on how often invoices are late; the build assumes a monthly pain. |
| 2 | Trial users connect accounts with an average of 1.3 overdue invoices each; several have zero and never see a reminder go out. |
| 3 | 8 paying customers. 3 cancel after their one invoice is paid: "will come back when I need it". |
| 4 | Monthly churn at 25%. New paying customers barely replace cancelled ones. |
| 5 | Exit survey: 6 of 9 cancellations say "only needed it once". |
| 6 | Paying base stuck at 12 to 15. 200 would need a churn rate under 5%; it runs at 25%. |

### Cause 4: The free reminder already inside Stripe and QuickBooks

- Likelihood: 40%
- Killed by: the platforms Nudge integrates with already send automatic overdue reminders for free, so the freelancers who cared about reminders already had them turned on, and the AI tone and escalation were not worth $29 a month on top.
- Traces to: D2, D3, cut: no competitor or alternative named anywhere in the plan
- Premise: "Nobody is doing polite AI escalation for freelancers; this is a gap."
- First warning sign: in the first 10 trial conversations or exit answers, 3 or more say "QuickBooks already sends reminders" or "Stripe does this".

| Month | What happened |
|---|---|
| 1 | Build proceeds without checking what the free reminders in Stripe and QuickBooks already do. |
| 2 | Product Hunt comments: "how is this different from the reminder setting in QuickBooks?" The founder answers "AI tone", the thread goes quiet. |
| 3 | Trial users who connect QuickBooks find their client now gets two reminders, Nudge's and QuickBooks', and turn one off; most turn off Nudge. |
| 4 | An established receivables tool posts a free tier for freelancers; two Nudge customers move. |
| 5 | The positioning is rewritten twice; neither version tests better than the first. |
| 6 | The paying base is the handful who do not use either platform's reminders. The plan dies with no differentiator. |

### Cause 5: $2,000 of ads bought 20 customers

- Likelihood: 35%
- Killed by: search ads for invoice-reminder terms cost several dollars a click and a $29 trial converted at a single-digit rate from cold traffic, so the $2,000 bought roughly 15 to 25 paying customers once, at a cost per customer above $80, and there was no second $2,000.
- Traces to: D6, D5, D3
- Premise: "$2,000 of ads is enough to get the first hundred customers and prove the channel."
- First warning sign: after the first $300 of spend, cost per trial above $25 and zero paid conversions.

| Month | What happened |
|---|---|
| 1 | Ads are planned but no tracking from click to trial to paid is built. |
| 2 | $800 spent in launch week on Google and Twitter ads alongside Product Hunt; the traffic sources blur, nobody can say which channel worked. |
| 3 | January: another $700. Cost per trial $28, trial to paid 12%, about $230 per paying customer from ads. |
| 4 | Last $500 spent on Reddit ads in r/freelance-adjacent subreddits; 2 paid. |
| 5 | Ad budget is gone. Paid acquisition is stopped with 9 customers attributed to it. |
| 6 | No money left to try any other paid channel. 200 is out of reach by a factor of ten. |

### Cause 6: The money and the founder ran out before the product found its market

- Likelihood: 30%
- Killed by: the $3,000 for tools and a 10 h/week designer covered about two months of the designer, the founder had no salary, and by month 4 the founder took contract work and Nudge got evenings only.
- Traces to: D4, D5, D6, cut: the founder's personal runway and living costs are not in the plan
- Premise: "$5,000 is enough to get to launch, and after launch the revenue will cover the rest."
- First warning sign: by week 8, more than $2,500 of the $5,000 is spent and MRR is under $300.

| Month | What happened |
|---|---|
| 1 | Designer at 10 h/week costs about $1,200 a month; tools (hosting, AI API, email sending, domain, analytics) about $150. |
| 2 | $2,700 of the $3,000 non-ad budget is gone by launch. Designer is cut. |
| 3 | MRR $170. Founder's personal savings, the same pool, are being spent on rent. |
| 4 | Founder signs a 30 h/week contract to pay the bills; Nudge drops to 10 hours a week. |
| 5 | No new features, slow support replies; two customers churn over response time. |
| 6 | Nudge is a side project with 10 paying customers. The plan as written, full time to 200, is dead. |

### Cause 7: A final notice hurt a client relationship, and r/freelance heard about it

- Likelihood: 20%
- Killed by: an AI-written "final notice" went out automatically to a freelancer's biggest client over an invoice that was disputed or already paid, the freelancer lost the client, and the story was posted in the same r/freelance the plan relies on.
- Traces to: D1, D2, D9
- Premise: "The AI keeps the tone polite, so an automatic escalation can only help the freelancer get paid."
- First warning sign: in the first 30 days of sending, any reply to a Nudge email containing "already paid", "dispute" or "unsubscribe", or an email spam-complaint rate above 0.3%.

| Month | What happened |
|---|---|
| 1 | Escalation runs on a fixed schedule with no human approval step and no check for a client reply. |
| 2 | First reminders go out from Nudge's sending domain; 20% land in spam, so clients never see the friendly step and only see the final one. |
| 3 | A client who had replied "paid by wire on Friday" receives the final notice; the freelancer apologises to the client and cancels Nudge. |
| 4 | A post titled "this invoice app cost me my best client" reaches the top of r/freelance with 400 upvotes. |
| 5 | Trial signups from Reddit and search drop to near zero; the founder's replies in the thread are downvoted. |
| 6 | The one community channel the plan had is closed for good. The plan is dead with a name problem in its own market. |

## 2. Verdict

- Most likely: Cause 1, one launch spike, then silence
- Most dangerous: Cause 7, a final notice hurt a client relationship, and r/freelance heard about it
- Why they differ: Cause 1 is the default outcome of a launch from 1,800 followers and one Product Hunt day, but it is recoverable: a founder who sees 40 trials in launch week can still build a waitlist, write content and relaunch in month 3. Cause 7 is less likely, and it cannot be undone: it damages the customer's own income, it happens in the one community the plan sells into, and a top post in r/freelance stays searchable for years. Cause 1 costs months; Cause 7 costs the market.
- Hidden assumption: that late invoices are a frequent, monthly pain freelancers will pay $29 a month to hand to a robot that speaks to their clients. Causes 1, 3, 4 and 7 all rest on it: Cause 1 assumes the pain is sharp enough for word of mouth, Cause 3 that it recurs every month, Cause 4 that the free reminders do not already cover it, Cause 7 that freelancers will let software talk to the client who pays them. None of that has been checked with a single freelancer in the plan.
- Fatal flaw: yes: the distribution as written cannot reach the goal. 200 paying customers at a typical 10 to 15% trial-to-paid rate needs roughly 1,300 to 2,000 trials, which at 2 to 4% visitor-to-trial needs 30,000 to 100,000 visitors. One Product Hunt day the week before Christmas, 1,800 followers, a subreddit that removes self-promotion and $2,000 of ads deliver perhaps 5,000 to 10,000 visitors in total, before any churn. The goal is off by a factor of five to ten, and nothing in the plan closes the gap.

## 3. Rebuild

Weeks are counted from departure, week 1 starting 2026-10-25. The rebuilt plan launches publicly in week 13 (2027-01-17), not in Christmas week.

| Change | Closes | Why |
|---|---|---|
| Weeks 1 to 3, before any code: interview 20 freelancers who invoice clients (from Twitter, r/freelance comment threads, freelancer Slack and Discord groups) on how many invoices went late in the last 90 days and what they do now, then sell a concierge version: for $29, the founder chases their late invoices by hand for one month, with their approval on every email. | Cause 3, Cause 4, Cause 7 | It tests the hidden assumption with money before the build: how often the pain recurs (Cause 3), whether the free Stripe and QuickBooks reminders already satisfy them (Cause 4), and which emails freelancers will and will not let go to a client (Cause 7). |
| Rewrite the goal: 60 paying customers and $1,700 MRR by 2027-04-25, with a weekly target line, and 200 paying as the 12-month goal. Keep the 200 only if the funnel numbers measured by week 16 show it can be reached. | Cause 1, Cause 6 | The fatal flaw is a goal five to ten times what the channels can carry. A goal sized to the channels gives a weekly number that shows a stall in week 14 instead of month 6, and stops the founder from burning runway chasing an impossible line. |
| MVP has one integration: the one most of the concierge customers use (Stripe or QuickBooks), plus manual invoice entry and CSV import. The second integration starts only after 25 paying customers. | Cause 2, Cause 6 | One integration done properly fits 6 weeks for one engineer; two do not. Manual entry means the product is usable on day one even if the API approval or sync is late. |
| Build in public from week 1: a landing page with a waitlist, two posts a week on Twitter with the interview findings and late-payment numbers, and one useful post a month in r/freelance with no link (late-fee wording, escalation templates) that earns the right to mention Nudge in comments. Target 300 waitlist emails by week 12. | Cause 1 | Product Hunt becomes the second wave, not the only one. The waitlist turns one launch day into a list the founder can email in every week after it. |
| Launch on Product Hunt in week 13 (2027-01-17) to the waitlist first, then Product Hunt, then Twitter, with a free downloadable set of escalation email templates as the lead magnet that keeps working through search after launch. | Cause 1, Cause 4 | Mid-January is when freelancers chase December invoices and plan the year; the templates give search traffic after the spike and a differentiator against the platform's single generic reminder. |
| Position against the free reminders explicitly: Nudge reads replies and stops on "paid" or "dispute", escalates in the freelancer's own voice, sends from the freelancer's address or reply-to, and adds the late fee and payment link. Every page names what QuickBooks and Stripe already do and what they do not. | Cause 4, Cause 7 | The plan never named its real competitor, which is the free setting already inside the integrations. Naming it forces a reason to pay; stopping on a reply removes the most common way a final notice offends a client. |
| Every step above "friendly heads-up" requires one-click approval by the freelancer, and the final notice is never sent automatically. Sending uses an authenticated domain (SPF, DKIM, DMARC) and is paused for the client the moment any reply arrives. | Cause 7 | The irreversible failure is a robot insulting the client who pays the freelancer. A human click on every escalation makes that failure the freelancer's decision, not Nudge's, and authentication keeps the friendly step out of spam. |
| Price: keep $29/month, add an annual plan at $240 and a "chase pack" of 3 months for $69 for people with one late invoice, and test both during the concierge month. | Cause 3 | If the pain is episodic, a pricing shape that matches the episode keeps the revenue the monthly plan loses to churn after one paid invoice. |
| Hold the $2,000 of ads until 30 organic trials give a measured trial-to-paid rate, then spend in $250 tranches, stopping any channel whose cost per paying customer goes above $90 (about 3 months of revenue). | Cause 5, Cause 6 | Ads become a measured experiment with a stop rule instead of a launch-week bonfire, and unspent ad money is runway. |
| Designer on a fixed scope for $1,200 total (landing page, app shell, email templates) delivered by week 6, not 10 h/week ongoing. Write down the founder's personal runway in months and a date by which MRR must cover a set share of living costs. | Cause 6 | An open-ended designer at 10 h/week spends the $3,000 in about ten weeks; a fixed scope ends the cost. A written personal runway date turns "I will take contract work" from a surprise in month 4 into a decision made in advance. |

### Pre-launch checklist

| Confirm | Quit if |
|---|---|
| Interview 20 freelancers who invoice clients by week 3: count how many had 2 or more late invoices in the last 90 days. | Fewer than 6 of 20 had 2 or more late invoices in 90 days. The pain is too rare for a subscription; stop Nudge as a SaaS. |
| Concierge pre-sale by week 4: offer a month of hand-run chasing at $29, paid up front, to the interviewees and the waitlist. | Fewer than 5 people pay. If people will not pay $29 for a human doing it, they will not pay $29 for software doing it. |
| With every concierge payer, by week 4: turn on the free reminders in their Stripe or QuickBooks account side by side and ask which they would keep. | 3 or more of the first 5 payers say the free reminder is enough. There is no product above the platform's free setting. |
| Waitlist by week 12, before the public launch: count confirmed emails from Twitter, Reddit, templates and interviews. | Fewer than 150 waitlist emails. The audience cannot carry a launch; do not spend the ad budget, rethink the channel or stop. |
| Approval test during the concierge month: count how many payers approve the second and final escalation emails when it is their client. | Fewer than half of the escalation steps get approved, or 2 of 5 payers refuse any email to their client in a voice that is not theirs. Freelancers will not let software escalate; the core of the product is gone. |

## 4. Adversary

- Who: the growth lead at an established, funded accounts-receivable automation tool that sells invoice chasing to small agencies and wants to move down-market to freelancers. A role, not a named person. Nudge is a cheap test of the exact segment they plan to enter in 2027, and if it fails they get a clear market and its waitlist.
- Attack point: the single integration and the positioning against free reminders (rebuilt D2, closing Cause 4). The rebuilt Nudge only exists as "better than the free reminder in Stripe or QuickBooks". I would make our free tier better than that free reminder, so Nudge is squeezed between a free setting and a free plan from a company with ten times the features, and Nudge's $29 has nothing under it (D3).
- Launch week: in the week of 2027-01-17, I launch a "free for freelancers, up to 5 invoices a month" plan with AI-written reminders, posted on Product Hunt the same day Nudge goes up so voters see both, with a comparison table that puts our free tier next to Nudge's $29. Our team answers every r/freelance thread about late invoices that week with our templates and a link, because we have the people to do it and Nudge has one founder. We also run search ads on "Nudge invoice" and "Nudge alternative" from launch day.
- Blind side: I would not attack the product; I would attack the funnel. The free escalation templates Nudge gives away as its lead magnet are the asset that ranks in search after launch. I republish an expanded version within two weeks with more templates, a late-fee calculator and the backing of a domain that already ranks, and by March the search traffic Nudge's plan counts on for the weeks after the spike goes to us. Nudge treats its content as fixed and owned; in search it is neither.
- Counter: the concierge month and the approval-on-every-escalation design (rebuilt plan, changes 1 and 7). A funded tool going down-market will automate everything to keep a free tier cheap; Nudge's defence is to be the one that freelancers trust with their client: replies read, sending from their own address, the final notice never automatic, and 5 to 20 concierge customers whose words are on the landing page before launch. To that, add one change: publish the templates as a free interactive tool on the Nudge domain (enter invoice, get the escalation sequence), not a PDF, so the asset collects emails and is harder to copy than a document.

## 5. Alarms

Weeks counted from departure, week 1 starting 2026-10-25; public launch is week 13 (2027-01-17).

| Cause | Signal | Threshold | Check week |
|---|---|---|---|
| Cause 1 | Waitlist confirmed emails in the landing-page email tool, counted every Friday | Fewer than 75 by week 8 (half of the 150 the checklist requires by week 12) | Week 8 |
| Cause 2 | A real overdue invoice from a real customer account synced end to end into Nudge and shown with the right amount and due date | 0 real invoices synced by the end of week 7 (3 weeks into the build) | Week 7 |
| Cause 3 | Concierge log: overdue invoices per paying concierge customer over their 30 days | Average under 1.5 late invoices per customer per 30 days | Week 8 |
| Cause 4 | Side-by-side answers from concierge payers in the interview notes: "would keep Nudge" against "free reminder is enough" | 3 or more of the first 5 say the free reminder is enough | Week 4 |
| Cause 5 | Ad spend in the ad dashboard divided by new paying customers in Stripe, per $250 tranche | Cost per paying customer above $90 after any $250 tranche | Week 16 |
| Cause 6 | Bank statement for the $5,000 plus Stripe MRR, checked side by side | More than $2,500 spent while MRR is under $300 | Week 14 |
| Cause 7 | Replies to Nudge emails containing "paid", "dispute" or "stop", and spam-complaint rate in the email sending provider | Any 1 reminder sent after a client replied "paid" or "dispute", or a spam-complaint rate above 0.3% | Week 14 |
