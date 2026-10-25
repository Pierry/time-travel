#!/usr/bin/env python3
"""
Every rule of the gate, both ways.

The clean trip in `sensors/fixtures/trip.md` must pass. Each case below
breaks it in one place and names the finding that must appear. A gate that
blocks a clean trip is as broken as one that releases a bad one, so the clean
trip is checked on every leg too.

    python3 sensors/test_sensors.py
    python3 sensors/test_sensors.py --verbose
"""

from __future__ import annotations

import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "sensors"))

import trip_lint as t  # noqa: E402

CLEAN = (ROOT / "sensors" / "fixtures" / "trip.md").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "templates" / "trip.md").read_text(encoding="utf-8")


def hard(text: str, phase: str = "all") -> list[str]:
    return [str(f) for f in t.run(text, phase) if f.severity == "hard"]


def soft(text: str, phase: str = "all") -> list[str]:
    return [str(f) for f in t.run(text, phase) if f.severity == "soft"]


def swap(old: str, new: str, text: str = CLEAN, count: int = 1) -> str:
    assert old in text, f"fixture drifted, not found: {old!r}"
    return text.replace(old, new, count)


def drop_cause(n: int, text: str = CLEAN) -> str:
    body = t.sections(text)["1"]
    marks = list(t.CAUSE_HEADING.finditer(body))
    m = marks[n - 1]
    end = marks[n].start() if n < len(marks) else len(body)
    return text.replace(body[m.start():end], "", 1)


class Clean(unittest.TestCase):
    def test_example_passes_every_leg(self):
        for phase in t.PHASES + ["all", "auto"]:
            with self.subTest(phase=phase):
                self.assertEqual(hard(CLEAN, phase), [])

    def test_example_has_no_warnings(self):
        self.assertEqual(soft(CLEAN), [])

    def test_untouched_template_is_not_gated_by_auto(self):
        self.assertIsNone(t.reached(TEMPLATE))
        self.assertEqual(hard(TEMPLATE, "auto"), [])

    def test_untouched_template_fails_all(self):
        self.assertGreater(len(hard(TEMPLATE, "all")), 20)

    def test_auto_gates_only_what_was_written(self):
        partial = TEMPLATE
        for key, value in (("Departure", "2026-10-25"), ("Arrival", "2027-04-25"), ("Goal", "open a bakery")):
            partial = re.sub(rf"^- {key}: .*$", f"- {key}: {value}", partial, count=1, flags=re.MULTILINE)
        self.assertEqual(t.reached(partial), "plan")
        found = hard(partial, "auto")
        self.assertTrue(any("`Budget`" in f for f in found))
        self.assertFalse(any("section 1" in f for f in found))

    def test_auto_reaches_the_last_leg_written(self):
        self.assertEqual(t.reached(CLEAN), "alarm")

    def test_pending_on_a_later_leg_does_not_raise_the_reach(self):
        text = TEMPLATE.replace("- Who: <a competitor", "- Who: pending: after the rebuild <a competitor")
        self.assertIsNone(t.reached(text))


class Plan(unittest.TestCase):
    def test_missing_section(self):
        text = swap("## 0. Plan", "## Plan")
        self.assertTrue(any("section 0: section missing" in f for f in hard(text, "plan")))

    def test_bad_date(self):
        text = swap("- Departure: 2026-10-25", "- Departure: today")
        self.assertTrue(any("not a YYYY-MM-DD" in f for f in hard(text, "plan")))

    def test_trip_must_be_six_months(self):
        text = swap("- Arrival: 2027-04-25", "- Arrival: 2026-12-25")
        self.assertTrue(any("days forward" in f for f in hard(text, "plan")))

    def test_seven_months_is_too_far(self):
        text = swap("- Arrival: 2027-04-25", "- Arrival: 2027-05-25")
        self.assertTrue(any("days forward" in f for f in hard(text, "plan")))

    def test_empty_goal(self):
        text = swap("- Goal: Launch Nudge", "- Goal: <the goal> Launch Nudge")
        self.assertTrue(any("`Goal`" in f for f in hard(text, "plan")))

    def test_pending_field(self):
        text = swap("- Budget: $5,000", "- Budget: pending: ask for the number $5,000")
        self.assertTrue(any("`Budget` is still pending" in f for f in hard(text, "plan")))

    def test_not_given_is_an_answer(self):
        text = swap("- Timeline: MVP in 6 weeks, Product Hunt launch in week 8", "- Timeline: not given")
        self.assertEqual(hard(text, "plan"), [])

    def test_too_few_details(self):
        body = t.sections(CLEAN)["0"].split("### Details")[1]
        text = CLEAN.replace(body, "\n\n1. D1: price\n2. D2: team\n\n", 1)
        self.assertTrue(any("2 plan details" in f for f in hard(text, "plan")))

    def test_gap_in_detail_numbers(self):
        text = swap("3. D3:", "3. D9:")
        self.assertTrue(any("no gap" in f for f in hard(text, "plan")))


class Autopsy(unittest.TestCase):
    def test_six_causes(self):
        self.assertTrue(any("exactly 7" in f for f in hard(drop_cause(7), "autopsy")))

    def test_eight_causes(self):
        extra = "\n### Cause 8: extra\n\n- Likelihood: 5%\n"
        text = CLEAN.replace("\n## 2. Verdict", extra + "\n## 2. Verdict", 1)
        self.assertTrue(any("exactly 7" in f for f in hard(text, "autopsy")))

    def test_unnamed_cause(self):
        text = swap("### Cause 3: The trial ends before the first invoice is late", "### Cause 3:")
        self.assertTrue(any("cause 3: the cause has no name" in f for f in hard(text, "autopsy")))

    def test_likelihood_without_percent(self):
        text = swap("- Likelihood: 45%", "- Likelihood: high")
        self.assertTrue(any("carries no percent" in f for f in hard(text, "autopsy")))

    def test_likelihood_out_of_range(self):
        text = swap("- Likelihood: 70%", "- Likelihood: 170%")
        self.assertTrue(any("outside 1 to 100" in f for f in hard(text, "autopsy")))

    def test_likelihood_must_not_rise(self):
        text = swap("- Likelihood: 35%", "- Likelihood: 50%")
        self.assertTrue(any("cause 4: likelihood 50.0% is above" in f for f in hard(text, "autopsy")))

    def test_equal_likelihood_is_allowed(self):
        text = swap("- Likelihood: 35%", "- Likelihood: 45%")
        self.assertEqual(hard(text, "autopsy"), [])

    def test_decimal_comma_likelihood(self):
        text = swap("- Likelihood: 15%", "- Likelihood: 12,5%")
        self.assertEqual(hard(text, "autopsy"), [])

    def test_missing_premise(self):
        text = swap("- Premise: both integrations are a weekend each\n", "")
        self.assertTrue(any("cause 5: field `Premise` is missing" in f for f in hard(text, "autopsy")))

    def test_missing_warning_sign(self):
        text = swap("- First warning sign: two weeks in a row with no distribution work shipped", "- First warning sign:")
        self.assertTrue(any("cause 6: `First warning sign`" in f for f in hard(text, "autopsy")))

    def test_trace_to_unknown_detail(self):
        text = swap("- Traces to: D7", "- Traces to: D12")
        self.assertTrue(any("D12, which section 0 does not list" in f for f in hard(text, "autopsy")))

    def test_trace_to_nothing(self):
        text = swap("- Traces to: D7", "- Traces to: the market")
        self.assertTrue(any("names no plan detail" in f for f in hard(text, "autopsy")))

    def test_trace_to_a_cut_is_allowed(self):
        text = swap("- Traces to: D8", "- Traces to: cut: the plan has no weekly metric at all")
        self.assertEqual(hard(text, "autopsy"), [])

    def test_bare_cut_is_not_a_reason(self):
        text = swap("- Traces to: D8", "- Traces to: cut:")
        self.assertTrue(any("cause 7" in f and "names no plan detail" in f for f in hard(text, "autopsy")))

    def test_mostly_cuts_warns(self):
        text = CLEAN
        for d in ("D1", "D2", "D3", "D5", "D6"):
            text = text.replace(f"- Traces to: {d}\n", "- Traces to: cut: something the plan never said\n", 1)
        self.assertEqual(hard(text, "autopsy"), [])
        self.assertTrue(any("generic advice" in f for f in soft(text, "autopsy")))

    def test_month_missing(self):
        text = swap("| 6 | 38 paying, 19% of the goal; savings cover two more months |\n", "")
        self.assertTrue(any("cause 1: the timeline covers months [1, 2, 3, 4, 5]" in f for f in hard(text, "autopsy")))

    def test_month_empty(self):
        text = swap("| 3 | Launch moves from week 8 to week 12 |", "| 3 | ... |")
        self.assertTrue(any("cause 5: month 3" in f for f in hard(text, "autopsy")))


class Verdict(unittest.TestCase):
    def test_two_causes_in_most_likely(self):
        text = swap("- Most likely: Cause 1,", "- Most likely: Cause 1 and Cause 3,")
        self.assertTrue(any("names 2 causes" in f for f in hard(text, "verdict")))

    def test_no_cause_named(self):
        text = swap("- Most dangerous: Cause 2,", "- Most dangerous: the trust one,")
        self.assertTrue(any("`Most dangerous` names 0 causes" in f for f in hard(text, "verdict")))

    def test_cause_that_does_not_exist(self):
        text = swap("- Most dangerous: Cause 2,", "- Most dangerous: Cause 9,")
        self.assertTrue(any("does not have" in f for f in hard(text, "verdict")))

    def test_most_likely_contradicts_the_autopsy(self):
        text = swap("- Most likely: Cause 1,", "- Most likely: Cause 4,")
        self.assertTrue(any("contradicts the autopsy" in f for f in hard(text, "verdict")))

    def test_same_cause_needs_same(self):
        text = swap("- Most dangerous: Cause 2,", "- Most dangerous: Cause 1,")
        self.assertTrue(any("starts with `same:`" in f for f in hard(text, "verdict")))

    def test_same_cause_with_reason_passes(self):
        text = swap("- Most dangerous: Cause 2,", "- Most dangerous: Cause 1,")
        text = swap("- Why they differ: Cause 1 is", "- Why they differ: same: no channel means no customers at all, and Cause 1 is", text)
        self.assertEqual(hard(text, "verdict"), [])

    def test_fatal_flaw_must_commit(self):
        text = swap("- Fatal flaw: yes:", "- Fatal flaw: maybe,")
        self.assertTrue(any("`Fatal flaw` starts with" in f for f in hard(text, "verdict")))

    def test_fatal_flaw_no_with_reason(self):
        text = swap("- Fatal flaw: yes:", "- Fatal flaw: no: each cause has a fix inside the budget, and")
        self.assertEqual(hard(text, "verdict"), [])

    def test_fatal_flaw_in_portuguese(self):
        text = swap("- Fatal flaw: yes:", "- Fatal flaw: sim:")
        self.assertEqual(hard(text, "verdict"), [])

    def test_missing_hidden_assumption(self):
        text = swap("- Hidden assumption: that freelancers", "- Hidden assumption: <the premise> that freelancers")
        self.assertTrue(any("`Hidden assumption`" in f for f in hard(text, "verdict")))


class Rebuild(unittest.TestCase):
    def test_cause_left_open(self):
        text = swap("| Cause 4 | a cheap test", "| nothing | a cheap test")
        self.assertTrue(any("cause 4 is not closed" in f for f in hard(text, "rebuild")))

    def test_change_with_no_cause(self):
        text = swap("| Cause 7 | the plan is judged", "| the goal | the plan is judged")
        self.assertTrue(any("closes no cause" in f for f in hard(text, "rebuild")))

    def test_change_with_empty_why(self):
        text = swap("| a cheap test answers the question before the budget is gone |", "| ... |")
        self.assertTrue(any("change 5 has an empty cell" in f for f in hard(text, "rebuild")))

    def test_no_change_table(self):
        body = t.sections(CLEAN)["3"]
        table = t.before_subsections(body)
        text = CLEAN.replace(table, "\nRewrite pending.\n\n", 1)
        self.assertTrue(any("no change table" in f for f in hard(text, "rebuild")))

    def test_checklist_missing(self):
        text = swap("### Pre-launch checklist", "### Before launch")
        self.assertTrue(any("checklist` is missing" in f for f in hard(text, "rebuild")))

    def test_checklist_too_short(self):
        text = swap("| Pre-sell: offer 3 months for $60 to the waitlist before writing the product | fewer than 10 people pay |\n", "")
        text = swap("| Price one community sponsorship and ask for its past click numbers | the cost per click implied is above $3 |\n", "", text)
        self.assertTrue(any("checklist has 2 items" in f for f in hard(text, "rebuild")))

    def test_checklist_too_long(self):
        row = "| Ask a bank how long a business loan takes | longer than 8 weeks |\n"
        anchor = "| Price one community sponsorship"
        text = swap(anchor, row + row + anchor)
        self.assertTrue(any("checklist has 6 items" in f for f in hard(text, "rebuild")))

    def test_checklist_without_quit(self):
        text = swap("| fewer than 10 people pay |", "| ... |")
        self.assertTrue(any("checklist item 3 has no `Quit if`" in f for f in hard(text, "rebuild")))


class Adversary(unittest.TestCase):
    def test_every_field_required(self):
        for key in ("Who", "Attack point", "Launch week", "Blind side", "Counter"):
            with self.subTest(key=key):
                text = re.sub(rf"^- {key}: .*$", f"- {key}:", CLEAN, count=1, flags=re.MULTILINE)
                self.assertTrue(any(f"`{key}`" in f for f in hard(text, "adversary")))


class Alarm(unittest.TestCase):
    def test_cause_without_alarm(self):
        text = swap("| Cause 6 | hours logged", "| Team | hours logged")
        self.assertTrue(any("alarm 6 names 0 causes" in f for f in hard(text, "alarm")))
        self.assertTrue(any("cause 6 has no alarm" in f for f in hard(text, "alarm")))

    def test_threshold_without_number(self):
        text = swap("| under 20% of launch week trials |", "| much lower than launch |")
        self.assertTrue(any("cause 1 has no number in its threshold" in f for f in hard(text, "alarm")))

    def test_vague_check_week(self):
        text = swap("| Week 14 |", "| every month |")
        self.assertTrue(any("cause 7 has no exact check week" in f for f in hard(text, "alarm")))

    def test_week_past_six_months(self):
        text = swap("| Week 14 |", "| Week 30 |")
        self.assertTrue(any("week 30" in f for f in hard(text, "alarm")))

    def test_portuguese_week(self):
        text = swap("| Week 14 |", "| Semana 14 |")
        self.assertEqual(hard(text, "alarm"), [])

    def test_date_inside_trip(self):
        text = swap("| Week 14 |", "| 2027-01-31 |")
        self.assertEqual(hard(text, "alarm"), [])

    def test_date_outside_trip(self):
        text = swap("| Week 14 |", "| 2027-09-01 |")
        self.assertTrue(any("outside the trip" in f for f in hard(text, "alarm")))

    def test_empty_cell(self):
        text = swap("| Cause 2 | share of drafts sent with no edit, from the app database |", "| Cause 2 |  |")
        self.assertTrue(any("alarm 2 has an empty cell" in f for f in hard(text, "alarm")))

    def test_two_alarms_for_one_cause_warns(self):
        row = "| Cause 3 | trial to paid conversion | under 10% | Week 12 |\n"
        text = swap("| Cause 4 | cost per trial", row + "| Cause 4 | cost per trial")
        self.assertEqual(hard(text, "alarm"), [])
        self.assertTrue(any("cause 3 has 2 alarms" in f for f in soft(text, "alarm")))


class Tone(unittest.TestCase):
    def test_reassurance_is_refused(self):
        for phrase in ("Don't worry, this is fixable", "You'll be fine", "great plan overall", "good luck",
                       "Não se preocupe", "fique tranquilo", "vai dar certo", "ótimo plano", "boa sorte"):
            with self.subTest(phrase=phrase):
                text = swap("- Hidden assumption: that", f"- Hidden assumption: {phrase}. That")
                self.assertTrue(any("reassurance" in f for f in hard(text, "plan")))

    def test_reassurance_on_any_leg(self):
        text = swap("| Week 14 |", "| Week 14, good luck |")
        self.assertTrue(any("reassurance" in f for f in hard(text, "plan")))

    def test_words_that_only_look_alike(self):
        text = swap("- Hidden assumption: that", "- Hidden assumption: the worry is that")
        self.assertEqual(hard(text), [])

    def test_preamble_is_not_checked(self):
        text = CLEAN.replace("One file per plan", "Good luck reading this. One file per plan", 1)
        self.assertEqual(hard(text), [])


class Cli(unittest.TestCase):
    def run_cli(self, text: str, phase: str = "all") -> int:
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "trip.md"
            p.write_text(text, encoding="utf-8")
            from contextlib import redirect_stdout
            import io
            with redirect_stdout(io.StringIO()):
                return t.main(["--artifact", str(p), "--phase", phase])

    def test_exit_zero_on_clean(self):
        self.assertEqual(self.run_cli(CLEAN), 0)

    def test_exit_one_on_blocker(self):
        self.assertEqual(self.run_cli(drop_cause(2)), 1)

    def test_exit_one_on_missing_file(self):
        import io
        from contextlib import redirect_stderr
        with redirect_stderr(io.StringIO()):
            self.assertEqual(t.main(["--artifact", "/nonexistent/trip.md"]), 1)


if __name__ == "__main__":
    verbosity = 2 if "--verbose" in sys.argv else 1
    argv = [a for a in sys.argv if a != "--verbose"]
    unittest.main(argv=argv, verbosity=verbosity)
