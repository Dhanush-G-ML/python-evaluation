# T05-E08 - JSON Lines event log
#
# `data/events.jsonl` has one JSON object per line (an event log), but a few lines are damaged. Write:
#
# - `read_events(path)` - returns `(events, bad_line_numbers)`; skips blank lines silently and records the 1-based number of every line that is not valid JSON (catch `json.JSONDecodeError`).
# - `write_jsonl(path, records)` - one `json.dumps` per line; creates the parent folder; returns the number of records.
# - `revenue_by_user(events)` - sum of `amount` of the `purchase` events per user, rounded to 2 decimals.
#
# Print: `Valid events: <n>`, `Bad lines: <list>`, the count of each event type sorted by name (name left-aligned width 9, count right-aligned width 3), revenue per user from highest to lowest (user left-aligned width 6, amount right-aligned width 8 with 2 decimals), then write only the purchase events to `output/purchases.jsonl` and print `Purchases written: <n>`, and read the file back: `Read back: <n> bad: <list> equal: <True/False>`.
