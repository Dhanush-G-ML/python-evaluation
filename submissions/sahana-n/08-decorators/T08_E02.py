# T08-E02: Closures: counters and multipliers
#
# A closure is an inner function that remembers variables from the function that created it.
#
# - `make_counter(start=0, step=1)` returns a function. The first call returns `start`, the next `start + step`,
#   and so on. Each counter keeps its own state (use `nonlocal`).
# - `make_multiplier(n)` returns a function that multiplies its argument by `n`.
# - `build_multipliers(factors)` returns a list of multiplier functions, one per factor.
#
# The driver also prints a "broken" list built with lambdas in a loop; study the output and explain why every
# function multiplies by 4.
