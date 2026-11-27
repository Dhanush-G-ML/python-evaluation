# T15-E10 - Code coverage with pytest-cov
#
# Coverage tells you which lines of the code under test ran while your tests ran. It does not prove the tests are good, but a line that never ran is certainly untested. Install with `py -m pip install pytest-cov`.
#
# 1. Run `py -m pytest --cov=loyalty --cov-report=term-missing` in the folder. `--cov=loyalty` measures the module `loyalty`; `term-missing` adds the `Missing` column with the line numbers that did not run. Write down the percentage and the missing line ranges.
# 2. Open `loyalty.py` and match every missing line number to the behaviour it belongs to (error branches, tiers, the `summary` function).
# 3. Add tests until the coverage is above 90 percent. Aim for tests that check real behaviours (the errors, the tier boundaries 499, 500, 1999, 2000, redeeming with exactly enough points, the summary with and without affordable rewards), not just lines.
# 4. Add `--cov-fail-under=90` to the command. The run now fails (exit code not zero) when the coverage is below 90, which is how a team keeps the level in a build.
# 5. Run again with `--cov-branch`, which also checks that both outcomes of each `if` were taken, and compare the numbers.
#
# A `.coverage` data file appears in the folder after each run. It is a result, not source code: do not commit it and delete it when you are done.
#
# Behaviours to test
#
# | Function | Behaviour |
# |----------|-----------|
# | `points_for_purchase` | whole units only, tier multipliers 1, 2, 3; negative amount and unknown tier raise `ValueError` |
# | `tier_for_points` | bronze below 500, silver below 2000, gold from 2000; negative raises |
# | `redeem` | subtracts the cost; exactly enough is allowed; too few raises `ValueError`; unknown reward raises `KeyError` |
# | `summary` | no rewards yet, or the most expensive affordable reward |
