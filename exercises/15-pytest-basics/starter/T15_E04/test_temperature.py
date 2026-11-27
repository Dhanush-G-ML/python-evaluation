import pytest

from temperature import c_to_f, c_to_k, describe, f_to_c


def test_freezing_point_in_fahrenheit():
    assert c_to_f(0) == 32


def test_boiling_point_in_fahrenheit():
    assert c_to_f(100) == 112


def test_body_temperature_in_celsius():
    assert f_to_c(100) == 37.78


def test_fifteen_degrees_is_cold():
    assert describe(15) == "cold"


def test_below_absolute_zero():
    assert c_to_k(-300) == 0
