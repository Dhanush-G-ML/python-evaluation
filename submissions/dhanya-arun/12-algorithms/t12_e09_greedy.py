# T12-E09 Greedy algorithms
#
# Write these functions:
#
# - `make_change(amount, coins=(200, 100, 50, 20, 10, 5, 2, 1))` returns a dict `{coin: count}`, always taking the largest coin first.
# - `select_activities(activities)` takes `(name, start, end)` tuples and picks the largest set of
#   activities that do not overlap, by always choosing the one that ends first.
# - `fractional_knapsack(items, capacity)` takes `(name, weight, value)` tuples, where fractions of
#   an item are allowed. It returns `(total_value, [(name, fraction_taken), ...])`.
