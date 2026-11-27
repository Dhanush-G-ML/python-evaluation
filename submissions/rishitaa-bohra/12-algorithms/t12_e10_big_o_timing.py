# T12-E10 Big-O analysis with timing
#
# You will measure growth in two ways.
#
# 1. **Counting operations.** Write `count_sum(n)`, which uses one loop, `count_all_pairs(n)`, which
#    uses nested loops over every pair, and `count_halving(n)`, which halves `n` until it reaches 1.
#    Each function returns how many times its innermost step ran.
# 2. **Estimating the growth rate.** `growth_exponent(sizes, costs)` returns
#    `log(cost_last / cost_first) / log(size_last / size_first)`. `classify(exponent)` turns that
#    number into a label: below 0.5 is sub-linear, below 1.5 is about linear, below 2.5 is quadratic,
#    and anything else is cubic or worse.
# 3. **Timing.** `time_function(func, *args, repeats=5)` returns the fastest of several
#    `time.perf_counter()` runs. `membership_experiment(sizes)` times the `in` operator on a list and
#    on a set, always searching for a value that is missing.
