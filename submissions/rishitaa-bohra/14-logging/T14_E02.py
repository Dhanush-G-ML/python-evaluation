# T14-E02 - Levels and thresholds
#
# Register a custom level `NOTICE` with number 25 (between `INFO` and `WARNING`) using `logging.addLevelName`.
#
# Write a handler class `ListHandler(logging.Handler)` that keeps every record it receives in a list called `records`.
#
# Write `emitted_at(threshold)`: it uses a logger named `levels.demo` (with `propagate = False` and one `ListHandler`), sets the logger level to `threshold` (a level name such as `"WARNING"`), logs one message at each of `DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL` and returns the list of level names that were actually recorded.
#
# Write `enabled_flags(threshold)` that returns a dict mapping each of the six level names to `logger.isEnabledFor(level)` for the same logger.
#
# Print the level numbers, then `emitted_at` for the thresholds `DEBUG`, `NOTICE`, `WARNING` and `CRITICAL` (name left-aligned to width 9, then `-> ` and the names joined by `, `), then the `enabled_flags("ERROR")` dict.
