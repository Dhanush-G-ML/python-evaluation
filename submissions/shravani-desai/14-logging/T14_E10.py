# T14-E10 - Analyse a log file
#
# `data/app.log` was written by the `logging` module with the format `%(asctime)s %(levelname)-8s %(name)s: %(message)s`. A line looks like this (the first lines of the file):
#
# ```text
# 2026-03-02 09:00:04,123 WARNING  app.auth: login failed for user bob
# 2026-03-02 09:00:13,123 INFO     app.web: GET /account 200 45ms
# 2026-03-02 09:00:23,123 DEBUG    app.db: query products took 52ms
# 2026-03-02 09:00:36,123 INFO     app.web: GET /cart 200 122ms
# ```
#
# Write `parse_line(line)` that returns a dict with `date`, `time`, `ms`, `level`, `logger`, `message` and `minute` (`YYYY-MM-DD HH:MM`) for a log line, or `None` when the line does not match. Write `load_records(path)` that returns the parsed records of a file. Write `summarise(records)` that returns a dict with: `total`; `levels` (dict in the order DEBUG, INFO, WARNING, ERROR, CRITICAL, only levels that occur); `loggers` (list of `(name, count)`, highest count first, ties by name); `first` and `last` (`date time` text of the first and last record); `errors` (the `ERROR` and `CRITICAL` records); `busiest` (the minute with the most records, and its count; ties go to the earlier minute); and for the `app.web` messages of the form `GET <path> <status> <n>ms`: the number of requests, the average time and the slowest request line.
#
# Print the report in the format shown in the expected output.
