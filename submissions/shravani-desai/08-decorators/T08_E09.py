# T08-E09: Retry decorator
#
# Write `retry(attempts=3, delay=0.0, backoff=1.0, exceptions=(Exception,), on_retry=None)`.
#
# - Call the function; if it raises one of `exceptions`, try again, up to `attempts` calls in total.
# - After the last failed attempt the **original exception** propagates.
# - Exceptions that are not in `exceptions` propagate immediately without any retry.
# - Between attempts call `time.sleep(wait)` when `wait` is not zero. `wait` starts at `delay` and is multiplied by
#   `backoff` after every sleep (so `delay=1, backoff=2` waits 1, 2, 4 seconds).
# - If `on_retry` is given, call `on_retry(attempt_number, exception)` before sleeping.
# - `attempts < 1` raises `ValueError("attempts must be at least 1")` when the decorator is created.
# - Keep metadata with `functools.wraps`.
#
# The driver uses three functions, with a shared dictionary `state = {"fetch": 0, "other": 0}`:
# `fetch()` fails twice with `ConnectionError(f"attempt {n} failed")` then returns `"payload"`
# (decorated with `attempts=3, delay=0, exceptions=(ConnectionError,)` and an `on_retry` that prints
# `retry <n>: <error>`); `always_fails()` raises `ValueError("bad input")` (decorated with `attempts=2`);
# `wrong_error()` raises `KeyError("not retried")` and counts its calls in `state["other"]`
# (decorated with `attempts=3, exceptions=(ConnectionError,)`).
