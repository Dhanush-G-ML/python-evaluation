"""Price helpers for a small shop. This is the code under test: do not change it.

Known bug (reported, not fixed yet): to_cents() cuts off fractions instead of
rounding, so to_cents(19.99) returns 1998 instead of 1999.
"""

import os


def apply_discount(price, percent):
    """Return the price after taking off a percentage (0 to 100)."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (100 - percent) / 100, 2)


def format_price(amount, currency="USD"):
    return f"{amount:.2f} {currency}"


def to_cents(price):
    return int(price * 100)


def line_separator():
    """The line ending used by this operating system."""
    return os.linesep
