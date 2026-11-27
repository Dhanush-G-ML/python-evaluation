# T06-E01 - match, search and fullmatch
#
# Write three functions using `re`:
#
# - `starts_with_number(text)` - `True` if the text begins with digits (use `re.match`).
# - `first_number(text)` - the first run of digits anywhere in the text as an `int`, or `None` (use `re.search`).
# - `is_whole_number(text)` - `True` only if the whole text is digits (use `re.fullmatch`).
#
# For every string in the list below print one line: the string with `repr` left-aligned in width 12, then `match=`, `search=` and `fullmatch=` with the results (each result left-aligned in width 5, except the last).
