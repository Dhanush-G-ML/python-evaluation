# T04-E09 - Challenge: retry decorator with backoff
#
# Write a decorator factory `retry(attempts=3, delay=1.0, backoff=2.0, exceptions=(Exception,), sleep=time.sleep)`. The decorated function is called; if it raises one of `exceptions`, wait with `sleep(wait)` and try again. The first wait is `delay`, and each following wait is multiplied by `backoff`. If the last attempt also fails, re-raise that exception (no sleep after the last attempt). Exceptions that are not in `exceptions` must propagate immediately without retrying. Keep the function name and docstring (`functools.wraps`).
#
# Also write `make_flaky(failures)` returning a function that raises `ConnectionError("temporary failure on call <n>")` for its first `failures` calls and then returns `data after <n> calls`.
#
# Main program (never really sleep: pass a `sleep` function that records the waits in a list):
# 1. `attempts=4, delay=1.0, backoff=2.0` on a service that fails twice: print the result and the recorded sleeps.
# 2. `attempts=3, delay=0.5` on a service that always fails: print `Gave up: <message>` and the sleeps.
# 3. A function raising `ValueError` decorated to retry only on `ConnectionError`: print the error, the number of calls and the sleeps, then the function's `__name__`.
