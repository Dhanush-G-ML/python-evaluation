# T04-E01 - Safe division
#
# Read lines from standard input until the input ends; skip blank lines. Each line should hold two numbers separated by a space. Write `divide_line(line)` that returns a message string:
#
# - Normal case: `<a> / <b> = <result>` using `:g` formatting for all three numbers (so `10.0` shows as `10`).
# - Division by zero: `Cannot divide by zero`.
# - Anything else wrong (not numbers, or not exactly two items): `Invalid input: expected two numbers`.
#
# Use `try`, specific `except` clauses and `else`; do not use a bare `except:`. Print the message for every line.
