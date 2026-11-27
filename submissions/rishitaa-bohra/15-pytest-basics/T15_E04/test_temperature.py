# T15-E04 - Parametrize and reading failure output
#
# Part A - read the failures. Run `py -m pytest` in the folder. Four tests fail. For each one, read the failure report from the bottom: the `E` lines say what was compared, the line with `>` marks the failing statement, and the last line names the exception. Decide for each failure whether the TEST or the CODE is wrong. The code in `temperature.py` is correct, as its docstrings say; fix the tests:
#
# - `test_boiling_point_in_fahrenheit` has a wrong expected value;
# - `test_body_temperature_in_celsius` compares floating point numbers with `==` (use `pytest.approx`);
# - `test_fifteen_degrees_is_cold` disagrees with the docstring of `describe` (look at the boundary);
# - `test_below_absolute_zero` does not expect the exception that is documented.
#
# Part B - parametrize. Add parametrized tests (one test function each, many rows of data):
#
# 1. `c_to_f` for `(0, 32)`, `(100, 212)`, `(-40, -40)`, `(37, 98.6)`, `(-273.15, -459.67)`, compared with `pytest.approx`.
# 2. `f_to_c` for `(32, 0)`, `(212, 100)`, `(-40, -40)`, `(98.6, 37)` with readable ids: `ids=["freezing", "boiling", "equal-point", "body"]`.
# 3. `describe` for the boundaries `-10, 0, 0.1, 14.9, 15, 24.9, 25, 40` with the expected words.
# 4. `c_to_k` raises `ValueError` for `-273.16` and `-500` (parametrize `celsius`, use `pytest.raises` inside).
# 5. One test that `c_to_k(-273.15)` is accepted and gives about 0.
#
# Behaviours to test
#
# | Function | Behaviour |
# |----------|-----------|
# | `c_to_f` | the five pairs above |
# | `f_to_c` | the four pairs above |
# | `describe` | `<= 0` freezing, below 15 cold, below 25 mild, otherwise hot |
# | `c_to_k` | below -273.15 raises `ValueError`; -273.15 itself is allowed |
