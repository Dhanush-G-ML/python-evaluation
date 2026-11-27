# T14-E08 - Structured logging: JSON lines
#
# Write `JsonFormatter(logging.Formatter)` whose `format(record)` returns one line of JSON with the keys `level`, `logger` and `message` (the message with its arguments filled in), followed by every extra field that was passed with `extra=`, and, when the record carries an exception, the key `exception` with the text `<ExceptionType>: <message>`. Values that JSON cannot store (such as `Decimal` and `Path`) must be turned into strings.
#
# Write `make_logger(stream)` for a logger named `json.demo` (level `DEBUG`, `propagate = False`) with one `StreamHandler(stream)` that uses the formatter. Write `produce_lines()` that logs the following into an `io.StringIO` and returns the lines:
#
# ```python
# logger.info("user %s signed in", "ana", extra={"user_id": 7, "ip": "10.0.0.5"})
# logger.warning("slow payment", extra={"amount": Decimal("19.90"), "file": Path("invoices/a-17.pdf")})
# try:
#     {}["missing"]
# except KeyError:
#     logger.error("lookup failed", exc_info=True)
# logger.debug("plain message")
# ```
#
# Write `summarise(lines)` that parses the lines with `json.loads` and returns `(Counter of levels, list of dicts)`. The main program prints the four lines, then `Per level: <dict>`, `Lines with an exception: <list of messages>` and `Extra keys seen: <sorted list of keys other than level, logger and message>`.
