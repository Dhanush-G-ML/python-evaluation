# T04-E10 - Challenge: robust order processor
#
# `data/orders.csv` has columns `order_id,customer,quantity,unit_price`, and some rows are bad. Build an order processor.
#
# 1. Exceptions: `OrderError(Exception)` with attributes `row` (data row number, starting at 1) and `order_id`; subclasses `MissingFieldError` and `InvalidValueError`.
# 2. `parse_order(row_number, row)` returns a dictionary `order_id, customer, quantity, unit_price, total` (total rounded to 2 decimals). Checks in this order: empty `customer` or empty `unit_price` raise `MissingFieldError` with the messages `customer is missing` / `unit_price is missing`. Then `quantity` must be a whole number (`quantity must be a whole number (got 'two')`) and positive (`quantity must be positive (got 0)`); then `unit_price` must be a number (`unit_price must be a number (got 'abc')`) and not negative (`unit_price must not be negative (got -5.0)`). Use `raise ... from exc` when you convert a `ValueError` into your own exception.
# 3. `process_orders(path)` returns `(orders, errors)`; a bad row must not stop the processing of the other rows.
# 4. Main program: print `Row <n> (order <id>): <message>` for each error, then `Processed <n> rows: <ok> ok, <bad> failed`, then `Total value of valid orders: <value>` (two decimals). If there are errors, raise `ExceptionGroup("order errors", errors)` and handle it with two `except*` clauses, printing `except* MissingFieldError: <n> errors` and `except* InvalidValueError: <n> errors`.
