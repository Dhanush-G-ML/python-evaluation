# T07-E10: Money value object
#
# Write an immutable `Money` class that stores whole **cents** (an integer) and a currency code (default `"EUR"`).
#
# - `Money(cents, currency="EUR")`, read-only properties `cents` and `currency`, and `Money.from_str("12.50")`
#   (also accept `"2.5"` meaning 2.50 and negative values such as `"-3.05"`).
# - `repr` gives `Money(250, 'EUR')`; `str` gives `12.50 EUR` (negative: `-12.50 EUR`).
# - `+` and `-` between two `Money` values; mixing currencies raises `ValueError("Currency mismatch: EUR vs USD")`.
# - `*` with an `int` (both `m * 3` and `3 * m`); unary minus.
# - Equality, hashing (equal values must hash equal, so sets work), and ordering with all of `<, <=, >, >=`
#   (use `functools.total_ordering`; comparing different currencies raises `ValueError`).
# - `sum([...])` must work, so `0 + money` has to be supported.
# - `bool(Money(0))` is `False`.
# - `split(parts)` returns a list of `parts` shares that add up exactly to the original amount; leftover cents go
#   to the first shares (10.00 split 3 ways is 3.34, 3.33, 3.33).
