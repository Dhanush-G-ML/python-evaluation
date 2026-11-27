# T09-E03: Recursion versus iteration
#
# Implement each task twice: recursively and iteratively.
#
# - `power(base, exp)`: recursive **fast exponentiation** using the idea `x^n = (x^(n//2))^2`, times `x` when `n` is
#   odd. It must need only about `log2(exp)` calls. `power_iter(base, exp)` is the loop version. Negative `exp`
#   raises `ValueError("exp must be non-negative")`.
# - `gcd(a, b)`: Euclid's algorithm recursively (`gcd(a, b) = gcd(b, a % b)`, `gcd(a, 0) = a`) and `gcd_iter`.
# - `sum_to(n)`: `1 + 2 + ... + n` recursively and `sum_to_iter(n)` with a loop. Show that `sum_to(5000)` raises
#   `RecursionError` while the loop version works.
