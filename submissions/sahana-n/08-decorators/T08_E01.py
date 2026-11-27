# T08-E01: Functions as objects
#
# Functions can be stored in variables and dictionaries, passed to other functions and returned from them.
#
# Write:
#
# - `add(a, b)`, `sub(a, b)` and `mul(a, b)`.
# - A dictionary `OPERATIONS` mapping `"add"`, `"sub"` and `"mul"` to those functions (no `if/elif` chain).
# - `calculate(op_name, a, b)` that looks the operation up and calls it. For an unknown name raise
#   `ValueError(f"Unknown operation: {op_name}")`.
# - `apply_twice(func, value)` returning `func(func(value))`.
# - `compose(f, g)` returning a **new function** `h` such that `h(x) == f(g(x))`.
