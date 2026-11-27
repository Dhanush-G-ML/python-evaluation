# T15-E08 - Markers 2: custom markers, pytest.ini and -m
#
# Part A - the warning. Run `py -m pytest -v` in the folder. The tests pass, but pytest warns that `smoke` and `slow` are unknown marks (`PytestUnknownMarkWarning`), because a typo in a marker name would silently select nothing. Then run `py -m pytest --strict-markers` and see that it becomes an error.
#
# Part B - register the markers. Create `pytest.ini` in the folder:
#
# ```ini
# [pytest]
# markers =
#     smoke: fast checks that must always pass
#     slow: tests that take noticeably longer (deselect with -m "not slow")
# addopts = --strict-markers
# ```
#
# `addopts` adds `--strict-markers` to every run. Check with `py -m pytest --markers` that your two markers are listed with their descriptions, and run again: no warnings.
#
# Part C - write the tests. In `test_shipping.py` have these tests (the three given ones can be reshaped):
#
# 1. `shipping_cost(2) == 5.99` and `shipping_cost(2, "express") == 10.99`, both marked `@pytest.mark.smoke`.
# 2. A class `TestFreeShipping` marked `@pytest.mark.smoke` (a mark on a class applies to every test inside): an order total of 50 ships free (`shipping_cost(2, order_total=50) == 0.0`), a total of 49.99 pays 5.99.
# 3. Unknown method (`"pigeon"`) raises `ValueError` matching `unknown shipping method`; weight 0 raises `ValueError` matching `weight`. No marks.
# 4. `bulk_quote` parametrized with `(10, 1, 40.41)`, `(1, 1, 4.04)` and `(100, 2, 539.1)` for `(parcels, weight, expected)`, the whole test marked `@pytest.mark.slow`.
# 5. `delivery_days` parametrized with `pytest.param(..., marks=...)` so that single rows carry their own marks:
#
# | country | days | marks on the row |
# |---------|------|------------------|
# | IN | 3 | `pytest.mark.smoke` |
# | US | 6 | `[pytest.mark.smoke, pytest.mark.slow]` |
# | UK | 5 | none |
# | NZ | 10 | none |
# | FR | 4 | `pytest.mark.skip(reason="France rate not decided")` |
# | DE | 5 | `pytest.mark.xfail(reason="DE is not in the table, so it takes 10 days")` |
#
# Part D - select tests. Use `-m` with a marker expression and see how many tests are deselected. Expressions can combine marker names with `and`, `or`, `not` and brackets. `--collect-only -q` lists what a selection would run without running it.
#
# Behaviours to test
#
# | Marker or mark | What it selects |
# |----------------|-----------------|
# | `-m smoke` | the shipping cost checks, the class `TestFreeShipping`, and the rows IN and US |
# | `-m slow` | the three `bulk_quote` cases and the row US |
# | `-m "not slow"` | everything except those four |
# | `-m "smoke and not slow"` | smoke tests that are quick |
# | `-m "smoke and slow"` | only the row US (it has both marks) |
# | `-m "smoke or slow"` | anything with either mark |
