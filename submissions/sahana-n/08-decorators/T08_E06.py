# T08-E06: Timing decorator
#
# Write a decorator `timer` that measures how long each call takes with `time.perf_counter()` and stores
# statistics as attributes on the wrapper function:
#
# - `calls`: number of calls so far,
# - `last_duration`: seconds taken by the latest call,
# - `total_time`: sum of all durations.
#
# Failed calls must be timed and counted too, and the exception must still propagate. Keep the original name
# with `functools.wraps`.
#
# Define `slow(n)` (sleeps 0.05 seconds, returns `n * 2`) and `boom()` (raises `RuntimeError("failed")`), both
# decorated. The driver uses `time`, so import it.
