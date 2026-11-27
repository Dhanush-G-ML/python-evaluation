# T03-E09 - Challenge: clean a messy contact file
#
# `data/dirty_contacts.csv` has columns `name,email,phone,city` and messy data. Write `clean_contacts(src, good_dst, reject_dst)` that reads it and writes two CSV files, returning a summary dictionary `{"read": n, "kept": n, "rejected": {reason: count}}`.
#
# Cleaning rules for a row (row numbers count data rows from 1):
#
# - Name: remove extra spaces and use title case. Empty name: reject with reason `missing name`.
# - Email: strip and lower-case. It must contain exactly one `@`, no spaces, a non-empty part before the `@`, and a domain that contains a dot (not at the start or end). Otherwise reject with `invalid email`.
# - An email already kept earlier is rejected with `duplicate email`. Check the rules in this order: name, email format, duplicate.
# - Phone: keep digits only, but keep a leading `+`. An empty phone is allowed.
# - City: remove extra spaces and use title case.
#
# `good_dst` has header `name,email,phone,city`. `reject_dst` has header `row,reason,name,email` and the original (stripped) name and email. In the main program use `output/clean_contacts.csv` and `output/rejects.csv`; print the counts, the full reject file, then the first 4 lines of the clean file.
