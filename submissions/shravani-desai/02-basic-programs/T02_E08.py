# T02-E08 - Number guessing with a fixed seed
#
# Make a guessing game that is reproducible. At the start call `random.seed(42)` and pick the secret with `random.randint(1, 100)` (this gives the same number every run). The player has 7 valid attempts. Read one guess per line (no prompt text):
#
# - Not a whole number: print `Please enter a whole number` (does not use an attempt).
# - Outside 1 to 100: print `Out of range, use 1 to 100` (does not use an attempt).
# - Valid guess number `k`: print `Guess k: <guess> is too low` or `... is too high`, or on success `Guess k: <guess> is correct! Solved in k attempts` and stop.
# - After 7 valid wrong guesses print `Out of attempts. The number was <secret>`.
#
# Write a helper `check_guess(secret, guess)` returning `"low"`, `"high"` or `"correct"`.
