# T14-E01 - First log messages with basicConfig
#
# Write `setup_logging(level)` that calls `logging.basicConfig` with the given level, the format `%(levelname)s:%(name)s:%(message)s`, `stream=sys.stdout` and `force=True` (so it can be called again with a new level).
#
# Write `checkout(cart)` where `cart` is a list of `(name, price)` pairs. Use a logger named `shop` and return the total price:
#
# - `DEBUG` `cart has <n> item(s)` at the start.
# - An empty cart logs `ERROR` `cart is empty, nothing to charge` and returns `0.0`.
# - Otherwise log `INFO` `total is <total with two decimals>`.
# - A total over 100 also logs `WARNING` `large order: <total>` (two decimals).
# - A total over 500 also logs `CRITICAL` `order exceeds the limit, flagged for review`.
#
# In the main program run these three carts twice: once with level `DEBUG` (print `--- level DEBUG ---` first) and once with level `WARNING` (print `--- level WARNING ---` first):
#
# ```python
# CARTS = [
#     [("pen", 1.5), ("book", 12.0)],
#     [],
#     [("laptop", 899.0)],
# ]
# ```
