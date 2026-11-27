from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def check_subtract():
    assert subtract(5, 3) == 2


class CalculatorTests:
    def test_multiply(self):
        assert multiply(4, 3) == 12
