"""Shipping calculator. This is the code under test: do not change it."""

import time

RATES_PER_KG = {"standard": 1.5, "express": 4.0}
FREE_SHIPPING_FROM = 50


def shipping_cost(weight_kg, method="standard", order_total=0):
    """Cost of sending a parcel. Orders of 50 or more ship for free."""
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if method not in RATES_PER_KG:
        raise ValueError(f"unknown shipping method: {method}")
    if order_total >= FREE_SHIPPING_FROM:
        return 0.0
    return round(2.99 + weight_kg * RATES_PER_KG[method], 2)


def delivery_days(country):
    days = {"IN": 3, "US": 6, "UK": 5}
    return days.get(country, 10)


def bulk_quote(parcels, weight_kg):
    """Price a big batch of identical parcels. Pretends to call a slow service."""
    time.sleep(0.2)
    return round(parcels * shipping_cost(weight_kg) * 0.9, 2)
