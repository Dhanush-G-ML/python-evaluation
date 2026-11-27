# T06-E09 - Challenge: analyse an application log
#
# `data/app.log` mixes single-line entries and multi-line Python tracebacks. An entry looks like `2026-03-14 09:05:10,120 ERROR [db.pool] Connection timeout after 30s (host=10.0.0.5)`; any line that is not an entry belongs to the previous entry (traceback lines).
#
# Write `analyze_app_log(text)` returning a dictionary with:
#
# - `entries` - number of entries; `continuation_lines` - number of non-blank lines that are not entries;
# - `by_level` - dictionary of level to count, sorted by level name;
# - `problems` - list of `(time_without_milliseconds, module, message)` for `ERROR` and `CRITICAL` entries in file order;
# - `avg_request_ms` - the average of the numbers in `completed in <n>ms` messages rounded to 1 decimal (`None` if there are none);
# - `timeout_seconds` - the sum of the numbers in `after <n>s` messages;
# - `hosts` - sorted list of the distinct IPv4 addresses found in `host=<ip>`;
# - `exceptions` - the exception names (such as `ValueError`) that end the tracebacks, in order.
#
# Print the report in the layout shown.
