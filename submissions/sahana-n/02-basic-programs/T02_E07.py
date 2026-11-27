# T02-E07 - Simple menu program
#
# Write a calculator that shows a menu and repeats until the user chooses Quit. Print the menu exactly as shown each time, then read the choice (no prompt text). For choices 1 to 4 read two more lines (the two numbers). Behaviour:
#
# - `5` prints `Goodbye` and ends the program.
# - Any other choice prints `Invalid choice` and shows the menu again.
# - If either number is not a valid number, print `Not a number` and show the menu again.
# - Division by zero prints `Cannot divide by zero`.
# - Otherwise print `Result: <value>` formatted with `:g` (so 8.0 shows as `8`).
#
# Put the arithmetic in `calculate(op, a, b)` which returns `None` for division by zero.
