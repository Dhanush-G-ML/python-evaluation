import sys

import pytest

from price import apply_discount, format_price, line_separator, to_cents


def test_apply_discount():
    assert apply_discount(200, 25) == 150


def test_format_price():
    assert format_price(5) == "5.00 USD"

# TODO: refund test that is skipped, three skipif tests (Windows, not Windows,
#       Python version), and two xfail tests for to_cents (see exercises.md).
