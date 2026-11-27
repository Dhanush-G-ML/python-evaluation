# T08-E07: Caching: memoize and lru_cache
#
# Compare three versions of a recursive Fibonacci function.
#
# 1. `fib_plain(n)`: plain recursion.
# 2. `fib_memo(n)`: decorated with your own `memoize` decorator (store results in a dict keyed by the argument
#    tuple; expose the dict as `wrapper.cache`).
# 3. `fib_lru(n)`: decorated with `functools.lru_cache(maxsize=None)`.
#
# Each version increments its own counter in the dictionary `calls` (`"plain"`, `"memo"`, `"lru"`) every time the
# body actually runs. Also define `square(n)` with `@lru_cache(maxsize=2)` and observe `cache_info()` after calling it
# with 1, 2, 1, 3, 2.
