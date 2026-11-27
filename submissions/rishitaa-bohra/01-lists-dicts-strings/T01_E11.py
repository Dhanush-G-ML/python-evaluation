# T01-E11 - Challenge: merge two nested inventories
#
# Two warehouses keep stock as nested dictionaries `{item: {"qty": int, "price": float}}`. Write:
#
# 1. `merge_inventories(a, b)` - returns a new inventory. For items in both, add the quantities and keep the higher price. Items in only one warehouse are copied. The input dictionaries must not be modified and the result must not share inner dictionaries with them.
# 2. `low_stock(inventory, threshold=50)` - sorted list of item names with quantity below the threshold.
# 3. `total_value(inventory)` - sum of `qty * price`, rounded to 2 decimals.
#
# Print each merged item sorted by name as `name` (width 8), `qty` (width 4, right-aligned) and `price` (two decimals), then the low-stock list, the total value, and whether warehouse A is unchanged (`A unchanged: True`).
