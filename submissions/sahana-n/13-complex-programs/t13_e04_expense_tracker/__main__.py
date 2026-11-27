# T13-E04 Expense tracker with CSV and JSON storage
#
# Build an expense tracker. The data file is given with `--file` and can be `.csv` or `.json`; the
# file extension decides the format. It has these subcommands:
#
# - `add DATE CATEGORY AMOUNT [--note TEXT]` validates the input: the date must be `YYYY-MM-DD`,
#   the amount must be a positive number, and the category must not be empty. Categories are
#   stored in lowercase.
# - `list [--month YYYY-MM] [--category NAME]` lists matching expenses and their total.
# - `summary [--month YYYY-MM] [--budget AMOUNT]` prints category totals, largest first, each with
#   a text bar chart. Without a month, it also prints the total for each month. With a budget, it
#   says whether you are under or over.
# - `export OUTPUT` saves all the expenses in the other format.
#
# Use `decimal.Decimal` for money, never `float`.
#
# Suggested modules: `models.py` (`Expense` with validation), `storage.py` (CSV and JSON load and
# save), `reports.py` (filters and totals), `cli.py`.
