#!/usr/bin/env python3
"""The calendar export: dates, escaping, folding, and what it skips."""

from __future__ import annotations

import sys
import unittest
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import alarms_ics as a  # noqa: E402

CLEAN = (ROOT / "examples" / "invoice-nudge" / "trip.md").read_text(encoding="utf-8")
NOW = datetime(2026, 10, 25, 12, 0, tzinfo=timezone.utc)


class Export(unittest.TestCase):
    def test_one_event_per_alarm(self):
        self.assertEqual(a.ics(CLEAN, "trip", NOW).count("BEGIN:VEVENT"), 7)

    def test_week_is_the_last_day_of_that_week(self):
        self.assertEqual(a.check_day(date(2026, 10, 25), "Week 1"), date(2026, 10, 31))
        self.assertEqual(a.check_day(date(2026, 10, 25), "Week 4"), date(2026, 11, 21))

    def test_portuguese_week(self):
        self.assertEqual(a.check_day(date(2026, 10, 25), "Semana 2"), date(2026, 11, 7))

    def test_explicit_date(self):
        self.assertEqual(a.check_day(date(2026, 10, 25), "2027-01-31"), date(2027, 1, 31))

    def test_unreadable_week_is_skipped(self):
        text = CLEAN.replace("| Week 14 |", "| every month |", 1)
        self.assertEqual(len(a.alarms(text)), 6)

    def test_cause_name_in_summary(self):
        self.assertIn("SUMMARY:Alarm\\, cause 5: QuickBooks review eats the runway", a.ics(CLEAN, "trip", NOW))

    def test_lines_are_folded_and_crlf(self):
        body = a.ics(CLEAN, "trip", NOW)
        for line in body.split("\r\n"):
            self.assertLessEqual(len(line.encode("utf-8")), 75)
        self.assertTrue(body.endswith("END:VCALENDAR\r\n"))

    def test_fold_keeps_multibyte_characters_whole(self):
        folded = a.fold("DESCRIPTION:" + "não " * 40)
        for part in folded.split("\r\n"):
            self.assertLessEqual(len(part.encode("utf-8")), 75)
        self.assertEqual(folded.replace("\r\n ", ""), "DESCRIPTION:" + "não " * 40)

    def test_escaping(self):
        self.assertEqual(a.escape("a, b; c\nd"), r"a\, b\; c\nd")

    def test_stable_uids(self):
        self.assertEqual(a.ics(CLEAN, "trip", NOW), a.ics(CLEAN, "trip", NOW))

    def test_no_departure_is_an_error(self):
        with self.assertRaises(ValueError):
            a.alarms(CLEAN.replace("- Departure: 2026-10-25", "- Departure:", 1))


if __name__ == "__main__":
    verbosity = 2 if "--verbose" in sys.argv else 1
    unittest.main(argv=[x for x in sys.argv if x != "--verbose"], verbosity=verbosity)
