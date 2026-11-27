import pytest

from loyalty import points_for_purchase, redeem, summary, tier_for_points


def test_bronze_points():
    assert points_for_purchase(12.80) == 12


def test_silver_points_are_doubled():
    assert points_for_purchase(10, "silver") == 20


def test_bronze_tier_for_new_members():
    assert tier_for_points(0) == "bronze"


def test_redeem_a_coffee():
    assert redeem(150, "coffee") == 50
