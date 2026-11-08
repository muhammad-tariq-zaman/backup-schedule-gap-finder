# backup-schedule-gap-finder

Find backup jobs whose last backup is older than expected from a CSV: GAP when days since the last backup exceed the expected interval, otherwise OK — largest gap first.

## How to run

```sh
python3 main.py backups.csv --as-of 2026-11-07
```

## Example output

```
DB-nightly: GAP (last backup 2026-10-20, 18 days ago, expected every 7 day(s))
Files-weekly: OK (last backup 2026-11-06, 1 days ago, expected every 7 day(s))
1 gap(s) found.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
