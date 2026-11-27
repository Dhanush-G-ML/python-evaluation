# T06-E03 - Clean text with sub
#
# Write four functions with `re.sub`:
#
# 1. `collapse_spaces(text)` - replace every run of whitespace (spaces, tabs, newlines) by one space and strip the ends.
# 2. `mask_numbers(text)` - every run of 6 or more digits is replaced by asterisks except its last 4 digits (use a function as the replacement). Shorter numbers stay.
# 3. `camel_to_snake(name)` - `userFirstName` becomes `user_first_name`; `HTTPResponse` becomes `h_t_t_p_response` with this simple rule (capital letter becomes `_` plus lower-case letter, no leading underscore).
# 4. `censor(text, words)` - replace each whole word from the list, ignoring case, by asterisks of the same length. `badminton` must not be touched when `bad` is censored.
#
# Print the results in the order shown.
