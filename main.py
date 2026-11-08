"""Find backup jobs whose last backup is older than expected.

Usage: python3 main.py backups.csv [--as-of 2026-11-07]
CSV columns: job,last_backup (ISO date),expected_days.
GAP when days since the last backup exceed expected_days,
otherwise OK. Largest gap first, so the riskiest job is on top.
"""
import argparse, csv, sys
from datetime import date

def find_gaps(rows, as_of=None):
    as_of = as_of or date.today()
    out = []
    for row in rows:
        last = date.fromisoformat(row["last_backup"].strip())
        gap = (as_of - last).days
        expected = int(row["expected_days"])
        verdict = "GAP" if gap > expected else "OK"
        out.append((row["job"].strip(), last.isoformat(), gap, expected, verdict))
    return sorted(out, key=lambda r: -r[2])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--as-of", default=None, help="reference date YYYY-MM-DD (default: today)")
    args = parser.parse_args(argv)
    as_of = date.fromisoformat(args.as_of) if args.as_of else None
    with open(args.path, newline="", encoding="utf-8") as f:
        results = find_gaps(list(csv.DictReader(f)), as_of)
    for job, last, gap, expected, verdict in results:
        print(f"{job}: {verdict} (last backup {last}, {gap} days ago, expected every {expected} day(s))")
    print(f"{sum(1 for *_, v in results if v == 'GAP')} gap(s) found.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
