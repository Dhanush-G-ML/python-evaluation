# T12-E12 Dynamic programming: knapsack and LCS (challenge)
#
# Write these functions:
#
# 1. `climb_stairs(n)` counts the ways to climb `n` steps when you can take 1 or 2 steps at a time. This is the warm-up.
# 2. `knapsack(items, capacity)` solves the 0/1 knapsack problem for `(name, weight, value)` items.
#    It returns `(best_value, chosen_names)`, using a bottom-up table and then walking back through
#    the table to find which items were chosen.
# 3. `knapsack_memo(items, capacity)` solves the same problem top-down with `functools.lru_cache`
#    and returns only the best value. Pass the items as a tuple.
# 4. `lcs(a, b)` returns one longest common subsequence of two strings.
