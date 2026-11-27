# T09-E04: Fibonacci with memoization
#
# Write three Fibonacci functions (`fib(0) = 0`, `fib(1) = 1`):
#
# - `fib_naive(n, counter=None)`: plain double recursion. If `counter` is a one-element list, add 1 to `counter[0]`
#   on every call.
# - `fib_memo(n, memo=None, counter=None)`: recursive, but results are stored in a dictionary `memo` that is
#   shared by all recursive calls and created fresh on each top-level call. Count calls the same way.
# - `fib_iter(n)`: a loop version, used to cross-check the other results.
