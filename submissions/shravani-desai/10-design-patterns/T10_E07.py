# T10-E07: Observer: order events
#
# **Pattern: Observer.** Write a class `EventBus` for a shop:
#
# - `subscribe(event, handler)` registers a callable for an event name.
# - `unsubscribe(event, handler)` removes it; removing a handler that is not registered does nothing.
# - `publish(event, **data)` calls every handler of that event with `**data`, in subscription order, and returns the number
#   of handlers that **completed without raising**. If a handler raises, record `f"{handler.__name__}: {error}"` in the
#   list `bus.errors` and carry on with the remaining handlers. Publishing an event nobody listens to returns `0`.
#
# Also write the module-level list `audit` and these handlers, all taking `(order_id, customer)`:
#
# - `send_email` prints `EMAIL <customer>: order <order_id> update`
# - `send_sms` prints `SMS <customer>: order <order_id> update`
# - `audit_log` appends `order_id` to `audit`
# - `broken_handler` raises `RuntimeError("service down")`
