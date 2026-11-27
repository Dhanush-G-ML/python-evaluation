# T04-E08 - Logging instead of print
#
# Process `data/readings.txt` with the `logging` module. Write `process_readings(lines, logger)` that returns the list of accepted floats and logs:
#
# - `WARNING` `line <n>: empty line` for blank lines.
# - `WARNING` `line <n>: not a number: <text as repr>` for lines that are not numbers.
# - `WARNING` `line <n>: reading <value> out of range` for values outside -20 to 60.
# - `DEBUG` `line <n>: accepted <value>` for good lines.
# - `INFO` `Processed <total> lines: <valid> valid, <skipped> skipped` at the end.
#
# Write `average(values, logger)` that returns the mean, or logs an `ERROR` `Could not compute average: <exception>` and returns `None` when there are no values (catch `ZeroDivisionError`).
#
# Set up a logger named `readings` with format `%(levelname)s:%(name)s:%(message)s`: a console handler showing `INFO` and above, and a file handler writing everything (`DEBUG` and above) to `output/readings.log`. In the main program print the average, call `average([], logger)` to show the error, and print the number of lines in the log file.
