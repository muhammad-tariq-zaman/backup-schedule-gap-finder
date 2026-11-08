import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import find_gaps

import datetime
AS_OF = datetime.date(2026, 11, 7)

def row(j, last, exp):
    return {"job": j, "last_backup": last, "expected_days": str(exp)}

class TestBackupGaps(unittest.TestCase):
    def test_gap(self):
        self.assertEqual(find_gaps([row("DB", "2026-10-20", 7)], AS_OF)[0][4], "GAP")
    def test_ok(self):
        self.assertEqual(find_gaps([row("DB", "2026-11-06", 7)], AS_OF)[0][4], "OK")
    def test_exactly_at_interval_ok(self):
        self.assertEqual(find_gaps([row("DB", "2026-10-31", 7)], AS_OF)[0][4], "OK")
    def test_gap_days_computed(self):
        self.assertEqual(find_gaps([row("DB", "2026-10-20", 7)], AS_OF)[0][2], 18)
    def test_largest_gap_first(self):
        r = find_gaps([row("A", "2026-11-06", 7), row("B", "2026-10-20", 7)], AS_OF)
        self.assertEqual(r[0][0], "B")
