# T08-E05: Decorators with arguments
#
# A decorator that takes arguments is a function that **returns** a decorator.
#
# - `repeat(times)` runs the decorated function `times` times and returns the list of all results. `repeat(0)`
#   (or less) must raise `ValueError("times must be at least 1")` immediately, when the decorator is created.
# - `clamp_result(low, high)` forces the numeric result of the decorated function into the range `low..high`.
#
# Use `functools.wraps` in both. Define `hello(name)` decorated with `@repeat(3)`; it prints `Hello, <name>` and
# returns the upper-cased name. Define `score(raw)` decorated with `@clamp_result(0, 100)` returning `raw * 2`.
