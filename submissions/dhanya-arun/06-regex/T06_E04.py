# T06-E04 - Dates with groups
#
# `data/dates.txt` has 25 lines, each supposed to be a date. Accepted shapes are `YYYY-MM-DD`, `DD/MM/YYYY` and `D Mon YYYY` (for example `5 Jan 2026`, month names `Jan` to `Dec`). Write `parse_date(text)` that returns a `datetime.date`. It must raise `ValueError("unrecognised format")` when the text matches none of the shapes (the whole text must match) and `ValueError("invalid date")` when the shape is right but the calendar date does not exist (`31/02/2026`, month 13, 29 February in a non-leap year).
#
# Print one line per input line: the text left-aligned in width 15, ` -> `, and the ISO date (`YYYY-MM-DD`) or the error message. Finally print a dictionary with the counts of `ok`, `invalid date` and `unrecognised format`.
