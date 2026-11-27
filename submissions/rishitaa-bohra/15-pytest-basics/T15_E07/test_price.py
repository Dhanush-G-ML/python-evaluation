# T15-E07 - Markers 1: skip, skipif and xfail
#
# Built-in markers change what pytest does with a test without changing the test body. Add these tests to `test_price.py`:
#
# 1. `test_apply_discount` and `test_format_price` (given): `apply_discount(200, 25) == 150`, `format_price(5) == "5.00 USD"`.
# 2. `test_refund_is_calculated`: a test for a feature that does not exist yet. Mark it `@pytest.mark.skip(reason="refunds are not implemented yet")`. It is never run.
# 3. `test_line_separator_on_posix`: `line_separator() == "\n"`, with `@pytest.mark.skipif(sys.platform == "win32", reason="Linux and macOS line endings")`.
# 4. `test_line_separator_on_windows`: `line_separator() == "\r\n"`, with `@pytest.mark.skipif(sys.platform != "win32", reason="Windows line endings")`. On any machine exactly one of tests 3 and 4 runs and the other is skipped.
# 5. `test_copy_replace_exists`: asserts `hasattr(copy, "replace")` (a function added in Python 3.13) with `@pytest.mark.skipif(sys.version_info < (3, 13), reason="copy.replace needs Python 3.13")`. On Python 3.12 it is skipped.
# 6. `test_to_cents_of_19_99`: asserts `to_cents(19.99) == 1999`. The code has a documented bug (see the docstring at the top of `price.py`): it returns 1998. Mark the test `@pytest.mark.xfail(reason="known bug: to_cents truncates instead of rounding", strict=True)`. It is an expected failure.
# 7. `test_to_cents_of_a_whole_price`: asserts `to_cents(2.5) == 250` with `@pytest.mark.xfail(reason="not sure this one works, check later")` (not strict). This one passes, which pytest reports as "unexpectedly passed".
#
# Run with `py -m pytest -v -rsxX`. The `-r` option adds a short summary: `s` skipped (with reason), `x` expected failures, `X` unexpected passes.
#
# Part B - strict. Change the code temporarily: in `price.py` replace `int(price * 100)` with `round(price * 100)`, run again, and read what happens to test 6 (and to test 7). Change the code back afterwards.
#
# Behaviours to test
#
# | Marker | Used for | Result symbol |
# |--------|----------|---------------|
# | `skip` | a test that must not run at all | `s` (SKIPPED) |
# | `skipif(condition, reason=...)` | a test that only makes sense on some systems or versions | `s` when the condition is true, otherwise the normal `.` |
# | `xfail(reason=...)` | a test for a known bug | `x` (XFAIL) while it still fails |
# | `xfail` (not strict) that passes | | `X` (XPASS): reported but the run still succeeds |
# | `xfail(strict=True)` that passes | | shown as FAILED with the text `[XPASS(strict)]`: the run fails, which tells you the bug is fixed and the marker must go |
