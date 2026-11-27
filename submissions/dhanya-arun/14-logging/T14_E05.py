# T14-E05 - Rotating log files
#
# Write `setup_logging(directory, max_bytes=200, backups=3)` that creates the folder, deletes any old `app.log*` files in it, and configures a logger named `rotating.demo` (level `INFO`, `propagate = False`) with a `RotatingFileHandler` for `app.log` (UTF-8, the given limits, format `%(message)s`). Write `close_logging(logger)` as in the last exercise.
#
# Write `write_events(logger, count)` that logs `event <nn>: batch processed` for `nn` from 1 to `count` (two digits, `event 01`). Write `describe(directory)` that returns `(file name, line count, first line, last line)` for `app.log`, `app.log.1`, `app.log.2`, ... in that order.
#
# In the main program write 30 events into `output/rotating` and print a table: the file name left-aligned to width 10, the line count right-aligned to width 5, two spaces, then the first 8 characters of the first line, ` -> ` and the first 8 characters of the last line. The header is shown in the expected output.
