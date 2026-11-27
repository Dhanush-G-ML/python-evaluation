# T14-E11 - Challenge: log analyser for rotated files with tracebacks
#
# A service wrote its log with the `logging` module and a `RotatingFileHandler`. The older records are in `data/service.log.1` and the newer ones in `data/service.log`. Some records span several lines: a message with line breaks, or an `ERROR` written by `logger.exception`, which is followed by a traceback. The first lines of the older file:
#
# ```text
# 2026-03-02 10:00:10,123 INFO     shop.orders: service started with settings:
#   workers=4
#   retries=3
# ```
#
# and one error record with its traceback:
#
# ```text
# 2026-03-02 10:01:15,123 ERROR    shop.payments: charge failed for order 1007
# Traceback (most recent call last):
#   File "/srv/shop/service.py", line 156, in make_service_logs
#     action()
#   File "/srv/shop/service.py", line 135, in <lambda>
#     7: ("shop.payments", lambda: shop.charge(750), "charge failed for order %d"),
#                                  ^^^^^^^^^^^^^^^^
#   File "/srv/shop/service.py", line 108, in charge
#     raise TimeoutError("payment gateway timed out")
# TimeoutError: payment gateway timed out
# ```
#
# Write a `Record` dataclass (`time` as `datetime`, `level`, `logger`, `message`, `extra` list of continuation lines) with a property `has_traceback` (the first continuation line is `Traceback (most recent call last):`) and a method `exception()` that returns `(exception type, text)` from the last line of the traceback, or `None`.
#
# Write `read_records(paths)` that reads the files in the order given (oldest first) and adds every line that does not start with a timestamp to the previous record. Write `analyse(records)` returning: the count per level (in severity order), the number of multi-line records and of records with a traceback, the exceptions as `(type, count)` (highest first, ties by name) with the first record where each type was seen, the number of `ERROR` and `CRITICAL` records per minute (`HH:MM`, sorted), and the longest gap between two consecutive records (if two gaps are equal, the earlier one wins).
#
# Print the report in the format of the expected output (one `#` per error in the minute list).
