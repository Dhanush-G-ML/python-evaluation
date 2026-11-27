import pytest

from shipping import bulk_quote, delivery_days, shipping_cost


@pytest.mark.smoke
def test_standard_shipping_cost():
    assert shipping_cost(2) == 5.99


@pytest.mark.slow
def test_bulk_quote_for_ten_parcels():
    assert bulk_quote(10, 1) == 40.41


def test_delivery_days_to_india():
    assert delivery_days("IN") == 3

# TODO: add more tests, register the markers in pytest.ini (see exercises.md).
