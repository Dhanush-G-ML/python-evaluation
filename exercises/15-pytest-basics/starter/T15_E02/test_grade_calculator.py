import pytest

from grade_calculator import average, has_passed, percent_to_grade


def test_percent_to_grade_a():
    assert percent_to_grade(95) == "A"

# TODO 1: test the boundaries (90, 89, 80, 79, 70, 69, 60, 59, 0 and 100).
# TODO 2: test average() with a normal list.
# TODO 3: use pytest.raises for the three error cases (see exercises.md).
