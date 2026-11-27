# T06-E08 - Flags: IGNORECASE, MULTILINE, DOTALL, VERBOSE
#
# Work with the multi-line text below. Write:
#
# - `error_lines(text)` - every line that starts with `error` in any capitalisation (`re.IGNORECASE | re.MULTILINE`).
# - `blocks(text)` - the blocks between a `BEGIN <name>` line and an `END <name>` line (case-insensitive, same name on both lines) as a list of `(name, list_of_lines)` (`re.DOTALL` and a lazy `.*?`).
# - `find_times(text)` - all clock times `H:MM` or `HH:MM` with optional `:SS`, hours 0 to 23, minutes and seconds 00 to 59. Write the pattern with `re.VERBOSE` and comments.
#
# Print the three results (as shown), and the case-sensitive result for `^error.*$` with only `re.MULTILINE` to show what the flag changes.
