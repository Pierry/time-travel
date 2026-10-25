// Every value below is copied from examples/invoice-nudge, the recorded run.
// Nothing is invented for the video.

export const PROMPT = "/time-travel:premortem plan.md";

export const PLAN = [
  "Nudge: a SaaS that chases late invoices for freelancers.",
  "$29/month, 14-day trial. Stripe + QuickBooks. AI reminder emails.",
  "Solo founder, $5,000, MVP in 6 weeks, Product Hunt in week 8.",
  "Success: 200 paying customers in six months.",
];

export const GATES = [
  { leg: "0 plan", detail: "11 details, D1..D11" },
  { leg: "1 autopsy", detail: "7 causes, 6 months each" },
  { leg: "2 verdict", detail: "fatal flaw: yes" },
  { leg: "3 rebuild", detail: "7 of 7 causes closed" },
  { leg: "4 adversary", detail: "launch week attack" },
  { leg: "5 alarm", detail: "7 alarms, weeks 4 to 16" },
];

export const CAUSES = [
  { n: 1, name: "One launch spike, then silence", p: 60 },
  { n: 2, name: "Two integrations ate the six weeks", p: 50 },
  { n: 3, name: "Late invoices are episodic, the subscription is monthly", p: 45 },
  { n: 4, name: "The free reminder already inside Stripe and QuickBooks", p: 40 },
  { n: 5, name: "$2,000 of ads bought 20 customers", p: 35 },
  { n: 6, name: "Money and founder ran out first", p: 30 },
  { n: 7, name: "A final notice hurt a client, and r/freelance heard", p: 20 },
];

export const VERDICT = {
  likely: "Cause 1, one launch spike, then silence",
  dangerous: "Cause 7, a final notice hurt a client relationship",
  flaw: "200 customers needs 30,000 to 100,000 visitors. The channels deliver 5,000 to 10,000.",
};

export const ALARMS = [
  { week: 4, cause: 4, text: "3 of 5 say the free reminder is enough" },
  { week: 7, cause: 2, text: "0 real invoices synced" },
  { week: 8, cause: 1, text: "under 75 waitlist emails" },
  { week: 14, cause: 6, text: "$2,500 spent, MRR under $300" },
  { week: 16, cause: 5, text: "over $90 per paying customer" },
];

export const STATS = [
  { value: "205 s", label: "wall time" },
  { value: "6 / 6", label: "gates passed first try" },
  { value: "7", label: "alarms in alarms.ics" },
];
