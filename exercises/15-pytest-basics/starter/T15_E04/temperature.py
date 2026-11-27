"""Temperature conversion helpers. This is the code under test: do not change it."""

ABSOLUTE_ZERO_C = -273.15


def c_to_f(celsius):
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def c_to_k(celsius):
    """Convert to Kelvin. Anything below absolute zero is impossible."""
    if celsius < ABSOLUTE_ZERO_C:
        raise ValueError("temperature is below absolute zero")
    return celsius + 273.15


def describe(celsius):
    """Return a one-word description: freezing (0 or below), cold (below 15),
    mild (below 25) or hot."""
    if celsius <= 0:
        return "freezing"
    if celsius < 15:
        return "cold"
    if celsius < 25:
        return "mild"
    return "hot"
