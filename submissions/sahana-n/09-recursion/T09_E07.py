# T09-E07: Subsets and the power set
#
# Write recursive functions that take any iterable and return lists of lists:
#
# - `subsets(items)`: all subsets (the power set). Order the result like this: first all subsets that do not
#   contain the first item, then those same subsets with the first item added in front (see expected output).
# - `combinations_of_size(items, k)`: all subsets with exactly `k` items, preserving the original item order
#   inside each combination (include-the-first-item results come before exclude-the-first-item results).
# - `subset_sum(items, target)`: all subsets whose items add up to `target` (include-first results first).
#
# A set of `n` items has `2**n` subsets; the driver checks this for `n = 10`.
