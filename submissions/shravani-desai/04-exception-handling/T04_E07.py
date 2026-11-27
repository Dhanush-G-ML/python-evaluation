# T04-E07 - Ask until valid
#
# Write `read_int(prompt, low, high, max_tries=3, read=input, out=print)` that asks for a whole number between `low` and `high`. Each time it asks, call `out(prompt)` (print the prompt on its own line), then `read()` to get the text. Messages: `Not a whole number, try again` for text that is not an integer, `Must be between <low> and <high>` for an out-of-range number. After `max_tries` invalid answers raise your own `TooManyAttemptsError`. Return the number as soon as it is valid.
#
# Main program: read an age (0 to 120) and print `Age accepted: <age>`. Then ask for a month (1 to 12) inside `try`; if `TooManyAttemptsError` is raised print `Giving up: too many invalid attempts`.
