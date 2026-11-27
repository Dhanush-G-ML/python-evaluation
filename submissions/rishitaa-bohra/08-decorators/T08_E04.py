# T08-E04: Logging decorator with functools.wraps
#
# Write a decorator `log_calls` that uses a logger named `"calls"` (`logging.getLogger("calls")`):
#
# - Before the call log at INFO: `Calling add(2, 3)` (positional args shown with `repr`, keyword args as `name=value`).
# - After a successful call log at INFO: `add returned 5`.
# - If the function raises, log at ERROR: `fail raised ZeroDivisionError: nope` and **re-raise** the exception.
# - Use `functools.wraps` so the wrapper keeps the original `__name__` and `__doc__`.
#
# Define `add(a, b)` with docstring `"Add two numbers."` and `fail()` raising `ZeroDivisionError("nope")`, both
# decorated. The driver configures logging with `basicConfig`; it needs `import sys` and `import logging`.
