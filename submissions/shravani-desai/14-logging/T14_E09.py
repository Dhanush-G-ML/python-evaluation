# T14-E09 - Logging exceptions with exc_info
#
# Write `ConfigError(Exception)` and `parse_amount(text)`:
#
# - Text that is not a number raises `ConfigError("bad amount <text as repr>")` chained with `from` to the original `ValueError`.
# - A negative amount raises `ValueError("negative amount")`.
# - Zero raises `ValueError("zero amount")`.
# - Otherwise it returns the amount as a float.
#
# A full traceback has file paths in it, which is too noisy for this exercise. Write `BriefFormatter(logging.Formatter)` that overrides `formatException(exc_info)` and returns one line: four spaces, `raised in <function name>(): ` and then the chain of exceptions as `Type: message`, joined with ` <- `, starting with the exception itself and following `__cause__` (or `__context__`). The function name is the last frame of the traceback.
#
# Write `setup_logging()` for a logger named `amounts` (level `DEBUG`, `propagate = False`, `StreamHandler` on `sys.stdout`, `BriefFormatter("%(levelname)s %(message)s")`) and `process(lines, logger)` that adds up the valid amounts and logs the failures in three different ways:
#
# - `ConfigError`: `logger.exception("line <n> skipped")`
# - negative amount: `logger.warning("line <n> rejected", exc_info=error)` (pass the exception object)
# - zero amount: `logger.error("line <n> ignored: <error>")` without any traceback
#
# Main program: process `["12.5", "abc", "7", "-3", "0", "2.5"]` and log `INFO` `total is <total, two decimals>`.
